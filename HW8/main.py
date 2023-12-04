from datetime import date, datetime, timedelta


def get_birthdays_per_week(users_dict):
    days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday",
                    "Friday", "Saturday", "Sunday"]
    result = {}
    current_year = date.today().year
    start_of_week = date.today()
    end_of_week = start_of_week + timedelta(days=6)
    for i in users_dict:

        birth_month_day = (i['birthday'].month, i['birthday'].day)
        if start_of_week.month == 12 and i['birthday'].month == 1:
            date_object = datetime(current_year + 1, *birth_month_day).date()
        else:
            date_object = datetime(current_year, *birth_month_day).date()
        week_index = date_object.weekday()
        week_object = days_of_week[week_index]

        if start_of_week <= date_object <= end_of_week:
            if week_object in ('Sunday', 'Saturday'):
                result.setdefault("Monday", []).append(i['name'])
            else:
                result.setdefault(week_object, []).append(i['name'])

    return result


if __name__ == "__main__":
    users = [
        {"name": "Jan Koum", "birthday": datetime(1976, 1, 1).date()},
    ]

    birth_dict = get_birthdays_per_week(users)
    print(birth_dict)
    for day_name, names in birth_dict.items():
        print(f"{day_name}: {', '.join(names)}")
