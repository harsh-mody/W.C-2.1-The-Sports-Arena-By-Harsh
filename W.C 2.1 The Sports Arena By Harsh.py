import itertools
enteredValue = int(input("Please Enter The Value: "))
listOfValues = []
for n in range(0, 12):
    priceOfItem = pow(2, n)
    listOfValues.append(priceOfItem)
    numberOfItemsInList = len(listOfValues)
result = [seq for i in range(enteredValue, 0, -1) for seq in itertools.combinations(listOfValues, i) if sum(seq) == enteredValue]
for i in range(0, len(result)):
    if sum(result[i]) == enteredValue:
        resultI = result[i]
        print("The Least Number Of Items :", len(resultI))
