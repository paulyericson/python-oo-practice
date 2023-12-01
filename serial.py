"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """
    def __init__(self, start=0):
        '''make a new generator, starting at start'''
        self.start = self.next = start

    def __repr__(self):
        '''shows results'''
        return f"<SerialGenerator start={self.start} next={self.next}"

    def generate(self):
        '''creates serial number and increaces by 1 every time it is called '''
        self.next += 1
        return self.next -1
    

    def reset(self):
        '''resets serial number'''
        self.next = self.start