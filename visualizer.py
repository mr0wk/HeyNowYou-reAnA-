import pygame


class Visualizer:
    def __init__(
        self, screen: pygame.Surface, offset: int, node_size: int, num_nodes: int
    ):
        self.screen = screen
        self.offset = offset
        self.node_size = node_size
        self.num_nodes = num_nodes

    def __get_node_coordinates(self, x: int, y: int) -> tuple:
        return (x - self.offset) // self.node_size, (y - self.offset) // self.node_size

    def draw_grid(self):
        grid_width = self.screen.get_width() - self.offset
        grid_height = grid_width

        self.screen.fill((0, 0, 0))

        # Draw vertical lines
        for x in range(self.offset, self.screen.get_width(), self.node_size):
            if x > grid_width:
                break
            start_pos = (x, self.offset)
            end_pos = (x, grid_height)
            pygame.draw.line(self.screen, (255, 255, 255), start_pos, end_pos)
        # Draw horizontal lines
        for y in range(self.offset, self.screen.get_height(), self.node_size):
            if y > grid_height:
                break
            start_pos = (self.offset, y)
            end_pos = (grid_width, y)
            pygame.draw.line(self.screen, (255, 255, 255), start_pos, end_pos)

    def mark_node(self, x: int, y: int, color: tuple):
        if x < 0 or y < 0 or x >= self.num_nodes or y >= self.num_nodes:
            return

        pygame.draw.rect(
            self.screen,
            color,
            (
                # Add 1 to the x and y coordinates to account for the grid lines
                x * self.node_size + self.offset + 1,
                y * self.node_size + self.offset + 1,
                # Subtract 1 from the width and height to account for the grid lines
                self.node_size - 1,
                self.node_size - 1,
            ),
        )
