# noinspection PyUnusedLocal
def fizz_buzz(number):
    if number%3==0 and number%5== 0:
        return("fizz buzz") 
    
    elif number%5==0:
        return("buzz")
    
    elif number%3==0:
        return("fizz")
    
    else:
        return(number)

print(fizz_buzz(13))