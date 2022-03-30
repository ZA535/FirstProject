from test_file import Box
from msilib.schema import File

import json

file_data = ''
with open("user_account_details.txt", 'r') as nf:
   print( nf.read())
lines = file_data.split('\n')
user_data = []
for line in lines:
    d = line.split(',')
    user_data.append({
        'Name': d[0],
        'Age': d[1],
        'Year': d[2]
    })
# json_data = json.dumps(user_data)
# with open('user_account_details.json', 'w') as nf:
#     nf.write(json_data)
# dict_js = None
# with open('user_account_details.txt.json', 'r') as nf:
#     jf = nf.read()
#     dict_js = json.loads(jf)
#
# print(dict_js[0])
# Box.__init__(5,9)
# print(Box(8,3))
#
# print(Box(8,9))
# print(Box.fun())
# def recursive(q):
#     if (q > 0):
#         result = q + recursive(q - 1)
#         print("Result", result)
#     else:
#         result = 0
#         return result

# recursive(9)
# array = ["Zain", "Umair", "Hussnain", "Mustafa", "Murtaza", "Danish"];
#
#
# def myfun(**kid):
#     # return= a+b;
#     return "Result", kid["a"] + kid["b"];
    # print("Addition of Two Number : ", c)


# print("My Name is Zain Ul abideen")

# print(myfun(b=9,a=1));
def test(food):
    for i in food:
        print(i)
# test(array)
# print(" ------------Cities----------------  \n Arifwala   Burewala   Vehari    Pakpattan")
# cityName = input("Enter City Name : ")
#
# if cityName == "Arifwala":
#     if 3>5:
#         print("You Are Form Arifwala")
#     else:
#         print("This is Big City")
# elif cityName == "Burewala":
#     print("You Are from Burewala.")
# elif cityName == "vehari":
#     print("You Are from vehari.")
# elif cityName == "Pakpattan":
#     print("You Are from Pakpattan.")
# else:
#     print("Sorry You Are not belong on Those Cities Which Mention in Above")

# array=["Zain","Umair","Hussnain","Mustafa","Murtaza","Danish"];
#
# for i in array:
#     print("Hi",i," Welcome",type())
#     # for i in array:
#     print("__________________")

# for i in range(10,20,3):
#     print(i)

from test_file import Box
print(Box(4,9))

#few changing