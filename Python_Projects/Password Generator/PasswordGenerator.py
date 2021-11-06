import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
letter_counter = 0
number_counter = 0
symbol_counter = 0

passw = ''
while True:
    randPassGen = random.randint(1,3)
    if randPassGen == 1:
        if letter_counter == nr_letters:
            passw+=''
        else:
            #passw+=letters[random.randint(0,26)]
            passw+=random.choice(letters)
            letter_counter+=1
    elif randPassGen == 2:
        if number_counter == nr_numbers:
           passw+=''
        else:
           #passw+=numbers[random.randint(0,9)]
           passw+=random.choice(numbers)
           number_counter+=1
    elif randPassGen == 3:
        if symbol_counter == nr_symbols:
            passw+=''
        else:
            #passw+=symbols[random.randint(0,8)]
            passw+=random.choice(symbols)
            symbol_counter+=1
    if letter_counter == nr_letters and number_counter == nr_numbers and symbol_counter == nr_symbols:
        break;

print("Password : "+passw)
