import random
import time

target = ['H','e','l','l','o',' ','W','o','r','l','d']

final = ['','','','','','','','','','','']

count = 0

while target != final:
    if target[count] != final[count]:
        final[count] = chr(random.randint(32,122))
    
    if target[count] == final[count]:
        count += 1

    print(''.join(final), end = '\r')    
    time.sleep(0.05)   

print(''.join(final))     
        
