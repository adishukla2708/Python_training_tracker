def for_loop():
    num = int(input('Enter a number: '))
    st = ""
    for i in range(1, num + 1):
        st = str(i) + st
    print(st)


for_loop()