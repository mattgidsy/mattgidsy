hrs = input("Enter Hours:")
h = float(hrs)
rate = input("Enter Pay Rate:")
r = float(rate)
othr = (h-40)
if h <= 40 :
    pay = (h*r)
else :
    pay = ((h*r)+(othr*r*.5))
print(pay)