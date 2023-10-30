from checkerbaord import Board
import random
class Game:
    def __init__(self, edge_len, num_sim):
        self.board = Board(edge_len)
        self.coupons = self.board.get_coupons()
        self.num_sim = num_sim

    def _get_possible_next_coords(self, coord):
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        next_coords = []
        for d in directions:
            next = (coord[0]+d[0], coord[1] + d[1])
            if not self.board.check_out_of_bounds(next):
                next_coords.append(next)
        return next_coords

    def _update_coupons(self, coord):
        for _ in range(self.coupons[coord[0]][coord[1]]):
            next_coords_list = self._get_possible_next_coords(coord)
            next_coord = random.choice(next_coords_list)
            self.coupons[coord[0]][coord[1]] -= 1
            self.coupons[next_coord[0]][next_coord[1]] += 1

    def _simulate(self):
        self.board.print_checkerboard(self.coupons)
        for _ in range(self.num_sim):
            traj = self.board.get_bird_trajectory()
            for coord in traj:
                self._update_coupons(coord=coord)
        print("Updated Coupons")
        self.board.print_checkerboard(self.coupons)
        print("#########################")

    def get_number_of_points_per_each_coupon:


if __name__=='__main__':
    g = Game(15, 2)
    g.simulate()

