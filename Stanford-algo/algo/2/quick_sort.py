__author__ = 'catherine'
comparisons = 0

def get_data(name):
  my_file = file(name)
  data = []

  for x in my_file.readlines():
    data.append(int(x))
  return data

def swap(data, i, j):
  data[i], data[j] = data[j], data[i]


def partition(data, left, right, pivot):
  swap(data, left, pivot)

  p = data[left]
  i = left + 1
  for j in xrange(left + 1, right):
    if data[j]  < p:
      data[i], data[j] = data[j], data[i]
      i += 1

  data[i-1], data[left] = data[left], data[i-1]
  return i-1

def pick_pivot(data, left, right):
  middle = left + (right - left  - 1) / 2

  m = [(left, data[left]), (right - 1, data[right - 1]), (middle, data[middle])]
  m = sorted(m, key=lambda x: x[1])
  return m[1][0]

  #return left
  #return right - 1

def quick_sort(data, left, right):
  if right - left <= 1: return 0
  pivot = pick_pivot(data, left, right)
  index = partition(data, left, right, pivot)
  count = right - left - 1

#  print index
  count += quick_sort(data, left, index)
  count += quick_sort(data, index+1, right)

  return count



if __name__ == "__main__":
  data = get_data("array.txt")
  count = quick_sort(data, 0, len(data))
  print count