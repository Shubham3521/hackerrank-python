if __name__ == '__main__':
    list=[]
    N = int(input())
    for i in range(1,N+1):
        arrays = input("")
        values = arrays.split()
        a = values[0]
        if a == "append":
            b = int(values[1])
            list.append(b)
        elif a == "insert":
            b = int(values[1])
            c = int(values[2])
            list.insert(b,c)
            print(list)
        elif a == "sort":
            b = ""
            c = ""
            list.sort()
        elif a == "pop":
            b = ""
            c = ""
            list.pop()
        elif a == "reverse":
            b = ""
            c = ""
            list.reverse()
        elif a == "remove":
            b = int(values[1])
            c = ""
            list.remove(b)
        elif a == "print":
            b = ""
            c = ""
            print(list)
