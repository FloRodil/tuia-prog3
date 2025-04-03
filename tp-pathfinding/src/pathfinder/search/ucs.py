from ..models.grid import Grid
from ..models.frontier import PriorityQueueFrontier
from ..models.solution import NoSolution, Solution
from ..models.node import Node


class UniformCostSearch:
    @staticmethod
    def search(grid: Grid) -> Solution:
        """Find path between two points in a grid using Uniform Cost Search

        Args:
            grid (Grid): Grid of points

        Returns:
            Solution: Solution found
        """
        # Initialize a node with the initial position
        node = Node("", grid.start, 0)

        # Inicializar frontera (Cola prioridad) 
        frontier = PriorityQueueFrontier()

        # Encolar el nodo inicial
        frontier.add(node, node.cost)

        # Initialize the explored dictionary to be empty
        alcanzados = {} 
        
        # Add the node to the explored dictionary
        alcanzados[node.state] = node.cost
        
        while True:
                # Retorno si la frontera está vacía
                if frontier.is_empty():
                    return NoSolution(alcanzados)
                
                # Remover un nodo de la frontera
                node = frontier.pop()

                # Aplicar test-objetivo al nuevo nodo
                if node.state == grid.end:
                    return Solution(node, alcanzados)
                
                successors = grid.get_neighbours(node.state)
                for a in successors:
                    new_state = successors[a]
                    new_costo = node.cost + grid.get_cost(new_state)
                    if new_state not in alcanzados or new_costo < alcanzados(node.state):
                        new_node = Node("", new_state, new_costo, node, a)
                        # Add the node to the explored dictionary
                        alcanzados[new_state] = new_costo
                        # Agregar a la frontera
                        frontier.add(new_state, new_costo)         
