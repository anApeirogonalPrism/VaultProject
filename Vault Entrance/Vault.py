from io import FileIO
import os

password = 20111128
chances = 3
t_chances = 0

print('Enter the password.')
attempt = input()
if attempt := password:
    os.startfile(r'C:\Users\user\Downloads\TORREZ ONLY\DONOTOPEN.html')
elif attempt != password:
    chances -= 1
    t_chances += 1
    print('Enter the password. (' + chances + 'chances remaining)')
elif attempt != password:
    chances -= 1
    t_chances += 1
    print('Enter the password. (' + chances + 'chances remaining)')
elif attempt != password:
    chances -= 1
    t_chances += 1
    print('Enter the password. (' + chances + 'chances remaining)')
    if chances := 0:
        print('GET OUT OF HERE!')
    # 2 auth system login verification
    elif t_chances := 3:
        print('GET OUT OF HERE!')