def most_frequent(string):
    frequency = {}
    string = string.lower()
    for char in string:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1

    sorted_frequency = sorted(frequency.items(), key=lambda x: x[1], reverse=True)
    for item in sorted_frequency:
        print(item[0], "=", item[1])

string=input("Please enter a string: ")
most_frequent("mississippi")
