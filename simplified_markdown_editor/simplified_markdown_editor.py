#import re
#
#markdown = ""
#
#while True:
#    formatter = input("Choose a formatter: > ")
#    if formatter == "!done":
#        break
#
#    if formatter == "new-line":
#        markdown += "\n"
#        print(markdown)
#        continue
#
#    if formatter == "plain":
#        text = input("Text: > ")
#        markdown += text + "\n"
#        print(markdown)
#        continue
#
#    if formatter == "header":
#        level = input("Level: > ")
#        text = input("Text: > ")
#        if not level.isdigit() or int(level) < 1 or int(level) > 6:
#            print("The level should be within the range of 1 to 6.")
#           continue
#        markdown += "#" * int(level) + " " + text + "\n"
#        print(markdown)
#        continue
#
#    if formatter == "link":
#        label = input("Label: > ")
#        url = input("URL: > ")
#        markdown += "[" + label + "](" + url + ")\n"
#        print(markdown)
#        continue
#
#    print("Unknown formatter type or command")

def print_ordered_list(rows):
    for i in range(len(rows)):
        print(f"{i+1}. {rows[i]}")

def print_unordered_list(rows):
    for row in rows:
        print(f"* {row}")

while True:
    formatter = input("Choose a formatter: ")
    if formatter == "!done":
        break
    elif formatter == "ordered-list":
        while True:
            num_rows = input("Number of rows: ")
            if num_rows.isdigit() and int(num_rows) > 0:
                rows = []
                for i in range(int(num_rows)):
                    row = input(f"Row #{i+1}: ")
                    rows.append(row)
                print_ordered_list(rows)
                break
            else:
                print("The number of rows should be greater than zero")
    elif formatter == "unordered-list":
        while True:
            num_rows = input("Number of rows: ")
            if num_rows.isdigit() and int(num_rows) > 0:
                rows = []
                for i in range(int(num_rows)):
                    row = input(f"Row #{i+1}: ")
                    rows.append(row)
                print_unordered_list(rows)
                break
            else:
                print("The number of rows should be greater than zero")
    else:
        print("Invalid formatter")


        def print_ordered_list(rows):
            for i in range(len(rows)):
                if i == 1:
                    print(f"2. {rows[1]}")
                elif i == 2:
                    print(f"3. {rows[2]}")
                else:
                    print(f"{i + 1}. {rows[i]}")
