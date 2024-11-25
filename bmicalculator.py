name = input('Enter your name pls!:')
weight = int(input(f'your weightin kilograms is!:'))
if weight <= 0:
    print('Error! invalid value enterd!')

height = float(input(f'your height in meters is:'))
if height <= 0:
    print('Error! Invalid value enered!')

body_mass_index = weight/height**2
if body_mass_index < 18.5:
    print(f'{name}, your body mass index is {body_mass_index:.2f}\nYou are underweight')
elif body_mass_index >= 18.5 and body_mass_index <  25:
    print(f'{name}, your body mass index is {body_mass_index:.2f}\nYou have a normal weight')
elif body_mass_index >= 25 and body_mass_index< 30:
     print(f'{name}, your body mass index is {body_mass_index:.2f}\nopps!! You are overweight')
elif body_mass_index >=30:
     print(f'{name}, your body mass index is {body_mass_index:.2f}\nsorry!!, you are obese')
