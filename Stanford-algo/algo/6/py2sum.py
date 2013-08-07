__author__ = 'ktisha'

data = set()
counter = 0
def find2sum(sum):
    print "sum, ", sum
    global counter
    for i in data:
        sum_i = sum - i
        if sum_i in data and sum_i != i:
            return True
    return False

if __name__ == "__main__":
    with open("data.txt") as source:
        for line in source:
            data.add(int(line))

    print "START"
    for i in xrange(-10000, 100001):
        if find2sum(i):
            counter += 1

    print counter
