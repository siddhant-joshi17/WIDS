from datetime import datetime as dt
from sympy import symbols, diff

print("All dates are in format dd-mm-yyyy")
PD= input("Last traded (dirty) price = ")
PT= input("Face Value = ")
rC= input("Coupon rate = ")
m= input("Coupon frequency = ")
T= input("Maturity date = ")
t= input("Current date = ")
p= input("Recent past coupon payment date = ")
P= input("Next coupon payment date = ")


M_d=dt.strptime(T, "%d-%m-%Y").date()
C_d=dt.strptime(t, "%d-%m-%Y").date()
past_d=dt.strptime(p, "%d-%m-%Y").date()
next_d= dt.strptime(P, "%d-%m-%Y").date()
coupon= float(rC) *float(PT)
mm=(next_d-past_d).days

num=C_d-past_d
den=next_d-past_d
acc_int =float(num/den)*(coupon/(float (m)))
clean_price=float(PD)-acc_int
diff=M_d-past_d
diff2= diff.days
n= (int((diff2+1)/mm))

x= symbols('x')
sum=0
for i in range(1, n+1):
    sum+=(float(coupon)/float(m)) * x**i
f = (int(PT)) * x**n +sum - clean_price
print(f)
derivative = diff(f, x)


x_1=float(rC)
print(x_1)
for i in range(10):
    f_valued= f.subs(x,x_1)
    f2_valued= derivative.subs(x,x_1)
    x_2= x_1 - (f_valued/f2_valued)
    x_1=x_2
print(x_1)
rate= (1/x_1)-1
print(f"{rate*100}%")
