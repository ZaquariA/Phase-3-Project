
class Customer:

    all = []

    def __init__(self, name):

        self.name = name
        Customer.all.append(self)

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if isinstance(name, str) and 2 < len(name) < 16:
            self._name = name
        else:
            raise Exception('Name must be of type str / Name must be between 2 to 16 characters long.')
