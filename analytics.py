# default sys.setrecursionlimit = 1000 so 3 years of daily activity will break FP tail recursion
from datetime import datetime, timedelta

def all(activities):
    """
    FP style: returning all activities' names
    """
    return list(map(lambda a: a.name, activities))

def by_periodicity_type(activities, periodicity_type):
    """
    FP style: returning only activities with type of periodicity
    """
    return list(map(lambda a: a.name, filter(lambda a: a.periodicity_type == periodicity_type, activities)))

def streak_for_one(activity):
    """
    Counting max streak for weekly or daily activity.
    All activity-out will be changed to time 11:59:59  --
    After that every range of dates will be compared with delta 1 day or 1 week.
    Don't use old dates before 2000 year.
    First date template is 3200 weeks before now.
    For this purpose safety buffer of 1000 weeks backwards was also added
    """
    if not activity.activity_out:
        return 0

    longest = 0
    _first = datetime.now() - timedelta(weeks = 3200)

    if activity.periodicity_type == 'DAILY':
        _delta = timedelta(days = 1)
        _shift_streak = 0
    else:
        _delta = timedelta(weeks = 1)
        _shift_streak = -1

    streak = _shift_streak

    for _datetime in activity.activity_out:
        _datetime_str = str(_datetime)
        _datetime00 = datetime.strptime(_datetime_str[:11]+"11:59:59.000000", "%Y-%m-%d %H:%M:%S.%f")
        #print(f"{_first} == {_datetime00}             {_delta}")
        if  _datetime00 - _first == _delta or _datetime00 - _first > timedelta(weeks = 1000):
            streak += 1
        else:
            streak = 0

        longest = max(longest, streak)
        _first = _datetime00

    return longest
    

def streak_for_all(activities):
    """
    FP style: finding max streak for all activities
    """
    return max([streak_for_one(a) for a in activities], default=0)

def streak_for_activity(activity):
    """
    Only abstraction for good name of function
    """
    return streak_for_one(activity)
