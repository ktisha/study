__author__ = 'ktisha'

length = 200

def get_data(name):
    my_file = file(name)
    data = {}

    for i in xrange(1, length+1):
        data[i] = {}

    for line in my_file.readlines():
        vertex_line = line.split()
        for vertex_pair in vertex_line[1:]:
            vertex, weight = vertex_pair.split(",")
            a = data[int(vertex_line[0])]
            a[int(vertex)] = int(weight)
            data[int(vertex_line[0])] = a

    return data

def dijkstra(net, s, t):
    labels={}
    order={}
    for i in net.keys():
        if i == s: labels[i] = 0
        else: labels[i] = float("inf")
    from copy import copy
    drop1 = copy(labels)

    while len(drop1) > 0:

        minNode = min(drop1, key = drop1.get)

        for i in net[minNode]:
            if labels[i] > (labels[minNode] + net[minNode][i]):
                labels[i] = labels[minNode] + net[minNode][i]
                drop1[i] = labels[minNode] + net[minNode][i]
                order[i] = minNode
        del drop1[minNode]

    return labels[t]

def main():
    data = get_data("dijkstraData.txt")
    source = 1
    targets = [7,37,59,82,99,115,133,165,188,197]

    for target in targets:
        print str(dijkstra(data, source, target)) + ","

if __name__ == "__main__":
    main()