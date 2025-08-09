import tkinter as tk
from Weather import get_five_cities, search_city

root = tk.Tk()
root.title("Weather Task 2")
root.configure(bg="#F5DEB3")

search_frame = tk.Frame(root, bg="#F5DEB3")
search_frame.pack(side="top", pady=20)

search_entry = tk.Entry(search_frame, width=30, font=("Arial", 12))
search_entry.pack(side="left", padx=5)

search_button = tk.Button(search_frame, text="🔎 Search", font=("Arial", 10), command=lambda: on_search())
search_button.pack(side="left")

card_frame = tk.Frame(root, bg="#F5DEB3")
card_frame.pack(expand=True)

def on_search():
    city_data = search_city(search_entry.get())
    if city_data:
        top = tk.Toplevel(root, bg="#F5DEB3")
        top.title(f"Weather in {city_data['name']}")

        card = tk.Frame(top, bd=2, relief="solid", padx=10, pady=10, bg="#f0f0f0")
        card.pack(expand=True)

        tk.Label(card, text=city_data['name'], font=("Arial", 14, "bold"), bg="#f0f0f0").pack(anchor="w")
        tk.Label(card, text=city_data['desc'].capitalize(), bg="#f0f0f0").pack(anchor="w")
        tk.Label(card, text=f"Temperature: {city_data['temp']}°C", bg="#f0f0f0").pack(anchor="w")
        tk.Label(card, text=f"Humidity: {city_data['humidity']}%", bg="#f0f0f0").pack(anchor="w")

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

        tk.Label(card, text=f"{name}", font=("Arial", 14, "bold"), bg="#f0f0f0").pack(anchor="w")
        tk.Label(card, text=f"The weather is: {desc}", bg="#f0f0f0").pack(anchor="w")
        tk.Label(card, text=f"Temperature: {temp}°C", bg="#f0f0f0").pack(anchor="w")
        tk.Label(card, text=f"Humidity: {humidity}%", bg="#f0f0f0").pack(anchor="w")

show_random_cities()
root.mainloop()
