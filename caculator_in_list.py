** start of main.py **

def evaluate(numbers, operators):
    for n in numbers:
        if not isinstance(n, int):
            return
    
    for o in operators:
        if not o in "+-*/%":
            return
          
    result = numbers[0]
    x = 0
    
    for i in range(1, len(numbers)):
        match operators[x]:
            case "+":
                result += numbers[i]
            case "-":
                result -= numbers[i]
            case "*":
                result *= numbers[i]
            case "/":
                result /= numbers[i]
            case "%":
                result %= numbers[i]
        x = x + 1 if x < len(operators)-1 else 0

    return result

print(evaluate([17, 61, 40, 24, 38, 14], ['+', '%']))

** end of main.py **

