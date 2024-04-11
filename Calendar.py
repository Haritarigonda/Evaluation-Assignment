class Calendar:
    def __init__(self):
        self.calendar = []

    def book(self, start: int, end: int) -> bool:
        for s, e in self.calendar:
            if start < e and end > s:
                return False
        self.calendar.append((start, end))
        return True

calendar = Calendar()
print(calendar.book(5, 10))  # Expect True
print(calendar.book(8, 13))  # Expect False
print(calendar.book(10, 15))  # Expect True