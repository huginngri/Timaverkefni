hstoll = int(input("Input the cost of the item in $: "))
month = 1
while hstoll > 0:
    if hstoll > 1000:
        intrest = round(hstoll * 0.015, 2)
        jaja = 50.0
        payment = jaja - intrest
        hstoll -= payment
    elif hstoll <= 1000 and hstoll >49.26:
        intrest = round(hstoll * 0.015, 2)
        jaja = 50.0
        payment = jaja - intrest
        hstoll -= payment
    else:
        intrest = round(hstoll * 0.015, 2)
        jaja = hstoll
        payment = hstoll - intrest
        hstoll -= payment
    print("Month: ", month, "Payment: ", jaja, "Interests paid: ", intrest, "Remaining debt: ", hstoll )


    
