__author__ = 'catherine'

def get_data(name):
    my_file = file(name)
    data = []

    for x in my_file.readlines():
        data.append(int(x))
    return data

def merge_and_count(left, right):
    result = []
    i = 0
    j = 0
    count = 0
    while i != len(left) or j != len(right):
        if i == len(left):
            result.append(right[j])
            j += 1
        elif j == len(right):
            result.append(left[i])
            i += 1
        elif left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
            count += len(left) - i
    return result, count

def merge_sort(array):
    my_count = 0
    if len(array) <= 1:
        return array, my_count
    else:
        middle = len(array)/2
        left = array[:middle]
        left, i = merge_sort(left)
#        print "left ", i
        my_count += i
        right = array[middle:]
        right, i = merge_sort(right)
#        print "right ", i
        my_count += i
        result, count = merge_and_count(left, right)
        my_count += count
#        print "merge ", count
        return result, my_count


if __name__ == "__main__":
    data = get_data("integerArray.txt")
    print data
    result, count = merge_sort(data)
    print result
    print count

#    ind = len(data)
#    count = 0
#    for i in xrange(ind):
#        for j in xrange(i+1, ind):
#            if data[j] < data[i]:
#                count += 1
#    print count