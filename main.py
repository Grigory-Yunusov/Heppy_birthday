import collections
from collections import defaultdict
from datetime import date, datetime, timedelta
def get_birthdays_per_week(users):
    if len(users) == 0:
        return {}
    date_today = date.today()
    day_week_today = date_today.isoweekday()
    birthday_per_week = []
    for dict in users:
        user = list(dict.values())
        full_name = user[0].split(' ')
        birthday_date = user[1].replace(year=date_today.year)
        if birthday_date <= date_today - timedelta(days=3):
            birthday_date = birthday_date.replace(year=date_today.year+1)
        day_week = birthday_date.isoweekday()
        Person = collections.namedtuple('Person', ['name', 'birthday', 'week_day'])
        person = Person(full_name[0], birthday_date, day_week)
        if day_week_today == 1:
            start_date = date_today - timedelta(days=2)
            end_date = date_today + timedelta(days=4)
            if start_date <= birthday_date <= end_date:
                birthday_per_week.append(person)
        else:
            end_date = date_today + timedelta(days=6)
            if date_today <= birthday_date <= end_date:
                birthday_per_week.append(person)
    if day_week_today == 1 or day_week_today == 6 or day_week_today == 7:
        users = defaultdict(list)
        for item in birthday_per_week:
            if item.week_day == 1:
                users['Monday'].append(item[0])
            if item.week_day == 6:
                users['Monday'].append(item[0])
            if item.week_day == 7:
                users['Monday'].append(item[0])
            if item.week_day == 2:
                users['Tuesday'].append(item[0])
            if item.week_day == 3:
                users['Wednesday'].append(item[0])
            if item.week_day == 4:
                users['Thursday'].append(item[0])
            if item.week_day == 5:
                users['Friday'].append(item[0])
    if day_week_today == 2:
        users = defaultdict(list)
        for item in birthday_per_week:
            if item.week_day == 2:
                users['Tuesday'].append(item[0])
            if item.week_day == 3:
                users['Wednesday'].append(item[0])
            if item.week_day == 4:
                users['Thursday'].append(item[0])
            if item.week_day == 5:
                users['Friday'].append(item[0])
            if item.week_day == 1:
                users['Monday'].append(item[0])
            if item.week_day == 6:
                users['Monday'].append(item[0])
            if item.week_day == 7:
                users['Monday'].append(item[0])
    if day_week_today == 3:
        users = defaultdict(list)
        for item in birthday_per_week:
            if item.week_day == 3:
                users['Wednesday'].append(item[0])
            if item.week_day == 4:
                users['Thursday'].append(item[0])
            if item.week_day == 5:
                users['Friday'].append(item[0])
            if item.week_day == 1:
                users['Monday'].append(item[0])
            if item.week_day == 6:
                users['Monday'].append(item[0])
            if item.week_day == 7:
                users['Monday'].append(item[0])
            if item.week_day == 2:
                users['Tuesday'].append(item[0])
    if day_week_today == 4:
        users = defaultdict(list)
        for item in birthday_per_week:
            if item.week_day == 4:
                users['Thursday'].append(item[0])
            if item.week_day == 5:
                users['Friday'].append(item[0])
            if item.week_day == 1:
                users['Monday'].append(item[0])
            if item.week_day == 6:
                users['Monday'].append(item[0])
            if item.week_day == 7:
                users['Monday'].append(item[0])
            if item.week_day == 2:
                users['Tuesday'].append(item[0])
            if item.week_day == 3:
                users['Wednesday'].append(item[0])
    if day_week_today == 5:
        users = defaultdict(list)
        for item in birthday_per_week:
            if item.week_day == 5:
                users['Friday'].append(item[0])
            if item.week_day == 1:
                users['Monday'].append(item[0])
            if item.week_day == 6:
                users['Monday'].append(item[0])
            if item.week_day == 7:
                users['Monday'].append(item[0])
            if item.week_day == 2:
                users['Tuesday'].append(item[0])
            if item.week_day == 3:
                users['Wednesday'].append(item[0])
            if item.week_day == 4:
                users['Thursday'].append(item[0])
    return users
if __name__ == "__main__":
    users = [{"name": "Bill Gates", "birthday": datetime(1955, 11, 11).date()}, 
         {"name": "Anna Gates", "birthday": datetime(1978, 12, 30).date()}, 
         {"name": "Gearge Gates", "birthday": datetime(2013, 1, 6).date()}, 
         {"name": "Nona Gates", "birthday": datetime(1955, 1, 7).date()},   
         {"name": "Katya Gates", "birthday": datetime(1955, 1, 2).date()},  
         {"name": "Mila Gates", "birthday": datetime(1955, 1, 12).date()},  
         {"name": "Dana Gates", "birthday": datetime(1955, 12, 28).date()}  
         ]
    result = get_birthdays_per_week(users)
    print(result)
        # Виводимо результат
    for day_name, names in result.items():
        print(f"{day_name}: {', '.join(names)}")
