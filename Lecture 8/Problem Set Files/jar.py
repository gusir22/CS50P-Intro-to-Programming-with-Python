class Jar:
    def __init__(self, capacity=12):
        self.capacity = capacity  # default is 12 cookie cap
        self.size = 0  # init cookie stock amount at 0

    def __str__(self):
        cookie = "🍪"
        multiplier = self.size
        return multiplier * cookie

    def deposit(self, n):
        new_deposit = self.size + n  # calculate new cookie balance
        if new_deposit > self.capacity:  # if user adds more than capacity allows,
            raise ValueError("Too Many Cookies")
        else:
            self.size = new_deposit  # save new deposit

    def withdraw(self, n):
        new_deposit = self.size - n  # calculate new cookie balance
        if new_deposit < 0:  # if user withdraws more than balance allows,
            raise ValueError("Not Enough Cookies")
        else:
            self.size = new_deposit  # save new deposit

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        if isinstance(capacity, int) and capacity > 0:
            self._capacity = capacity
        else:
            raise ValueError("capacity is non-negative integer")

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, size):
        self._size = size
