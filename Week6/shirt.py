import sys
from os.path import splitext
from PIL import Image, ImageOps

def main():
    argument()
    #Oppening the puppet image
    try:
        imageFile = Image.open(sys.argv[1])
    except FileNotFoundError:
        sys.exit("Input does not exist")
    #Oppening the shirt image
    shirtImage = Image.open("shirt.png")
    #Getting the size of the shirt
    size = shirtImage.size
    #Reasizing the muppet image to fit the shirt
    muppet = ImageOps.fit(imageFile, size)
    #Past the shirt into the muppet
    muppet.paste(shirtImage, shirtImage)
    #Creat the output image
    muppet.save(sys.argv[2])

def argument():
    #Checking how many arguments on the command-line
    if len(sys.argv) < 3:
        sys.exit("Two few command-line arguments")
    if len(sys.argv) > 3:
        sys.exit("Two many command-line arguments")
    file1 = splitext(sys.argv[1])
    file2 = splitext(sys.argv[2])
    #Checking if it is an image file
    if extension(file1[1]) == False:
        sys.exit("Invalid input")
    if extension(file2[1]) == False:
        sys.exit("Invalid output")
    #Checking if the extensions on both files is the same
    if file1[1].lower() != file2[1].lower():
        sys.exit("Input and output have different extensions")

def extension(file):
    if file in [".jpeg", ".jpg", ".png"]:
        return True
    return False


if __name__ == "__main__":
    main()