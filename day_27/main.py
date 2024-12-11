import tkinter as tk

window = tk.Tk()
window.title("My first gui app")
window.minsize(width=800, height=600)

my_lable = tk.Label(window, text="Hello, World!", font=("Helvetica", 20))
my_lable.pack(side="top")

# Store original window size
original_width = 800
original_height = 600

def reset_size(event):
    # Center window on screen with original size
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    center_x = int(screen_width/2 - original_width/2)
    center_y = int(screen_height/2 - original_height/2)
    window.geometry(f'{original_width}x{original_height}+{center_x}+{center_y}')

# Bind double-click event to the window
window.bind('<Double-Button-1>', reset_size)

# Center window on screen
window_width = 800
window_height = 600
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
center_x = int(screen_width/2 - window_width/2)
center_y = int(screen_height/2 - window_height/2)
window.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

# Make window appear on top
window.lift()
window.attributes('-topmost', True)

#Button
def button_clicked():
    my_lable.config(text=input.get())
    #clear the input
    input.delete(0, tk.END)

button = tk.Button(window, text="Click me", command=button_clicked)
button.pack() #pack is used to add the button to the window

# Entry
input = tk.Entry(window, width=10)
input.pack()
print(input.get())#get the text from the input

#Text
text = tk.Text(window, height=5, width=30)
text.pack()


window.mainloop()
