import tkinter as tk
import customtkinter as ctk

class MileToKmConverter:
    def __init__(self):
        self.BACKGROUND = "#f0f0f3"  # Light gray
        self.ACCENT = "#8e8e93"      # Neutral gray
        self.TEXT_COLOR = "#1c1c1e"  # Dark gray
        
        self.setup_window()
        self.create_widgets()
        
    def setup_window(self):
        self.window = tk.Tk()
        self.window.title("Mile to Km Converter")
        self.window.minsize(width=300, height=150)
        self.window.configure(bg=self.BACKGROUND)
        self.window.attributes('-topmost', True)  # Keep window on top
        
        # Center the window
        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()
        window_width = 300
        window_height = 150
        center_x = int(screen_width / 2 - window_width / 2)
        center_y = int(screen_height / 2 - window_height / 2)
        self.window.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
        
        # Set light appearance mode
        ctk.set_appearance_mode("light")
        
    def create_widgets(self):
        # Entry for miles
        self.miles_input = ctk.CTkEntry(
            self.window, 
            width=100,
            fg_color="#ffffff",
            border_color=self.ACCENT,
            text_color=self.TEXT_COLOR
        )
        self.miles_input.grid(column=1, row=0, padx=10, pady=10)
        self.miles_input.insert(0, "0")
        
        # Miles label
        self.miles_label = ctk.CTkLabel(
            self.window, 
            text="Miles", 
            text_color=self.TEXT_COLOR
        )
        self.miles_label.grid(column=2, row=0, padx=10, pady=10)
        
        # "is equal to" label
        self.equal_label = ctk.CTkLabel(
            self.window, 
            text="is equal to", 
            text_color=self.TEXT_COLOR
        )
        self.equal_label.grid(column=0, row=1, padx=10, pady=10)
        
        # Km result label
        self.km_result_label = ctk.CTkLabel(
            self.window, 
            text="0", 
            text_color=self.TEXT_COLOR
        )
        self.km_result_label.grid(column=1, row=1, padx=10, pady=10)
        
        # Km label
        self.km_label = ctk.CTkLabel(
            self.window, 
            text="Km", 
            text_color=self.TEXT_COLOR
        )
        self.km_label.grid(column=2, row=1, padx=10, pady=10)
        
        # Calculate button
        self.calculate_button = ctk.CTkButton(
            self.window, 
            text="Calculate", 
            command=self.calculate,
            fg_color=self.ACCENT,
            text_color="#ffffff"
        )
        self.calculate_button.grid(column=1, row=2, padx=10, pady=10)
        
    def calculate(self):
        miles = float(self.miles_input.get())
        km = miles * 1.60934
        self.km_result_label.configure(text=f"{km:.2f}")
        
    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    app = MileToKmConverter()
    app.run()