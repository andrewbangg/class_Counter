class Counter:
    """Я счетчик. Вот и все."""

    def __init__(self, inition):
        self.value = inition

    def increment(self):
        self.value += 1

    def unincrement(self):
        self.value -= 10

    def get(self):
        return self.value
