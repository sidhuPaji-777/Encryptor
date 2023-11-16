print("Welcome to Enigma-lite")
print("I support Rainbow")

print('''\n 
-------------------------------------------------------------------
\n''')



ask = str(input("For encryption press 1, for decryption press 2:"))

if(ask=="1"):
    def number_to_color_name(number):
        color_mapping = {
            '0': 'Violet',
            '1': 'Indigo',
            '2': 'Blue',
            '3': 'Green',
            '4': 'Yellow',
            '5': 'Orange',
            '6': 'Red',
            '7': 'Redindigo',
            '8': 'Redblue',
            '9': 'Redgreen'
        }  

        color_names = [color_mapping[digit] for digit in str(number)]
        result = ', '.join(color_names)
        
        return result

    def main():
        try:
            user_input = input("Enter the number you want to encrypt: ")
            if all(0 <= int(digit) <= 9 for digit in user_input):
                color_name = number_to_color_name(user_input)
                print(f"The encrypted code is: {color_name}")
            else:
                print("Please enter a valid number consisting of digits between 0 and 9.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    if __name__ == "__main__":
        main()



# _-------------------------------------------------------------------------------
elif(ask=="2"):
    def color_name_to_value(color_name):
        color_mapping = {
            'Violet': 0,
            'Indigo': 1,
            'Blue': 2,
            'Green': 3,
            'Yellow': 4,
            'Orange': 5,
            'Red': 6,
            'Redindigo': 7,
            'Redblue': 8,
            'Redgreen': 9
        }
        return color_mapping.get(color_name, -1)

    def colors_to_numbers(colors):
        color_list = colors.split(', ')
        number_list = [color_name_to_value(color) for color in color_list]
        return number_list

    def main():
        color_input = input("Enter the code to decrypt it(seprated by commas): ")
        number_list = colors_to_numbers(color_input)

        print(f"The decrypted message {number_list}")

    if __name__ == "__main__":
        main()
