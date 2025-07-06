active = True

while active:
    
    height = ""
    feet = "'"
    inches = '"'
    foot_zero_remover = ""
    answer = ""
    inch = 2.54
    foot = 30.48
    
    while type(height) != type(1.0):
        
        try:
            height = input("How tall are you in cm? ")
        
            height = float(height)
        
            if height > 274 or height <= 0:
                height = int(height)
                print("-")
                print("Try again!")
        
            elif height == 274:
                print("-")
                print("You're the tallest human ever recorded!")
                
            else:
                pass
        
        except ValueError:
            print("-")
            print("It's not a number. Try again!")

    height_in_inch = height / inch
    height_in_feet = height_in_inch // 12
    stringed = str(height_in_feet)

    for zero in stringed:
        if zero in ".0":
            foot_zero_remover += ""

        else:
            foot_zero_remover += zero

    remained_inch = height_in_inch % 12
    remained_inch = round(remained_inch, 2)

    feet_inches = foot_zero_remover + feet + str(remained_inch) + inches
    print("---------")
    print(feet_inches)
    print("---------")

    while answer != "y" and answer != "n":
        answer = input("Would you like to continue? ").lower()

    if answer == "y":
        print("-")
        continue
        
    else:
        print("-")
        input("Press Enter to terminate.")
        active = False