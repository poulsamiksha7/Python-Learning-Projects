import converter_tools

def unit_converter():
    try:
        if user_input==1:
            km=int(input("Enter Value of Kilometer: "))
            return converter_tools.km_to_miles(km)
        elif user_input==2:
            c=int(input("Enter Value of Celcius: "))
            return converter_tools.celcius_to_fahrenheit(c)
        elif user_input==3:
            kg=int(input("Enter Value of Kilogram: "))
            return converter_tools.kg_to_pounds(kg)
        elif user_input==4:
            l=int(input("Enter Value of Liters: "))
            return converter_tools.liters_to_gallons(l)
        else:
            print("Invalid Input")
    except ValueError:
        return "Invalid Input."
    
print("Menu \n 1)KiloMeters to Miles \n 2)Celcius to Fahrenheit \n 3)Kilogram to Pounds \n 4)Liters to Gallons ")
user_input=int(input("\n Choose (1/2/3/4)"))
print(unit_converter())


