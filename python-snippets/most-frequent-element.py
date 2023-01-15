# Get most frequent element in list

def most_frequent(list):
    return max(set(list), key = list.count)

numbers = [1,1,1,2,3,3,4]
print(most_frequent(numbers))
