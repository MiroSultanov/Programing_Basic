book_name = input()
counter = 0
book_is_found = False
next_book = input()
while next_book != "No More Books":
    if next_book == book_name:
        book_is_found = True
        break
    counter += 1
    next_book = input()
if book_is_found:
    print(f"You checked {counter} books and found it.")
else:
    print(f"The book you search is not here!")
    print(f"You checked {counter} books.")

