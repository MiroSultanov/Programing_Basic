# Ani goes to her hometown after a very long period abroad. On her way home, she sees her grandmother's old library and remembers her favorite book. 
# Help Annie by writing a program in which she enters the book (text) she is looking for. Until Annie finds her favorite book or checks all the books in the library, 
# the program must read each time on a new line the name of each subsequent book (text) that she checks. The books in the library are gone as soon as you receive the text
# "No More Books".
# ⦁ If he does not find the book he is looking for, print it in two lines:
# ⦁ "The book you search is not here!"
# ⦁ "You checked {number} books."
# ⦁ If he finds his book, one line is printed:
# ⦁ "You checked {number} books and found it."

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

