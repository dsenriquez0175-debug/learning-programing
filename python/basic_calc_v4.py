import os

# Main menu function
def main_menu():

   print("#### MAIN MENU ####")
   print("1. addition")
   print("2. substraction")
   print("3. multiplication")
   print("4. division")
   print("5. average")
   print("6. all options")

os.system('clear')
# Inputs
n1= float(input("Enter first number: "))
n2= float(input("Enter second number: "))

main_menu()
opt = int(input("Enter any option: "))

if(opt ==1):
    add = n1 + n2
   print(f"addition is: {add}") # print("addition is: ", add)
else:
    if(opt ==2):
    subs = n1 - n2
   print(f"substraction is: {subs}") # print("substraction is: ", subs)
   else:
    if(opt ==3):
        mult = n1 * n2
   print(f"multiplication is: {mult}") # print("multiplication is: ", mult)
   else:
    if (opt == 4):
        div = n1 / n2
        print(f"division is: {div}") # print("division is: ", div)
        else:
            if(opt ==5)
            avg = (n1 + n2) / 2
            print(f"average is: {avg}") # print("average is: ", avg)
            else:
                if(opt ==6)
                   add = n1 + n2
                   subs = n1 - n2
                   mult = n1 * n2
                   div = n1 / n2
                   avg = (n1 + n2) / 2
                   
                   print(f"addition is: {add}") 
                   print(f"substraction is: {subs}")
                   print(f"multiplication is: {mult}")
                   print(f"division is: {div}")
                   print(f"average is: {avg}")
                   else: 
                    print(":::invalid option:::")

