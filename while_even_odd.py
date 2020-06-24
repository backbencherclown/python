e=0
o=0
n=1

while n!=0 :
    n=int(input('enter the number: '))
    if n%2==0 :
        e+=1
    else :
        o+=1

print('odd:',o,'\teven',e)