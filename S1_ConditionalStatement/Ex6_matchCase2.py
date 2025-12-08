
inp="MON"

match inp:
    case "mon":
        print("1")
    case "tue":
        print("2")
    case "wed":
        print("3")
    case "thr":
        print("4")
    case "fri":
        print("5")
    case "sat":
        print("6")
    case "sun":
        print("7")
    case _:
        print("Invalid input")
