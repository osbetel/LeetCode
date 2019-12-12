#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'calculate_total_owed' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING_ARRAY actions as parameter.





def calculate_total_owed(actions):
    # Write your code here
    # key things to know:
    # actions is an array of lines (str)
    # RIP. This function is supposed to handle a list of multiple invoices

    total_owed = 0
    invoice_id = -1
    previous_line = None

    for line in actions:

        if not line.__contains__("currency=USD") and not line.startswith("PAY:"): continue

        line_dict = dict(zip(re.findall(r"\b(?!currency\b)[a-z]+", line),
                             re.findall(r"[0-9]+", line)))

        line_id = int(line_dict.get("id"))

        if invoice_id == -1:
            invoice_id = line_id
        elif line_id != invoice_id:
            continue


        if line.startswith("CREATE:"):
            if previous_line == "FINALIZE": continue
            total_owed += int(line_dict.get("amount"))
            previous_line = "CREATE"


        elif line.startswith("FINALIZE:"):
            if previous_line != "CREATE": continue # cannot be finalized unless invoice created with values
            total_owed = int(line_dict.get("amount"))
            previous_line = "FINALIZE"

        elif line.startswith("PAY:"):
            if previous_line != "FINALIZE": return total_owed # cannot be paid unless finalized

            if "amount" not in line_dict.keys():
                # "PAY: id=14" marks invoice 14 as fully paid,
                return 0
            else:
                # whereas "PAY: id=14&amount=300&currency=USD" simply pays off 300 of that invoice
                total_owed -= int(line_dict.get("amount"))
                return total_owed

        else:
            # assuming the line is invalid or not formatted as expected
            continue

    return total_owed

def sep_invoices(actions):
    invoices = {}
    for line in actions:

        line_dict = dict(zip(re.findall(r"\b(?!currency\b)[a-z]+", line),
                             re.findall(r"[0-9]+", line)))

        line_id = int(line_dict.get("id"))

        if line_id in invoices.keys():
            invoices.update({line_id: invoices.get(line_id).append(line)})
        else:
            invoices.update({line_id: [line]})




if __name__ == '__main__':
    actions = ["CREATE: id=13&amount=800&currency=USD",
               "FINALIZE: id=13&amount=500&currency=USD",
               "CREATE: id=12&amount=2800&currency=USD",
               "CREATE: id=14&amount=800&currency=USD",
               "FINALIZE: id=14&amount=500&currency=USD",
               "CREATE: id=14&amount=2800&currency=USD"
               ]
    print(sep_invoices(actions))

    # print(calculate_total_owed(actions))



