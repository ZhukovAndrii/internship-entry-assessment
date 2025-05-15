import random

for i in range(1, 101):
    number = random.randint(1, 100)
    print(i, number, 'Lucky number' if number % 7 == 0 else '')
    print('---') if i % 5 == 0 else None

#I know that in Python it is possible to create one-line solution and the task is to make the program as short as possible, so here it is:
#for i in range(1,101): n = random.randint(1,100); print(i, n, 'Lucky number' if n % 7 == 0 else ''); print('---') if i % 5 == 0 else None
