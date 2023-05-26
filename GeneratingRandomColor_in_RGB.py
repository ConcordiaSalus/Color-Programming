
import random

def GeneratingRandomColor_in_RGB ():
    r = random.randint( 0, 255 )
    g = random.randint( 0, 255 )
    b = random.randint( 0, 255 )
    
    return [ r, g, b ]

print ( GeneratingRandomColor_in_RGB () )