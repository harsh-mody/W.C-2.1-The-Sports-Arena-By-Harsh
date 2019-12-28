n = 0
enteredValue = int(input("Please Enter The Value: "))
listOfValues = []
for n in range(0, 12):
    priceOfItem = pow(2, n)
    if enteredValue >= priceOfItem:
        listOfValues.append(priceOfItem)
        numberOfItemsInList = len(listOfValues)
        min_len = numberOfItemsInList + 1
        for start in range(0,numberOfItemsInList):
            curr_sum = listOfValues[start]
            if curr_sum > enteredValue:
                print("Error")
            for end in range(start+1,numberOfItemsInList):
                curr_sum += listOfValues[end]
                if curr_sum > enteredValue and (end - start + 1) < min_len:
                    min_len = (end - start + 1)
print(min_len)