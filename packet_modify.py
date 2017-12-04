##############################################################
# packet_modify.py
# menocu
# march 2016
#
# Read the data section of a tcp packet from the fs,
# and perform some arbitrary modifications to it 
#
##############################################################

import os
import sys
import random

# shuffle words, don't mess with the error bytes
def shuffle_words(foo):
    err_bytes = foo[-4:]
    foo = foo[:-4]
    words = foo.split(' ')
    random.shuffle(words)
    words = ' '.join(words)
    return words + err_bytes

# shuffle chars within words, don't mess with the error bytes
def shuffle_chars(foo):
    err_bytes = foo[-4:]
    foo = foo[:-4]
    
    words = foo.split(' ')
    l = []
    for word in words:
        wrdlst = list(word)
        random.shuffle(wrdlst)
        l.append(''.join(wrdlst))
    
    words = ' '.join(l)
    return words + err_bytes

#def insert_error_bytes(foo):
#    num_chars = len(foo)
#    num_words = len(foo.split(' '))    
#    foo = foo + chr(num_words)
#    foo = foo + chr(num_chars)
#    return foo

# Read packet data in from the location 
# provided in the first arg, then 
# delete the file.

data = ""
with open(sys.argv[1], 'r') as f:
    data = f.read()
os.remove(sys.argv[1])

#data[9] = str(int(data[9]) + 1);


#case = random.randrange(3)

# The first three cases will mess with the 
# packet content, but it will still pass validation
#if case == 0:
#    data = shuffle_words(data)
#elif case == 1:
#    data = shuffle_chars(data)
#elif case == 2:
#    data = shuffle_chars(data)
#    data = shuffle_words(data)
    
# replace the packet with the message that will
# get the 'flag' from the server
#elif case == 3: 
#    data = insert_error_bytes("ICE ICE BABY")

# Mess the packet up, get an error back.    
#else: 
#    data = data[:5] + "Pizza party " + data[5:]

#write to stdout and we're done

#bjnp = "BJNP"
#data = bjnp + data
#print(data)
sys.stdout.write(data)