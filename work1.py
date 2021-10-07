n = 'ШАЛАШ'
def Palindrome(n):
    if n == n[::-1]:
        return True
    else:
        return False
print(Palindrome(n))
