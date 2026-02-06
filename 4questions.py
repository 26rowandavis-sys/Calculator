#find if all number in list are positive
myList = [1, 2, 3,4, 5, 6, 7, 8, 9, -10]

def allPositive(inputList):
    positive = True
    for item in inputList:
        if item < 0:
            positive = False
    return positive

print(allPositive(myList))


#Determine the greatest value
myList = [1, 2, 3, 4, 5, 7, 9, 10, 20]
def largestInteger(inputList):
    largest = inputList[0]
    for item in inputList: 
        if item > largest:
            largest = item
            return largest
        
    