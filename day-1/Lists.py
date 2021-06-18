list = []
no_times = int(input("Enter number of operations you want to perform: "))

for i in range(1,no_times+1):
    function = input("Enter the function: ")
    if function == "append":
        digit = int(input("Enter the digit to append: "))
        list.append(digit)
    elif function == "insert":
        digit = int(input("Enter the digit to insert: "))
        position = int(input("Enter the position to insert digin in array: "))
        list.insert(position,digit)
    elif function == "sort":
        list.sort()
    elif function == "pop":
        list.pop()
    elif function == "reverse":
        list.reverse()
    elif function == "remove":
        digit = int(input("Enter the digit to renove: "))
        list.remove(digit)
    elif function == "print":
        print(list)


    

