import random
class Board():
    def __init__(self, edge_len: int):
        self.edge_len = edge_len
        self.array = [[1 for i in range(edge_len)] for j in range(edge_len)]

    def get_coupons(self):
        return self.array

    def check_out_of_bounds(self, coord: tuple) -> bool:
        for i in range(2):
            if coord[i]<0 or coord[i]>self.edge_len-1:
                return True
        return False

    def _generate_path(self, start_coord):
        # print("start_coord: ", start_coord)
        directions = []
        self.trajectory = [start_coord]
        for i in range(-1, 2):
            for j in range(-1, 2):
                if i==0 and j==0:
                    continue
                directions.append((i,j))
        # print(directions)
        exit_board = False
        cur = start_coord
        while not exit_board:
            random_dir = random.choice(directions)
            next = (cur[0]+random_dir[0], cur[1]+random_dir[1])
            # print("current_coord", cur)
            # print("next_coord", next)
            if next in self.trajectory:
                continue
            if self.check_out_of_bounds(next):
                exit_board = True
                self._show_bird_trajectory()
            else:
                self.trajectory.append(next)
                cur = next


    def _show_bird_trajectory(self):
        mat = [["*" for i in range(self.edge_len)] for j in range(self.edge_len)]
        for i,coord in enumerate(self.trajectory):
            mat[coord[0]][coord[1]] = i
        self.print_checkerboard(mat)


    def get_bird_trajectory(self):
        self.edge_cells = [(0,i) for i in range(self.edge_len)] + [(self.edge_len-1,i) for i in range(self.edge_len)] + [(i,self.edge_len-1) for i in range(1, self.edge_len-1)] + [(i,0) for i in range(1,self.edge_len-1)]
        start_coord = random.choice(self.edge_cells)
        self._generate_path(start_coord=start_coord)
        return self.trajectory

    def print_checkerboard(self, matrix):
        for i in matrix:
            print('\t'.join(map(str, i)))


