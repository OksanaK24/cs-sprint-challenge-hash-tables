
def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here
    result = []

    negatives = {}
    a.sort()
    for num in a:
        if num < 0:
            negatives[-num] = num
        if num > 0 and num in negatives:
            result.append(num)

    # print(negatives)
    # print(result)
    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))