class NumberProcessor:
    def __init__(self):
        
        self.numbers = []

    def add_number(self, number):
        
        self.numbers.append(number)

    def search_number(self, x):
        
        if x in self.numbers:
            return self.numbers.index(x) + 1  # Convert to 1-based index
        return -1
