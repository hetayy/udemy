# Money in wallet
money_in_wallet = 40

print(money_in_wallet)

# Net price of sweets
sweets_price = 7.50

# Calculating tax
sales_tax = 0.2 * sweets_price

# Calculating gross price (adding tax to the net price of sweets)
sweets_price += sales_tax

# Updating money in wallet
money_in_wallet -= sweets_price

print(money_in_wallet)