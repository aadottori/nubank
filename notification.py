import requests
import info_getter
import os
from dotenv import load_dotenv

load_dotenv()

card_bills = info_getter.get_card_bills()

base_url = "https://alertzy.app/send"
accountKey = os.getenv("accountKey")

title = "Resumo Nubank"
message = f"Cartão Antonio: {card_bills['antonio']} \n Cartão Milla: {card_bills['milla']} \n Total: {card_bills['total']}"

url = f"{base_url}?accountKey={accountKey}&title={title}&message={message}"

requests.post(url)