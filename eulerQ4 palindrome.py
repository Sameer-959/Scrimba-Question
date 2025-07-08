

def is_palindrome(value):
    value = str(value)
    return value == value[::-1]
def main():    
     max_palindrome = 0
     for i in range (999,100,-1):
        for j in range (999,100,-1):
             product = i * j
             if product <= max_palindrome:
                 break
             if is_palindrome(product):
                 max_palindrome = product
                                
     print("The maximum palindrome number is ", max_palindrome)

main()

                        
        