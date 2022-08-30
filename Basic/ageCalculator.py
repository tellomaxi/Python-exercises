import datetime

def ageCalculator(y, m, d):
    today = datetime.datetime.now().date()
    dob = datetime.date(y, m, d)
    age = int((today-dob).days / 365.25)
    print("Your age is: ",age)

#y=year m=month d=day
y=int(input("Enter your Birth Year: "))
m=int(input("Enter your Birthday month(1-12): "))
d=int(input("Enter your Birth Day(1-31): "))
ageCalculator(y, m, d)