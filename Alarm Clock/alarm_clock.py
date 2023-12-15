from time import *
from datetime import *

"""Check input string against current time"""


def alarm(alarm_time):
    time_list = alarm_time.split(":")
    current_time = datetime.now().time()
    current_time_min = current_time.minute
    current_time_hour = current_time.hour
    sleep(10)

    if int(time_list[0]) == current_time_hour:
        if int(time_list[1]) == current_time_min:
            return False
        else:
            return True
    else:
        return True


def main():
    alarm_time = input("Enter time in 24 hours format: hh:mm\n")
    while alarm(alarm_time):
        pass
    print(f"Wake Up!!!")


if __name__ == "__main__":
    main()
