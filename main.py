Reset = '\033[0m'
Red = '\033[31m'

Age = int(input("Please enter your age: "))

Final_Age = Age * 365.3

Final_Age = round(Final_Age, 0)
print(f"You have lived for {Red} {Final_Age} {Reset} number of days in total.")