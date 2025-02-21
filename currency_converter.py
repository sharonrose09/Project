# Simple Currency Converter

# Define a function for currency conversion
def convert_currency(amount, from_currency, to_currency, exchange_rate):
    converted_amount = amount * exchange_rate
    return converted_amount

# Example exchange rates (These are sample exchange rates, you can use real-time APIs like 'forex-python' or 'openexchangerates' for live rates)
exchange_rates = {
    'USD': {'EUR': 0.92, 'GBP': 0.81, 'INR': 83.14},
    'EUR': {'USD': 1.09, 'GBP': 0.88, 'INR': 90.34},
    'GBP': {'USD': 1.23, 'EUR': 1.14, 'INR': 102.32},
    'INR': {'USD': 0.012, 'EUR': 0.011, 'GBP': 0.0098}
}

# Input from user
amount = float(input("Enter amount to convert: "))
from_currency = input("Enter source currency (USD, EUR, GBP, INR): ").upper()
to_currency = input("Enter target currency (USD, EUR, GBP, INR): ").upper()

# Perform the conversion
if from_currency in exchange_rates and to_currency in exchange_rates[from_currency]:
    exchange_rate = exchange_rates[from_currency][to_currency]
    converted_amount = convert_currency(amount, from_currency, to_currency, exchange_rate)
    print(f"{amount} {from_currency} is equal to {converted_amount:.2f} {to_currency}")
else:
    print("Currency conversion rate not available.")
