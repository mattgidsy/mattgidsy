#repeatedly asks users for numbers until the user enters done
#once done is entered, print out the total, count and average of the numbers
#use a try and except to print an error message if the wrong value is entered
#the program must continue to prompt after error

count = 0
total = 0.0
# This is an infinite loop bc we will end it with 'done'
while True :
    strval = input('Enter a number: ')
    if strval == 'done' :
        break
    try :
        fval = float(strval)
    except :
        print("Error detected. Try again.")
        continue
    count = count + 1
    total = total + fval
print (total,count,total/count)