class Node:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def calculate_g_cost(self, start_node):
        # Calculate the g cost from the start node to this node
        # Implementation goes here
        pass

    def calculate_h_cost(self, end_node):
        # Calculate the h cost from this node to the end node
        # Implementation goes here
        pass

    def calculate_f_cost(self, start_node, end_node):
        # Calculate the f cost (g cost + h cost) for this node
        # Implementation goes here
        pass
