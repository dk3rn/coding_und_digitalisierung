import tkinter as tk

def on_button_click():
  user_input = entry.get()
  label.config(text=f"Eingabe: {user_input}")


# Hauptfenster erstellen
root = tk.Tk()
root.title("Mini Tkinter App")
root.geometry("300x200")

# Eingabefeld (Entry)
entry = tk.Entry(root, width=25, font=("Arial", 12))
entry.pack(pady=20)

# Button
button = tk.Button(
    root, text="Absenden", command=on_button_click, font=("Arial", 10)
)
button.pack(pady=10)

# Label zur Anzeige des Ergebnisses
label = tk.Label(root, text="", font=("Arial", 11))
label.pack(pady=10)

# Hauptschleife starten
root.mainloop()