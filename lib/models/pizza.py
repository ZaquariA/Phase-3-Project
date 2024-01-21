

class Pizza:

    all = []

    def __init__(self, name):

        self.name = name
        Pizza.all.append(self)

    @property

    def name(self):
        return self._name
    
    @name.setter
    
    def name(self, name):
        if isinstance(name, str) and not hasattr(self, 'name'):
            self._name = name
        else:
            raise Exception('Name must be of type str / name can not be changed.')
