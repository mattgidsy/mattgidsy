#prompt for hours and rate
#input data will be 45hr and 10.50 rate
#pay should be 1x rate <= 40hr and 1.5x > 40hr
#input to read string and float() to convert to number
#errorchecking jfc

hrs = input("Enter Hours:")
rate = input("Enter Rate of Pay:")
try:
    h = float(hrs)
    r = float(rate)
except:
    print("There has been a silly error. Please enter a numeric value.")
    quit()
ohr = (h - 40)
orate = (r*1.5)
     
def computepay(payrate):
    if payrate > 40 : 
        total = ((ohr*orate)+(40*r))
        return total
    else :
        total = (h*r)
        return total
       
print("Pay", computepay(h))