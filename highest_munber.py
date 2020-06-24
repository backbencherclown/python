a=int(input('enter first number : ' ))
b=int(input('enter second number : ' ))
c=int(input('enter third number : ' ))

if a>b :
    if a>c :
        gt=a
    else :
        gt=c
else :
     if b>c :
         gt=b
     else :
        gt=c

print('greatest number :',gt)