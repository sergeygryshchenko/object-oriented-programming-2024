class TDirectedGraph:
    def __init__(self):
        self.adjacency_matrix = []

    def file_init(self, file):
        with open(file, 'r') as f:
            self.adjacency_matrix = [list(map(int, line.split())) for line in f.readlines()]

    def vertices_count(self):
        return len(self.adjacency_matrix)

    def get_element(self, i, j):
        return self.adjacency_matrix[i][j]