def main():
    file_extension = file_type(input("File name: "))


def file_type(f):
    """str > str
    Returns the file name extension of a given file
    >>>file_type('.gif'):
    "image/gif"
    >>>file_type('.jpg'):
    "image/jpeg"
    """
    file_extension = f.strip().lower()
    if file_extension.endswith('.gif'):
        print("image/gif")
    elif file_extension.endswith('.jpg'):
        print("image/jpeg")
    elif file_extension.endswith('jpeg'):
        print("image/jpeg")
    elif file_extension.endswith('png'):
        print("image/png")
    elif file_extension.endswith('.pdf'):
        print("application/pdf")
    elif file_extension.endswith('.txt'):
        print("text/plain")
    elif file_extension.endswith('.zip'):
        print("application/zip")
    else:
        print("application/octet-stream")


main()
