n = int(input("Saisissez un nombre entier: "))

symbol = '*'
space = " "
for i in range(0,n):
    print(f"{(n-1)*space}{symbol} {symbol}")
    symbol = symbol + '*'