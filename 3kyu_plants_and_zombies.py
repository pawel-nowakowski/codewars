from typing import List


def plants_and_zombies(lawn: List, zombies: List) -> int or None:
    """
    plants and zombies: https://www.codewars.com/kata/5a5db0f580eba84589000979

    :param lawn: list that shows lawn and cannon placement
    :param zombies: zombies with format x (but reversed, counting from -1), y, hp
    :return:
    """
    return PlantsAndZombies(lawn, zombies).main()


class PlantsAndZombies:
    def __init__(self, lawn, zombies):
        self.y_lawn_length = len(lawn)
        self.lawn_length = len(lawn[0])
        self.lawn = [list(lawn_y) for lawn_y in lawn]
        self.zombies = zombies
        self.cannons_dmg = []
        self.cannons_s = []
        self.turn = 0
        self.penetrated_defenses = False

    def main(self) -> int:
        """
        main game logic
        :return: nr of turns it took to break defenses or None if cannons managed to def
        """
        self.cannon_list()
        self.turn_loop()
        while self.check_win_cond() is False:
            self.turn_loop()
        return self.check_win_cond()

    def turn_loop(self):
        """
        each loop consists of spawning zombies (or moving them) and if defenses are intact, the cannons will strike
        :return: None
        """
        self.spawn_zombies()
        if self.penetrated_defenses is False:
            self.attack_linear()
            self.attack_diagonally()

    def spawn_zombies(self):
        """
        spawns zombies or move them by one field to the left (cleans the field to do so and create zombies at new
        position if they are still alive)
        :return: None
        """
        self.clean_lawn()
        zombie_inx = 0
        while zombie_inx < len(self.zombies):
            zombie = self.zombies[zombie_inx]
            zombie[0] -= 1

            pos_x = zombie[0]
            pos_y = zombie[1]

            if pos_x < -self.lawn_length:
                self.penetrated_defenses = True
                break

            hp = zombie[2]
            if int(hp) <= 0:
                self.del_zombie(zombie_inx)
                continue

            zombie_inx += 1
            if pos_x < 0:
                self.lawn[pos_y][pos_x] = f"Z{hp}"

        else:
            self.turn += 1
        self.cannon_list()

    def del_zombie(self, ind: int):
        """
        delete zombie from input index
        :param ind: index to delete
        :return: None
        """
        del self.zombies[ind]

    def clean_lawn(self):
        """
        cleans lawn from zombies
        :return: None
        """
        for row in range(self.y_lawn_length):
            for col in range(self.lawn_length):
                if "Z" in self.lawn[row][col]:
                    self.lawn[row][col] = " "
                else:
                    continue

    def cannon_list(self):
        """
        changes self.cannons_dmg to lists with cannons dmg in format x, y, hp and self.cannon_s in
        format x, y
        :return: None
        """
        self.cannons_dmg = []
        self.cannons_s = []
        for y in range(len(self.lawn)):
            for x, spot in enumerate(self.lawn[y]):
                try:
                    self.cannons_dmg.append([x, y, int(spot)])
                except ValueError:
                    if spot == "S":
                        self.cannons_s.append([x, y])
        self.cannons_s = sorted(self.cannons_s, key=lambda index: (-index[0], index[1]))

    def attack_linear(self):
        """
        all self.cannons_dmg strikes lineary
        :return: None
        """
        for cannon in self.cannons_dmg:
            gotcha = False
            cannon_dmg_left = 0
            nr = 0
            while nr < len(self.zombies):
                zombie = self.zombies[nr]
                if zombie[0] >= 0:
                    break
                if zombie[1] == cannon[1]:
                    for i in range(cannon[0], self.lawn_length):
                        if zombie[0] == i - self.lawn_length:
                            dmg = cannon[2] if cannon_dmg_left == 0 else cannon_dmg_left
                            self.zombies[nr][2] -= dmg
                            if int(self.zombies[nr][2]) <= 0:
                                cannon_dmg_left = int(self.zombies[nr][2]) * -1
                                self.del_zombie(nr)
                                nr -= 1
                            else:
                                cannon_dmg_left = 0
                            gotcha = True if cannon_dmg_left == 0 else False
                            break
                if gotcha:
                    break
                nr += 1

    def attack_diagonally(self):
        """
        all cannon_s strikes forward and diagonally for 1 dmg
        :return: None
        """
        for cannon in self.cannons_s:
            x, y = cannon[0], cannon[1]
            x_up, y_up = x, y
            x_down, y_down = x, y
            gotcha = False
            nr = 0
            while nr < len(self.zombies):
                zombie = self.zombies[nr]
                if zombie[0] >= 0:
                    break
                if zombie[1] == y:
                    for i in range(cannon[0], self.lawn_length):
                        if zombie[0] == i - self.lawn_length:
                            self.zombies[nr][2] -= 1
                            if int(self.zombies[nr][2]) <= 0:
                                self.del_zombie(nr)
                                nr -= 1
                            gotcha = True
                            break
                if gotcha:
                    break
                nr += 1

            for _ in range(max(self.lawn_length, self.y_lawn_length)):
                gotcha = False
                x_up += 1
                y_up += 1
                if y_up >= self.y_lawn_length or x_up >= self.lawn_length:
                    break
                reverse_x = x_up - self.lawn_length
                nr = 0
                while nr < len(self.zombies):
                    zombie = self.zombies[nr]
                    if zombie[0] >= 0:
                        break
                    if zombie[0] == reverse_x and zombie[1] == y_up:
                        self.zombies[nr][2] -= 1
                        if self.zombies[nr][2] <= 0:
                            self.del_zombie(nr)
                        gotcha = True
                        break
                    nr += 1
                if gotcha:
                    break

            for _ in range(max(self.lawn_length, self.y_lawn_length)):
                x_down += 1
                y_down -= 1
                gotcha = False
                if y_down < 0 or x_down >= self.lawn_length:
                    break
                reverse_x = x_down - self.lawn_length
                nr = 0
                while nr < len(self.zombies):
                    zombie = self.zombies[nr]
                    if zombie[0] >= 0:
                        break
                    if zombie[0] == reverse_x and zombie[1] == y_down:
                        self.zombies[nr][2] -= 1
                        if self.zombies[nr][2] <= 0:
                            self.del_zombie(nr)
                        gotcha = True
                        break
                    nr += 1
                if gotcha:
                    break

    def check_win_cond(self):
        """
        checks win condition, if not fullfilled, returns False
        :return: int, False or None
        """
        if self.penetrated_defenses:
            return self.turn
        elif len(self.zombies) > 0:
            return False
        else:
            return None


if __name__ == "__main__":
    print(
        plants_and_zombies(
            ["2       ", "  S     ", "21  S   ", "13      ", "2 3     "],
            [[0, 4, 28], [1, 1, 6], [2, 0, 10], [2, 4, 15], [3, 2, 16], [3, 3, 13]],
        )
        == 10
    )

    print(
        plants_and_zombies(
            [
                "1         ",
                "SS        ",
                "SSS       ",
                "SSS       ",
                "SS        ",
                "1         ",
            ],
            [
                [0, 2, 16],
                [1, 3, 19],
                [2, 0, 18],
                [4, 2, 21],
                [6, 3, 20],
                [7, 5, 17],
                [8, 1, 21],
                [8, 2, 11],
                [9, 0, 10],
                [11, 4, 23],
                [12, 1, 15],
                [13, 3, 22],
            ],
        )
        is None
    )

    print(
        plants_and_zombies(
            ["11      ", " 2S     ", "11S     ", "3       ", "13      "],
            [
                [0, 3, 16],
                [2, 2, 15],
                [2, 1, 16],
                [4, 4, 30],
                [4, 2, 12],
                [5, 0, 14],
                [7, 3, 16],
                [7, 0, 13],
            ],
        )
        == 12
    )

    print(
        plants_and_zombies(
            [
                "12        ",
                "3S        ",
                "2S        ",
                "1S        ",
                "2         ",
                "3         ",
            ],
            [
                [0, 0, 18],
                [2, 3, 12],
                [2, 5, 25],
                [4, 2, 21],
                [6, 1, 35],
                [6, 4, 9],
                [8, 0, 22],
                [8, 1, 8],
                [8, 2, 17],
                [10, 3, 18],
                [11, 0, 15],
                [12, 4, 21],
            ],
        )
        == 20
    )

    print(
        plants_and_zombies(
            [
                "2121                ",
                "6    S              ",
                "3 2  S              ",
                "22 S S              ",
                "2 1 2S              ",
                "311                 ",
            ],
            [
                [0, 4, 49],
                [0, 0, 88],
                [0, 1, 92],
                [0, 2, 75],
                [1, 5, 69],
                [1, 3, 78],
                [3, 1, 24],
                [4, 2, 18],
                [4, 5, 21],
                [6, 0, 51],
                [7, 4, 59],
                [7, 1, 29],
                [10, 2, 34],
                [11, 5, 37],
                [11, 1, 42],
                [13, 0, 44],
                [13, 3, 33],
                [13, 2, 59],
                [15, 1, 54],
                [16, 0, 24],
                [16, 2, 42],
                [17, 5, 36],
                [18, 3, 48],
                [18, 4, 39],
                [19, 2, 85],
            ],
        )
        == 35
    )

    print(
        plants_and_zombies(
            ["S 22    ", " 6S1    ", "S31     ", "1211    ", "42 2    "],
            [
                [3, 0, 18],
                [3, 1, 28],
                [3, 2, 18],
                [3, 3, 18],
                [3, 4, 28],
                [4, 0, 12],
                [4, 1, 19],
                [4, 2, 12],
                [5, 1, 14],
                [5, 4, 23],
                [6, 3, 16],
                [8, 1, 15],
                [8, 2, 13],
                [8, 3, 11],
                [8, 4, 20],
                [9, 0, 15],
                [9, 2, 9],
                [9, 4, 14],
                [10, 0, 11],
                [10, 1, 16],
                [10, 3, 11],
                [12, 4, 15],
                [13, 0, 10],
                [13, 2, 12],
                [13, 3, 10],
                [16, 1, 19],
                [16, 2, 9],
                [16, 4, 16],
            ],
        )
        == 16
    )

    print(
        plants_and_zombies(
            [
                "42S1            ",
                "6S              ",
                "32 S  S         ",
                "22 S S S        ",
                "6               ",
                "5 1 2           ",
                "3 2 S  6        ",
                "4 1 S           ",
                "  8   S         ",
                "8SS             ",
            ],
            [
                [0, 8, 48],
                [0, 1, 47],
                [0, 2, 55],
                [0, 9, 99],
                [0, 6, 58],
                [0, 7, 42],
                [0, 0, 92],
                [0, 3, 39],
                [0, 5, 66],
                [0, 4, 71],
                [2, 3, 36],
                [2, 5, 59],
                [2, 8, 36],
                [4, 0, 21],
                [4, 7, 21],
                [5, 2, 14],
                [6, 1, 48],
                [8, 6, 23],
                [11, 1, 41],
                [11, 9, 25],
                [11, 3, 53],
                [12, 1, 54],
                [12, 0, 75],
                [13, 5, 48],
                [13, 9, 113],
                [14, 8, 66],
                [15, 7, 82],
                [15, 5, 54],
                [16, 0, 76],
                [16, 4, 96],
                [16, 9, 42],
                [18, 1, 23],
                [18, 8, 91],
                [18, 3, 39],
                [19, 0, 16],
                [20, 5, 37],
            ],
        )
        == 34
    )

    print(
        plants_and_zombies(
            [
                "3 S 22       ",
                "1113S        ",
                "3SS          ",
                " 51  3       ",
                "S11S         ",
                "11           ",
                "S31  1       ",
                "1S1S         ",
                "111S         ",
                "S3S 13       ",
            ],
            [
                [0, 1, 56],
                [0, 2, 40],
                [0, 3, 72],
                [0, 4, 32],
                [0, 6, 48],
                [0, 8, 32],
                [0, 9, 72],
                [1, 0, 69],
                [1, 5, 17],
                [2, 1, 30],
                [2, 3, 39],
                [2, 7, 37],
                [2, 8, 17],
                [2, 9, 39],
                [3, 0, 36],
                [3, 4, 19],
                [3, 5, 9],
                [3, 7, 16],
                [6, 2, 31],
                [7, 1, 29],
                [7, 3, 37],
                [7, 6, 40],
                [7, 8, 16],
                [7, 9, 37],
                [8, 0, 34],
                [8, 4, 17],
                [9, 2, 21],
                [9, 5, 9],
                [9, 7, 19],
                [10, 6, 27],
                [11, 3, 36],
                [11, 8, 16],
                [11, 9, 36],
                [12, 4, 17],
                [13, 0, 37],
                [13, 1, 37],
                [13, 2, 20],
                [13, 7, 17],
                [14, 5, 10],
                [14, 6, 25],
                [15, 3, 36],
                [15, 8, 16],
                [16, 9, 42],
                [17, 0, 34],
                [17, 1, 31],
                [17, 2, 20],
                [17, 7, 16],
                [18, 4, 21],
                [18, 5, 9],
                [18, 6, 24],
                [19, 3, 36],
                [19, 8, 16],
                [21, 9, 38],
                [23, 0, 33],
                [23, 7, 16],
                [25, 4, 18],
                [25, 5, 8],
                [25, 6, 24],
                [26, 1, 38],
                [26, 3, 36],
                [26, 8, 16],
                [29, 2, 29],
                [29, 9, 37],
                [31, 0, 32],
                [32, 4, 17],
                [32, 5, 8],
                [32, 6, 24],
                [33, 1, 32],
                [33, 7, 21],
                [34, 2, 24],
                [34, 8, 19],
                [35, 0, 32],
                [35, 3, 47],
            ],
        )
        == 16
    )
