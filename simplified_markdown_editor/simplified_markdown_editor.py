import re

markdown = ""

while True:
    formatter = input("Choose a formatter: > ")
    if formatter == "!done":
        break

    if formatter == "new-line":
        markdown += "\n"
        print(markdown)
        continue

    if formatter == "plain":
        text = input("Text: > ")
        markdown += text + "\n"
        print(markdown)
        continue

    if formatter == "header":
        level = input("Level: > ")
        text = input("Text: > ")
        if not level.isdigit() or int(level) < 1 or int(level) > 6:
            print("The level should be within the range of 1 to 6.")
            continue
        markdown += "#" * int(level) + " " + text + "\n"
        print(markdown)
        continue

    if formatter == "link":
        label = input("Label: > ")
        url = input("URL: > ")
        markdown += "[" + label + "](" + url + ")\n"
        print(markdown)
        continue

    print("Unknown formatter type or command")
