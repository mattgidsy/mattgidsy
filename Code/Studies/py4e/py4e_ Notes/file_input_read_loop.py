#find top 10 common words the long way
while True:
    try:
        file_name = input("Enter a file:")
        file_handle = open(file_name)
        print(file_handle.read())
        break
    except:
        print(file_name, "was not found. Please try again.")
        continue
#fhandle = open('romeo.txt')