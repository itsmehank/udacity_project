"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
TASK 0:
What is the first record of texts and what is the last record of calls?
Print messages:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""

def first_record(data):
    first_income = str(data[0][0])
    first_answer = str(data[0][1])
    first_time = str(data[0][2])
    if len(data[0]) == 3: data_name ='texts'
    else: data_name = 'calls'
    return ("First record of " + data_name+', ' + first_income + ' ' + data_name+ ' ' + first_answer + ' at time '+ first_time)
    
def last_record(data):
    last_income = str(data[-1][0])
    last_answer = str(data[-1][1])
    last_time = str(data[-1][2])
    if len(data[0]) == 3: data_name ='texts'
    else: data_name = 'calls'
    return ("Last record of " + data_name + ', ' + last_income + ' ' + data_name + ' ' + last_answer + ' at time '+ last_time)    


print (first_record(texts))
print (last_record(calls))
