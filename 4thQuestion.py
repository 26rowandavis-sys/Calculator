myList = [1, 2, 12]
temp = myList [0]
myList.remove (temp)
myList.insert (0, myList[2])
myList.remove (myList [1])
myList.insert (2, myList [1])
myList.insert (1, temp)

print (myList)
