def is_palindrome(s: str) -> bool:
    # WRITE YOUR BRILLIANT CODE HERE
    s = [c.lower() for c in s if c.isalnum()]
    left_pointer = 0
    right_pointer = len(s) - 1
    while left_pointer < right_pointer:
        if s[left_pointer] != s[right_pointer]:
            print('I am in while and if')
            return False
            
        left_pointer += 1
        right_pointer -= 1
    return True
if __name__ == '__main__':
    s = input()
    res = is_palindrome(s)
    print('true' if res else 'false')