def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here
    numbers = {}

    for array in arrays:
        for number in array:
            if number in numbers:
                numbers[number] +=1
            else:
                numbers[number] = 1

    length = len(arrays)

    result = []

    for number in numbers:
        if numbers[number] == length:
            result.append(number)
        
    # print(result)
    return result

# if one array has the duplicates??

if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))