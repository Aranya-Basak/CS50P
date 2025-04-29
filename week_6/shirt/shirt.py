from PIL import Image, ImageOps
import sys
import os
format = [".jpg", ".jpeg", ".png"]

def main():
    if len(sys.argv) > 3:                                       # checks for errors
        sys.exit("Too many arguements")
    elif len(sys.argv) < 3:
        sys.exit("Too few arguements")
    _, extension_1 = os.path.splitext(sys.argv[1])
    _, extension_2 = os.path.splitext(sys.argv[2])
    if not extension_1 in format:
        sys.exit("Not in required format")
    elif not extension_2 in format:
        sys.exit("Not in required format")
    elif extension_1 != extension_2:
        sys.exit("Input and Output are different extensions")
    else:
        magic(sys.argv[1], sys.argv[2])


def magic(inpt, outpt):
    try:
        shirt = Image.open("shirt.png")
        r_size = shirt.size
        inp_img = Image.open(inpt)
        r_img = ImageOps.fit(inp_img, r_size)
        r_img.paste(shirt, mask = shirt)
        r_img.save(outpt)
        return None
    except FileNotFoundError:
        sys.exit("File does not exist")


main()
