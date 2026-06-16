month_number = int(input("Enter the month number: "))

# 1 = January
# 2 = February
# 3 = March
# 4 = April
# 5 = May
# 6 = June
# 7 = July
# 8 = August
# 9 = September
# 10 = October
# 11 = November
# 12 = December

# match statement
match month_number:
    case 1:
        if month_number == 1:
            print("January")

    case 2:
        if month_number == 2:
            print("February")

    case 3:
        if month_number == 3:
            print("March")

    case 4:
        if month_number == 4:
            print("April")

    case 5:
        if month_number == 5:
            print("May")

    case 6:
        if month_number == 6:
            print("June")

    case 7:
        if month_number == 7:
            print("July")

    case 8:
        if month_number == 8:
            print("August")

    case 9:
        if month_number == 9:
            print("September")

    case 10:
        if month_number == 10:
            print("October")

    case 11:
        if month_number == 11:
            print("November")

    case 12:
        if month_number == 12:
            print("December")

    case _:
        print("Invalid month number")
