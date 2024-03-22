import uuid
import networkx as nx
import matplotlib.pyplot as plt

class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color  
        self.id = str(uuid.uuid4()) 
        self.heap_value = key 

def min_heapify(node):
    smallest = node
    if node.left is not None and node.left.heap_value < smallest.heap_value:
        smallest = node.left
    if node.right is not None and node.right.heap_value < smallest.heap_value:
        smallest = node.right
    if smallest != node:
        node.heap_value, smallest.heap_value = smallest.heap_value, node.heap_value
        min_heapify(smallest)

def build_min_heap(root):
    if root is None:
        return
    build_min_heap(root.left)
    build_min_heap(root.right)
    min_heapify(root)

def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)  
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph

def draw_min_heap(heap_root):
    heap = nx.DiGraph()
    pos = {heap_root.id: (0, 0)}
    heap = add_edges(heap, heap_root, pos)

    colors = [node[1]['color'] for node in heap.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in heap.nodes(data=True)}  

    plt.figure(figsize=(8, 5))
    nx.draw(heap, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()


heap_root = Node(4)
heap_root.left = Node(10)
heap_root.right = Node(5)
heap_root.left.left = Node(15)
heap_root.left.right = Node(20)
heap_root.right.left = Node(30)

build_min_heap(heap_root)

draw_min_heap(heap_root)
