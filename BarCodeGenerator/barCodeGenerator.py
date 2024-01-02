from barcode import EAN13

# import ImageWriter to generate an image file
from barcode.writer import ImageWriter

number = input("Enter a number for BarCode: ")
# For example,
# number = '5901432115697'

generated_barcode = EAN13(number, writer=ImageWriter())
generated_barcode.save("barCodePicture")
