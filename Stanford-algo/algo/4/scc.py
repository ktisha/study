__author__ = 'catherine'
length = 875714

class Vertex:
    def __init__(self):
        self.out_edges = set()
        self.in_edges = set()
        self.time = 0
        self.leader = None
        self.explored = False

    def add_in_edge(self, index):
        self.in_edges.add(index)

    def add_out_edge(self, index):
        self.out_edges.add(index)

    def revert(self):
        tmp = self.in_edges
        self.in_edges = self.out_edges
        self.out_edges = tmp

    def __repr__(self):
        return str(self.time)

def get_data(name):
    my_file = file(name)
    data = []

    for i in xrange(length):
        data.append(Vertex())

    for line in my_file.readlines():
        vertexes = line.split()

        data[int(vertexes[0])-1].add_out_edge(int(vertexes[1])-1)
        data[int(vertexes[1])-1].add_in_edge(int(vertexes[0])-1)

    return data


def revert_graph(data):
    for vertex in data:
        vertex.revert()
        vertex.explored = False


t = 0
s = None

def dfs_loop(graph, indexes):
    global s
    global t

    for i in indexes[::-1]:
        vertex = graph[i]
        if not vertex.explored:
            s = vertex
            dfs(graph, vertex)


def dfs(graph, vertex):
    global s
    global t
#    print vertex
#    print graph.index(vertex)
    vertex.explored = True
    vertex.leader = s

    for out_index in vertex.in_edges:
        vertex_ = graph[out_index]
        if not vertex_.explored:
            dfs(graph, vertex_)
    t += 1
    vertex.time = t



def main():
    global s
    global t
    s = None
    t = 0
    data = get_data("data.txt")

    revert_graph(data)

    indexes = range(length)

    dfs_loop(data, indexes)
    revert_graph(data)
#
    s = None
    t = 0
#    print indexes
#    print data
    indexes.sort(key=lambda x:data[x].time)
#
#    print indexes
    dfs_loop(data, indexes)

    leaders = [0 for i in range(length)]
    for v in data:
        leaders[data.index(v.leader)] +=1

    print leaders

if __name__ == "__main__":
    import threading, sys
    threading.stack_size(67108864) # 64MB stack
    sys.setrecursionlimit(2 ** 20)  # approx 1 million recursions
    thread = threading.Thread(target = main) # instantiate thread object
    thread.start() # run program at target