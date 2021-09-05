
def sum_digits(number):
    sumdigits = 0
    while number // 10 > 0:
        modulus = number % 10
        sumdigits  = sumdigits + modulus
        number = number // 10
    sumdigits = sumdigits + number
    return sumdigits


input_number = int(input('Enter Number: '))
sum_all_Digits = sum_digits(input_number)

print('Sum Digits ', sum_all_Digits)





