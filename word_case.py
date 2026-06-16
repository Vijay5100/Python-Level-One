word = (input("Enter the word: "))

# match statement
match word:
    case "happy":
            print("sad")
    case "cold":
            print("hot")
    case "big":
            print("small")
    case "fast":
            print("slow")
    case "light":
            print("dark")
    case "up":
            print("down")
    case "young":
            print("old")
    case "soft":
            print("hard")
    case "full":
            print("empty")
    case "open":
            print("closed")
    case _:
        print("Number not found")
