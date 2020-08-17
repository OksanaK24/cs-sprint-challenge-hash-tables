# Your code here

def finder(files, queries):
    """
    YOUR CODE HERE
    """
    # Your code here
    result = []

    querie_dict = {}

    for querie in queries:
        querie_dict[querie] = ""

    for file in files:
        list_file = file.split("/")
        last_item = len(list_file) - 1
        if list_file[last_item] in querie_dict:
            result.append(file)

    # print(result)
    return result

if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))