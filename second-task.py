from collections import deque

def is_palindrome(string: str) -> bool:
    prepared_string = deque(''.join(string.lower().split()))

    while len(prepared_string) > 1:
        if prepared_string.popleft() != prepared_string.pop():
            return False
    return True

if __name__ == "__main__":
    test_strings = [
        "The antique shop offers a treasure",
        "Visitors can browse through shelves",
        "No lemon no melon",
        "madam",
        "nureses nur",
        "Able was I ere I saw Elba",
        "Hello",
        "Was it a car or a cat I saw"
    ]

    for test in test_strings:
        res = is_palindrome(test)
        if res:
            print(f"'{test}' is a palindrome!")
        else:
            print(f"'{test}' is not a palindrome.")