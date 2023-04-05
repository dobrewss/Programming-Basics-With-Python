from math import ceil
serial_name = input()
episode_lenght = int(input())
break_lenght = int(input())

lunch_time = break_lenght / 8
leisure_time = break_lenght / 4

time_taken = lunch_time + leisure_time + episode_lenght
time_left = break_lenght - time_taken

if time_left >= 0:
    print(f"You have enough time to watch {serial_name} and left with {ceil(time_left)} minutes free time.")
else:
    print(f"You don't have enough time to watch {serial_name}, you need {ceil(abs(time_left))} more minutes.")