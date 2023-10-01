import math
class Vertex:
    """Vertex object that includes a list of labels and edges for the graph to use"""
    def __init__(self, label):
        self.label = label
        self.edges = {}
class Graph:
    def __init__(self):
        """initialization function for the graph's vertices"""         
        self.vertices = {}
        self.adj_list = {}

    def add_vertex(self, label):
        """adds a vertex to the graph for any given label"""         
        if not isinstance(label, str):
            raise ValueError("Label must be a string")
        if label in self.vertices:
            return self
        self.vertices[label] = Vertex(label)
        return self

    def add_edge(self, src, dest, w):
        """adds an edge to the graph that adds the source, destination path, and the weight of using said path"""
        if src not in self.vertices or dest not in self.vertices:
            raise ValueError("Source or destination not added to graph")
        if isinstance(w, str):
            raise ValueError("Weight must be \'int\' not \'str\' object")
        if w < 0:
            raise ValueError("Weight must be non-negative")
        self.vertices[src].edges[dest] = w
        return self

    def get_weight(self, src, dest):
        """retrives the weight of going from a specifc source to a destination"""         
        if src not in self.vertices or dest not in self.vertices:
            raise ValueError("Source or destination not added to graph")
        if dest in self.vertices[src].edges:
            return self.vertices[src].edges[dest]
        else:
            return math.inf

    def dfs(self, starting_vertex):
        """a function for traversing the graph in depth-first order starting from the specified vertex"""
        if starting_vertex not in self.vertices:
            raise ValueError("Starting vertex not added to graph")
        visited = set()
        stack = [starting_vertex]
        while stack:
            vertex = stack.pop()
            if vertex not in visited:
                visited.add(vertex)
                yield vertex
                for neighbor in self.vertices[vertex].edges:                     
                    stack.append(neighbor)

    def bfs(self, starting_vertex):
        """a function for traversing the graph in bredth-first order starting from the specified vertex"""
        if starting_vertex not in self.vertices:
            raise ValueError("Starting vertex not added to graph")
        visited = set()
        queue = [(starting_vertex, [starting_vertex])]
        while queue:
            vertex, path = queue.pop(0)
            if vertex not in visited:
                visited.add(vertex)
                yield vertex
                for neighbor in self.vertices[vertex].edges:
                    if neighbor not in path:
                        queue.append((neighbor, path + [neighbor]))

    def dsp(self, src, dest):
        """returns a tuple of the path length and lists the destination points in order to get from src to dest"""
        if src not in self.vertices or dest not in self.vertices:
            raise ValueError("Source or destination not added to graph")
        distances = {vertex: math.inf for vertex in self.vertices}
        distances[src] = 0
        prev_vertices = {}
        unvisited = set(self.vertices.keys())
        while unvisited:
            current = min(unvisited, key=lambda vertex: distances[vertex])             
            unvisited.remove(current)
            if distances[current] == math.inf:
                break
            for neighbor in self.vertices[current].edges:
                alt_distance = distances[current] + self.vertices[current].edges[neighbor]
                if alt_distance < distances[neighbor]:
                    distances[neighbor] = alt_distance
                    prev_vertices[neighbor] = current
        path = []
        current_vertex = dest
        while current_vertex != src:             
            path.append(current_vertex)
            if current_vertex not in prev_vertices:
                return math.inf, []
            current_vertex = prev_vertices[current_vertex]         
        path.append(src)
        path.reverse()
        return distances[dest], path

    def dsp_all(self, src):
        """Returns a dictionary of the shortest path between src and all other verticies using Dijkstra's Shortest Path algorithm"""
        if src not in self.vertices:
            raise ValueError("Starting vertex not added to graph")
        distances = {vertex: math.inf for vertex in self.vertices}
        distances[src] = 0
        prev_vertices = {}
        unvisited = set(self.vertices.keys())
        while unvisited:
            current = min(unvisited, key=lambda vertex: distances[vertex])             
            unvisited.remove(current)
            if distances[current] == math.inf:
                break
            for neighbor in self.vertices[current].edges:
                alt_distance = distances[current] + self.vertices[current].edges[neighbor]
                if alt_distance < distances[neighbor]:
                    distances[neighbor] = alt_distance
                    prev_vertices[neighbor] = current
        result = {}
        for vertex in distances:
            if distances[vertex] == math.inf:
                result[vertex] = []
            else:
                path = []
                current_vertex = vertex
                while current_vertex != src:                     
                    path.append(current_vertex)
                    current_vertex = prev_vertices[current_vertex]                 
                    path.append(src)
                path.reverse()
                result[vertex] = path
        return result

    def __str__(self):
        """returns a string representation of the graph using GraphViz dot notation"""
        result = """digraph G {\n"""
        for vertex in self.vertices.values():
            for dest, weight in vertex.edges.items():
                result += f"""   {vertex.label} -> {dest} [label=\"{str(float(weight))}\",weight=\"{str(float(weight))}\"];\n"""
        result += """}"""
        if '->' in result:
            return result