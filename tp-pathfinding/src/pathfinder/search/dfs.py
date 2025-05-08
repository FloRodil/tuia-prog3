from ..models.grid import Grid
from ..models.frontier import StackFrontier
from ..models.solution import NoSolution, Solution
from ..models.node import Node


class DepthFirstSearch:
    @staticmethod
    def search(grid: Grid) -> Solution:
        """Find path between two points in a grid using Depth First Search

        Args:
            grid (Grid): Grid of points
            
        Returns:
            Solution: Solution found
        """
        # Initialize a node with the initial position
        node = Node("", grid.start, 0)

        # Aplicar test-objetivo al nodo raíz
        if node.state == grid.end:
            return Solution(node)
        
        # Inicializar frontera (Pila) y apilar el nodo inicial
        frontier = StackFrontier()
        frontier.add(node)

        # Initialize the explored dictionary to be empty
        expandidos = {} 

        # Bucle while, se ejecuta mientras la frontera no esté vacía 
        while frontier:
                # Retorno si la frontera está vacía
                # if frontier.is_empty():
                #     return NoSolution(expandidos)
                
                # Remover un nodo de la frontera
                node = frontier.remove()

                # Se evita expandir un estado ya expandido, antes de continuar
                if node.state in expandidos:
                    pass
                expandidos[node.state] = True
                successors = grid.get_neighbours(node.state)
                for a in successors:
                    new_state = successors[a]
                    if new_state not in expandidos:
                        new_node = Node("", new_state, node.cost + grid.get_cost(new_state), node, a)
                
                        # Aplicar test-objetivo al nuevo nodo
                        if new_node.state == grid.end:
                            return Solution(new_node,expandidos)

                        # Agregar a la frontera
                        frontier.add(new_node)
