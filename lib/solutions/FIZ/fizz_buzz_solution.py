# noinspection PyUnusedLocal
def samedigit(num):
    r = []
    digits = list(str(num))
    for n in range(len(digits)-1):
        if digits[n] != digits[n+1]:
            r.append(1)
        else:
            r.append(0)
    if max(r)>0:
        return False
    else:
        return True

def fizz_buzz(number):

    if (number%3==0 or "3" in str(number)) and (number%5== 0 or "5" in str(number)) and number%2!=0:
        return("fizz buzz fake deluxe")   
    
    elif (number%3==0 or "3" in str(number)) and  (number%5== 0 or "5" in str(number)):
        return("fizz buzz deluxe")

    elif (number%5==0 and "5" in str(number)) and number%2!=0:
        return("buzz fake deluxe")

    elif (number%5==0 and "5" in str(number)):
        return("buzz deluxe")
    
    elif (number%3==0 and "3" in str(number)) and number%2!=0:
        return("fizz fake deluxe")

    elif(number%3==0 and "3" in str(number)):
        return("fizz deluxe")

    elif number%2!=0 and ((number%3==0 and "3" in str(number)) or (number%5== 0 and "5" in str(number))):
        return("fake deluxe")

    elif (number%3==0 and "3" in str(number)) or (number%5== 0 and "5" in str(number)) :
        return("deluxe")

    elif (number%3==0 or "3" in str(number)) and (number%5== 0 or "5" in str(number)):
        return("fizz buzz") 
    
    elif number%5==0 or "5" in str(number):
        return("buzz")
    
    elif number%3==0 or "3" in str(number):
        return("fizz")
    
    else:
        return(number)

#print(fizz_buzz(111))


