print('Score Average Calculator')
number = input('How any classes? ')
while not (number.isdigit()):
    number = input('How any classes? ')
number = int(number)
total = 0
count = 0

while (count<number):
    score = input('Enter your score: ')
    while not (score.isdigit() and 0<=int(score)<=100):
        score = input('Enter your score: ')
    score = int(score)
    total += score
    count += 1

if (count>0):
    average = total/number
    print('Your average score =', round(average,1))
else:
    print('Your average score = 0.0')