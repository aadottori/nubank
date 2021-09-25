from pynubank import Nubank, MockHttpClient
import config
from json_handler import create_json
import types


#nu = Nubank(MockHttpClient())
nu = Nubank()
nu.authenticate_with_cert(config.login_info["user"], config.login_info["password"], config.login_info["authentication"])


def card_statements():
    return nu.get_card_statements()

def transactions():
    return nu.get_account_statements()

def bills():
    return nu.get_bills()

def card_feed():
    return nu.get_card_feed()

def card_payments():
    return nu.get_card_payments()

def customer():
    return nu.get_customer()

def bill_details(bill):
    return nu.get_bill_details(bill)

def account_feed():
    return nu.get_account_feed()

def account_statements():
    return nu.get_account_statements()

def account_balance():
    return nu.get_account_balance()

def account_investments_details():
    return nu.get_account_investments_details()

def account_investments_yield():
    return nu.get_account_investments_yield()

def available_pix_keys():
    return nu.get_available_pix_keys()


defined_functions = [f for f in globals().values() if type(f) == types.FunctionType]
functions_not_to_call = [create_json, bill_details]

for function in defined_functions:
    if function not in functions_not_to_call:
        create_json(function)
