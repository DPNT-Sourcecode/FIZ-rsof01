# noinspection PyUnusedLocal
"""
def fizz_buzz(number):
    if number > 10 and ??
    
    if (number%3==0 or "3" in str(number)) and (number%5== 0 or "5" in str(number)):
        return("fizz buzz") 
    
    elif number%5==0 or "5" in str(number):
        return("buzz")
    
    elif number%3==0 or "3" in str(number):
        return("fizz")
    
    else:
        return(number)

print(fizz_buzz(30))
"""

s = "111"

#letters = list(s)

#print(len(letters))

def samedigit(num):
    digits = list(str(num))
    for n in range(len(digits)-1):
        if digits[n] != digits[n+1]:
            return False
            break
        else:
            return True
    

print(samedigit(335333))

