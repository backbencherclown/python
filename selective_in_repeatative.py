c=0
for i in range (100,200) :
    if i%6==0 and i%7==0 :
        print(i)
        c+=i
print('total sum:',c)