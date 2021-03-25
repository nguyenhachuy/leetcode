from datetime import date
from datetime import timedelta

def extract_date_components(date):
    tokens = date.split("/")
    return [int(token) for token in tokens]

def move_date_forward_monday(date):
    weekday = date.weekday()
    if weekday == 0:
        return [0, date]

    remainder = 7 - weekday
    new_date = date + timedelta(days=remainder)

    return [max(0, remainder-2), new_date]

def move_date_backwards_sunday(date):
    weekday = date.weekday()
    if weekday == 6:
        return [0, date]

    new_date = date - timedelta(days=weekday+1)

    return [min(5, weekday+1), new_date]

def count_holidays(start_date, end_date, holidays):
    result = 0

    for holiday in holidays:
        month,day,year = extract_date_components(holiday)
        holidate = date(year,month,day)
        if start_date <= holidate <= end_date:
            result += 1

    return result

def calculate_working_days(start_date, end_date, holidays):
    # import pudb; pu.db
    start_month, start_day, start_year = extract_date_components(start_date)
    end_month, end_day, end_year = extract_date_components(end_date)
    f_date = date(start_year, start_month, start_day)
    l_date = date(end_year, end_month, end_day)
    holidays_offset = count_holidays(f_date, l_date, holidays)

    start_delta, start_adjusted_date = move_date_forward_monday(f_date)
    end_delta, end_adjusted_date = move_date_backwards_sunday(l_date)

    if start_adjusted_date > l_date:
        saturday = 1 if l_date.weekday() >= 5 else 0
        sunday = 1 if l_date.weekday() >= 6 else 0

        return (l_date-f_date).days+1 - (saturday+sunday) - holidays_offset
    if start_adjusted_date > end_adjusted_date:
        return start_delta + end_delta - holidays_offset

    weeks_delta = ((end_adjusted_date - start_adjusted_date).days + 1) // 7
    working_days_count = start_delta + end_delta + weeks_delta * 5

    return working_days_count - holidays_offset


import unittest

class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual(calculate_working_days("7/2/2014", "7/11/2014", ""), 8)
        self.assertEqual(calculate_working_days("2/1/2021", "2/24/2021", ""), 18)
        self.assertEqual(calculate_working_days("2/6/2021", "2/8/2021", ""), 1)
        self.assertEqual(calculate_working_days("2/23/2021", "2/23/2021", ""), 1)
        self.assertEqual(calculate_working_days("2/6/2021", "2/6/2021", ""), 0)
        self.assertEqual(calculate_working_days("2/6/2021", "2/7/2021", ""), 0)
        self.assertEqual(calculate_working_days("2/7/2021", "2/8/2021", ""), 1)
        self.assertEqual(calculate_working_days("2/2/2021", "2/3/2021", ""), 2)
        self.assertEqual(calculate_working_days("11/2/2020", "5/6/2021", ""), 134)
        self.assertEqual(calculate_working_days("9/4/2017", "10/30/2017", ""), 41)
        self.assertEqual(calculate_working_days("9/4/2017", "10/30/2017", ['09/04/2017', '10/09/2017', '11/10/2017']), 39)
if __name__ == '__main__':
    unittest.main()

"""
end-start = x weeks
move start date from anything to a Monday (calculate between that) ->
    can contribute at most 2 days if it's saturday, sunday contribute 1 and
move end date from anything back to a Sunday (calculate between that) ->
    can contribute at most 1 day, if 2 days then its already sunday
"""
