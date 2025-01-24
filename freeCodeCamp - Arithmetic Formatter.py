def arithmetic_arranger(problems, show_answers=False):
    if (len(problems) > 5):
        return 'Error: Too many problems.' 

    row1 = ''
    row2 = ''
    row3 = ''
    row4 = ''

    for problem in problems:
        operand1 = sort_operands(problem)[0]
        operator = sort_operands(problem)[1]
        operand2 = sort_operands(problem)[2]

        if(len(str(operand1)) > 4 or len(str(operand2)) > 4):
            return 'Error: Numbers cannot be more than four digits.'

        try:
            if operator == '+':
                result = int(operand1) + int(operand2)
            else:
                result = int(operand1) - int(operand2)
        except:
            return 'Error: Numbers must only contain digits.'


        if(operator == '+' or operator == '-'):
            dashes = ''

            if len(str(operand1)) < len(str(operand2)):
                for i in range(len(str(operand2)) + 2):
                    dashes += '-'
            else:
                for i in range(len(str(operand1)) + 2):
                    dashes += '-'
            


            formatted_operand1 = str(operand1)
            formatted_operand2 = operator
            if len(str(operand1)) < len(str(operand2)):
                while len(formatted_operand2) < len(dashes) - max(len(str(operand1)), len(str(operand2))):
                    formatted_operand2 += ' '
            else:
                while len(formatted_operand2) < len(dashes) - min(len(str(operand1)), len(str(operand2))):
                    formatted_operand2 += ' '
            
            formatted_operand2 += operand2
            formatted_result = str(result)      

            for _ in dashes:
                if len(formatted_operand1) < len(dashes):
                    formatted_operand1 = ' ' + formatted_operand1
                if len(formatted_operand2) < len(dashes):
                    formatted_operand2 = ' ' + formatted_operand2
                if len(formatted_result) < len(dashes):
                    formatted_result = ' ' + formatted_result

            row1 += formatted_operand1
            row2 += formatted_operand2
            row3 += dashes
            row4 += formatted_result

            if (problem != problems[-1]):
                row1 += '    '
                row2 += '    '
                row3 += '    '
                row4 += '    '
        else:
            return "Error: Operator must be '+' or '-'."


    formated_problems = f'{row1}\n{row2}\n{row3}'
    formated_problems_with_answers = f'{row1}\n{row2}\n{row3}\n{row4}'

    if show_answers == True:
        return formated_problems_with_answers
    else:
        return formated_problems


def sort_operands(problem):
    elements = problem.split(' ')
    
    operand1 = elements[0]
    operand = elements[1]
    operand2 = elements[2]
    
    new_elements = [operand1, operand, operand2]
    return new_elements

print(f'\n{arithmetic_arranger(["32 - 698", "1 - 3801", "45 + 43", "123 + 49", "988 + 40"], True)}')