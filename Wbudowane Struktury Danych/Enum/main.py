from enum import Enum


class WeekStr:
    MONDAY = "MONDAY"
    TUESDAY = "TUESDAY"
    WEDNESDAY = "WEDNESDAY"
    THURSDAY = "THURSDAY"
    FRIDAY = "FRIDAY"
    SATURDAY = "SATURDAY"
    SUNDAY = "SUNDAY"


def is_weekend_str(week_day):
    return week_day == WeekStr.SATURDAY or week_day == WeekStr.SUNDAY


class Week(Enum):
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6
    SUNDAY = 7

# week = Week
# print(week.FRIDAY)

friday = Week.FRIDAY
print(friday)
print(friday.value)
print(friday.name)

print(friday is Week.FRIDAY)
print(friday is Week.SATURDAY)


def is_weekend(week_day):
    return week_day is Week.SATURDAY or week_day is Week.SUNDAY