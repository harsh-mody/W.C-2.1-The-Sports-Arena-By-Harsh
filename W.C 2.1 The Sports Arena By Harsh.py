import itertools
enteredValue = int(input("Please Enter The Value: "))
listOfValues = []
for n in range(0, 12):
    priceOfItem = pow(2, n)
    if enteredValue >= priceOfItem:
        listOfValues.append(priceOfItem)
        numberOfItemsInList = len(listOfValues)
result = [seq for i in range(len(listOfValues), 0, -1) for seq in itertools.combinations(listOfValues, i) if sum(seq) == enteredValue]
print(result)