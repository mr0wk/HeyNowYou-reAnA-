from enum import Enum


class NodeColor(Enum):
    STARTING_POINT = (0, 255, 0)  # Green
    END_POINT = (0, 0, 255)  # Blue
    OBSTACLE = (255, 0, 0)  # Red


class NodeType(Enum):
    START_POINT = "start point"
    END_POINT = "end point"
    OBSTACLE = "obstacle"
    FREE = "free"
