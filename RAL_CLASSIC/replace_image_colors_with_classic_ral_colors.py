
import csv
from PIL import Image
from math import sqrt

Reference_X =  94.811
Reference_Y = 100.000
Reference_Z = 107.304

def XYZ_to_CIE_Lab ( X, Y, Z ):
    var_X = X / Reference_X
    var_Y = Y / Reference_Y
    var_Z = Z / Reference_Z

    if ( var_X > 0.008856 ): var_X = var_X ** ( 1/3 )
    else:                    var_X = ( 7.787 * var_X ) + ( 16 / 116 )
    if ( var_Y > 0.008856 ): var_Y = var_Y ** ( 1/3 )
    else:                    var_Y = ( 7.787 * var_Y ) + ( 16 / 116 )
    if ( var_Z > 0.008856 ): var_Z = var_Z ** ( 1/3 )
    else:                    var_Z = ( 7.787 * var_Z ) + ( 16 / 116 )

    CIE_L = ( 116 * var_Y ) - 16
    CIE_a = 500 * ( var_X - var_Y )
    CIE_b = 200 * ( var_Y - var_Z )

    return CIE_L, CIE_a, CIE_b


def Standard_RGB_to_XYZ ( sR, sG, sB ):
    var_R = ( sR / 255 )
    var_G = ( sG / 255 )
    var_B = ( sB / 255 )

    if ( var_R > 0.04045 ): var_R = ( ( var_R + 0.055 ) / 1.055 ) ** 2.4
    else:                   var_R = var_R / 12.92
    if ( var_G > 0.04045 ): var_G = ( ( var_G + 0.055 ) / 1.055 ) ** 2.4
    else:                   var_G = var_G / 12.92
    if ( var_B > 0.04045 ): var_B = ( ( var_B + 0.055 ) / 1.055 ) ** 2.4
    else:                   var_B = var_B / 12.92

    var_R = var_R * 100
    var_G = var_G * 100
    var_B = var_B * 100

    X = var_R * 0.4124564 + var_G * 0.3575761 + var_B * 0.1804375
    Y = var_R * 0.2126729 + var_G * 0.7151522 + var_B * 0.0721750
    Z = var_R * 0.0193339 + var_G * 0.1191920 + var_B * 0.9503041

    return X, Y, Z


def Delta_E_1994 ( CIE_L1, CIE_a1, CIE_b1, CIE_L2, CIE_a2, CIE_b2 ):
    WHT_L = 1
    WHT_C = 1
    WHT_H = 1
    xC1 = sqrt( ( CIE_a1 ** 2 ) + ( CIE_b1 ** 2 ) )
    xC2 = sqrt( ( CIE_a2 ** 2 ) + ( CIE_b2 ** 2 ) )
    xDL = CIE_L2 - CIE_L1
    xDC = xC2 - xC1
    xDE = sqrt( ( ( CIE_L1 - CIE_L2 ) * ( CIE_L1 - CIE_L2 ) )
            + ( ( CIE_a1 - CIE_a2 ) * ( CIE_a1 - CIE_a2 ) )
            + ( ( CIE_b1 - CIE_b2 ) * ( CIE_b1 - CIE_b2 ) ) )

    xDH = ( xDE * xDE ) - ( xDL * xDL ) - ( xDC * xDC )
    if ( xDH > 0 ):
        xDH = sqrt( xDH )
    else:
        xDH = 0

    xSC = 1 + ( 0.045 * xC1 )
    xSH = 1 + ( 0.015 * xC1 )
    xDL /= WHT_L
    xDC /= WHT_C * xSC
    xDH /= WHT_H * xSH

    Delta_E_1994 = sqrt( xDL ** 2 + xDC ** 2 + xDH ** 2 )

    return Delta_E_1994


filename                = 'Lenna_(test_image).png'
filepath                = f"RAL_CLASSIC/images/{filename}"

ral_classic             = []

with open( 'RAL_CLASSIC/ral_classic.csv', newline = '' ) as csvfile:
    reader = csv.reader( csvfile, delimiter = ',', quotechar = '|' )
    next( reader )
    for row in reader:
        ral_classic.append( row )

# Load the original image, and get its size and color mode.
im                      = Image.open( filepath )
width, height           = im.size
mode                    = im.mode

imResult = Image.new ( "RGB", im.size, color = ( 0, 0, 0)  )

# Show information about the original image.
print( f"Original image: {filename}" )
print( f"Size: {width} x {height} pixels" )
print( f"Mode: {mode}" )

res_ral_classic_final       = []

for i in range( width ): 
    for j in range( height ):
        rgbr, rgbg, rgbb    = im.getpixel( ( i, j ) )

        x,y,z               = list( Standard_RGB_to_XYZ ( rgbr, rgbg, rgbb ) )
        l, a, b             = list ( XYZ_to_CIE_Lab ( x, y, z ) )
        
        res_ral_classic     = []
        for res in range( len ( ral_classic ) ):
            x1,y1,z1        = list( Standard_RGB_to_XYZ ( int( ral_classic[ res ][ 3 ] ), 
                                                  int( ral_classic[ res ][ 4 ] ), 
                                                  int( ral_classic[ res ][ 5 ] ) ) )
            l1, a1, b1      = list ( XYZ_to_CIE_Lab ( x1, y1, z1 ) )
            taux            = Delta_E_1994 ( l1, a1, b1, l, a, b )
            res_ral_classic.append( [ ral_classic[ res ][ 3 ], 
                                     ral_classic[ res ][ 4 ], 
                                     ral_classic[ res ][ 5 ], 
                                     taux ] )

        res_ral_classic.sort(key = lambda row:row[ 3 ], reverse = True )

        imResult.putpixel( ( i, j ), 
                          ( int( res_ral_classic[ 0 ][ 1 ] ), 
                           int( res_ral_classic[ 0 ][ 2 ] ), 
                           int( res_ral_classic[ 0 ][ 3 ] ) ) )

        res_ral_classic_final.append( [ rgbr, 
                                       rgbg, 
                                       rgbb, 
                                       res_ral_classic[ 0 ][ 0 ], 
                                       res_ral_classic[ 0 ][ 1 ], 
                                       res_ral_classic[ 0 ][ 2 ], 
                                       res_ral_classic[ 0 ][ 3 ] ] )

print ( res_ral_classic_final )

imResult.save("RAL_CLASSIC/images/Lenna_(result_test_image).png", "PNG")