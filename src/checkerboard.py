import random
from coupon import Coupon
class Board():
    def __init__(self, edge_len: int):
        self.edge_len = edge_len
        self.coupons = [[Coupon(1) for i in range(edge_len)] for j in range(edge_len)]
        self.edge_cells = [(0,i) for i in range(self.edge_len)] + [(self.edge_len-1,i) for i in range(self.edge_len)] + [(i,self.edge_len-1) for i in range(1, self.edge_len-1)] + [(i,0) for i in range(1,self.edge_len-1)]

    def get_coupons(self):
        return self.coupons

    def _get_possible_next_coords_for_pointee(self, coord: tuple) -> list:
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        next_coords = []
        for d in directions:
            next = (coord[0]+d[0], coord[1] + d[1])
            if not self._check_out_of_bounds(next):
                next_coords.append(next)
        return next_coords
    def _get_random_choice(self,choice_set):
        return random.choice(choice_set)
    def _update_coupons(self, coord: tuple):
        for _ in range(self.coupons[coord[0]][coord[1]].value):
            next_coords_list = self._get_possible_next_coords_for_pointee(coord)
            next_coord = self._get_random_choice(next_coords_list)
            self.coupons[coord[0]][coord[1]].value -= 1
            self.coupons[next_coord[0]][next_coord[1]].value += 1

    def _check_out_of_bounds(self, coord: tuple) -> bool:
        for i in range(2):
            if coord[i]<0 or coord[i]>self.edge_len-1:
                return True
        return False

    def simulate_bird(self, display_traj=False):
        display_traj = [["*" for i in range(self.edge_len)] for j in range(self.edge_len)]
        start_coord = self._get_random_choice(self.edge_cells)
        directions = []

        for i in range(-1, 2):
            for j in range(-1, 2):
                if i==0 and j==0:
                    continue
                directions.append((i,j))

        exit_board = False
        cur = start_coord
        steps = 0

        while not exit_board:
            display_traj[cur[0]][cur[1]] = steps
            steps += 1

            self._update_coupons(cur)

            random_dir = self._get_random_choice(directions)
            next = (cur[0]+random_dir[0], cur[1]+random_dir[1])

            if self._check_out_of_bounds(next):
                exit_board = True
                if display_traj:
                    print("Trajectory")
                    self.print_matrix(display_traj)
            else:
                cur = next

    def print_matrix(self, matrix):
        for row in matrix:
            print('\t'.join(map(str, row)))


