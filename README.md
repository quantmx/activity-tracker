# Activity Tracker App

    as per 2025.08.21

## Overview

This app allows users to create, manage, delete, and analyze their activities. It supports daily and weekly tracking, shows streaks, start and finish of activity and provides analytics on activity performance.

## Features

* Creating new activities with daily or weekly periodicity type.
* Mark activities as completed with start/finish time points and track streaks.
* Analyze activities with built-in analytics functions.
* Command-line interface (CLI) using pure Python function "print" and input, whenever possible with exceptions handling.
* Delete activities
* one JSON file for all data storage 
* Pure unittest for tests

## Requirements 

- Python >= 3.7 

## Installation
  
* Clone the repository or download ZIP with green button "CODE" on github page and unzip it:
```bash
   git clone https://github.com/quantmx/activity-tracker
   cd activity-tracker
```

## Tree of files
| File/Dir | Description |
|------|-------------|
| runme.py | Command-line interface for user interaction |
| activity.py | OOP module for activities |
| analytics.py | FP module for analysis|
| activities.json | File for storage JSON data. Also will be used for generating/saving predefined activities, if they are missing |
| test_analytics.py | Unit tests for analytics FP module | 
| test_activity.py | Unit tests for activity OOP module |
| README.md | Documentation file | 
| __pycache__ | Python Runtime directory


## How to use

### First run

*  **For first run in terminal:**

```bash
    cd activity-tracker
    python3 runme.py
``` 
*  **Message: activities data file is yet missing:** 
``` bash
 ERROR: [Errno 2] No such file or directory: 'activities.json', 
 SEEMS DATA FILE WITH YOUR ACTIVITIES IS MISSING.
 LIST OF ACTIVITIES/TESTS DATASET IS NOW PREDEFINED 
```
*  **Menu:** 
``` bash
0. EXIT
1. ACTIVITY IN
2. ACTIVITY OUT
3. SHOW ACTIVITY/-IES
4. CREATE ACTIVITY
5. ANALYTICS SHOW ALL
6. ANALYTICS SHOW ALL WITH THE SAME TYPE OF PERIODICITY
7. ANALYTICS SHOW THE LONGEST RUN STREAK OF ALL
8. ANALYTICS SHOW THE LONGEST RUN STREAK FOR A GIVEN NAME
9. DELETE ACTIVITY FROM WORKING LIST

WAITING FOR NUMBER OF ITEM(+ ENTER OR RETURN):
```
* **input `0`, then  ENTER**

    *  **data file activities.json is created and saved for next uses** 

```bash
WAITING FOR NUMBER OF ITEM(+ ENTER OR RETURN): 0
BYE BYE 👋
```

* **Restart activity tracker:**

```bash
    python runme.py
``` 


###  First use

**Show predefined activities**
 
* **Show ALL predefined activities with details: `3`, then two times `ENTER`** 
 
```bash
WAITING FOR NUMBER OF ITEM ( + ENTER OR RETURN): 3
ENTER ACTIVITY NAME OR LEAVE EMPTY FOR ALL:

ACTIVITY NAME: EXERCISES
 PERIODICITY TYPE: DAILY
 LAST IN/OUT: 2025-08-20 06:48:24 / 2025-08-20 07:37:14
 DESCRIPTION: EXERCISES
 CREATED AT: 2025-07-24 07:19:34
  ...
     AND SO ON ...
```
* **Show only one activity: `ENTER`, then its name:**

```bash
WAITING FOR NUMBER OF ITEM(+ ENTER OR RETURN): 3
ENTER ACTIVITY NAME OR LEAVE EMPTY FOR ALL: EXERCISES

ACTIVITY NAME: EXERCISES
PERIODICITY TYPE: DAILY
LAST IN/OUT: 2025-08-14 15:54:49 / 2025-08-14 16:08:08
DESCRIPTION: EXERCISES
CREATED AT: 2025-07-18 15:56:58
```

### Creating new activity 

*  **`4` + name, description and periodicity type with `D` or `W` (case insensitive):**
```bash
WAITING FOR NUMBER OF ITEM(+ ENTER OR RETURN): 4
ENTER ACTIVITY NAME: TEST
ENTER ACTIVITY DESCRIPTION: Test
ENTER PERIODICITY TYPE OF ACTIVITY (D)AILY OR (W)EEKLY: D
JUST ADDED ACTIVITY 'TEST' WITH DESCRIPTION: 'Test' AND PERIODICITY TYPE: 'DAILY'
```
*  **Activity created**

* **The activity will be saved for future use in activity.json on exit with `0`**  

### Starting/ending (compteting) existing activity 

* **`1` for starting:**

```bash
WAITING FOR NUMBER OF ITEM(+ ENTER OR RETURN): 1
ENTER ACTIVITY NAME: TEST
```

* **`2` for ending**
```bash
WAITING FOR NUMBER OF ITEM(+ ENTER OR RETURN): 2
ENTER ACTIVITY NAME: TEST
```

* **`3` + activity name to show this activity's in/out:**
```bash
ACTIVITY NAME: TEST
PERIODICITY TYPE: DAILY
LAST IN/OUT: 2025-08-15 17:24:00 / 2025-08-15 17:24:46
DESCRIPTION: Test
CREATED AT: 2025-08-15 17:20:46
```

### Delelting activity from datafile

**`9` + activity name:**

```bash
WAITING FOR NUMBER OF ITEM(+ ENTER OR RETURN): 9
ENTER ACTIVITY NAME: TEST
ACTIVITY TEST JUST DELETED.
```

### Analytics

* **Show all activities (only names): `5`**
```bash
WAITING FOR NUMBER OF ITEM(+ ENTER OR RETURN): 5
ALL ACTIVITY NAMES:
EXERCISES
LEARNING ENGLISH
READING BOOK
WATCHING NEWS
WALK IN THE FOREST
TEST
```

* **Show all activities with same type of periodicity: `6`, then `D` or `W`**
```bash
WAITING FOR NUMBER OF ITEM(+ ENTER OR RETURN): 6
ENTER PERIODICITY TYPE OF ACTIVITY (D)AILY OR (W)EEKLY: D

ALL ACTIVITY NAMES WITH TYPE OF PERIODICITY DAILY:
EXERCISES
LEARNING ENGLISH
READING BOOK
WATCHING NEWS
TEST
```
* **Show longest run streak of all activities: `7`**
```bash
WAITING FOR NUMBER OF ITEM(+ ENTER OR RETURN): 7
LONGEST STREAK FOR ALL ACTIVITIES: 28
```

* **Show longest run streak for a given activity: `8` , then name**
```bash
WAITING FOR NUMBER OF ITEM(+ ENTER OR RETURN): 8
ENTER ACTIVITY NAME: TEST
LONGEST STREAK FOR 'TEST' : 1
```

### Exiting App:

* **Exit: `0`**

```bash
WAITING FOR NUMBER OF ITEM(+ ENTER OR RETURN): 0
BYE BYE 👋
```
* **NOTE: all changes (created /deleted  activities, activities ins, outs and in/outs) will be saved in activities.json for further use**  

 
