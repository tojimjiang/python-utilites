error_code_1a = 0
error_code_1b = 0
allow_user = 0
while allow_user != 6:
    global username
    username = str(input('Please enter a username: '))
    count_upper = 0
    count_lower = 0
    user_len = len(username)
    if user_len <= 7:
        error_code_1a = 1 #too short
    elif user_len >=16:
        error_code_1a = 2 #too long
    if username.isalnum():
        error_code_1a = 0 #is alphanumeric
    else:
        error_code_1a = 3 #is NOT alphanumeric
    if username.isalpha():
        error_code_1a = 4 #no numbers
    if username[0].isnumeric():
        error_code_1a = 5 #first is number
    elif username[user_len-1].isnumeric():
        error_code_1a = 6 #last is number
    if username.isupper():
        error_code_1a = 7 #no lowercase
    elif username.islower():
        error_code_1a = 8 #no uppercase

    print(error_code_1a)
    #print out from error codes:
    if error_code_1a == 1:
        print('Username must be between 8 and 15 characters.')
    elif error_code_1a == 2:
        print('Username must be between 8 and 15 characters.')
    elif error_code_1a == 3:
        print('Username must contain only alphanumeric characters.')
    elif error_code_1a == 4:
        print('Username must contain at least one numeric character.')
    elif error_code_1a == 5:
        print('First / last character in username cannot be numeric.')
    elif error_code_1a == 6:
        print('First / last character in username cannot be numeric.')
    elif error_code_1a == 7:
        print('Username must contain at least one lowercase character.')
    elif error_code_1a == 8:
        print('Username must contain at least one uppercase character.')
    elif error_code_1a == 0:
        print('Username is valid!')
        break
    else:
        print('Error - Input Correction')
    error_code_1a = 0
    print()
    
#password validator
while allow_user != 6:
    global password
    password = str(input('Please enter a password: '))
    passc_valid = 0
    passc_inval = 0
    passc_lower = 0
    passc_spec = 0
    passc_num = 0
    error_code_1b = 0
    pass_len = len(password)
    if pass_len <= 7:
        error_code_1b = 1 #too short
    if password.isalnum():
        error_code_1b = 3 #no symbols
    if password.isalpha():
        error_code_1b = 4 #no numbers
    if password.isupper():
        error_code_1b = 7 #no lowercase
    elif password.islower():
        error_code_1b = 8 #no uppercase
    for x in range(0,pass_len):
        if ord(password[x]) == 35 or ord(password[x]) == 36 or ord(password[x]) == 37 or ord(password[x]) == 38:
            passc_spec += 1
        elif password[x].isalnum():
            passc_valid += 1
        else:
            passc_inval += 1
    if passc_spec == 0:
        error_code_1b = 11 #no specials
    if passc_inval != 0:
        error_code_1b = 9 #invaild chars exist
    user_in_pass = password.count(username)
    if user_in_pass != 0:
        error_code_1b = 12 #username is in password
    print( error_code_1b)
    #print out from error codes:   
    if error_code_1b == 1:
        print('Password must be at least 8 characters long.')
    elif error_code_1b == 3:
        print('Password must contain at least one \'special\' character.')
    elif error_code_1b == 4:
        print('Password must contain at least one numeric character.')
    elif error_code_1b == 7:
        print('Username must contain at least one lowercase character.')
    elif error_code_1b == 8:
        print('Username must contain at least one uppercase character.')
    elif error_code_1b == 9:
        print('Password contains atleast one invalid character.')
    elif error_code_1b == 11:
        print('Password must contain atleast one \'special\' character.')
    elif error_code_1b == 12:
        print('Cannot use part of your username in your password')
    elif error_code_1b == 0:
        print('Password is valid!')
        break
    else:
        print('Error - Input Correction')
    print()
