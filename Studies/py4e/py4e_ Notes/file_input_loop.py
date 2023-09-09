#find top 10 common words the long way
while True:
    file_name = input("Enter a file:")
    if file_name == 'romeo.txt':
        file_handle = open(file_name)
        print(file_handle.read())
    else:
        print("Unsupported file. Please try again" )
    continue
#fhandle = open('romeo.txt')