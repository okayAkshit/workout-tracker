import json
from datetime import date,datetime
import random

ex=[]
def show_daily_quote():
    quotes = [
        "Push yourself, because no one else is going to do it for you.",
        "Don’t limit your challenges, challenge your limits.",
        "The body achieves what the mind believes.",
        "Sweat is fat crying.",
        "Go hard or go home!",
        "Every rep counts, every set builds, every workout matters."
    ]
    today = date.today()
    index = today.toordinal() % len(quotes)
    print("\n🏋️ DAILY MOTIVATION 🏋️")
    print(f"\"{quotes[index]}\"\n")

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
    print("\n1: Add excercise \n2: View all excercise\n3: If done escercise\n4: History\n5. Todat excercise\n6. Delete excercise\n7.exit")
def add_ex():
    name=input("enter the excercise name you wanna do")
    try:
        weight=int(input("my budy tell me weight you gonna bash"))
        sets=int(input("enter the sets of excercise you wanna perform"))
        reps =int(input("enter the reps you wanna do each sets"))
    except ValueError:
        print("⚠️ Please enter numbers only for weight, sets, and reps.")
        return
    today_date= date.today().strftime("%Y-%m-%d")
    ex.append({'name':name,'weight':weight,'sets':sets,"reps":reps,'done':False,"date":today_date})
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
def history():
    completed=[e for e in ex if e.get("done")]
    if not completed:
        print("No excer cise done until now")
    else:
        for i,exercise in enumerate(completed):
            print(f"{i+1}. {exercise['name']} - {exercise['weight']} kg, {exercise['sets']}x{exercise['reps']}")
def view_today():
    today_date = datetime.now().strftime("%Y-%m-%d")
    today_excercises=[e for e in ex if e.get("date")== today_date]
    if not today_excercises:
        print("\nNo exercises added today. Let's get to work! 💪 ")
    else:
        print(f"\n📅 TODAY'S WORKOUT ({today_date}):")

        for i ,excercise in enumerate(today_excercises):
            status="✓" if excercise.get("done",False) else "✗"
            print(f"{i+1}. {status} {excercise['name']}- {excercise['weight']} kg, {excercise['sets']}x{excercise['reps']}")
def del_exc():
    not_done=[i for i in ex if i.get("done",False)]
    if not not_done:
        print("you have allredy done every excercise so you dont need to delete any excercie")
    else:
        print(("\n❌ Exercises you can delete:"))
        for i ,exercise in enumerate(not_done,start=1):
            print(f"{i}. {exercise['name']}-{exercise['weight']} kg, {exercise['sets']}x{exercise['reps']}")
        try:
            choice=int(input("enter the number of the exercise you want to delete:"))
            if 1<=choice>len(not_done):
                to_delete=not_done[choice-1]
                ex.remove()(to_delete)
                save_data()
                print(f"🗑️ Deleted: {to_delete['name']}")
            else:
                print("invalid choice")
        except ValueError:
            print("enter intefger value")

load_data()
show_daily_quote()
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
            history()
        elif choice==5:
            view_today()
        elif choice==6:
            del_exc()
        elif choice==7:
             print("Be a monster my darling")
             today_date = datetime.now().strftime("%Y-%m-%d")
             today_ex = [e for e in ex if e.get("date") == today_date]
             completed = sum(1 for e in today_ex if e.get("done"))
             total = len(today_ex)
             print(f"🏋️ Summary: {completed}/{total} exercises completed today!")
             break
    except  ValueError:
        print("please enter a valid no (1-4)")

