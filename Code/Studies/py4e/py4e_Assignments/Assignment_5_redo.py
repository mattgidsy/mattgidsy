num_list = list()
while True:
    num = input("input an integer:")
    if num == "done!":
        print( "maximum is:", max(num_list))
        print("minimum is:", min(num_list))
        break
    else:
        try:
            num = int(num)
            num_list.append(num)
        except:
            print(num, "is not a valid input. Try again.")
            continue    