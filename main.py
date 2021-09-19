from pynubank import Nubank, MockHttpClient
import config
from json_handler import create_json


nu = Nubank(MockHttpClient())
nu.authenticate_with_qr_code(config.login_info["user"],
                            config.login_info["password"], 
                            config.login_info["authentication"])


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



create_json(card_statements)
create_json(card_feed)
create_json(card_payments)

create_json(transactions)
create_json(bills)

create_json(customer)

create_json(account_feed)
create_json(account_balance)
create_json(account_statements)
create_json(account_investments_details)
create_json(account_investments_yield)



