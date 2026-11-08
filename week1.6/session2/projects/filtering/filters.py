from image import Image
import random

def blur(originalfile,blurredfile):
    img =Image()
    img.read_pgm(f"{originalfile}.pgm")

    for row in range(1,img.height -1):
           for col in range(1,img.width -1):
               total = img.get(row,col)
                 

    # randrow = random.randint(1,img.height -1)
    # randcol = random.randint(1,img.height -1)
    # blurColour = img.get(randrow,randcol)

    blurColour = round(total/9)
    
    for row in range(1,img.height -1):
        for col in range(1,img.width -1):
            img.set(row,col,blurColour)

    img.write_pgm(f"{blurredfile}.pgm")
