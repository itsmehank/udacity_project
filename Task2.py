"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""


def complete_dict(list):
    time_dict = dict()
    for data in list:
        time_dict[data[0]] = time_dict.get(data[0], 0) + int(data[3])
        time_dict[data[1]] = time_dict.get(data[1], 0) + int(data[3])
    return time_dict
    

def longest_number(dict):
    longest_num = 0
    longest_time = 0
    for key in dict:
        if dict[key] > longest_time or longest_time == 0:
            longest_time = dict[key]
            longest_num = key
    return  str(longest_num) + " spent the longest time, " + str(longest_time) + " seconds, on the phone during September 2016."



print(longest_number(complete_dict(calls)))
