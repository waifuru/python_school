import datetime


def friday_13():
    curr_day = datetime.date.today()
    week_day = curr_day.isoweekday()

    while week_day != 5:
        curr_day += datetime.timedelta(days=1)
        week_day = curr_day.isoweekday()

    i = 0

    while i < 10:
        if curr_day.day == 13:
            print(curr_day)
            i += 1
        curr_day += datetime.timedelta(days=7)


if __name__ == '__main__':
    friday_13()

