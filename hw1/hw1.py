# PYTHON ADVANCED COURSE. FALL
#         KONVISAROVA ANASTASIIA.
#         HOMEWORK1

import sys

def main():
    menu()


def menu():
    print("Konvisarova Anastasiia. Homework1. Main menu:")
    choice = input("""Choose the task:
                    1. Check URL for Catalog
                    2. Get center character
                    3. Count_symbols
                    4. Mixing strings 
                    5: Even list generator
                    Q: exit
                    
                    Please make your choice\n""")
    if choice == "1":
        url_list = ["/home/Desktop", "/catalog/usr",
                    "/home/python", "/Desktop/anastasiia/catalog/"]
        print("The initial list is: ", url_list)
        print("\nFiltering is with /catalog/ condition:\n")
        print(catalog_finder(url_list))
        check_confition()
    elif choice == "2":
        input_str1 = "agressive unicorn"
        input_str2 = "cognetive pandas"
        print("Middle letters are:", get_str_center(input_str1))
        print("Middle letters are:", get_str_center(input_str2))
        check_confition()
    elif choice == "3":
        input_str1 = "agressive unicorn"
        input_str2 = "cognetive pandas"
        print(count_symbols(input_str1))
        print(count_symbols(input_str2))
        check_confition()
    elif choice == "4":
        str1 = "agressive    unicorn"
        str2 = "cognitive"
        print("String 1 is", str1, "\nString 2 is", str2)
        print("New string is:", mix_strings(str1, str2))
        check_confition()
    elif choice == "5":
        print(even_int_generator())
        check_confition()
    elif choice == "Q" or choice == "q":
        sys.exit
    else:
        print("You should check the valid option: ")
        menu()

#first task
def catalog_finder(url_list):
    result_list = [url for url in url_list if "/catalog/" in url]
    return result_list

#second task
def get_str_center(input_str):
    print("String is:", input_str, "\nThe length is: ", len(input_str))
    if len(input_str) % 2 == 0:
        print("even")
        output_str = input_str[int(len(input_str)/2 - 1)] + \
            input_str[int(len(input_str)/2)]
    else:
        print("odd")
        output_str = input_str[int(len(input_str)/2 - 2)] + \
            input_str[int(len(input_str)/2) - 1] + \
            input_str[int(len(input_str)/2)]
    return output_str

#third task
def count_symbols(input_str):
    output_dict = {}
    print("The initial string is:", input_str)
    print("Amount of Characters ")
    for ch in input_str:
        output_dict[ch] = input_str.count(ch)
    return output_dict

#forth task
def mix_strings(str1, str2):
    result_str = str1[:int(len(str1)/2)] + str2 + \
                str1[int(len(str1)/2):]
    return result_str

#fifth task
def even_int_generator():
    even_int_list = list()
    for item in range(0, 100):
        if item % 2 == 0:
            even_int_list.append(item)
    return even_int_list

#menu fun
def check_confition():
    check = input("Do you want to go back to the menu? y/n\n")
    if check == "y" or check == "yes" or check == "Y" or check == "Yes":
        menu()
    elif check == "n" or check == "no" or check == "N" or check == "No":
        sys.exit
    else: 
        print("plese check the answer")
        sys.exit
main()
