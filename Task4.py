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

def get_tele(calls, texts):
    make_call=set()
    text_n_receive = set()
    for data in calls:
        make_call.add(data[0])
        text_n_receive.add(data[1])
    for data in texts:
        text_n_receive.add(data[0])
        text_n_receive.add(data[1])
    tele_set = make_call - (make_call & text_n_receive)
    tele_list= sorted(list(tele_set))
    print ("These numbers could be telemarketers: ")
    for num in tele_list[:-1]:
        print (num)
    return tele_list[-1]    


print(get_tele(calls,texts))





