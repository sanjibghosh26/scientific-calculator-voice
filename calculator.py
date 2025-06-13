import tkinter as tk 
from tkinter import messagebox 
import math 
import re 
import speech_recognition as sr 
 
# Function to evaluate the mathematical expression 
def evaluate_expression(): 
    try: 
        expression = entry.get() 
 
        # Handle factorial properly 
        expression = re.sub(r'(\d+)\s*factorial', r'math.factorial(\1)', expression) 
 
        # Handle trigonometric functions with degrees converted to radians 
        expression = re.sub(r'(\d+)\s*(sin|cos|tan)', r'math.\2(math.radians(\1))', 
expression) 
 
        # Replace common math function names 
        expression = expression.replace('sqrt', 'math.sqrt') 
        expression = expression.replace('log', 'math.log10')  # log10 base 
        expression = expression.replace('ln', 'math.log')     # natural log 
        expression = expression.replace('pi', str(math.pi)) 
        expression = expression.replace('e', str(math.e)) 
        expression = expression.replace('^', '**')  # Power operator 
 
        result = eval(expression) 
        entry.delete(0, tk.END) 
        entry.insert(tk.END, str(result)) 
    except Exception as e: 
        messagebox.showerror("Error", "Invalid Expression") 
 
# Function to insert text into the entry field 
def insert_text(value): 
    entry.insert(tk.END, value) 
 
# Function to clear the entry field 
def clear_entry(): 
    entry.delete(0, tk.END) 
 
# Function to recognize voice input 
# Function to recognize voice input 
def voice_input(): 
    recognizer = sr.Recognizer() 
    with sr.Microphone() as source: 
        try: 
            entry.delete(0, tk.END) 
            entry.insert(tk.END, "Listening...") 
            window.update() 
 
            audio = recognizer.listen(source, timeout=5) 
            text = recognizer.recognize_google(audio) 
 
            # Replace spelled out numbers with digits 
            text = text.replace('zero', '0') 
            text = text.replace('one', '1') 
            text = text.replace('two', '2') 
            text = text.replace('three', '3') 
            text = text.replace('four', '4') 
            text = text.replace('five', '5') 
            text = text.replace('six', '6') 
            text = text.replace('seven', '7') 
            text = text.replace('eight', '8') 
            text = text.replace('nine', '9') 
 
            # Handle potential misheard words 
            text = text.replace('sign', 'sin')  # Treat 'sign' as 'sin' 
            text = text.replace('tan of', 'tan')  # Treat 'tang' as 'tan' 
            text = text.replace('coss', 'cos')  # Treat 'coss' as 'cos' 
 
            # Replace common math function names 
            text = text.replace('plus', '+') 
            text = text.replace('minus', '-') 
            text = text.replace('times', '*') 
            text = text.replace('divided by', '/') 
            text = text.replace('into', '*') 
            text = text.replace('by', '/') 
            text = text.replace('power', '^') 
            text = text.replace('square root of', 'sqrt') 
            text = text.replace('log of', 'log') 
            text = text.replace('factorial of', 'factorial') 
            text = text.replace('pi', 'pi') 
            text = text.replace('e', 'e') 
            text = text.replace('bracket 1', '(') 
            text = text.replace('bracket one', '(') 
            text = text.replace(' bracket two', ')') 
            text = text.replace(' bracket 2', ')') 
            text = text.replace(' bracket second', ')') 
            text = text.replace('10', 'tan') 
 
            # Ensure 'sin', 'cos', 'tan' are interpreted correctly 
            text = text.replace('sin', 'sin') 
            text = text.replace('cos', 'cos') 
            text = text.replace('tan', 'tan') 
 
            entry.delete(0, tk.END) 
            entry.insert(tk.END, text) 
            evaluate_expression() 
 
        except sr.UnknownValueError: 
            messagebox.showerror("Error", "Could not understand the audio") 
        except sr.RequestError: 
            messagebox.showerror("Error", "Could not request results; check your internet connection") 
        except Exception as e: 
            messagebox.showerror("Error", str(e)) 
 
# Setting up the main window 
window = tk.Tk() 
window.title("Advanced Scientific Calculator") 
window.geometry("400x600") 
window.configure(bg="#222831") 
 
# Entry widget 
entry = tk.Entry(window, font=("Arial", 20), bd=8, relief=tk.RIDGE, justify='right') 
entry.pack(padx=10, pady=20, fill=tk.BOTH) 
 
# Frame for buttons 
button_frame = tk.Frame(window, bg="#393E46") 
button_frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True) 
 
# Buttons Layout 
buttons = [ 
    ['7', '8', '9', '/', 'sqrt'], 
    ['4', '5', '6', '*', 'log'], 
    ['1', '2', '3', '-', 'sin'], 
    ['0', '.', '=', '+', 'cos'], 
    ['(', ')', '!', '^', 'tan'], 
    ['pi', 'e', 'C', 'Voice'] 
] 
 
# Dynamically create buttons 
# Dynamically create buttons 
for row in buttons: 
    row_frame = tk.Frame(button_frame, bg="#393E46") 
    row_frame.pack(fill=tk.BOTH, expand=True) 
    for btn in row: 
        action = lambda x=btn: insert_text(x) if x not in ['=', 'C', 'Voice'] else ( 
            evaluate_expression() if x == '=' else clear_entry() if x == 'C' else 
voice_input()) 
         
        # Set button color based on the button text 
        if btn in ['sqrt', 'sin', 'cos', 'tan', 'log', 'ln', 'factorial']: 
            bg_color = "#FF8C00"  # Orange 
        elif btn == '=': 
            bg_color = "#007BFF"  # Blue 
        elif btn == 'C': 
            bg_color = "#FF4C4C"  # Red 
        elif btn == 'DEL': 
            bg_color = "#AAAAAA"  # Light Grey 
        else: 
            bg_color = "#2E2E2E"  # Dark Grey for others 
         
        b = tk.Button(row_frame, text=btn, font=("Arial", 18), bd=5, relief=tk.RAISED, 
                      command=action, bg=bg_color, fg="white") 
        b.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=2, pady=2) 
 
# Bind Enter key to evaluate 
window.bind('<Return>', lambda event: evaluate_expression()) 
# Start the main event loop 
window.mainloop() 