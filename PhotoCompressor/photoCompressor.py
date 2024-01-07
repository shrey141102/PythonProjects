import math
from PIL import Image

def compress_image(imagePath, fileSize=24000):
    try:
        inputImage = Image.open(imagePath)
        pixelCount = 2.8114 * fileSize

        factor = pixelCount / math.prod(inputImage.size)
        factor = 1 if factor > 1 else factor
        
        newDimensions = [int(dim * factor) for dim in inputImage.size]
        
        copy_constructor = type(inputImage.size)
        newDimensions = copy_constructor(newDimensions)
        
        compressedPhoto = inputImage.resize(newDimensions, resample=Image.LANCZOS)
        parts = imagePath.split(".")
        outputPath = "".join(parts[0:1]) + "_compressed." + parts[-1]
        compressedPhoto.save(outputPath, optimize=True, quality=95)

        print("Picture is compressed successfully!")
    
    except:
        print("There is some error either in imagePath, Modules may not found, etc.")

imagePath = input("\nEnter the image file path: ")
# imagePath = "PhotoCompressor\\JaiShriKrishna.jpg"

fileSize = int(input("\nEnter the output image file size(in bytes): "))
# fileSize = 24000

compress_image(imagePath, fileSize)
