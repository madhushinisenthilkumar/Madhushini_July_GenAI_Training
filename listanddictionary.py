students=[
    {"Name":"Anu","Age":19,"Department":"BCA"},
    {"Name":"Madhu","Age":20,"Department":"B.Sc CS"},
    {"Name":"Kavin","Age":20,"Department":"BCA"}
]
print("Student Details:\n")
for student in students:
    print("Name:",student["Name"])
    print("Age:",student["Age"])
    print("Department:",student["Department"])
    print("------------------")