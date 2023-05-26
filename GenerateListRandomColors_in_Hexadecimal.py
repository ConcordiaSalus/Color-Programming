
import random

def GenerateListRandomColors_in_Hexadecimal ( number ):
    rand_colors = []
    for j in range( number ):
        rand_colors.append( "#" + '' . join( [ random.choice( 'ABCDEF0123456789' ) for i in range( 6 ) ] ) )
    
    return rand_colors

print ( GenerateListRandomColors_in_Hexadecimal ( 50 ) )