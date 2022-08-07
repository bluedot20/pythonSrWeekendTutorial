number=12345
number=str(number)
print(number[ : :-1])

def isPalindrome(number):
    number=str(number)
    reversedNum=number[::-1]
    return reversedNum == number
print(isPalindrome(1234321)) 