import sys
import os
import time



def encode(mess):
    if not mess:
        return "error, empty input"
    old = mess[0]
    count = 1
    res = []
    for c in mess[1:]:
        if c == old:
            count += 1
        else:
            res.append(f'{count}{old}')
            count = 1
            old = c
    res.append(f'{count}{old}')
    #print(mess)
    return ''.join(res)

    
    
def decode(mess):
    res = ''
    count = 0
    for c in mess:
        if c.isdigit():
            count = count*10 + int(c)
        else:
            res += c*count
            count = 0
    return  res



if __name__ == '__main__':
    argv = sys.argv
   #time.sleep(1)
    #print(argv)
    if argv[1] == "-d":
        print (decode(argv[2]))
    if argv[1] == "-e":
        with open(argv[2],'r') as f:
            print(encode(f.read()))
    exit(0)
    
    
    