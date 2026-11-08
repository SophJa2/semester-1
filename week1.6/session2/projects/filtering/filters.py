from image import Image
import random

def blur(originalfile,blurredfile):
    img =Image()
    img.read_pgm(f"{originalfile}.pgm")
    img.copy()

    for row in range(1,img.height -1):
        for col in range(1,img.width -1):
            total = 0
            for r in range(row-1,row+2):
                for c in range(col-1,col+2):
                    total = total + img.get(r,c)
            blurColour = round(total/9)
            img.set(row,col,blurColour)

    img.write_pgm(f"{blurredfile}.pgm")
