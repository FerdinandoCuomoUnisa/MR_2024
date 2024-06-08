import enum

class Directions(enum): 
    NORD = 'nord'
    SUD = 'sud'
    EST = 'est'
    OVEST = 'ovest'

class Signs(enum): 
    STOP = 'STOP'
    RIGHT = 'RIGHT'
    LEFT = 'LEFT'
    STRAIGHTON = 'STRAIGHTON'
    GOBACK = 'GOBACK'

class Coordinates(enum): 
    A = [-22.9, 0.044]
    B = [-23.74, -8.72]
    C = [-3.11, 0.11]
    D = [-3.3, -9.51]
    E = [16.64, 0.03]
    F = [16.8, -9.66]
    G = [36.72, -0.88]
    H = [36.70, -10]
    I = [58, -2]
    L = [58, -11]