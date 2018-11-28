# noinspection PyUnusedLocal
def fizz_buzz(number):
    if number%3==0:
        print("Fizz")
    
    elif number%5==0:
        print("Buzz")
    
    elif number%3==0 and number%5==0:
        print("Fizz Buzz")
    
    else:
        print(str(1))

fizz_buzz(30)
