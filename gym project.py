import json

ex=[]
def load_data():
    global ex
    try:
        with open('workout_data.json','r')as f:
            ex=json.load(f)
    except FileNotFoundError:
        ex = []
    
def save_data():
         with open('workout_data.json', 'w') as f:
            json.dump(ex, f)

def menu():
    print(f"Yeh buddy light weight baby")
    print("\n1: Add excercise \n2: View all excercise\n3: If done escercise\n4: Exit")
def add_ex():
    a=input("Enter excercise you will boom  ")
    ex.append({"Excercise":a,"done":False})
    print(f"{a} is added to check list of exc")
    save_data()
def view():
    if not ex:
        print("No excercise added")
    else:
        for i,Excercise in enumerate(ex):
            status="✓" if Excercise["done"] else "✗"
            print(f"{i+1} {status} {Excercise['Excercise']}")
def mark():
    view()
    if not ex:
        return
    try:
        choice=int(input("enter the excercise number you wanna mark as done  "))
        if 1<= choice <=len(ex):
            ex[choice-1]['done']=True
            save_data()
        else:
            print("enter valid no")
    except:
        print("enter a valid no.")
load_data()

while True:
    menu()
    try:
        choice=int(input("enter the number  "))
        if choice==1:
            add_ex()
        elif choice==2:
            view()
        elif choice==3:
            mark()
        elif choice==4:
            print("Be a monster my darling")
            break
    except  ValueError:
        print("please enter a valid no (1-4)")

