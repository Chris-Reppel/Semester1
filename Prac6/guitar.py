current_year = 2020
vintage_age = 50


class Guitar:
    def __init__(self, name="", year=0, cost=0):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return "{} ({}) : $ {:,.2f}".format(self.name, self.year, self.cost)

    def get_age(self):
        return current_year - self.year

    def is_vintage(self):
        return self.get_age() >= vintage_age

    def __lt__(self, other):
        return self.year < other.year
