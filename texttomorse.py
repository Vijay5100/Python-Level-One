print("1. Text to Morse Code")
print("2. Morse Code to Text")

choice = input("Choose 1 or 2: ")

if choice == "1":
    text = input("Text: ").lower()
    print("Morse Code: ",end=" ")
    for character in text: 
        match character:
            case 'a':
                print(".-",end=" ")
            case 'b':
                print("-...",end=" ")
            case 'c':
                print("-.-.",end=" ")
            case 'd':
                print("-..",end=" ")
            case 'e':
                print(".",end=" ")
            case 'f':
                print("..-.",end=" ")
            case 'g':
                print("--.",end=" ")
            case 'h':
                print("....",end=" ")
            case 'i':
                print("..",end=" ")
            case 'j':
                print(".---",end=" ")
            case 'k':
                print("-.-",end=" ")
            case 'l':
                print(".-..",end=" ")
            case 'm':
                print("--",end=" ")
            case 'n':
                print("-.",end=" ")
            case 'o':
                print("---",end=" ")
            case 'p':
                print(".--.",end=" ")
            case 'q':
                print("--.-",end=" ")
            case 'r':
                print(".-.",end=" ")
            case 's':
                print("...",end=" ")
            case 't':
                print("-",end=" ")
            case 'u':
                print("..-",end=" ")
            case 'v':
                print("...-",end=" ")
            case 'w':
                print(".--",end=" ")
            case 'x':
                print("-..-",end=" ")
            case 'y':
                print("-.--",end=" ")
            case 'z':
                print("--..",end=" ")
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
                print("/",end=" ")
                
elif choice == "2":
    morse = input("Morse Code: ").split(" ")

    print("Text: ", end="")
    for c in morse:
        match c:
            case ".-":
                print("a", end="")
            case "-...":
                print("b", end="")
            case "-.-.":
                print("c", end="")
            case "-..":
                print("d", end="")
            case ".":
                print("e", end="")
            case "..-.":
                print("f", end="")
            case "--.":
                print("g", end="")
            case "....":
                print("h", end="")
            case "..":
                print("i", end="")
            case ".---":
                print("j", end="")
            case "-.-":
                print("k", end="")
            case ".-..":
                print("l", end="")
            case "--":
                print("m", end="")
            case "-.":
                print("n", end="")
            case "---":
                print("o", end="")
            case ".--.":
                print("p", end="")
            case "--.-":
                print("q", end="")
            case ".-.":
                print("r", end="")
            case "...":
                print("s", end="")
            case "-":
                print("t", end="")
            case "..-":
                print("u", end="")
            case "...-":
                print("v", end="")
            case ".--":
                print("w", end="")
            case "-..-":
                print("x", end="")
            case "-.--":
                print("y", end="")
            case "--..":
                print("z", end="")
            case "-----":
                print("0", end="")
            case ".----":
                print("1", end="")
            case "..---":
                print("2", end="")
            case "...--":
                print("3", end="")
            case "....-":
                print("4", end="")
            case ".....":
                print("5", end="")
            case "-....":
                print("6", end="")
            case "--...":
                print("7", end="")
            case "---..":
                print("8", end="")
            case "----.":
                print("9", end="")
            case "/":
                print(" ", end="")
            case _:
                print("?", end="")

else:
    print("Invalid choice.")
