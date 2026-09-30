def findSum (num):
    if(num == -1):
        return 0
    return findSum(num-1) + num

print("The Sum of First Five Numbers is : ", findSum(5))

list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def printList (indx):
    if(indx > len(list)-1):
        return
    print(list[indx])
    printList(indx + 1)

printList(0)