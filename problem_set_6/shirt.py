import sys
from PIL import Image, ImageOps


def main():
    if verify_arguments():
        create_image()


def verify_arguments():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    if verify_extension(sys.argv[1]) == False:
        sys.exit("Invalid input")
    elif verify_extension(sys.argv[2]) == False:
        sys.exit("Invalid output")
    else:
        try:
            if sys.argv[1].split(".")[1].lower() != sys.argv[2].split(".")[1].lower():
                sys.exit("Input and Output have different extensions")
            else:
                return True
        except IndexError:
             sys.exit("Input and Output have different extensions")   
        

def verify_extension(file: str):
    try:
        if file.split(".")[1].lower() in ("png","jpg","jpeg"):
            return True
        return False
    except IndexError:
        return False
    

def create_image():
    try:
        image_file = Image.open(sys.argv[1])
    except FileNotFoundError:
        sys.exit("Input does not exist")

    shirt = Image.open("shirt.png")
    shirt_size = shirt.size
    face_img = ImageOps.fit(image_file, shirt_size)
    face_img.paste(shirt, shirt)
    face_img.save(sys.argv[2])


if __name__ == "__main__":
    main()