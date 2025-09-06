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
            json.dump(ex, f,indent=4)

def menu():
    print(f"Yeh buddy light weight baby")
    print("\n1: Add excercise \n2: View all excercise\n3: If done escercise\n4: Exit")
def add_ex():
    name=input("enter the excercise name you wanna do")
    try:
        weight=int(input("my budy tell me weight you gonna bash"))
        sets=int(input("enter the sets of excercise you wanna perform"))
        reps =int(input("enter the reps you wanna do each sets"))
    except ValueError:
        print("⚠️ Please enter numbers only for weight, sets, and reps.")
        return
    ex.append({'name':name,'weight':weight,'sets':sets,"reps":reps,'done':False})
    print(f"{name} is added!")
    save_data()
def view():
    if not ex:
        print("No excercise added")
    else:
        for i,exercise in enumerate(ex):
            status="✓" if exercise.get("done",False) else "✗"
            print(f"{i+1}. {status} {exercise['name']} - {exercise['weight']} kg, {exercise['sets']}x{exercise['reps']}")
def mark():
    view()
    if not ex:
        return
    try:
        choice=int(input("enter the excercise number you wanna mark as done  "))
        if 1<= choice <=len(ex):
            ex[choice-1]['done']=True
            print(f"✅ {ex[choice-1]['name']} marked as done!")
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
            completed = sum(1 for e in ex if e.get("done"))
            total = len(ex)
            print(f"🏋️ Summary: {completed}/{total} exercises completed today!")
            break
    except  ValueError:
        print("please enter a valid no (1-4)")

