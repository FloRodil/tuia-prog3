from ..models.grid import Grid
from ..models.frontier import QueueFrontier
from ..models.solution import NoSolution, Solution
from ..models.node import Node


class BreadthFirstSearch:
    @staticmethod
    def search(grid: Grid) -> Solution:
        """Find path between two points in a grid using Breadth First Search

        Args:
            grid (Grid): Grid of points
            
        Returns:
            Solution: Solution found
        """
        # Initialize a node with the initial position
        node = Node("", grid.start, 0)

        # Initialize the explored dictionary to be empty
        explored = {}
        explored[node.state] = True

        # Aplicar test-objetivo al nodo raíz
        if node.state == grid.end:
            return Solution(node, explored)
        
        # Inicializar frontera (Cola) y encola el nodo inicial
        frontier = QueueFrontier()
        frontier.add(node)
        
        # Bucle while, se ejecuta mientras la frontera no esté vacía
        while frontier:
                # Retorno si la frontera está vacía
                # if frontier.is_empty():
                #     return NoSolution(explored)
                
                # Remover un nodo de la frontera
                node = frontier.remove()

                successors = grid.get_neighbours(node.state)
                for a in successors:
                    new_state = successors[a]
                    if new_state not in explored:
                        new_node = Node("", new_state, node.cost + grid.get_cost(new_state), node, a)
               
                        # Aplicar test-objetivo al nuevo nodo
                        if new_node.state == grid.end:
                            return Solution(new_node, explored)
                            
                        # Add the node to the explored dictionary
                        explored[new_state] = True

                        # Agregar a la frontera
                        frontier.add(new_node)

