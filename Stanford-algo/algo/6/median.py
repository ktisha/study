__author__ = 'ktisha'
import heapq

heap_low = []
heap_high = []

def median_insert(x):
    global heap_low, heap_high

    if len(heap_low) == 0:
        heapq.heappush(heap_low, -x)
    else:
        m = -heap_low[0]
        if x > m:
            heapq.heappush(heap_high, x)
            if len(heap_high) > len(heap_low):
                y = heapq.heappop(heap_high)
                heapq.heappush(heap_low, -y)
        else:
            heapq.heappush(heap_low, -x)
            if len(heap_low) - len(heap_high) > 1:
                y = -heapq.heappop(heap_low)
                heapq.heappush(heap_high, y)

    return -heap_low[0]


def main():
    lines = open('Median.txt').read().splitlines()
    data = map(lambda x: int(x), lines)
    medians = []

    for x in data:
        median = median_insert(x)
        medians.append(median)

    print(reduce(lambda x,y: (x+y) % 10000, medians))


if __name__ == '__main__':
    main()
