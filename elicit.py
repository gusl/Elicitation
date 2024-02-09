import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Initialize the list of probabilities
probabilities = []

# Create the main window
root = tk.Tk()
root.title("Probability Visualizer")

# Create a frame for the terminal-like input on the left
frame = tk.Frame(root)
frame.pack(side=tk.LEFT, fill=tk.Y)

# Input label and entry
input_label = tk.Label(frame, text="Enter Probability:")
input_label.pack(pady=5)
input_entry = tk.Entry(frame)
input_entry.pack(pady=5)

# Function to update the graph
def update_graph(probability):
    probabilities.append(probability)
    aggregate = sum(probabilities) / len(probabilities)
    ax.clear()
    ax.bar(['Aggregate Probability'], [aggregate], color='blue')
    ax.set_ylim(0, 1)
    canvas.draw()

# Function to handle the input
def handle_input(event):
    user_input = input_entry.get().strip().lower()
    input_entry.delete(0, tk.END)  # Clear the input field
    
    try:
        # Handle percentage inputs
        if user_input.endswith('%'):
            probability = float(user_input[:-1]) / 100
        else:
            probability = float(user_input)
        
        if 0 <= probability <= 1:
            update_graph(probability)
        else:
            print("Error: Probability must be between 0 and 1, or 0% to 100%.")
    except ValueError:
        print("Error: Invalid input. Please enter a valid number.")

input_entry.bind("<Return>", lambda event: handle_input(event))

# Create a Matplotlib figure and a bar graph
fig = Figure(figsize=(5, 4), dpi=100)
ax = fig.add_subplot(111)

# Embed the figure in the Tkinter window
canvas = FigureCanvasTkAgg(fig, master=root)  # A tk.DrawingArea.
canvas.draw()
canvas.get_tk_widget().pack(side=tk.RIGHT, fill=tk.BOTH, expand=1)

root.mainloop()
