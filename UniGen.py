import os
os.system("clear")
on=input('of: ')
os.system("clear")
onn=input('to: ')
for i in range(of, to):
    print(chr(i), end=' ')
    if (i - 1) % 10 == 0:
        print()
os.system("clear")
print()