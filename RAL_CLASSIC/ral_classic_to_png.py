
import csv
from PIL import Image, ImageDraw, ImageFont
from os import path, mkdir, remove

folder_picture = 'RAL_CLASSIC/ral_classic_images'

if not path.exists( folder_picture ):
    mkdir( folder_picture )

with open( 'RAL_CLASSIC/ral_classic.csv', newline = '' ) as csvfile:
    spamreader = csv.reader( csvfile, delimiter = ',', quotechar = '|' )
    next( spamreader )
    for row in spamreader:
        filename = row[ 0 ].replace( " ", "_" ) + '.png'
       
        im = Image.new( "RGB", ( 222, 337 ), ( int( row[ 3 ]), int( row[ 4 ] ), int( row[ 5 ] ) ) )
        draw = ImageDraw.Draw( im )
        draw.rectangle( [ ( 0, 223 ), ( 222, 337 ) ], ( 255, 255, 255 ) )
        
        font = ImageFont.truetype( 'RAL_CLASSIC/fonts/Roboto-Black.ttf', 32 )
        draw.text( ( 10, 230 ), row[ 0 ] , fill = ( 0, 0, 0 ), font = font )

        font = ImageFont.truetype( 'RAL_CLASSIC/fonts/Roboto-Regular.ttf', 16 )
        draw.text( ( 10, 270 ), row[ 1 ] , fill = ( 0, 0, 0 ), font = font )

        font = ImageFont.truetype( 'RAL_CLASSIC/fonts/Roboto-Regular.ttf', 16 )
        draw.text( ( 10, 290 ), row[ 2 ], fill = ( 0, 0, 0 ), font = font )

        if path.exists( folder_picture + '/' + filename ):
            remove( folder_picture + '/' + filename )

        im.save( folder_picture + '/' + filename, "PNG" )