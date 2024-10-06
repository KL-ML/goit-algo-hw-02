def is_closed_brackets(expression):
    stack = []
    brackets = {
        '(': ')',
        '{': '}',
        '[': ']',
    }
    opening_brackets = set(brackets.keys())
    closing_brackets = set(brackets.values())

    for char in expression:
        if char in opening_brackets:
            stack.append(char)
        elif char in closing_brackets:
            if not stack or char != brackets[stack.pop()]:
              return "Закриваючі дужки не симетричні"
    if stack:
        return "Закриваючі дужки не симетричні"
    return "Закриваючі дужки симетричні"


list = [
    '( ) { [ ] ([]{()} ) ( ) { } } ]',
    '( ){[ 1 ]( 1 + 3 )( ){ }}',
    '( 23 ( 2 - 3);',
    '( 11 }',
    '{ 87 }'
    '[({ 67 })]',
    '} wer }[]'
]

for example in list:
    print(is_closed_brackets(example))