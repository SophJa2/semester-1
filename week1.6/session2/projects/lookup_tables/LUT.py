from image import Image


def Lut(filename,invertname):
    img = Image()
    img.read_pgm(f"images/{filename}.pgm")
    img.copy()

    for row in range(0,img.height-1):
        for col in range(0,img.width-1):
            x = img.get(row,col)
            img.set(row,col,(255-x))

    img.write_pgm(f"{invertname}.pgm")

    