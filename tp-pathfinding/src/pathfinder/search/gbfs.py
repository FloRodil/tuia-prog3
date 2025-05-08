from ..models.grid import Grid
from ..models.frontier import PriorityQueueFrontier
from ..models.solution import NoSolution, Solution
from ..models.node import Node


class GreedyBestFirstSearch:
    @staticmethod
    def search(grid: Grid) -> Solution:
        """Find path between two points in a grid using Greedy Best First Search

        Args:
            grid (Grid): Grid of points
            h: función heurística

        Returns:
            Solution: Solution found
        """
        # Initialize a node with the initial position
        node = Node("", grid.start, 0)
        #print(grid.end)

        # Inicializar frontera (Cola prioridad) 
        frontier = PriorityQueueFrontier()

        # Encolar el nodo inicial
        node.manhattan_distance(grid.end)
        frontier.add(node, node.estimated_distance)

        # Initialize the reached dictionary to be empty
        reached = {} 
        
        # Add the node to the reached dictionary
        reached[node.state] = node.estimated_distance
        #print(reached)

        # Bucle while, se ejecuta mientras la frontera no esté vacía
        while frontier:
                # Retorno si la frontera está vacía
                # if frontier.is_empty():
                #     return NoSolution(reached)
                
                # Remover un nodo de la frontera, el de menor valor de heurística
                node = frontier.pop()
                #print(f"Desencolando nodo: {node.state}, h={node.estimated_distance}")

                # Aplicar test-objetivo al nuevo nodo
                if node.state == grid.end:
                    return Solution(node, reached)
                
                # Se buscan todos los sucesores del nodo actual
                successors = grid.get_neighbours(node.state)
                for a in successors:
                    new_state = successors[a]
                    #print (new_state)
                    # Se calcula el costo acumulado para evitar ciclos, no para decidir cuál nodo expandir
                    new_cost = node.cost + grid.get_cost(new_state) 
                    #print (new_cost)
                    
                    if new_state not in reached or new_cost < reached[new_state]:
                        new_node = Node("", new_state, new_cost , node, a)
                        new_node.manhattan_distance(grid.end)
                        #print(f"distancia nuevo nodo:", new_node.estimated_distance)
                  
                        # Add the node to the explored dictionary
                        reached[new_state] = new_node.estimated_distance

                        # Agregar a la frontera
                        #print(f"Encolando nodo {new_state} con heurística = {new_node.estimated_distance}")
                        frontier.add(new_node, new_node.estimated_distance)

        # Si no se encontró solución
        return NoSolution(reached)


