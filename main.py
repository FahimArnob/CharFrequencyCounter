# Takes an input from user

text = input('Paste the text here: ').lower().strip()
alphabets = 'abcdefghijklmnopqrstuvwxyz0123456789 ' # intentionally added white space
freq = [0 for _ in range(36)]

# Cornerstone of the App

for letter in text:
    if letter is not ' ':
        freq[alphabets.index(letter)] += 1
    elif letter is ' ':
        pass
    else:
        print('Bro I wanted just plain old simple text.\n')
        break

# Printing output

for l in alphabets:
    try:
        if freq[alphabets.index(l)] is 0:
            pass
        else:
            print(l, freq[alphabets.index(l)], sep=':')
    except:
        pass     # Little cheating cause you know me

print(end='Done')

# END OF CODE----------------------------------------------------------------------------------------------------------------
