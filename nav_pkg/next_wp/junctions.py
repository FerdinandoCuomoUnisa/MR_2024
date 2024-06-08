from constants import Directions, Signs, JunctionCoordinates
from waypoint import Waypoint

class Junctions(): 


    def __init__(self): 
        self.a = JunctionCoordinates.A
        self.b = JunctionCoordinates.B
        self.c = JunctionCoordinates.C
        self.d = JunctionCoordinates.D
        self.e = JunctionCoordinates.E
        self.f = JunctionCoordinates.F
        self.g = JunctionCoordinates.G
        self.h = JunctionCoordinates.H
        self.i = JunctionCoordinates.I
        self.l = JunctionCoordinates.L
        self.initialize_graph()  # aggiunge ai singoli incroci informazioni sugli incroci limitrofi 

        
    def initialize_graph(self): 
        '''Per ogni incocio, specifica quale incrocio è a nord, quale è a sud, quale è a est e quale è a nord'''

        # Punto A
        self.a.set_nord(self.c)  # cioè a nord del punto a c'è il punto c
        self.a.set_est(self.b)   # ad est del punto a c'è il punto b
        self.a.set_sud(None)     # a sud del punto a non c'è niente (un muro ad esmepio)
        self.a.set_ovest(None)

        # Punto B 
        self.b.set_nord(self.d)
        self.b.set_est(None)
        self.b.set_sud(None)
        self.b.set_ovest(self.a)

        # Punto C
        self.c.set_nord(self.e)
        self.c.set_est(self.d)
        self.c.set_sud(self.a)
        self.c.set_ovest(None)

        # Punto D
        self.d.set_nord(self.f)
        self.d.set_est(None)
        self.d.set_sud(self.b)
        self.d.set_ovest(self.c)

        # Punto E
        self.e.set_nord(self.g)
        self.e.set_est(self.f)
        self.e.set_sud(self.c)
        self.e.set_ovest(None)

        # Punto F
        self.f.set_nord(self.h)
        self.f.set_est(None)
        self.f.set_sud(self.d)
        self.f.set_ovest(self.e)

        # Punto G
        self.g.set_nord(self.i)
        self.g.set_est(self.h)
        self.g.set_sud(self.e)
        self.g.set_ovest(None)

        # Punto H
        self.h.set_nord(self.l)
        self.h.set_est(None)
        self.h.set_sud(self.f)
        self.h.set_ovest(self.g)

        # Punto F
        self.f.set_nord(self.h)
        self.f.set_est(None)
        self.f.set_sud(self.d)
        self.f.set_ovest(self.e)

        # Punto I
        self.i.set_nord(None)
        self.i.set_est(self.l)
        self.i.set_sud(self.g)
        self.i.set_ovest(None)

        # Punto L
        self.l.set_nord(None)
        self.l.set_est(None)
        self.l.set_sud(self.h)
        self.l.set_ovest(self.i)


    def _get_next_direction(self, current_direction, sign):
        next_direction = ''
        # Se è orientato verso nord
        if current_direction == Directions.NORD: 
            if sign == Signs.LEFT: 
                next_direction = Directions.OVEST
            elif sign == Signs.RIGHT: 
                next_direction = Directions.EST
            elif sign == Signs.STRAIGHTON: 
                next_direction = Directions.NORD
            elif sign == Signs.GOBACK: 
                next_direction = Directions.SUD

        # Se è orientato verso sud 
        elif current_direction == Directions.SUD: 
            if sign == Signs.LEFT: 
                next_direction = Directions.EST
            elif sign == Signs.RIGHT: 
                next_direction = Directions.OVEST
            elif sign == Signs.STRAIGHTON: 
                next_direction = Directions.SUD
            elif sign == Signs.GOBACK: 
                next_direction = Directions.NORD

        # Se è orientato verso est 
        elif current_direction == Directions.EST: 
            if sign == Signs.LEFT: 
                next_direction = Directions.NORD
            elif sign == Signs.RIGHT: 
                next_direction = Directions.SUD
            elif sign == Signs.STRAIGHTON: 
                next_direction = Directions.EST
            elif sign == Signs.GOBACK: 
                next_direction = Directions.OVEST

        # Se è orientato verso ovest
        elif current_direction == Directions.OVEST: 
            if sign == Signs.LEFT: 
                next_direction = Directions.SUD
            elif sign == Signs.RIGHT: 
                next_direction = Directions.NORD
            elif sign == Signs.STRAIGHTON: 
                next_direction = Directions.OVEST
            elif sign == Signs.GOBACK: 
                next_direction = Directions.EST

        return next_direction
    

    
    def get_next_junciton_waypoint(self, current_point, current_direction, sign):
        '''Restituisce il prossimo waypoint in cui andare in base al segnale ricevuto 
        e alla posa (coordinate + direzione) corrente'''

        next_direction = self._get_next_direction(current_direction, sign)

        next_point = '' 
        if next_direction == Directions.NORD: 
            next_point = current_point.get_nord()
        elif next_direction == Directions.SUD: 
            next_point = current_point.get_sud()
        elif next_direction == Directions.EST: 
            next_point = current_point.get_est()
        elif next_direction == Directions.OVEST: 
            next_point = current_point.get_ovest()

        waypoint = Waypoint(next_point.get_x(), next_point.get_y(), next_direction)

        return waypoint
        
     


    