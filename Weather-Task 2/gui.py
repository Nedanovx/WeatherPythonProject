import tkinter as tk
from Weather import get_five_cities

root = tk.Tk()
root.title("Weather Task 2")
root.configure(bg="#F5DEB3")
card_frame = tk.Frame(root,bg="#F5DEB3")
card_frame.pack(expand=True)

def show_random_cities():
    for widget in card_frame.winfo_children():
        widget.destroy()

    cities = get_five_cities()

    for name, data in cities.items():
        temp = data["temp"]
        desc = data["desc"].capitalize()
        humidity = data["humidity"]

        card = tk.Frame(card_frame, bd=2, relief="solid", padx=10, pady=10, bg="#f0f0f0")
        card.pack(side='left', padx=10, pady=10)

        tk.Label(card, text=f" {name}", font=("Arial", 14, "bold"), bg="#f0f0f0").pack(anchor="w")
        tk.Label(card, text=f"The weather is: {desc}", bg="#f0f0f0").pack(anchor="w")
        tk.Label(card, text=f"Temperature: {temp}°C", bg="#f0f0f0").pack(anchor="w")
        tk.Label(card, text=f"Humidity: {humidity}%", bg="#f0f0f0").pack(anchor="w")


show_random_cities()
root.mainloop()
