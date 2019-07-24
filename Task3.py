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
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""

# Part A

def call_from(code, calls):
    code_set =set()
    for data in calls:
        if data[0][0] == '(' and data[0][1:4] == code:
            if data[1][0] == '(':
                temp =''
                for i in range(1,len(data[1])):
                    if data[1][i] != ')':
                       temp += data[1][i]
                    elif data[1][i] ==')':
                        break;
                code_set.add(temp)        
            elif data[1][0] == '7' or data[1][0] == '8' or data[1][0] == '9':
                code_set.add(data[1][0:4])          
            elif data[1][0:3] == '140':
                code_set.add('140')
    code_list = sorted(list(code_set))
    print ("The numbers called by people in Bangalore have codes:")
    for num in code_list[:-1]:
        print (num) 
    return code_list[-1]

print(call_from('080',calls))


print('\n')

# Part B

def percent_samearea(code):
    total_call = 0
    same_count = 0
    for data in calls:
        if data[0][0] == '(' and data[0][1:4] == code:
            if data[1][0] == '(' and data[1][1:4] == code:
                same_count += 1
            total_call += 1
    percent = round((same_count / total_call * 100),2)   
    return str(percent) + " percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore."


print(percent_samearea('080'))

