a ='welcome to my crypto hub!'
Student_name = input('Enter your name:')
print (f'Hola! {Student_name}! {a}') 
exam_score = float(input('Enter your score:'))
if exam_score < 0 or exam_score > 100:
    print('error!!'); print('you are a faliour')
elif exam_score >= 90 and exam_score <= 100:
    print(f'hi {Student_name} you scored {exam_score} You got an A! Congratulations')
elif exam_score >= 80 and exam_score <= 89:
    print(f'hi {Student_name} you scored {exam_score} You made a B! Well done')
elif exam_score >= 70 and exam_score <= 79:
    print(f'hi {Student_name} you scored {exam_score} You made a C! keep it up')
elif exam_score >= 60 and exam_score <= 69:
    print(f'hi {Student_name} you scored {exam_score} You made a D! quit play and read your books')
else:
    print(' You made an F! you are a big faliour go and start selling fish')
