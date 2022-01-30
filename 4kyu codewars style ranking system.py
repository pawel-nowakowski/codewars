class User:
    def __init__(self):
        self.ranking = [-8, -7, -6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6, 7, 8]
        self.n = 0
        self.points = 0
        self.index_call = -2

    def inc_progress(self, progress_nr):
        self.index_call = self.ranking.index(progress_nr)

        x = self.index_call - self.n

        if x == 0:
            self.points += 3
        elif x == -1:
            self.points += 1
        elif x >= 1:
            self.points += 10 * x * x
        else:
            self.points += 0

        if self.n == 15:
            self.points = 0

        while self.points >= 100:
            self.points = self.points - 100
            if self.n == 15:
                self.n += 0
                self.points = 0
            else:
                self.n += 1

    @property
    def progress(self):
        return self.points

    @property
    def rank(self):
        return self.ranking[self.n]

user = User()
user.inc_progress(-8)
print(user.progress)
print(user.rank)
user.inc_progress(-7)
print(user.progress)
print(user.rank)
user.inc_progress(-6)
print(user.progress)
print(user.rank)
user.inc_progress(-5)
print(user.progress)
print(user.rank)
user.inc_progress(-4)
print(user.progress)
print(user.rank)
user.inc_progress(-8)
print(user.progress)
print(user.rank)
user.inc_progress(1)
print(user.progress)
print(user.rank)
user.inc_progress(1)
print(user.progress)
print(user.rank)
user.inc_progress(1)
print(user.progress)
print(user.rank)
user.inc_progress(1)
print(user.progress)
print(user.rank)
user.inc_progress(1)
print(user.progress)
print(user.rank)
user.inc_progress(2)
print(user.progress)
print(user.rank)
user.inc_progress(-1)
print(user.progress)
print(user.rank)
user.inc_progress(3)
print(user.progress)
print(user.rank)
user.inc_progress(8)
print(user.progress)
print(user.rank)
user.inc_progress(8)
print(user.progress)
print(user.rank)
user.inc_progress(8)
print(user.progress)
print(user.rank)
user.inc_progress(8)
print(user.progress)
print(user.rank)
user.inc_progress(8)
print(user.progress)
print(user.rank)
user.inc_progress(8)
print(user.progress)
print(user.rank)
user.inc_progress(8)
print(user.progress)
print(user.rank)
user.inc_progress(8)
print(user.progress)
print(user.rank)
user.inc_progress(8)
print(user.progress)
print(user.rank)
user.inc_progress(8)
print(user.progress)
print(user.rank)
user.inc_progress(8)
print(user.progress)
print(user.rank)
