
def HEX_to_RGB ( HEX ):
    return [ int( HEX[ i : i + 2 ], 16) for i in range( 1, 6, 2 ) ]

def RGB_to_HEX ( RGB ):
    RGB = [ int( x ) for x in RGB ]
    return "#" + "" . join( [ "0{0:x}" . format( v ) if v < 16 else
            "{0:x}" . format( v ) for v in RGB ] )

def ColorsDict ( gradient ):
    return { "hex":[ RGB_to_HEX( RGB ) for RGB in gradient ],
        "r":[ RGB[ 0 ] for RGB in gradient ],
        "g":[ RGB[ 1 ] for RGB in gradient ],
        "b":[ RGB[ 2 ] for RGB in gradient ] }

def LinearGradientHex ( start, end = "#FFFFFF", n = 10 ):
    s = HEX_to_RGB( start )
    f = HEX_to_RGB( end )
    RGB_list = [ s ]

    for t in range( 1, n ):
        curr_vector = [
            int( s[ j ] + ( float( t ) / ( n - 1 ) ) * ( f[ j ] - s[ j ] ) )
            for j in range( 3 )
        ]
        RGB_list.append( curr_vector )

    return ColorsDict( RGB_list )

print ( LinearGradientHex ( '#D8EB86', '#81E2C2', 10 ) )