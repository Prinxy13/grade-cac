x = float(input('What is the length of the first side of the triangle!?'))
y = float(input('what is the lenght of the second side of triangle!?'))
z = float(input('what is the length of third side of the triangle!?'))

if x + y <= z or y + z <= x or z + x<=y:
    print('Error!! Triangle does not exist')

else:
    if x == y == z:
        print('This is an equilateral triangle.\nThe three sides and three angles are equal.')

    elif x == y or y == z or z == x:
        print('This is an isoceles Triangle.\nTwo sides have egual lenght.')

    else:
        print('This is a Scalene Triangle.\nThree sides have equal lengths.')        