def main():
    file = input("File Name: ").lower().strip()
    file_extension = get_file_extension(file)
    print(get_media_type(file_extension))


def get_media_type(file_extension):
    match file_extension:
        case ".gif":
            return "image/gif"
        case ".jpg" | ".jpeg":
            return "image/jpeg"
        case ".png":
            return "image/png"
        case ".pdf":
            return "application/pdf"
        case ".txt":
            return "text/plain"
        case ".zip":
            return "application/zip"
        case _:
            return"application/octet-stream"


def get_file_extension(file):
    """Finds the dot in the file path and then slices the file path from the dot index
    to the end to return the extension"""
    # Uses optional string range parameter to ensure it always pulls the final extension
    # Example get ".pdf" from "file_example.txt.pdf"
    extension_dot_index = file.find(".", -5)
    return file[extension_dot_index:]


main()
