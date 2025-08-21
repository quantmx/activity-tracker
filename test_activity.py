import unittest
from datetime import datetime, timedelta
from activity import Activity, ActivityManager

class TestActivityManager(unittest.TestCase):
    def setUp(self):
        self.manager = ActivityManager()

    def test_activity_adding(self):
        self.manager.append("TESTACTIVITYADDING", "TestActivityAdding", "WEEKLY")

        self.assertEqual(len(self.manager.activities), 1)
        self.assertEqual(self.manager.activities[0].name, "TESTACTIVITYADDING")
        self.assertEqual(self.manager.activities[0].description, "TestActivityAdding")
        self.assertEqual(self.manager.activities[0].periodicity_type, "WEEKLY")
        
        with self.assertRaises(ValueError):
            self.manager.append("TESTACTIVITYADDING", "TestActivityAdding", "WEEKLY")

    def test_activity_in(self):
        self.manager.append("TESTACTIVITYADDING", "TestActivityAdding", "WEEKLY")
        self.assertEqual(len(self.manager.activities[0].activity_in), 0)

        self.manager.activities[0].touch_in()

        self.assertEqual(len(self.manager.activities[0].activity_in), 1)

    def test_activity_out(self):
        self.manager.append("TESTACTIVITYADDING", "TestActivityAdding", "WEEKLY")
        self.assertEqual(len(self.manager.activities[0].activity_out), 0)

        self.manager.activities[0].touch_out()

        self.assertEqual(len(self.manager.activities[0].activity_out), 1)

    def test_activity_deleting(self):
        self.manager.append("TESTACTIVITYDELETING", "TestActivityDeleting", "WEEKLY")

        self.assertEqual(len(self.manager.activities), 1)
        self.manager.delete("TESTACTIVITYDELETING")
        self.assertEqual(len(self.manager.activities), 0)

        with self.assertRaises(ValueError):
            self.manager.delete("TESTACTIVITYDELETING")

    def test_acts(self):
        self.manager.append("TESTACTIVITIES", "TestActivities", "WEEKLY")
        
        self.assertEqual(self.manager.acts()[0].name, "TESTACTIVITIES")
        self.assertEqual(self.manager.acts("TESTACTIVITIES")[0].name, "TESTACTIVITIES")

if __name__ == "__main__":
    unittest.main()
