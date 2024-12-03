class TMatrix:
    def __init__(self):
        self.matrix = []

    def from_file(self, file):
        with open(file, 'r') as f:
            self.matrix = [list(map(int, line.split())) for line in f.readlines()]

    def from_list(self, matrix_list):
        self.matrix = matrix_list

    def get_element(self, i, j):
        return self.matrix[i][j]

    def vertices_count(self):
        return len(self.matrix)

    def events_count(self):
        return len(self.matrix[0]) if self.matrix else 0