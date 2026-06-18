'''
Text: Sharukh123
Morse Code: ...
'''

text = input("Text: ").lower()

print("Morse Code: ", end=" ")
for character in text:
    match character:
        case 'a':
            print(".-", end=" ")
        case 'b':
            print("-...", end=" ")
        case 'c':
            print("-.-.", end=" ")
        case 'd':
            print("-..", end=" ")
        case 'e':
            print(".", end=" ")
        case 'f':
            print("..-.", end=" ")
        case 'g':
            print("--.", end=" ")
        case 'h':
            print("....", end=" ")
        case 'i':
            print("..", end=" ")
        case 'j':
            print(".---", end=" ")
        case 'k':
            print("-.-", end=" ")
        case 'l':
            print(".-..", end=" ")
        case 'm':
            print("--", end=" ")
        case 'n':
            print("-.", end=" ")
        case 'o':
            print("---", end=" ")
        case 'p':
            print(".--.", end=" ")
        case 'q':
            print("--.-", end=" ")
        case 'r':
            print(".-.", end=" ")
        case 's':
            print("...", end=" ")
        case 't':
            print("-", end=" ")
        case 'u':
            print("..-", end=" ")
        case 'v':
            print("...-", end=" ")
        case 'w':
            print(".--", end=" ")
        case 'x':
            print("-..-", end=" ")
        case 'y':
            print("-.--", end=" ")
        case 'z':
            print("--..", end=" ")
        case '0':
            print("-----", end=" ")
        case '1':
            print(".----", end=" ")
        case '2':
            print("..---", end=" ")
        case '3':
            print("...--", end=" ")
        case '4':
            print("....-", end=" ")
        case '5':
            print(".....", end=" ")
        case '6':
            print("-....", end=" ")
        case '7':
            print("--...", end=" ")
        case '8':
            print("---..", end=" ")
        case '9':
            print("----.", end=" ")
        case ' ':
            print("/", end=" ")
        case _:
            print("?", end=" ")
