#ask user for date
month = int(input('Enter a month (1-12): '))
day = int(input('Enter a day (1-31): '))
#create accumulator so later if statements don't erroneously allow invalid dates:
valid = 0
#check month entered is a valid value:
if month > 12 :
    print()
    print('That\'s not a valid date!')
    valid += 1
elif month == 0 :
    print()
    print('That\'s not a valid date!')
    valid += 1
#check day is corect with the months
elif day == 0:
    print()
    print('That\'s not a valid date!')
    valid += 1
if month in (1, 3, 5, 7, 8, 10, 12) :
    if day > 31 :
        print()
        print('That\'s not a valid date!')
        valid += 1
elif month in (4, 6, 9, 11) :
    if day > 30 :
        print()
        print('That\'s not a valid date!')
        valid += 1
elif month == 2 :
    if day > 29:
        print()
        print('That\'s not a valid date!')
        valid += 1
#convert month to words
if month == 1:
    month_text = 'January'
elif month == 2:
    month_text = 'Febuary'
elif month == 3:
    month_text = 'March'
elif month == 4:
    month_text = 'April'
elif month == 5:
    month_text = 'May'
elif month == 6:
    month_text = 'June'
elif month == 7:
    month_text = 'July'
elif month == 8:
    month_text = 'August'
elif month == 9:
    month_text = 'September'
elif month == 10:
    month_text = 'October'
elif month == 11:
    month_text = 'November'
elif month == 12:
    month_text = 'December'
#Check for before september
if valid == 0 :
    if month < 9 :
        if month > 0:
            print(month_text, day, 'is before the start of the Fall 2016 term.')
#Check september
    elif month == 9:
        if day < 6:
            print(month_text, day, 'is before the start of the Fall 2016 term.')
        elif day == 6:
            print(month_text, day, 'is the beginning of the Fall 2016 term.')
        else:
            print(month_text, day, 'is not a holiday at NYU. NYU is open on this day.')
#check october
    elif month == 10 :
        if day == 10 :
            print(month_text, day, 'is Fall recess. NYU is not open on this day.')
        else :
            print(month_text, day, 'is not a holiday at NYU. NYU is open on this day.')
#check november
    elif month == 11 :
        if day < 23 :
            if day > 27 :
                print(month_text, day, 'is Thanksgiving recess. NYU is not open on this day.')
            else :
                print(month_text, day, 'is not a holiday at NYU. NYU is open on this day.')
        else :
            print(month_text, day, 'is not a holiday at NYU. NYU is open on this day.')
#check december
    elif month == 12 :
        if day < 16 :
            print(month_text, day, 'is not a holiday at NYU. NYU is open on this day.')
        if day == 16 :
            print(month_text, day, 'is the end of the Fall 2016 term.')
        else :
            print(month_text, day, 'is after the end of the Fall 2016 term.')

