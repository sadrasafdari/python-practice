members_datas=[]
for i in range(3):
    while True:
        name=input("enter employee name: ").strip()
        if name!="":
            break
        print("the name is empty, please fill it in")
    while True:
        try:
            age=int(input("enter employee age: "))
            break
        except ValueError:
            print("age must be numeric")        
    while True:
        try:
            salary=int(input("enter employee salary: "))
            break
        except ValueError:
            print("salary must be numeric")
    employee={
            "name":name,
            "age":age,
            "salary":salary
}
    members_datas.append(employee)
   
with open("datas.txt","w") as file:
    for employee in members_datas:
        file.write(f"{employee['name']},{employee['age']},{employee['salary']}\n")
most_salary=members_datas[0]
for employee in members_datas:
    if employee['salary']>most_salary['salary']:
        most_salary=employee
print("highest salary: ",most_salary['name']," ",most_salary['salary'])
total_salary=0
for employee in members_datas:
    total_salary+=employee['salary']
average_salary=total_salary/len(members_datas)
print("average: ",average_salary)

