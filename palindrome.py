def is_palindrome(s):
    if len(s) == 0 or len(s) == 1:
        return True
    elif s[0] != s[-1]:
        return False
    elif s[0] == s[-1]:
        return is_palindrome(s[1:-1])

def is_palindrome_itr(s):
    res = True
    for i in range(len(s)//2):
        left = s[i]
        right = s[-1-i]
        if left == right:
            continue
        elif left != right:
            res = False
    return res

test_cases = [
    ("racecar", True),
    ("madam", True),
    ("hello", False),
    ("a", True),
    ("", True),
    ("abccba", True),
    ("abcdecba", False),
]
for s, expected in test_cases:
    assert is_palindrome(s) == expected, f"Recursion failed for: {s}"
    assert is_palindrome_itr(s) == expected, f"Iteration failed for: {s}"
    print(f"{s!r} → {expected}")