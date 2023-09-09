rawstr = input('Enter a number:')
try:
    ival = float(rawstr)
except:
    print(rawstr, "is a word")
    quit()
if ival >=0 :
    print('Nice work')
else :
    print('Trixie Hobbitses')