v=0
i=0
n=1

while n!=0:
    n=int(input('enter the marks: '))
    if n>0 and n<100 :
        v+=1
    else :
        i+=1
print('valid marks:',v,'\tinvalid marks:',i)