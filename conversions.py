#! /user/bin/env/python3
#conversions by Zach Palmer
#this is the midterm program

from Converter import Conversions as convert #use alias

useKel = False
convertOps = ["Miles", "Ounces","Fahrenheit temp","Celcius temp","Meters","Liters"]
def main():
    global useKel
    print("Welcome to the English-Metric Converter")
    kel = input("Do you want include Kelvin in temp conversions (Y/N) : ")
    print()
    try:
        if kel.lower() == "y":
            useKel = True
        elif kel.lower() == "n":
            useKel = False
        else:
            print("I did not understand your request. So Kelvin will not be used")
            print()
    except ValueError:
        print("Invalid input: Kelvin will not be used.")
        print()

    choice = getChoice()
    while choice != 0:
        try:
            data = input(f"Enter your {convertOps[choice-1]} to be converted : ")
            if choice == 1:
                #miles to kilometers
                km = convert.MileToKm(data)
                print(f"{data} miles = " + "{:.3f}".format(km) + " kilometers")
            elif choice == 2:
                gr = convert.OunceToGram(data)
                print(f"{data} ounces = " + "{:.3f}".format(gr) + " grams")
            elif choice == 3:
                cel = convert.FahrenheitToCel(data) #raise exception in function so if below absolute zero will display error msg
                print(f"A temp of {data} Fahrenheit = " + "{:+.3f}".format(cel) + " Celcius")
                if useKel:
                    kel = convert.CelciusToKel(cel)
                    print(f"\tThis is also a temperature of " + "{:+.3f}".format(kel) + " Kelvin")
            elif choice == 4:
                fh = convert.CelciusToFahrn(data)
                print(f"A temp of {data} Celcius = " + "{:+.3f}".format(fh) + " Fahrenheit")
                if useKel:
                    kel = convert.CelciusToKel(data)
                    print(f"\tThis is also a temperature of " + "{:+.3f}".format(kel) + " Kelvin")
            elif choice == 5:
                ft = convert.MeterToFt(data)
                print(f"{data} meters = " + "{:.3f}".format(ft) + " feet")
            elif choice == 6:
                gal = convert.LiterToGal(data)
                print(f"{data} liters = " + "{:.3f}".format(gal) + " gallons")
            else:
               print("Unknown conversion")
        except ValueError as errMsg: # errMsg is a variable can be anything and holds erro message from converter
            print(f"Data Error: {errMsg}")
        except Exception as gErrMsg:
            print(f"General Error: {gErrMsg}")

        print()
        choice = getChoice()
    print()
    print("Thanks for using the converter")

    
def getChoice():
    goodInput = False
    while not goodInput:
        try:
            c = int(input("Conversion? 1=Mi-Km,2=0z-Gr,3=F-C,4=C-F,5=M-Ft,6=Li-Gal,0=End : "))
            if c not in range(0,7):
                print("Error: valid operations are 1-6 or 0 to quit")
            else:
                goodInput = True
        except ValueError:
            print("Error: valid operations are 1-6 or 0 to quit")
            goodInput = False
    return c        
            


if __name__ == "__main__":
    main()
