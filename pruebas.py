import tkinter as tk
from tkinter import messagebox
from tkinter import font

# Function to add participant
def add_participant():
    name = entry_name.get()
    contribution = entry_contribution.get()
    
    if name and contribution:
        try:
            contribution = float(contribution)
            participants.append({'name': name, 'contribution': contribution})
            listbox_participants.insert(tk.END, f"{name}: ${contribution:.2f}")
            entry_name.delete(0, tk.END)
            entry_contribution.delete(0, tk.END)
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid number for the contribution.")
    else:
        messagebox.showerror("Input Error", "Please fill in both name and contribution fields.")

# Function to remove selected participant
def remove_participant():
    try:
        selected_index = listbox_participants.curselection()[0]
        listbox_participants.delete(selected_index)
        del participants[selected_index]
    except IndexError:
        messagebox.showerror("Selection Error", "Please select a participant to remove.")

# Function to calculate debts
def calculate_debts():
    total = sum(p['contribution'] for p in participants)
    num_participants = len(participants)
    
    if num_participants == 0:
        messagebox.showerror("No Participants", "Add at least one participant to calculate debts.")
        return

    average = total / num_participants
    result_text = f"Total collected: ${total:.2f}\nAverage contribution: ${average:.2f}\n\n"
    
    debtors = []
    creditors = []

    for p in participants:
        debt = p['contribution'] - average
        if debt < 0:
            debtors.append({'name': p['name'], 'debt': -debt})
        elif debt > 0:
            creditors.append({'name': p['name'], 'credit': debt})
    
    # Determine who should pay whom
    i, j = 0, 0
    while i < len(debtors) and j < len(creditors):
        if debtors[i]['debt'] <= creditors[j]['credit']:
            result_text += f"{debtors[i]['name']} owes {creditors[j]['name']} ${debtors[i]['debt']:.2f}\n"
            creditors[j]['credit'] -= debtors[i]['debt']
            i += 1
        else:
            result_text += f"{debtors[i]['name']} owes {creditors[j]['name']} ${creditors[j]['credit']:.2f}\n"
            debtors[i]['debt'] -= creditors[j]['credit']
            j += 1

    text_result.delete(1.0, tk.END)
    text_result.insert(tk.END, result_text)

# Function to clear all fields
def clear_fields():
    entry_name.delete(0, tk.END)
    entry_contribution.delete(0, tk.END)
    listbox_participants.delete(0, tk.END)
    text_result.delete(1.0, tk.END)
    participants.clear()

# Create main window
root = tk.Tk()
root.title("Debt Calculator")
root.config(bg="#f5f5f5")  # Soft light gray background

# List to store participants and their contributions
participants = []

# Load custom font (Fredoka Medium)
try:
    fredoka_font = font.Font(family="Fredoka Medium", size=10)
except:
    messagebox.showwarning("Font Warning", "Fredoka Medium font not found, using default font.")
    fredoka_font = None

# Labels and entry fields for participants
label_name = tk.Label(root, text="Participant Name:", bg="#f5f5f5", fg="#2f4f4f", font=fredoka_font or ("Arial", 10, "bold"))
label_name.grid(row=0, column=0, padx=10, pady=10, sticky="ew")
entry_name = tk.Entry(root, bg="#d1e7dd", fg="black", font=fredoka_font or ("Arial", 10))
entry_name.grid(row=0, column=1, padx=10, pady=10, sticky="ew")

label_contribution = tk.Label(root, text="Contribution ($):", bg="#f5f5f5", fg="#2f4f4f", font=fredoka_font or ("Arial", 10, "bold"))
label_contribution.grid(row=1, column=0, padx=10, pady=10, sticky="ew")
entry_contribution = tk.Entry(root, bg="#d1e7dd", fg="black", font=fredoka_font or ("Arial", 10))
entry_contribution.grid(row=1, column=1, padx=10, pady=10, sticky="ew")

# Listbox to display participants
listbox_participants = tk.Listbox(root, width=40, height=10, bg="#d1e7dd", fg="black", font=fredoka_font or ("Arial", 10))
listbox_participants.grid(row=2, column=0, columnspan=2, padx=10, pady=10, sticky="ew")

# Buttons for actions
button_add = tk.Button(root, text="Add Participant", command=add_participant, bg="#008080", fg="white", font=fredoka_font or ("Arial", 10, "bold"))
button_add.grid(row=3, column=0, padx=10, pady=10, sticky="ew")

button_remove = tk.Button(root, text="Remove Participant", command=remove_participant, bg="#f08080", fg="white", font=fredoka_font or ("Arial", 10, "bold"))
button_remove.grid(row=3, column=1, padx=10, pady=10, sticky="ew")

button_calculate = tk.Button(root, text="Calculate Debts", command=calculate_debts, bg="#008080", fg="white", font=fredoka_font or ("Arial", 10, "bold"))
button_calculate.grid(row=4, column=0, padx=10, pady=10, sticky="ew")

button_clear = tk.Button(root, text="Clear", command=clear_fields, bg="#008080", fg="white", font=fredoka_font or ("Arial", 10, "bold"))
button_clear.grid(row=4, column=1, padx=10, pady=10, sticky="ew")

# Text widget to display results
text_result = tk.Text(root, height=10, width=40, bg="#d1e7dd", fg="black", font=fredoka_font or ("Arial", 10))
text_result.grid(row=5, column=0, columnspan=2, padx=10, pady=10, sticky="ew")

# Make the window responsive
for i in range(2):
    root.grid_columnconfigure(i, weight=1)
for i in range(6):
    root.grid_rowconfigure(i, weight=1)

# Run the main loop
root.mainloop()
