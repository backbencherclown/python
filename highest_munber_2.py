a=int(input('enter first number : ' ))
b=int(input('enter second number : ' ))
c=int(input('enter third number : ' ))
if a>b and a>c :
    gt=a
elif b>c :
    gt=b
else :
    gt=c
print('high',gt)