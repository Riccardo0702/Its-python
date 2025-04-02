def check_parentheses(expression: str) -> bool:
    verifica = False
    for i in expression:
        if i == "(":
            for i in expression:
                if i == ")":
                    verifica = True
                else:
                    verifica = False
    return verifica


print(check_parentheses(")("))


def check_parentheses(expression: str) -> bool:
    count_aperte = 0  

    for tonda in expression:
        if tonda == '(':  
            count_aperte += 1  
        elif tonda == ')':  
            count_aperte -= 1  
            
            if count_aperte < 0:
                return False

    return count_aperte == 0