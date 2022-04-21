#converts roman numerals to decimals
def romanToDecimal(roman):
    #i is our counter
    i = int (0)
    #decimal will be the decimal version of the roman numeral we are looking for
    decimal = 0
    #stopAt tells us when to stop our loop
    stopAt = len(roman)

    #as long as i is less than the length of the string, it will contnue adding
    while i < stopAt:
        #these if statements check for the subtraction element of roman numerals
        if roman[i:(i + 2)].upper() == "CM":
            decimal = decimal + 900
            i = i + 2
        elif roman[i:(i + 2)].upper() == "CD":
            decimal = decimal + 400
            i = i + 2
        elif roman[i:(i + 2)].upper() == "XC":
            decimal = decimal + 90
            i = i + 2
        elif roman[i:(i + 2)].upper() == "XL":
            decimal = decimal + 40
            i = i + 2
        elif roman[i:(i + 2)].upper() == "IX":
            decimal = decimal + 9
            i = i + 2
        elif roman[i:(i + 2)].upper() == "IV":
            decimal = decimal + 4
            i = i + 2
        #this if statments check and add the basic roman numerals
        elif roman[i].upper() == "M":
            decimal = decimal + 1000
            i = i + 1
        elif roman[i].upper() == "D":
            decimal = decimal + 500
            i = i + 1
        elif roman[i].upper() == "C":
            decimal = decimal + 100
            i = i + 1
        elif roman[i].upper() == "L":
            decimal = decimal + 50
            i = i + 1
        elif roman[i].upper() == "X":
            decimal = decimal + 10
            i = i + 1
        elif roman[i].upper() == "V":
            decimal = decimal + 5
            i = i + 1
        elif roman[i].upper() == "I":
            decimal = decimal + 1
            i = i + 1

    #we will return the decimal version of our roman numeral
    return decimal

#converts decimals to roman numerals
def decimalToRoman(decimal):
    roman = ""
    dec = formatDec(decimal)
    stopAt = 0
    i = len(dec) - 1
    while i >= stopAt:
        #deals with the 1000s place value
        if i == 0:
            if dec[i] == '3':
                roman = ("MMM" + roman)
            elif dec[i] == '2':
                roman = ("MM" + roman)
            elif dec[i] == '1':
                roman = ("M" + roman)
        #deals with the 100s place value
        elif i == 1:
            if dec[i] == '9':
                roman = ("CM" + roman)
            elif dec[i] == '8':
                roman = ("DCCC" + roman)
            elif dec[i] == '7':
                roman = ("DCC" + roman)
            elif dec[i] == '6':
                roman = ("DC" + roman)
            elif dec[i] == '5':
                roman = ("D" + roman)
            elif dec[i] == '4':
                roman = ("CD" + roman)
            elif dec[i] == '3':
                roman = ("CCC" + roman)
            elif dec[i] == '2':
                roman = ("CC" + roman)
            elif dec[i] == '1':
                roman = ("C" + roman)
        #deals with the 10s place value
        elif i == 2:
            if dec[i] == '9':
                roman = ("XC" + roman)
            elif dec[i] == '8':
                roman = ("LXXX" + roman)
            elif dec[i] == '7':
                roman = ("LXX" + roman)
            elif dec[i] == '6':
                roman = ("LX" + roman)
            elif dec[i] == '5':
                roman = ("L" + roman)
            elif dec[i] == '4':
                roman = ("XL" + roman)
            elif dec[i] == '3':
                roman = ("XXX" + roman)
            elif dec[i] == '2':
                roman = ("XX" + roman)
            elif dec[i] == '1':
                roman = ("X" + roman)
        #deals with the 1s place value
        elif i == 3:
            if dec[i] == '9':
                roman = (roman + "IX")
            elif dec[i] == '8':
                roman = (roman + "VIII")
            elif dec[i] == '7':
                roman = (roman + "VII")
            elif dec[i] == '6':
                roman = (roman + "VI")
            elif dec[i] == '5':
                roman = (roman + "V")
            elif dec[i] == '4':
                roman = (roman + "IV")
            elif dec[i] == '3':
                roman = (roman + "III")
            elif dec[i] == '2':
                roman = (roman + "II")
            elif dec[i] == '1':
                roman = (roman + "I")
        i = i - 1
    return roman

#formats decimal to have 4 digits in it
def formatDec(decimal):
    i = len (decimal)
    if i == 1:
        decimal = ("000" + decimal)
    elif i == 2:
        decimal = ("00" + decimal)
    elif i == 3:
        decimal = ("0" + decimal)
    return decimal

#asks what type of conversion they wish to make, and gets the number
def getTask():
    choice = ""
    roman = ""
    decimal = 0
    while True:
        choice = input ("do you wish to enter a roman numeral or a decimal? (r/d) ")
        if choice.lower() == "r":
            roman = input("please input the roman numeral you wish to convert: ")
            answer = int(romanToDecimal(roman))
            print ("the roman numeral", roman.upper(), "in decimal form is", answer)
            break
        elif choice.lower() == "d":
            decimal = input("please input the decimal number you wish to convert: ")
            answer = decimalToRoman(decimal)
            print ("the decimal", decimal, "in roman numeral form is", answer)
            break
        else:
            print ("please enter a valid answer")

def main():

    #checks if they want too conver numbers

    while True:
        do = input("would you like to convert some roman numerals and decimals? (y/n) ")
        if do.lower() == "y":
            print("\nWARNING: cannot process number higher than 3,999\n")
            getTask()
        elif do.lower() == "n":
            print("thank you for you time, good luck doing archeology!")
            break
        else:
            print("please enter a valid answer")

if __name__ == '__main__':
    main()
