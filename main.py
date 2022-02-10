# This is a basic BMI Calculator, hope you like it and enjoy
height = input("enter your height in meters: ") # This asks you for your height
weight = input("enter your weight in kg: ") # This asks you for your weight

convertHeight = float(height) # This converts height from string to a float nummber.
convertWeight = int(weight) # This converts height from string to a integer nummber.
calculation = convertWeight / convertHeight ** 2 # This divides the weight with height², because the BMI formula = Weight(KG) / Height(m²)
round_nummber = round(calculation) # This line of code rounds the nummber to a integer.

print(round_nummber)

# Overall this is not the best way to do it but i'am still learning Python and it is my second programming languange that i'am learning now.