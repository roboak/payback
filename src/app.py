from checkerboard import Board
class Game:
    def __init__(self, edge_len, num_sim):
        self.board = Board(edge_len)
        self.num_sim = num_sim




    def simulate(self):
        # self.board.print_checkerboard(self.coupons)
        for _ in range(self.num_sim):
            self.board.simulate_bird(display_traj=False)

        print("Updated Coupons")

        display_mat = [[coupon.value for coupon in row] for row in self.board.get_coupons()]
        self.board.print_matrix(display_mat)

        print("#########################")


    def get_number_of_points_per_each_coupon(self):
        return self.board.get_coupons()

    def get_max_coupons(self):
        max = -1

        for i,row in enumerate(self.board.get_coupons()):
            for j,ele in enumerate(row):
                if ele.value > max:
                    max = ele.value
                    indices = [(i,j)]
                elif ele.value == max:
                    indices.append((i,j))

        print("Max Coupons: ", indices)
        print("Value", max)
        return indices
if __name__=='__main__':
    g = Game(2, 1)
    g.simulate()
    g.get_number_of_points_per_each_coupon()
    g.get_max_coupons()
    # x = [i for i in range(12)]
    # for _ in range(100):
    #     num = random.choice(x)
    #     print(num)


