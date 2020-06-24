h=int(input("enter the hr : "))
if 1 < h < 12 :
   print("valid")

else:
    print("not valid")
m=int(input("enter the min : "))
if 0 < h < 59 :
   print("valid")

else:
    print("not valid")
s=int(input("enter the sec : "))
if 0 < h < 59 :
   print("valid")

else:
    print("not valid")

s+=10
if s>=60 :
    m+=1
    s-=60
    if m>=60 :
        h+=1
        m-=60
        if h>=12 :
            h-=12

print(h,m,s)