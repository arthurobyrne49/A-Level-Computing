def factorial(n: int):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)

def is_palindrome(s: str):
    if len(s) < 2:
        return True
    if s[0] == s[-1]:
        return is_palindrome(s[1:-1])
    else:
        return False