def bubblesort(numbers):
    for y in range(len(numbers)):
        for x in range(len(numbers)-1):
            if numbers[x] > numbers[x+1]:
                numbers.insert(x+2,numbers[x])
                numbers.remove(numbers[x])
    return numbers
