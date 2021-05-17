import progressbar
import random 
import string

ascii = string.ascii_letters + string.digits + '{$+,’^>?!|{!£>¥}!]$#+!}!¥'

phrase = ""

long = int(input("Quanto lunga deve essere? "))

for i in progressbar.progressbar(range(long)):
    phrase = phrase + random.choice(ascii)

print(phrase)
