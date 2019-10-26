# wordlist generator
# python 3

import random
import string


length = int(input("How many characters in your passwords? \n"))
numofpwds = int(input("How many passwords to generate? \n"))

#open the text file
file1 = open(str(length) + "chars" + ".txt","a") 

#generate and write random pwds
for newentry in range(numofpwds):
    pwd = ""
    count = 0
    while count != length:

        upper = [random.choice(string.ascii_uppercase)]
        lower = [random.choice(string.ascii_lowercase)]
        num = [random.choice(string.digits)]
        symbol = [random.choice(string.punctuation)]
        everything = upper + lower + num + symbol

        pwd += random.choice(everything)
        count += 1
        continue

    if count == length:
        #print(pwd)
        file1.write(pwd + "\n")

file1.close()

print('Finished')

# using input to keep cmd window from closing
# input()
