import click
import pygame

from enums import NodeColor
from visualizer import Visualizer

CELL_COLOR = NodeColor.STARTING_POINT.value
SCREEN = None
GRID = None


def calculate_dimension(num_cells, cell_size, offset) -> int:
    """
    Calculates the total dimension based on the number of cells, cell size, and offset.

    Args:
        num_cells (int): The number of cells.
        cell_size (int): The size of each cell.
        offset (int): The offset value.

    Returns:
        int: The total dimension.

    """
    return offset * 2 + num_cells * cell_size


def get_cell_coordinates(offset, cell_size) -> tuple:
    """
    Calculates the coordinates of the cell based on the mouse position.

    Parameters:
    offset (int): The offset value to adjust the mouse position.
    cell_size (int): The size of each cell.

    Returns:
    tuple: The x and y coordinates of the cell.
    """
    mouse_pos = pygame.mouse.get_pos()
    x = (mouse_pos[0] - offset) // cell_size
    y = (mouse_pos[1] - offset) // cell_size

    return x, y


def reset() -> None:
    """
    Resets the game state by clearing the screen, redrawing the grid, and resetting the starting and ending point coordinates.
    """
    global CELL_COLOR, STARTING_POINT_COORDINATES, END_POINT_COORDINATES, SCREEN, GRID, CELL_COLOR
    SCREEN.fill((0, 0, 0))
    GRID.draw_grid()
    STARTING_POINT_COORDINATES = ()
    END_POINT_COORDINATES = ()
    CELL_COLOR = NodeColor.STARTING_POINT.value


def handle_key_event(event):
    global CELL_COLOR

    if event.key == pygame.K_r:
        reset()
    elif event.key == pygame.K_o:
        CELL_COLOR = NodeColor.OBSTACLE.value
    elif event.key == pygame.K_s:
        CELL_COLOR = NodeColor.STARTING_POINT.value
    elif event.key == pygame.K_e:
        CELL_COLOR = NodeColor.END_POINT.value


@click.command()
@click.option("--cell_size", default=10, help="Size of each cell in pixels")
@click.option("--num_cells", default=10, help="Number of cells in the grid")
def main(cell_size, num_cells):
    global SCREEN, GRID
    offset = 10

    pygame.init()

    width = calculate_dimension(num_cells, cell_size, offset)
    height = width
    SCREEN = pygame.display.set_mode((width, height))
    clock = pygame.time.Clock()
    GRID = Visualizer(SCREEN, offset, cell_size, num_cells)

    GRID.draw_grid()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                handle_key_event(event)

        if pygame.mouse.get_pressed()[0]:
            x, y = get_cell_coordinates(offset, cell_size)

            # TODO: Refactor and separate it into a function
            if CELL_COLOR == NodeColor.STARTING_POINT.value:
                if STARTING_POINT_COORDINATES == ():
                    GRID.mark_node(
                        STARTING_POINT_COORDINATES[0],
                        STARTING_POINT_COORDINATES[1],
                        CELL_COLOR,
                    )
            elif CELL_COLOR == NodeColor.END_POINT.value:
                if END_POINT_COORDINATES == ():
                    END_POINT_COORDINATES = (x, y)
                    GRID.mark_node(
                        END_POINT_COORDINATES[0], END_POINT_COORDINATES[1], CELL_COLOR
                    )
            elif CELL_COLOR == NodeColor.OBSTACLE.value:
                if (x, y) != STARTING_POINT_COORDINATES and (
                    x,
                    y,
                ) != END_POINT_COORDINATES:
                    GRID.mark_node(x, y, CELL_COLOR)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()
