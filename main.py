from graph import Graph
import math

def main():
    """runs the main code"""     
    graph = Graph()
# Add vertices
    graph.add_vertex('A')     
    graph.add_vertex('B')     
    graph.add_vertex('C')     
    graph.add_vertex('D')     
    graph.add_vertex('E')     
    graph.add_vertex('F')
# Add edges with weights
    graph.add_edge('A', 'B', 2.0)     
    graph.add_edge('A', 'F', 9.0)     
    graph.add_edge('B', 'C', 8.0)     
    graph.add_edge('B', 'D', 15.0)     
    graph.add_edge('B', 'F', 6.0)     
    graph.add_edge('C', 'D', 1.0)
    graph.add_edge('E', 'C', 7.0)     
    graph.add_edge('E', 'D', 3.0)     
    graph.add_edge('F', 'B', 6.0)     
    graph.add_edge('F', 'E', 3.0)
    print(graph)
    print("\nstarting BFS with vertex A")     
    for vertex in graph.bfs("A"):
        print(vertex, end = "")     
        print()
    print("\nstarting DFS with vertex A")     
    for vertex in graph.dfs("A"):
        print(vertex, end = "")     
        print('\n')
# Assuming the graph object has been created and populated with vertices and edges
    for vertexa in graph.vertices:
        path_length, path_vertices = graph.dsp('A', vertexa)
        if path_length == math.inf:
            print(f"No path exists between vertex A and vertex {vertexa}")         
        else:
            path_str = ' -> '.join(path_vertices)
            print(f"The shortest path from vertex A to vertex {vertexa} is {path_str}, with a path length of {path_length}")

if __name__ == '__main__':     
    main()
