id=int(input("enter the product id "))
pd=str(input("enter the product "))
cp=float(input("enter the cost price of the product "))
sp=float(input("enter the selling price of the product "))
qt=int(input("enter the quantity of the product "))
print("product name :",pd,"\nproduct id :",id,"\ncost price of the product :",cp,"\nselling price of the product :",sp,"\nquantity of the product :",qt)
profit=(sp-cp)*qt
print("profit =",profit)