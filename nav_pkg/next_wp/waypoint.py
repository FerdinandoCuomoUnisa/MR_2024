from constants import Directions

class waypoint(): 
    
    def __init__(self, x, y, direction):
        self._x = x 
        self._y = y
        if not isinstance(direction, Directions):
            raise TypeError('La direzione deve essere un\'istanza della classe Directions (nel file constants)')
        else: 
            self._direction = direction

    def set_x(self, x): 
        self._x = x

    def set_y(self, y): 
        self._y = y

    def set_direction(self, direction): 
        if not isinstance(direction, Directions):
            raise TypeError('La direzione deve essere un\'istanza della classe Directions (nel file constants)')
        else: 
            self._direction = direction 

    def get_x(self): 
        return self._x

    def get_y(self): 
        return self._y
    
    def get_direction(self):
        return self._direction