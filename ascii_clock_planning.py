c = input("input your prefered character") #c is the users preffered character

num0 = {"line1": c + c + c,
        "line2": c + " " + c,
        "line3": c + " " + c,
        "line4": c + " " + c,
        "line5": c + c + c,
    }
num1 = {"line1": " " + c + " ",
        "line2": c + c + " ",
        "line3": " " + c + " ",
        "line4": " " + c + " ",
        "line5": c + c + c,
    }
num2 = {"line1": c + c + c,
        "line2": " " + " " + c,
        "line3": c + c + c,
        "line4": c + " " + " ",
        "line5": c + c + c,
    }
num3 = {"line1": c + c + c,
        "line2": " " + " " + c,
        "line3": c + c + c,
        "line4": " " + " " + c,
        "line5": c + c + c,
    }
num4 = {"line1": c + " " + c,
        "line2": c + " " + c,
        "line3": c + c + c,
        "line4": " " + " " + c,
        "line5": " " + " " + c,
    }
num5 = {"line1": c + c + c,
        "line2": c + " " + " ",
        "line3": c + c + c,
        "line4": " " + " " + c,
        "line5": c + c + c,
    }
num6 = {"line1": c + c + c,
        "line2": c + " " + " ",
        "line3": c + c + c,
        "line4": c + " " + c,
        "line5": c + c + c,
    }
num7 = {"line1": c + c + c,
        "line2": " " + " " + c,
        "line3": " " + " " + c,
        "line4": " " + " " + c,
        "line5": " " + " " + c,
    }
num8 = {"line1": c + c + c,
        "line2": c + " " + c,
        "line3": c + c + c,
        "line4": c + " " + c,
        "line5": c + c + c,
    }
num9 = {"line1": c + c + c,
        "line2": c + " " + c,
        "line3": c + c + c,
        "line4": " " + " " + c,
        "line5": c + c + c,
    }

numberList = {0: num0, 1: num1, 2: num2, 3: num3, 4: num4, 
              5: num5, 6: num6, 7: num7, 8: num8, 9: num9,
              }
user_choice = input("your choice")
digit1 = int(user_choice[0])
digit2 = int(user_choice[1])
digit3 = int(user_choice[3])
digit4 = int(user_choice[4])
digits = [digit1, digit2, digit3, digit4]
for j in numberList[0]:

    for i in range(len(digits)):
        print(numberList[digits[i]][j], end=" ")

        if i == 1:
            if j == "line2" or j == "line4":
                print(":", end=" ")
            else:
                print(" ", end=" ")
    print()