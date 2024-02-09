import pygame


class Grid:
    def __init__(
        self, screen: pygame.Surface, offset: int, cell_size: int, num_cells: int
    ):
        self.screen = screen
        self.offset = offset
        self.cell_size = cell_size
        self.num_cells = num_cells

    def draw(self):
        """
        Draws a grid on the given screen surface.

        Args:
            screen (pygame.Surface): The surface to draw the grid on.
            offset (int): The offset from the left and top edges of the screen.
            cell_size (int): The size of each cell in the grid.
        """
        grid_width = self.screen.get_width() - self.offset
        grid_height = grid_width

        self.screen.fill((0, 0, 0))

        # Draw vertical lines
        for x in range(self.offset, self.screen.get_width(), self.cell_size):
            if x > grid_width:
                break
            start_pos = (x, self.offset)
            end_pos = (x, grid_height)
            pygame.draw.line(self.screen, (255, 255, 255), start_pos, end_pos)
        # Draw horizontal lines
        for y in range(self.offset, self.screen.get_height(), self.cell_size):
            if y > grid_height:
                break
            start_pos = (self.offset, y)
            end_pos = (grid_width, y)
            pygame.draw.line(self.screen, (255, 255, 255), start_pos, end_pos)

    def color_cell(self, x: int, y: int, color: tuple):
        """
        Set the color of the cell at the given position.

        Args:
            x (int): The x-coordinate of the cell.
            y (int): The y-coordinate of the cell.
            color (tuple): The color to set the cell to.
        """
        if x < 0 or y < 0 or x >= self.num_cells or y >= self.num_cells:
            return

        pygame.draw.rect(
            self.screen,
            color,
            (
                # Add 1 to the x and y coordinates to account for the grid lines
                x * self.cell_size + self.offset + 1,
                y * self.cell_size + self.offset + 1,
                # Subtract 1 from the width and height to account for the grid lines
                self.cell_size - 1,
                self.cell_size - 1,
            ),
        )
