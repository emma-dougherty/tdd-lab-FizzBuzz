# def return_string(number):
#     return str(number)

def fizzbuzz(input_number):
    # for number in range(0, 50):
    if input_number % 3 == 0 and input_number % 5 == 0:
        return "FizzBuzz"
    
    if input_number % 3 == 0:
        return "Fizz"
    elif input_number % 5 == 0:
        return "Buzz"
    else:
        return str(input_number)