import sys
from PIL import Image, ImageOps


def main():
    validate_argv_commands()
    fit_shirt()


def fit_shirt():
    """Rescales output image to perfectly have the shirt image overlaid on top of it"""

    try:
        output_image = Image.open(sys.argv[1])
    except FileNotFoundError:
        sys.exit("Input does not exist")

    shirt_image = Image.open("shirt.png")  # get shirt
    shirt_size = shirt_image.size  # get shirt_image size
    output_file = ImageOps.fit(output_image, shirt_size)  # rescale output image to fit shirt image

    output_file.paste(shirt_image, shirt_image)  # overlay shirt to output image

    # save final output image
    output_file.save(
        sys.argv[2]  # name output file after user input
    )


def validate_argv_commands():
    """Reads the argv commands passed on by the user. If argv's are invalid, program will exit prematurely"""

    # validate argvs length tests
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")

    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    # init extensions data
    valid_extensions = [".jpg", ".jpeg", ".png"]
    input_extension = get_extension(sys.argv[1])
    output_extension = get_extension(sys.argv[2])

    # validate extension tests
    if output_extension not in valid_extensions:
        sys.exit("Invalid Output")

    if input_extension != output_extension:
        sys.exit("Input and output have different extensions")


def get_extension(file):
    """Returns the extension of a file as string"""
    dot_index = file.find(".")  # find dot index to slice string at file extension
    return file[dot_index:].lower()


if __name__ == "__main__":
    main()
