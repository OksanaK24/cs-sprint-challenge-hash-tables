def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here
    weight_dict = {}

    result = [None]*2

    if len(weights) <= 1:
        return None

    for i in range(0, len(weights)):
        if weights[i] not in weight_dict:
            weight_dict[weights[i]] = i
        else:
            current_value = weight_dict[weights[i]]
            weight_dict[weights[i]] = []
            weight_dict[weights[i]].append(current_value)
            weight_dict[weights[i]].append(i)

    # print(weight_dict)

    for weight in weight_dict:
        difference = limit - weight
        if difference == weight:
            # print(weight_dict[weight][0])
            if weight_dict[weight][0] > weight_dict[weight][1]:
                result[0] = weight_dict[weight][0]
                result[1] = weight_dict[weight][1]
            else:
                result[0] = weight_dict[weight][1]
                result[1] = weight_dict[weight][0]
        if difference in weight_dict and difference != weight:
            if weight_dict[difference] > weight_dict[weight]:
                result[0] = weight_dict[difference]
                result[1] = weight_dict[weight]
            else:
                result[0] = weight_dict[weight]
                result[1] = weight_dict[difference]
    # print(result)
    return result