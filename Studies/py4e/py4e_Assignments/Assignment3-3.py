score = input("Enter a score between 0.0 and 1.0:")
try : 
    fscore = float(score)
except :
    print("There has been a silly error. Please try again.")
    quit()
if fscore >= 1.0 :
    print("Score is out of range (0.0 - 1.0). Please try again.")
    quit()    
elif fscore >= 0.9 :
    print("A")
elif fscore >= 0.8 :
    print("B")
elif fscore >= 0.7 :
    print("C")
elif fscore >= 0.6 :
    print("D")
else :
    print("F")