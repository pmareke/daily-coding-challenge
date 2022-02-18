class Sum(object):
    def __init__(self, numbers):
        self.numbers = numbers

    def upTo(self, k):
        seen = []

        for number in self.numbers:
            if (k - number) in seen:
                return True
            else:
                seen.append(number)
        return False
