import unittest
from datetime import datetime, timedelta
from activity import Activity, ActivityManager
from analytics import (
        streak_for_activity,
        all,
        by_periodicity_type,
        streak_for_all
)

class TestActivityManager(unittest.TestCase):
    def setUp(self):
        self.manager = ActivityManager()

    def test_all(self):
        self.manager.append("TESTACTIVITYADDING1", "TestActivityAdding1", "WEEKLY")
        self.manager.append("TESTACTIVITYADDING2", "TestActivityAdding2", "DAILY")

        self.assertEqual(len(all(self.manager.acts())), 2)
        self.assertEqual(all(self.manager.acts())[0], "TESTACTIVITYADDING1")
        self.assertEqual(all(self.manager.acts())[1], "TESTACTIVITYADDING2")

    def test_by_periodicity_type(self):
        self.manager.append("TEST_BY_PERIODICITY_TYPE", "Test_by_periodicity_type", "WEEKLY")
        self.assertEqual(by_periodicity_type(self.manager.acts(), 'WEEKLY')[0], "TEST_BY_PERIODICITY_TYPE")

    def test_streak_for_activity(self):
        self.manager.append("TEST_STREAK_FOR_ACTIVITY", "Test_streak_for_activity", "DAILY")
        for _day in range(14, 0, -1):
            self.manager.activities[0].activity_in.append(datetime.now()-timedelta(days=_day))
            self.manager.activities[0].activity_out.append(datetime.now()-timedelta(days=_day) + timedelta(hours=1))
        self.assertEqual(streak_for_activity(self.manager.activities[0]),14)

if __name__ == "__main__":
    unittest.main()
