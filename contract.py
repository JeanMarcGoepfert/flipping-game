""" official contract
    signed by andy zhang
"""

from datetime import datetime

today = datetime.now()
deadline = datetime(2014, 3, 2)

def compare_dates(first_date, second_date):
    if today > deadline:
        return True
    else:
        return False

def does_andy_owe_jm_beers(val):
    if val == True:
        return "Andy - you owe jm beers. Go buy them"
    else:
        return "Andy - you will owe jm beers soon. Go buy them"

has_deadline_passed =  compare_dates(today, deadline)

print does_andy_owe_jm_beers(has_deadline_passed)