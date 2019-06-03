#created vairable that control while loops
columns = 0
allowed_c = 0
allowed_d = 0
printed_top = 0
#ask for columns
while allowed_c != 1:
    columns = int(input('How many columns? '))
    if columns > 0:
        allowed_c += 1
    else:
        print('Invalid entry, try again!')
#ask for side
while allowed_d != 1:
    direction = input('Direction? (l)eft or (r)ight: ')
    if direction == 'l':
        allowed_d += 1
    elif direction == 'r':
        allowed_d += 1
    else:
        print('Invalid entry, try again!')

#print result using string addition
#pointing right
if direction == 'r':
    while columns != printed_top:
        print(' ' * printed_top, '*', sep='')
        printed_top += 1
    #This results in spacing being 2 more than necessary so subtract 2
    printed_top -= 2
    while printed_top > -1:
        print(' ' * printed_top, '*', sep='')
        printed_top -= 1
#pointing left
if direction == 'l':
    printed_top = columns - 1
    while printed_top != 0:
        print(' ' * printed_top, '*', sep='')
        printed_top -= 1
        #we did not print a zero spaced start so we just have it run first.
    while printed_top != columns:
        print(' ' * printed_top, '*', sep='')
        printed_top += 1
