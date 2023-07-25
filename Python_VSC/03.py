def swap_case():
    st = input("Enter the string to be swapped: ")
    res = ""
    for x in st:
        if x.isupper():
            res = res + x.lower()
        elif x.islower():
            res = res + x.upper()
        else:
            res = res + x

    print(res)


swap_case()