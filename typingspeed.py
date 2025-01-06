import tkinter as tk
from tkinter import messagebox
import time
import random

# Sample texts for the typing test
SAMPLE_TEXTS = [
    "The quick brown fox jumps over the lazy dog.",
    "Python is an amazing programming language.",
    "Practice makes a man perfect.",
    "A journey of a thousand miles begins with a single step.",
    "Typing speed can improve with regular practice.",
    "He is one of the leading authors in the educational psychology."
    "You are one of the lazy boy in this world.",
    "I am manifesting to get an USA visa stamped in my passport."
    "Life is better when you're laughing.",
    "Dream big and dare to fail.",
    "Happiness is a journey, not a destination.",
    "Stay positive, work hard, make it happen.",
    "Every moment is a fresh beginning.",
    "Do what you can with what you have.",
    "Believe in yourself and all that you are.",
    "Success is the sum of small efforts repeated daily.",
    "Kindness is free; sprinkle it everywhere."
]

def start_typing():
    """Starts the typing test by displaying a random text, enabling the text entry, and recording the start time."""
    global start_time, current_text
    current_text = random.choice(SAMPLE_TEXTS)
    sample_text_display.config(text=current_text)
    start_time = time.time()
    entry_field.config(state=tk.NORMAL)
    entry_field.delete(0, tk.END)
    entry_field.focus()
    start_button.config(state=tk.DISABLED)

def calculate_speed():
    """Calculates and displays the typing speed."""
    global start_time

    if start_time is None:
        messagebox.showwarning("Warning", "Please start the test before submitting!")
        return

    end_time = time.time()
    elapsed_time = end_time - start_time

    typed_text = entry_field.get()

    if typed_text.strip() == "":
        messagebox.showerror("Error", "You did not type anything!")
        return

    # Calculate typing speed
    words = len(typed_text.split())
    wpm = (words / elapsed_time) * 60

    # Compare with the sample text for accuracy
    accuracy = calculate_accuracy(current_text, typed_text)

    # Display results
    result_message = (
        f"Time: {elapsed_time:.2f} seconds\n"
        f"Words Per Minute (WPM): {wpm:.2f}\n"
        f"Accuracy: {accuracy:.2f}%"
    )
    messagebox.showinfo("Typing Test Results", result_message)

    # Reset the state
    start_button.config(state=tk.NORMAL)
    entry_field.config(state=tk.DISABLED)

def calculate_accuracy(sample, typed):
    """Calculates accuracy by comparing the sample text with the typed text."""
    sample_words = sample.split()
    typed_words = typed.split()

    correct_count = sum(1 for s, t in zip(sample_words, typed_words) if s == t)
    accuracy = (correct_count / len(sample_words)) * 100 if sample_words else 0
    return accuracy

# Initialize the main application window
app = tk.Tk()
app.title("Typing Speed Test")
app.geometry("500x300")

# Add the sample text label
sample_label = tk.Label(app, text="Sample Text:", font=("Arial", 14))
sample_label.pack(pady=10)

sample_text_display = tk.Label(app, text="", font=("Arial", 12), wraplength=480, justify="center")
sample_text_display.pack(pady=5)

# Add the text entry field
entry_field = tk.Entry(app, font=("Arial", 14), width=50, state=tk.DISABLED)
entry_field.pack(pady=10)

# Add the start button
start_button = tk.Button(app, text="Start Test", font=("Arial", 12), command=start_typing)
start_button.pack(pady=10)

# Add the submit button
submit_button = tk.Button(app, text="Submit", font=("Arial", 12), command=calculate_speed)
submit_button.pack(pady=10)

# Initialize global variables
start_time = None
current_text = ""

# Run the tkinter main loop
app.mainloop()
