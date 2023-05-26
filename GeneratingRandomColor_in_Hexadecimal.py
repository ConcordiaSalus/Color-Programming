
import random

def GeneratingRandomColor_in_Hexadecimal ():
    hexadecimal = [ "#" + '' . join( [ random.choice( 'ABCDEF0123456789' ) for i in range( 6 ) ] ) ]
    
    return hexadecimal

print ( GeneratingRandomColor_in_Hexadecimal () )