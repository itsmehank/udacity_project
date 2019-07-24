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

def first_text(data):
    first_income = str(data[0][0])
    first_answer = str(data[0][1])
    first_time = str(data[0][2])
    return ("First record of text " + first_income + ' texts ' + first_answer + ' at time '+ first_time)
    
def last_call(data):
    last_income = str(data[-1][0])
    last_answer = str(data[-1][1])
    last_time = str(data[-1][2])
    calling_time = str(data[-1][3])
    return ("Last record of calls " + last_income + ' calls ' + last_answer + ' at time '+ last_time + ", lasting " + calling_time + " seconds")    


print (first_text(texts))
print (last_call(calls))
