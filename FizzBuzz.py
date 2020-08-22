count = 0
while count < 100:
    count = count + 1
    if count % 3 == 0:
        if count % 5 == 0:
            print('FizzBuzz')
        else:
            print('Fizz')
    else: 
        if count % 5 == 0:
            print('Buzz')
        else:
            print(count)