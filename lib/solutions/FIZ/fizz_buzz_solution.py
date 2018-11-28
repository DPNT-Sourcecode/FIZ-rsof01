# noinspection PyUnusedLocal
def fizz_buzz(number):
    if number%3==0 and number%5==0:
        return("fizz buzz") 
    
    elif number%5==0:
        return("buzz")
    
    elif number%3==0 OR "3" in str(number):
        return("fizz")
    
    else:
        return(number)

fizz_buzz(1)

