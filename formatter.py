def number_to_currency(number):
    return "R${:,.2f}". format(number/100).replace(".","-").replace(",",".").replace("-",",")