# noinspection PyUnusedLocal
def fizz(num):
    if num%3==0 or '3' in str(num):
        return True
    else:
        return False
    
def buzz(num):
    if num%5==0 or '5' in str(num):
        return True
    else:
        return False
    
def deluxe(num):
    if num%2==0 and ((num%3==0 and '3' in str(num)) or (num%5==0 and '5' in str(num))):
        return True
    else:
        return False
    
def fake_deluxe(num):
    if num%2!=0 and ((num%3==0 and '3' in str(num)) or (num%5==0 and '5' in str(num))):
        return True
    else:
        return False
   

def fizz_buzz(num):
    if fizz(num)==True and buzz(num)==True and fake_deluxe(num)==True:
        return("fizz buzz fake deluxe")
        
    elif fizz(num)==True and buzz(num)==True and deluxe(num)==True:
        return("fizz buzz deluxe")
        
    elif buzz(num)==True and fake_deluxe(num)==True:
        return("buzz fake deluxe")
        
    elif buzz(num)==True and deluxe(num)==True:
        return("buzz deluxe")
        
    elif fizz(num)==True and fake_deluxe(num)==True:
        return("fizz fake deluxe")
        
    elif fizz(num)==True and deluxe(num)==True:
        return("fizz deluxe")
        
    elif fake_deluxe(num)==True:
        return("fake deluxe")
        
    elif deluxe(num)==True:
        return("deluxe")
        
    elif buzz(num)==True and fizz(num)==True:
        return("fizz buzz")
        
    elif buzz(num)==True:
        return("buzz")
        
    elif fizz(num)==True:
        return("fizz")
        
    else:
        return(num)

print(buzz(30))     