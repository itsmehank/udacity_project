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
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""


def get_list(list):
    number_list = []
    for data in list:
        if data[0] not in number_list:
            number_list.append(data[0])
        if data[1] not in number_list:
            number_list.append(data[1])
    return number_list


def outg0_1ncome_list(list, int):
    number_list = []
    for data in list:
        if data[int] not in number_list:
            number_list.append(data[int])
    return number_list


def telemarket_num(textdata, calldata):
    text_list = get_list(textdata)
    outgo_call_list = outg0_1ncome_list(calldata, 0)
    income_call_list = outg0_1ncome_list(calldata,1)
    telemarket_list = []
    for num in outgo_call_list:
        if num not in text_list and num not in income_call_list:
            telemarket_list.append(num)
        elif num in text_list:
            text_list.remove(num)
        elif num in income_call_list:
            income_call_list.remove(num)
    telemarket_list.sort()        
    print ("These numbers could be telemarketers: ")
    for num in telemarket_list[:-1]:
        print (num)
    return telemarket_list[-1]    
        
print (telemarket_num(texts, calls))

