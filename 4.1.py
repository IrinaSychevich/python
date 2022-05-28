from sys import argv
script_name, hourly_rate, time, reward = argv
def salary():
    return int(hourly_rate) * int(time) + int(reward)
print(salary())