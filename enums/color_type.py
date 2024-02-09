from enum import Enum


class ColorType(Enum):
    OBSTACLE = (255, 0, 0)  # Red
    STARTING_POINT = (0, 255, 0)  # Green
    END_POINT = (0, 0, 255)  # Blue
