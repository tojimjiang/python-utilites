#Thesurus Text File Retrival
read_thesaurus = open('thesaurus.txt', 'r')
thesaurus_whole = read_thesaurus.read()
thesaurus_data = thesaurus_whole.split()
thesaurus_len = len(thesaurus_data)
#Dividing Thersurus By Alphabet via Groups [List or String Items]

#Key Location Dictonary [string or list]
thes_type = {}
#Storage Dictionaries
#List Dictionaries
thes_l = {}
#String Dicitonaries
thes_s = {}
#Thesaurus Word Count
word_count = 0

for x in range(0,len(thesaurus_data)-1):
#for x in range(1000,4000):
    entry = thesaurus_data[x].split(',')
    entry_len = len(entry)
    if entry_len == 2:
        thes_type[entry[0].lower()] = 's'        
    #String, only one entry
        thes_s[entry[0].lower()] = entry[1]
        word_count += 1
    elif entry_len > 2:
        thes_type[entry[0].lower()] = 'l' 
    #List Type Words:
        thes_l[entry[0].lower()] = entry[1:]
        word_count += 1

#Print Word Cunt:
print ('Word in thesaurus:', word_count)
print()
read_thesaurus.close()
                
#import random
import random

#Reading Lyric File
read_lyric = open('bieber_baby.txt', 'r')
lyric_whole = read_lyric.read()
lyric_whole_len = len(lyric_whole)
lyric_list = lyric_whole.split('\n')
lyric_list_len = len(lyric_list)
read_lyric.close()

#User Input:
valid_check = 0
while valid_check == 0:
    change_chance = input('Enter a % chance to change a word: ')
    try:
        if float(change_chance) > 1.0:
            print('Your value is too high, enter a decimal % from 0 - 1')
            print() 
        elif float(change_chance) < 0.0:
            print('Your value is too low, enter a decimal % from 0 - 1')
            print()
        else:
            print()
            break
    except:
        print('Please do not use the % sign when entering a value')
    print()
#Adjust Check Chance to 10000's
change_chance_int = float(change_chance)
adj_chance = 10000 * change_chance_int

#Change Words Here
while valid_check == 0:
    #Start processing the words
    for strings in range(0,lyric_list_len):
        current_string = lyric_list[strings]
        #String Clean up:
        current_string_len = len(current_string)
        temp_string = ''
        for chars in range(0,current_string_len):
            if current_string[chars].isalpha():
                temp_string += current_string[chars]
            elif current_string[chars].isspace():
                temp_string += current_string[chars]
        word_list = temp_string.split()
        for words in range(0, len(word_list)):
            current_word = word_list[words]
            if current_word in thes_type:
                random_chance = random.randint(1,10000)
                if adj_chance >= random_chance:
                    #identify if string type or list type
                    if thes_type[current_word] == 's':
                        print(thes_s[current_word].upper(), end = ' ')
                    elif thes_type[current_word] == 'l':
                        #find length of the items in list:
                        list_len = len(thes_l[current_word])
                        random_number = random.randint(0, list_len - 1)
                        print(thes_l[current_word][random_number].upper(),end = ' ')
                else:
                    print(current_word, end = ' ')
            else:
                print(current_word, end = ' ')
        print('\n', end='')
    break


