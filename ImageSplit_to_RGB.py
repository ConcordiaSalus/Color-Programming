
from PIL import Image

filename                = 'Lenna_(test_image).png'
filepath                = f"RAL_CLASSIC/images/{filename}"

im                      = Image.open( filepath )
dataim                  = im.getdata()

R = [ ( d[ 0 ], 0, 0 ) for d in dataim ]
G = [ ( 0, d[ 1 ], 0 ) for d in dataim ]
B = [ ( 0, 0, d[ 2 ] ) for d in dataim ]

im.show()

im.putdata( R )
im.save( "RAL_CLASSIC/images/Lenna_(red_result_test_image).png", "PNG")
im.show()

im.putdata( G )
im.save( "RAL_CLASSIC/images/Lenna_(green_result_test_image).png", "PNG")
im.show()

im.putdata( B )
im.save( "RAL_CLASSIC/images/Lenna_(blue_result_test_image).png", "PNG")
im.show()