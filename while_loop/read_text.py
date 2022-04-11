# Write a program that reads text from the console (string) and prints it until it receives the "Stop" command.

while True:
    text = input()
    if text == "Stop":
        break
    print(text)
