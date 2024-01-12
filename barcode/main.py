#import barcode 
from barcode import Code128
from barcode.writer import ImageWriter
def generate_barcode(data):
    code = Code128(data, writer = ImageWriter())
    code.save("barcode.svg")
    print(code)
    print("Barcode generated.")

data = "123"
generate_barcode(data)