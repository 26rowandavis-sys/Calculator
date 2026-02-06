#Find largest integer
myList = [1, 2, 3, 4, 5, 7, 9, 10, 20]
def largestInteger(inputList):
    largest = inputList[0]
    for item in inputList: 
        if item > largest:
            largest = item
    return largest

print(largestInteger(myList))
        
    