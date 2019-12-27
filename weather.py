import random


def get_days():
   # List<string> days = new List<string>();
   # days = []

   days =  [ 'mon', 'tues', 'wed',  'thurs', 'fri', 'sat', 'sun']

   return days

def get_random_report():
    weather = ['sunny', 'lovely', 'cool','cold']

    return weather[random.randint(0, len(weather) - 1)]   


def main():
    days = get_days()

    for day in days:
        report = get_random_report()
        print("On {0} it will be  {1}".format(day, report))


# to reuse as library without main interference i.e. like namespace
if __name__ == "__main__":
    main()
