def coutinue(cont):
    if cont == 'y':
        return 0
    else:
        return 1

def share_num(num):
    while True:
        try:
            num = input("Enter number of shares: ")
            quant_share = int(num)
            break
        except:
            print("Invalid number!")
    return quant_share

def price_share(num):
    while True:
        try:
            flott = input("Enter price (dollars, numerator, denominator): ")
            a, b, c = flott.split()
            int(a)
            int(b)
            int(c)
            break
        except:
            print("Invalid price!")
    return flott

def total_price(num, price):
    a,b,c = price.split()
    aa = int(a)
    bb = int(b)
    cc = int(c)
    return num*(aa+(bb/cc))

def printer(num, tot, stri):
    a,b,c = stri.split()
    print(num, 'shares with market price', a, '{}/{} have value ${:.2f}'.format(b,c,tot))
    return 1

n = 0
d = 0

while n == 0:
    bla = share_num(0)
    bla1 = price_share(0)
    bla2 = total_price(bla, bla1)
    bla3 = printer(bla, bla2, bla1) 
    n = coutinue(input("Continue: "))