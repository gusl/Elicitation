import tkinter as tk
from tkinter import scrolledtext
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Initialize the list of probabilities
probabilities = []

# Create the main window
root = tk.Tk()
root.title("Probability Visualizer")

# Create a scrolled text widget for displaying messages
text_area = scrolledtext.ScrolledText(root, height=10, state='disabled')
text_area.pack(padx=10, pady=10)

# Function to update the graphical display and text area
def update_display(message):
    text_area.config(state='normal')
    text_area.insert(tk.END, message + "\n")
    text_area.see(tk.END)  # Scroll to the bottom
    text_area.config(state='disabled')

# Function to update the graph
def update_graph(probability):
    probabilities.append(probability)
    aggregate = sum(probabilities) / len(probabilities)
    ax.clear()
    ax.bar(['Aggregate Probability'], [aggregate], color='blue')
    ax.set_ylim(0, 1)
    canvas.draw()
    update_display(f"Aggregate probability: {aggregate:.4f} (or {aggregate*100:.2f}%)")

# Function to handle the input
def handle_input(event):
    user_input = input_entry.get().strip().lower()
    input_entry.delete(0, tk.END)  # Clear the input field
    
    update_display(f"> {user_input}")  # Display user input
    
    if user_input == 'quit':
        root.quit()  # Close the application
        return
    
    try:
        # Handle percentage inputs
        if user_input.endswith('%'):
            probability = float(user_input[:-1]) / 100
        else:
            probability = float(user_input)
        
        if 0 <= probability <= 1:
            update_graph(probability)
        else:
            update_display("Error: Probability must be between 0 and 1, or 0% to 100%.")
    except ValueError:
        update_display("Error: Invalid input. Please enter a valid number.")

# Create an entry widget for user input
input_entry = tk.Entry(root)
input_entry.pack(padx=10, pady=5)
input_entry.bind("<Return>", handle_input)
input_entry.focus()

# Create a Matplotlib figure and a bar graph
fig = Figure(figsize=(5, 4), dpi=100)
ax = fig.add_subplot(111)

# Embed the figure in the Tkinter window
canvas = FigureCanvasTkAgg(fig, master=root)  # A tk.DrawingArea.
canvas.draw()
canvas.get_tk_widget().pack(fill=tk.BOTH, expand=1)

root.mainloop()
