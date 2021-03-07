class Yatzy:

    def __init__(self, dice):
        self.dice = dice
        self.dice_counts = {"1": 0, "2": 0, "3": 0, "4": 0, "5": 0, "6": 0}
        for die in dice:
            self.dice_counts[str(die)] += 1

    def chance(self):
        return sum(self.dice)

    def ones(self):
        return self.dice_counts["1"]

    def twos(self):
        return self.dice_counts["2"] * 2

    def threes(self):
        return self.dice_counts["3"] * 3

    def fours(self):
        return self.dice_counts["4"] * 4

    def fives(self):
        return self.dice_counts["5"] * 5

    def sixes(self):
        return self.dice_counts["6"] * 6

    def score_pair(self):
        for die in reversed(range(1, 7)):
            if self.dice_counts[str(die)] == 2:
                return die * 2

        return 0

    def two_pair(self):
        score = 0
        n = 0
        for die, count in self.dice_counts.items():
            if self.dice_counts[die] >= 2:
                score += int(die) * 2
                n += 1

        if n == 2:
            return score
        else:
            return 0

    def three_of_a_kind(self):
        for die, count in self.dice_counts.items():
            if self.dice_counts[die] >= 3:
                return int(die) * 3
        return 0

    def four_of_a_kind(self):
        for die, count in self.dice_counts.items():
            if self.dice_counts[die] >= 4:
                return int(die) * 4
        return 0

    def small_straight(self):

        self.dice_counts.pop("6")
        for die, count in self.dice_counts.items():
            if count != 1:
                return 0
        return 15

    def large_straight(self):
        self.dice_counts.pop("1")
        for die, count in self.dice_counts.items():
            if count != 1:
                return 0
        return 20

    def full_house(self):
        score = 0
        n = 0
        for die, count in self.dice_counts.items():
            if self.dice_counts[die] >= 3:
                score += int(die) * 3
                n += 1
                self.dice_counts[die] -= 3

            if self.dice_counts[die] >= 2:
                score += int(die) * 2
                n += 1

        if n == 2:
            return score
        else:
            return 0

    def yatzy(self):
        for die, count in self.dice_counts.items():
            if count == 5:
                return 50

        return 0
