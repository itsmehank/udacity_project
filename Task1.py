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
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""

'''
def get_list(list):
    number_list = []
    for data in list:
        if data[0] not in number_list:
            number_list.append(data[0])
        if data[1] not in number_list:
            number_list.append(data[1])
    return number_list

def check_overlap(list_a,list_b):
    for number in list_a:
        if number in list_b:
            list_b.remove(number)
    final_list = list_a + list_b
    return(final_list)

def how_many_number(data1,data2):
    list1 = get_list(data1)
    list2 = get_list(data2)
    return ("There are "+ str(len(check_overlap(list1,list2))) + " different telephone numbers in the records.")

'''

def count_unique_number(data1, data2):
    unique_number = set()
    for i in data1 + data2:
        unique_number.add(i[0])
        unique_number.add(i[1])
    count_number = len(unique_number)
    return ("There are "+ str(count_number) + " different telephone numbers in the records.")

print(count_unique_number(texts,calls))


