import tkinter as tk
import random

root = tk.Tk()
root.title("WORD GUESSING GAME")
root.geometry("1920x1080")
root.config(bg="black")

i = 0

def selection(item, d, name):
    global i
    i = 0
    button2.delete('1.0', tk.END)
    entry2.delete('1.0', tk.END)
    entry1.config(text=f"GUESS THE {name} NAME")
    entry.delete(0, tk.END)
    selected_word = random.choice(item)

    hint = selected_word[0] + "_" * (len(selected_word) - 2) + selected_word[-1]
    entry2.insert(tk.END, f"HINT: {hint}    LENGTH: {len(selected_word)} LETTERS")

    def check():
        global i
        user_input = entry.get().upper()
        if user_input == selected_word:
            button2.delete('1.0', tk.END)
            button2.insert(tk.END, f"CORRECT! IT'S {selected_word} 😊")
            button2.config(bg="green", fg="white")
            add_replay_button()
        else:
            i += 1
            if i < d:
                button2.delete('1.0', tk.END)
                button2.insert(tk.END, f"WRONG GUESS! ATTEMPT {i} OF {d}")
                button2.config(bg="red", fg="white")
            else:
                button2.delete('1.0', tk.END)
                button2.insert(tk.END, f"YOU LOST! THE WORD WAS: {selected_word}")
                button2.config(bg="red", fg="white")
                add_replay_button()

    b3 = tk.Button(root, text="CHECK", font=("Arial", 24), bg="blue", fg="white", command=check)
    b3.place(x=1000, y=320)

def birds():
    bird_names = ["SPARROW", "PEACOCK", "EAGLE", "CROW", "PIGEON", "PARROT", "SWAN", "WOODPECKER", "FLAMINGO", "KINGFISHER"]
    selection(bird_names, 3, "BIRD")

def animal():
    animal_names = ["LION", "TIGER", "ELEPHANT", "ZEBRA", "MONKEY", "DEER", "COW", "BUFFALO", "PANDA", "LEOPARD"]
    selection(animal_names, 3, "ANIMAL")

def flower():
    flower_names = ["ROSE", "LILY", "LOTUS", "TULIP", "DAISY", "SUNFLOWER", "JASMINE", "HIBISCUS", "MARIGOLD", "IRIS"]
    selection(flower_names, 3, "FLOWER")

def organs_name():
    organ_names = ["BRAIN", "HEART", "LIVER", "LUNGS", "KIDNEY", "STOMACH", "PANCREAS", "INTESTINE", "SPLEEN", "BLADDER"]
    selection(organ_names, 3, "BODY ORGAN")

def city():
    city_names = [
        "MUMBAI", "DELHI", "KOLKATA", "BENGALURU", "CHENNAI", "HYDERABAD", "PUNE",
        "AHMEDABAD", "KOCHI", "LUCKNOW", "JAIPUR", "SURAT", "PATNA", "INDORE",
        "CHANDIGARH", "BHOPAL", "RANCHI", "DEHRADUN", "NAGPUR", "AGRA", "VARANASI"
    ]
    selection(city_names, 3, "CITY")

def add_replay_button():
    replay_btn = tk.Button(root, text="PLAY AGAIN", font=("Arial", 20), bg="white", fg="black", command=yee)
    replay_btn.place(x=1000, y=550)

def yee():
    button2.delete('1.0', tk.END)
    entry2.delete('1.0', tk.END)
    entry1.config(text="CHOOSE A CATEGORY")
    entry.delete(0, tk.END)

bird_btn = tk.Button(root, text="GUESS BIRD NAME", font=("Arial", 28), bg="green", fg="white", command=birds)
bird_btn.place(x=100, y=150)

animal_btn = tk.Button(root, text="GUESS ANIMAL NAME", font=("Arial", 28), bg="orange", fg="white", command=animal)
animal_btn.place(x=100, y=250)

flower_btn = tk.Button(root, text="GUESS FLOWER NAME", font=("Arial", 28), bg="pink", fg="black", command=flower)
flower_btn.place(x=100, y=350)

organ_btn = tk.Button(root, text="GUESS BODY ORGAN", font=("Arial", 28), bg="purple", fg="white", command=organs_name)
organ_btn.place(x=100, y=450)

city_btn = tk.Button(root, text="GUESS CITY NAME", font=("Arial", 28), bg="blue", fg="white", command=city)
city_btn.place(x=100, y=550)

# Entry for user input
entry = tk.Entry(root, font=("Arial", 24), width=20, bg="black", fg="white", justify="center")
entry.place(x=1000, y=250)

# Label for game prompt
entry1 = tk.Label(root, text="CHOOSE A CATEGORY", font=("Arial", 28), fg="yellow", bg="black", width=50, anchor="w")
entry1.place(x=500, y=180)

# Hint and length display
entry2 = tk.Text(root, height=2, width=60, font=("Arial", 20), bg="black", fg="white")
entry2.place(x=500, y=400)

# Feedback area (correct/wrong)
button2 = tk.Text(root, height=2, width=60, font=("Arial", 20), bg="black", fg="white")
button2.place(x=500, y=470)

yee()
root.mainloop()
