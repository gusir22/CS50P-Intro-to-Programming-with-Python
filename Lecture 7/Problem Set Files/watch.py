import re


def main():
    print(parse(input("HTML: ")))


def parse(s):
    match = re.search(r'src="((?:https?://)?(?:www\.)?youtube\.com/embed/\w+)"', s, flags=re.IGNORECASE)

    try:
        link = match.group(1)
    except AttributeError:  # is raised if no matches to regex
        return None
    else:
        link = re.sub(r"http://", "https://", link)  # ensures link is using secure protocol
        link = re.sub(r"www.", "", link)  # remove "www."
        link = re.sub("youtube.com", "youtu.be", link)  # shortens domain to "youtu.be"
        link = re.sub("embed/", "", link)  # remove "embed/" from match for user friendly link
        return link


if __name__ == "__main__":
    main()
