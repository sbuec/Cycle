import pyray as pr
from shared.point import Point

class KeyboardService:

    def __init__(self, cell_size):
        self._cell_size = cell_size

    def key_pressed(self, player_num):
        p1_dx = 0
        p1_dy = 0

        p2_dx = 0
        p2_dy = 0


        #player 1 keys
        if pr.is_key_down(pr.KEY_A):
            p1_dx = -1

        if pr.is_key_down(pr.KEY_D):
            p1_dx = 1

        if pr.is_key_down(pr.KEY_W):
            p1_dy = -1

        if pr.is_key_down(pr.KEY_S):
            p1_dy = 1


        #player 2 keys
        if pr.is_key_down(pr.KEY_J):
            p2_dx = -1

        if pr.is_key_down(pr.KEY_L):
            p2_dx = 1

        if pr.is_key_down(pr.KEY_I):
            p2_dy = -1

        if pr.is_key_down(pr.KEY_K):
            p2_dy = 1

        p1_direction = Point(p1_dx, p1_dy)
        p2_direction = Point(p2_dx, p2_dy)

