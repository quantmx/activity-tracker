import json
from activity import ActivityManager
from analytics import (
        streak_for_activity,
        all,
        by_periodicity_type,
        streak_for_all
)

def prompt():
    """
    Main loop of menu
    Before entering menu, checking json file and loading it, if is present
    If  json file is absent it will be generated with predefined activites and test dataset
    """
    manager = ActivityManager()
    storage_file = 'activities.json'
    manager.load4file(storage_file)

    allowed_input = "0123456789"
    allowed_periodicity = "DW"
    infinity = True
    while infinity:
        print("",
              "0. EXIT / SAVE STATUS DURING EXIT (NEW ACITIVITES, INS/OUTS)",
              "1. ACTIVITY IN", 
              "2. ACTIVITY OUT",
              "3. SHOW ACTIVITY/-IES",
              "4. CREATE ACTIVITY",
              "5. ANALYTICS: SHOW ALL ACTIVITIES NAMES",
              "6. ANALYTICS: SHOW ALL ACTIVITIES NAMES WITH SAME TYPE OF PERIODICITY",
              "7. ANALYTICS: SHOW THE LONGEST RUN STREAK OF ALL ACTIVITIES",
              "8. ANALYTICS: SHOW THE LONGEST RUN STREAK FOR A GIVEN ACTIVITY",
              "9. DELETE ACTIVITY FROM WORKING LIST \n",
              
              sep='\n')

        raw_input = input("WAITING FOR NUMBER OF ITEM ( + ENTER OR RETURN): ").strip()
        item = "".join([char for char in raw_input if char in allowed_input])

        if len(item) == len(raw_input):
            if item == '0':
                manager.save2file(storage_file)
                print("BYE BYE 👋")
                break

            elif item == '1':
                search = input("ENTER ACTIVITY NAME: ").strip().upper()
                try:
                    activity = manager.activity(search)
                except ValueError as e:
                    print(f"ERROR: {e}")
                else:
                    activity.touch_in()

            elif item == '2':
                search = input("ENTER ACTIVITY NAME: ").strip().upper()
                try:
                    activity = manager.activity(search)
                except ValueError as e:
                    print(f"ERROR: {e}")
                else:
                    activity.touch_out()

            elif item == '3':
                search = input("ENTER ACTIVITY NAME OR LEAVE EMPTY FOR ALL: ").strip().upper()
                try:
                    activities = manager.acts(search)
                except ValueError as e:
                    print(f"ERROR: {e}")
                else:
                    if len(activities) == 0:
                        print("SORRY, BUT ACTIVITIES NOT FOUND.")
                    else:
                        for activity in activities:
                            print(f"\nACTIVITY NAME: {activity.name}\n PERIODICITY TYPE: {activity.periodicity_type}\n LAST IN/OUT: {str(activity.last_in())[:-7]} / {str(activity.last_out())[:-7]}\n DESCRIPTION: {activity.description}\n CREATED AT: {str(activity.created_at)[:-7]}")

            elif item == '4':
                status = "activated"
                name = input("ENTER ACTIVITY NAME: ").strip().upper()
                description = input("ENTER ACTIVITY DESCRIPTION: ").strip()
                while infinity:
                    raw_periodicity_type = input("ENTER PERIODICITY TYPE OF ACTIVITY (D)AILY OR (W)EEKLY: ").strip().upper()
                    periodicity_type_item = "".join([char for char in raw_periodicity_type if char in allowed_periodicity])
                    if (periodicity_type_item == 'D' or periodicity_type_item == 'W') and len(periodicity_type_item) == len(raw_periodicity_type): 
                        if periodicity_type_item == 'D':
                            periodicity_type = "DAILY"
                        else:
                            periodicity_type = "WEEKLY"
                        break
                    else:
                        print("SOMETHING WRONG HAPPENED WHEN YOU ENTERED PERIODICITY TYPE, REPEAT PLEASE.")
                try:
                    manager.append(name, description, periodicity_type)
                except ValueError as e:
                    print(f"ERROR: {e}")
                except Exception as e:
                    print(f"AN UNEXPEXTED ERROR OCCURED: {e}")
                else:
                    print(f"JUST ADDED ACTIVITY '{name}' WITH DESCRIPTION: '{description}' AND PERIODICITY TYPE: '{periodicity_type}'")

            elif item == '5':
                print("ALL ACTIVITY NAMES:")
                print("\n".join(map("{}".format, all(manager.acts()))))

            elif item == '6':
                while infinity:
                    analytics_raw_periodicity_type = input("ENTER PERIODICITY TYPE OF ACTIVITY (D)AILY OR (W)EEKLY: ").strip().upper()
                    analytics_periodicity_type_item = "".join([char for char in analytics_raw_periodicity_type if char in allowed_periodicity])
                    if (analytics_periodicity_type_item == 'D' or analytics_periodicity_type_item == 'W') and len(analytics_periodicity_type_item) == len(analytics_raw_periodicity_type): 
                        if analytics_periodicity_type_item == 'D':
                            analytics_periodicity_type = "DAILY"
                        else:
                            analytics_periodicity_type = "WEEKLY"
                        break
                    else:
                        print("SOMETHING WRONG HAPPENED WHEN YOU ENTERED PERIODICITY TYPE, REPEAT PLEASE.")
                
                print(f"\nALL ACTIVITY NAMES WITH TYPE OF PERIODICITY {analytics_periodicity_type}:")
                print("\n".join(map("{}".format, by_periodicity_type(manager.acts(), analytics_periodicity_type))))

            elif item == '7':
                print(f"LONGEST STREAK FOR ALL ACTIVITIES: {streak_for_all(manager.acts())}")

            elif item == '8':
                search = input("ENTER ACTIVITY NAME: ").strip().upper()
                try:
                    activity = manager.activity(search)
                except ValueError as e:
                    print(f"ERROR: {e}")
                else:
                    print(f"LONGEST STREAK FOR '{activity.name}' : {streak_for_activity(activity)}")

            elif item == '9':
                search = input("ENTER ACTIVITY NAME: ").strip().upper()
                try:
                    activity = manager.delete(search)
                except ValueError as e:
                    print(f"ERROR: {e}")

            else:
                print("SOMETHING WRONG HAPPENED WHEN YOU ENTERED PERIODICITY TYPE, REPEAT PLEASE.")
        else:
            print("THE ENTERED STRING CONTAINS INVALID CHARACTERS, REPEAT PLEASE.")

if __name__ == "__main__":
    prompt()
