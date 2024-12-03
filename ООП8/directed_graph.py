from matrix import TMatrix

class TDirectedGraph:
    def __init__(self):
        self.adjacency_matrix = TMatrix()

    def file_init(self, file):
        self.adjacency_matrix.from_file(file)

    def vertices_count(self):
        return self.adjacency_matrix.vertices_count()

    def get_adjacency_matrix_element(self, i, j):
        return self.adjacency_matrix.get_element(i, j)