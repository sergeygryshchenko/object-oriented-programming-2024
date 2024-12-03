from directed_graph import TDirectedGraph
from matrix import TMatrix

class TStateGraph(TDirectedGraph):
    def __init__(self):
        super().__init__()
        self.active_vertex = 0
        self.state_matrix = TMatrix()

    def file_init(self, file):
        self.state_matrix.from_file(file)
        self.init_adjacency_matrix()

    def events_count(self):
        return self.state_matrix.events_count()
    
    def get_state_matrix_element(self, i, j):
        return self.state_matrix.get_element(i, j)

    def vertices_count(self):
        return self.state_matrix.vertices_count()

    def set_active_vertex(self, vertex):
        if 0 <= vertex < self.vertices_count():
            self.active_vertex = vertex

    def process_event(self, event):
        if 0 <= event < self.events_count():
            new_active_vertex = self.get_state_matrix_element(self.active_vertex, event) - 1
            if 0 <= new_active_vertex < self.vertices_count():
                self.active_vertex = new_active_vertex

    def init_adjacency_matrix(self ):
        num_vertices = self.vertices_count()
        num_events = self.events_count()
        adjacency_matrix = [[0] * num_vertices for _ in range(num_vertices)]
        for i in range(num_vertices):
            for j in range(num_events):
                target_vertex = self.get_state_matrix_element(i,j) - 1
                if target_vertex != -1:
                    adjacency_matrix[i][target_vertex] = 1
        self.adjacency_matrix.from_list(adjacency_matrix)
