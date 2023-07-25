def is_leap():
    year = int(input("Enter the year to be checked: "))

    if year % 400 == 0:
        print('Leap Year')
    elif year % 100 == 0:
        print('Non-Leap Year')
    elif year % 4 == 0:
        print('Leap Year')
    else:
        print('Non-Leap Year')


is_leap()