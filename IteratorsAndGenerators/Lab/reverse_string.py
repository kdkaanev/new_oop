def reverse_text(text):
    i = -1
    for _ in range(len(text)):
        yield text[i]
        i -= 1

for char in reverse_text("step"):
    print(char, end='')
