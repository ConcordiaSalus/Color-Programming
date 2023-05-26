
import random

def GenerateListRandomColors_in_RGB ( number ):
    rand_colors = []
    for j in range( number ):
        r = random.randint( 0, 255 )
        g = random.randint( 0, 255 )
        b = random.randint( 0, 255 )
        rand_colors.append( [ r, g, b ] )

    return rand_colors

print ( GenerateListRandomColors_in_RGB ( 50 ) )