# source_type=input("enter your source").lower()
# if source_type=='csv':
#     print("this is the code to read csv")
# elif source_type=='json':
#     print("this is the code to read json")

# number=int(input("enter any number"))
# if number>0:
#     print("positive number")
# elif number==0:
#     print("number is zero")
# else:
#     print("negative number")

# age=int(input("enter your age"))
# if age>18:
#     print("you are eligible for vote")
# else:
#     print(f"not eligible.you will be eligible in {18-age} years")

# marks=int(input("enter marks"))
# if marks>=70:
#     print("Grade A")
# elif marks>60 and marks <70:
#     print("Grade B")
# elif marks>50 and marks<60:
#     print("Grade C")
# elif marks>40 and marks<50:
#     print("Grade D")
# else:
#     print("Grade D")

a=int(input("enter a"))
b=int(input("enter b"))
c=int(input("enter c"))
if a>b and a>c:
    print("a is greatest")
elif b>c:
    print("b is greater")
else:
    print("c is greater")