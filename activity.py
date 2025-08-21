import json
import random
from datetime import datetime, timedelta

class Activity:

    def __init__(self, name, description, periodicity_type):
        """
        Fundamental structure for activity objects
        """
        self.name = name
        self.periodicity_type = periodicity_type
        self.activity_in = []
        self.activity_out = []
        self.description = description
        self.created_at = datetime.now()

    def touch_in(self):
        """
        Adding new date and time for starting activity
        """
        self.activity_in.append(datetime.now())

    def touch_out(self):
        """
        Adding new date and time for ending activity
        """
        self.activity_out.append(datetime.now())

    def last_in(self):
        """
        returning last start date time for activity, or "" for empty list
        """
        if len(self.activity_in) == 0:
            return ""
        else:
            return self.activity_in[-1]

    def last_out(self):
        """
        returning last end date time for activity or "" for empty list.
        also returning "" for started but not ended activity
        """
        if len(self.activity_out) == 0:
            return ""
        else:
            if self.activity_out[-1] < self.activity_in[-1]:
                return ""
            else:
                return self.activity_out[-1]

class ActivityManager:
    def __init__(self):
        """
        main list of activities
        """
        self.activities = []

    def append(self, name, description, periodicity_type):
        """
        Adding activity with args
        Checking for duplicates and empty ones before adding
        """
        if not name or not periodicity_type:
            raise ValueError("NAME SHOULD BE NOT EMPTY")

        for activity in self.activities:
            if activity.name == name:
                raise ValueError(f"SORRY BUT ACTIVITY WITH NAME: {name} IS ALREADY PRESENT IN THE LIST.")

        activity_instance = Activity(name, description, periodicity_type)
        self.activities.append(activity_instance)

    def delete(self, name):
        """
        Delete activity by name
        """
        deleted = False

        for activity in self.activities:
            if activity.name == name:
                self.activities.remove(activity)
                deleted = True
                print(f"ACTIVITY {name} JUST DELETED.")
                break

        if not deleted:
            raise ValueError(f"SORRY BUT ACTIVITY WITH NAME: {name} NO FOUND IN THE LIST .")

    def activity(self, name):
        """
        Returning activity object by name
        Exception if name is not found
        """
        for activity in self.activities:
            if activity.name == name:
                return activity
        raise ValueError(f"SORRY BUT ACTIVITY WITH NAME: {name} IS NOT PRESENT IN THE LIST.")

    def acts(self, name=""):
        """
        Returnimg all activities as list
        1. By default name is empty.
        2. If name is not empty the function returns list with only one activity
        """
        if len(name) == 0:
            return self.activities
        return [self.activity(name)]

    def save2file(self, filename):
        """
        Save all activities to JSON file
        """
        activities = [{
            'name': activity.name,
            'periodicity_type': activity.periodicity_type,
            'activity_in': [datetime.isoformat() for datetime in activity.activity_in],
            'activity_out': [datetime.isoformat() for datetime in activity.activity_out],
            'description': activity.description,
            'created_at': activity.created_at.isoformat()
            } for activity in self.activities]
        with open(filename, 'w') as file:
            json.dump(activities, file)

    def load4file(self, filename):
        """
        Load data from JSON file.
        If file is not present it will generated wiht new 5 activities.
        4 daily activities, 4 weeks period, and last of them with broken streak at last day.
        1 for weekly activity with streak of 4 weeks
        """
        try:
            with open(filename, 'r') as file:
                activities = json.load(file)
        except Exception as e:
            print(f"\n ERROR: {e}, \n SEEMS DATA FILE WITH YOUR ACTIVITIES IS MISSING.\n LIST OF ACTIVITIES/TESTS DATASET IS NOW PREDEFINED \n ")
            #PREDEFINED ACTIVITIES
            self.activities = []
            weekly_predefined_names = ["WALK IN THE FOREST"]
            daily_predefined_names = ["EXERCISES", "LEARNING ENGLISH", "READING BOOK", "WATCHING NEWS"]

            _activity_shift = timedelta(minutes = 0)
            _create_shift = timedelta(minutes = -60)
            for _name in daily_predefined_names:
                _item = Activity(_name, _name, "DAILY")
                for _day in range(4*7, 0, -1):
                    _shift = timedelta(minutes=random.randint(0,60)-120) + _activity_shift + timedelta(seconds=random.randint(1, 59))
                    _item.activity_in.append(datetime.now()-timedelta(days=_day) + _shift)
                    _item.activity_out.append(datetime.now()-timedelta(days=_day) + _shift + timedelta(minutes=random.randint(10, 59)) + timedelta(seconds=random.randint(1, 59)))
                _item.created_at = datetime.now()-timedelta(days=4*7)-timedelta(minutes=random.randint(1,4)) + _create_shift
                _activity_shift += timedelta(minutes = random.randint(60,120))
                _create_shift += timedelta(minutes = random.randint(5,10))
                self.activities.append(_item)

            _tmp = self.activities[-1].activity_in.pop()
            _tmp = self.activities[-1].activity_out.pop()

            for _name in weekly_predefined_names:
                _item = Activity(_name, _name, "WEEKLY")
                for _week in range(4, -1, -1):
                    _week_hours_minutes = datetime.now() - timedelta(weeks=_week) - timedelta(days=1) + timedelta(hours=random.randint(0, 10)) + timedelta(minutes=random.randint(0,59)) + timedelta(seconds=random.randint(1, 59))
                    _item.activity_in.append(_week_hours_minutes)
                    _item.activity_out.append(_week_hours_minutes + timedelta(hours=random.randint(1, 3)) + timedelta(minutes=random.randint(0,59)) + timedelta(seconds=random.randint(1, 59)))
                _item.created_at = datetime.now()-timedelta(days=4*7)-timedelta(minutes=random.randint(1,4)) + _create_shift
                self.activities.append(_item)

        else:
            self.activities = []

            for activity in activities:
                item = Activity(activity['name'], activity['description'], activity['periodicity_type'])
                item.created_at = datetime.fromisoformat(activity['created_at'])
                item.activity_in = [datetime.fromisoformat(_datetime) for _datetime in activity['activity_in']]
                item.activity_out = [datetime.fromisoformat(_datetime) for _datetime in activity['activity_out']]
                self.activities.append(item)
