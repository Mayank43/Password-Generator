import tkinter as tk
from tkinter import ttk, messagebox
import random
import string
import pyperclip
import json
import os
from datetime import datetime

class PasswordGenerator:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator - by Mayank43")
        self.root.geometry("500x900")
        self.root.configure(bg='#2c3e50')
        
        # Initialize variables
        self.password_history = []
        self.password_var = tk.StringVar()
        self.length_var = tk.IntVar(value=12)
        self.status_var = tk.StringVar(value="Ready to generate passwords!")
        
        # Character type variables
        self.char_vars = {
            'uppercase': tk.BooleanVar(value=True),
            'lowercase': tk.BooleanVar(value=True),
            'numbers': tk.BooleanVar(value=True),
            'symbols': tk.BooleanVar(value=True),
            'exclude_similar': tk.BooleanVar(value=True),
            'exclude_ambiguous': tk.BooleanVar(value=True)
        }
        
        self.load_history()
        self.setup_ui()
    
    def setup_ui(self):
        """Create the user interface"""
        # Title section
        tk.Label(self.root, text="Password Generator", font=("Arial", 20, "bold"),
                bg='#2c3e50', fg='#ecf0f1').pack(pady=20)
        tk.Label(self.root, text="Created by Mayank43", font=("Arial", 10, "italic"),
                bg='#2c3e50', fg='#bdc3c7').pack(pady=5)
        
        # Password display section
        password_frame = tk.Frame(self.root, bg='#2c3e50')
        password_frame.pack(pady=20, padx=20, fill='x')
        
        self.password_entry = tk.Entry(password_frame, textvariable=self.password_var,
                                     font=("Courier", 14), bg='#34495e', fg='#ecf0f1',
                                     relief='flat', justify='center', readonlybackground='#34495e')
        self.password_entry.pack(fill='x', pady=5)
        self.password_entry.config(state='readonly')
        
        tk.Button(password_frame, text="Copy to Clipboard", command=self.copy_to_clipboard,
                 bg='#3498db', fg='white', font=("Arial", 12, "bold"),
                 relief='flat', cursor='hand2').pack(fill='x', pady=5)
        
        # Settings section
        settings_frame = tk.LabelFrame(self.root, text="Password Settings",
                                     font=("Arial", 12, "bold"), bg='#2c3e50', fg='#ecf0f1')
        settings_frame.pack(pady=20, padx=20, fill='x')
        
        # Length setting
        length_frame = tk.Frame(settings_frame, bg='#2c3e50')
        length_frame.pack(fill='x', padx=10, pady=5)
        tk.Label(length_frame, text="Password Length:", font=("Arial", 10),
                bg='#2c3e50', fg='#ecf0f1').pack(side='left')
        
        tk.Scale(length_frame, from_=4, to=50, orient='horizontal', variable=self.length_var,
                bg='#2c3e50', fg='#ecf0f1', highlightbackground='#2c3e50',
                command=lambda v: self.length_label.config(text=str(v))).pack(side='right', fill='x', expand=True)
        
        self.length_label = tk.Label(length_frame, text="12", font=("Arial", 10, "bold"),
                                   bg='#2c3e50', fg='#3498db')
        self.length_label.pack(side='right', padx=10)
        
        # Character options
        options_frame = tk.Frame(settings_frame, bg='#2c3e50')
        options_frame.pack(fill='x', padx=10, pady=10)
        
        # Checkbox configurations
        checkbox_configs = [
            ("Include Uppercase Letters (A-Z)", 'uppercase'),
            ("Include Lowercase Letters (a-z)", 'lowercase'),
            ("Include Numbers (0-9)", 'numbers'),
            ("Include Symbols (!@#$%^&*)", 'symbols'),
            ("Exclude Similar Characters (l, 1, I, O, 0)", 'exclude_similar'),
            ("Exclude Ambiguous Characters ({}, [], |, etc.)", 'exclude_ambiguous')
        ]
        
        for text, var_key in checkbox_configs:
            tk.Checkbutton(options_frame, text=text, variable=self.char_vars[var_key],
                          bg='#2c3e50', fg='#ecf0f1', selectcolor='#34495e',
                          font=("Arial", 10)).pack(anchor='w', pady=2)
        
        # Buttons section
        buttons_frame = tk.Frame(self.root, bg='#2c3e50')
        buttons_frame.pack(pady=20, padx=20, fill='x')
        
        button_configs = [
            ("Generate Password", self.generate_password, '#27ae60', 14, 2),
            ("View History", self.show_history, '#f39c12', 12, 1),
            ("Clear History", self.clear_history, '#e74c3c', 10, 1)
        ]
        
        for text, command, color, font_size, height in button_configs:
            tk.Button(buttons_frame, text=text, command=command, bg=color, fg='white',
                     font=("Arial", font_size, "bold"), relief='flat', cursor='hand2',
                     height=height).pack(fill='x', pady=5)
        
        # Status bar
        tk.Label(self.root, textvariable=self.status_var, font=("Arial", 9),
                bg='#34495e', fg='#bdc3c7', relief='sunken', anchor='w').pack(side='bottom', fill='x')
    
    def generate_password(self):
        """Generate a password based on user settings"""
        try:
            # Validate settings
            if not any([self.char_vars['uppercase'].get(), self.char_vars['lowercase'].get(),
                       self.char_vars['numbers'].get(), self.char_vars['symbols'].get()]):
                messagebox.showerror("Error", "Please select at least one character type!")
                return
            
            # Build character pool
            char_sets = {
                'uppercase': string.ascii_uppercase,
                'lowercase': string.ascii_lowercase,
                'numbers': string.digits,
                'symbols': "!@#$%^&*()_+-=[]{}|;:,.<>?"
            }
            
            chars = ''.join(char_sets[key] for key in ['uppercase', 'lowercase', 'numbers', 'symbols']
                           if self.char_vars[key].get())
            
            # Apply exclusions
            if self.char_vars['exclude_similar'].get():
                chars = chars.replace('l', '').replace('1', '').replace('I', '').replace('O', '').replace('0', '')
            if self.char_vars['exclude_ambiguous'].get():
                chars = chars.replace('{', '').replace('}', '').replace('[', '').replace(']', '').replace('|', '')
                chars = chars.replace('\\', '').replace('/', '').replace('"', '').replace("'", '')
            
            if not chars:
                messagebox.showerror("Error", "No characters available with current settings!")
                return
            
            # Generate password
            length = self.length_var.get()
            password = ''.join(random.choice(chars) for _ in range(length))
            
            self.password_var.set(password)
            self.add_to_history(password)
            self.status_var.set(f"Password generated successfully! Length: {length}")
            
        except Exception as e:
            messagebox.showerror("Error", f"Failed to generate password: {str(e)}")
            self.status_var.set("Error generating password")
    
    def copy_to_clipboard(self):
        """Copy the generated password to clipboard"""
        password = self.password_var.get()
        if password:
            try:
                pyperclip.copy(password)
                self.status_var.set("Password copied to clipboard!")
                messagebox.showinfo("Success", "Password copied to clipboard!")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to copy to clipboard: {str(e)}")
        else:
            messagebox.showwarning("Warning", "No password to copy!")
    
    def add_to_history(self, password):
        """Add password to history"""
        entry = {
            'password': password,
            'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            'length': len(password)
        }
        self.password_history.append(entry)
        if len(self.password_history) > 50:
            self.password_history = self.password_history[-50:]
        self.save_history()
    
    def show_history(self):
        """Show password history in a new window"""
        if not self.password_history:
            messagebox.showinfo("History", "No passwords in history!")
            return
        
        history_window = tk.Toplevel(self.root)
        history_window.title("Password History")
        history_window.geometry("500x600")
        history_window.configure(bg='#2c3e50')
        
        tk.Label(history_window, text="Password History", font=("Arial", 16, "bold"),
                bg='#2c3e50', fg='#ecf0f1').pack(pady=10)
        
        # Create treeview
        columns = ('Password', 'Length', 'Date')
        tree = ttk.Treeview(history_window, columns=columns, show='headings', height=15)
        
        for col in columns:
            tree.heading(col, text=col)
        
        tree.column('Password', width=200)
        tree.column('Length', width=80)
        tree.column('Date', width=120)
        
        # Add data
        for entry in reversed(self.password_history):
            tree.insert('', 'end', values=(entry['password'], entry['length'], entry['timestamp']))
        
        tree.pack(pady=10, padx=10, fill='both', expand=True)
        
        # Copy button
        def copy_selected():
            selection = tree.selection()
            if selection:
                password = tree.item(selection[0])['values'][0]
                pyperclip.copy(password)
                messagebox.showinfo("Success", "Password copied to clipboard!")
        
        tk.Button(history_window, text="Copy Selected", command=copy_selected,
                 bg='#3498db', fg='white', font=("Arial", 10, "bold")).pack(pady=10)
    
    def clear_history(self):
        """Clear password history"""
        if messagebox.askyesno("Confirm", "Are you sure you want to clear all password history?"):
            self.password_history = []
            self.save_history()
            self.status_var.set("Password history cleared!")
    
    def save_history(self):
        """Save password history to file"""
        try:
            with open('password_history.json', 'w') as f:
                json.dump(self.password_history, f)
        except Exception as e:
            print(f"Failed to save history: {e}")
    
    def load_history(self):
        """Load password history from file"""
        try:
            if os.path.exists('password_history.json'):
                with open('password_history.json', 'r') as f:
                    self.password_history = json.load(f)
        except Exception as e:
            print(f"Failed to load history: {e}")
            self.password_history = []

def main():
    """Main function to run the application"""
    root = tk.Tk()
    app = PasswordGenerator(root)
    
    # Center the window
    root.update_idletasks()
    x = (root.winfo_screenwidth() // 2) - (root.winfo_width() // 2)
    y = (root.winfo_screenheight() // 2) - (root.winfo_height() // 2)
    root.geometry(f"+{x}+{y}")
    
    root.mainloop()

if __name__ == "__main__":
    main()
