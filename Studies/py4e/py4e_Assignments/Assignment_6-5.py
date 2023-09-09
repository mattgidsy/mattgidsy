text = "X-DSPAM-Confidence:    0.8475"
number = text.find(" ")
fnumber = float(text[number+3:])
print(fnumber)
