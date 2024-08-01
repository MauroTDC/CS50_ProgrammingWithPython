def main():
    get_media_type(input("File name: "))


def get_media_type(filename: str) -> None:
    try:
        extension = filename.split(".")[1].lower()
    except IndexError:
        print("Invalid input")
    else:
        if extension == "gif":
            print( "image/gif")
        elif extension == "jpg":
            print( "image/jpg")
        elif extension == "jpeg":
            print( "image/jpeg")
        elif extension == "png":
            print( "image/png")
        elif extension == "pdf":
            print( "application/pdf")
        elif extension == "txt":
            print( "text/plain")
        elif extension == "zip":
            print( "application/zip")
        else:
            print("application/octet-stream")


if __name__ == "__main__":
    main()