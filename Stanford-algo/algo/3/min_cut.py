__author__ = 'catherine'

from random import randint

def get_data(name):
  my_file = file(name)
  data = {}

  for i in xrange(1, 41):
    data[str(i)] = []

  for line in my_file.readlines():
    vertexes = line.split()
    for v in vertexes[1:]:
      data[vertexes[0]].append(v)
  return data


def get_random(size):
  return randint(1, size)


def get_edge(data, index):
  for vertex, arr in data.items():
    if len(arr) > index:
      return vertex, arr[index]
    else:
      index -= len(arr)

def get_edge_count(data):
  edge_count = 0
  for item in data.values():
    edge_count += len(item)
  return edge_count

def remove_duplicates(list):
  seen = set()
  seen_add = seen.add
  return [ x for x in list if x not in seen and not seen_add(x)]

def remove_loop(list, v):
  for vertex in list:
    if vertex == v:
      list.remove(vertex)
  return list

def min_cut(data):

  while len(data) > 2:
    edge_count = get_edge_count(data)

    random = get_random(edge_count-1)
    edge = get_edge(data, random)

    v1 = edge[0]
    v2 = edge[1]

    data[v1] = [x for x in data[v1] if x != v2 ]

    for v in data[v2]:
      if v != v1:
        data[v1].append(v)
      data[v] = [x if x != v2 else v1 for x in data[v]]

    del data[v2]

  return get_edge_count(data)/2


if __name__ == "__main__":
  import sys
  minimum_cut = sys.maxint

  for i in xrange(64000):
    data = get_data("data")
    min = min_cut(data)
    if min < minimum_cut:
      minimum_cut = min

  print minimum_cut