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
    if  number > 10 and samedigit(number) == True and (number%3==0 or "3" in str(number) and  (number%5== 0 or "5" in str(number)):
        return("fizz buzz deluxe")

    elif number > 10 and samedigit(number) == True:
        return("delux")

    elif (number%3==0 or "3" in str(number)) and (number%5== 0 or "5" in str(number)):
        return("fizz buzz") 
    
    elif number%5==0 or "5" in str(number):
        return("buzz")
    
    elif number%3==0 or "3" in str(number):
        return("fizz")
    
    else:
        return(number)







