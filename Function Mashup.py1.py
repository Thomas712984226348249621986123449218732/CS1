
def chorus():
    print("music")
    print("What do you mean, when you wanna say yes, but you always say no")
    print("What do you mean?")
def sing_song():
    print("music")
    print("lyrics")
    chorus()
    print("lyrics")
    print("music")
    chorus()
    print("music")
    print("lyrics")
    chorus()
def add(num1, num2):
    print(num1 + num2)
def print_elements(my_list):
    for element in my_list:
        print(element)    
def element_in_list(my_list, element):
    return element in my_list    
def is_integer(parameter1):
    x = parameter1
    print(type(x))
    

def main():
    sing_song() 
    print("")
    foods = ["fries", "burgers", "chicken", "ice cream", "salad"]
    print_element(foods)
    print(element_in_list(["red","blue","green","orange","yellow"], "red"))

