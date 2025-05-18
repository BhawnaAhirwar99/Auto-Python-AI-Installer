import subprocess
import tkinter as tk
from tkinter import messagebox
import google.generativeai as genai

# PART 1: Add your own Gemini API key here
GEMINI_API_KEY = "PUT_YOUR_API_KEY_HERE"

# PART 2: Configure Gemini
genai.configure(api_key=GEMINI_API_KEY)

# PART 3: Python Installation Checker
def check_python():
    try:
        output = subprocess.check_output("python --version", stderr=subprocess.STDOUT)
        messagebox.showinfo("Python Version", output.decode())
    except Exception:
        messagebox.showerror("Error", "Python is not installed or not found in PATH.")

# PART 4: AI Error Checker Function
def check_errors():
    user_code = code_box.get("1.0", tk.END)
    if not user_code.strip():
        messagebox.showwarning("No Code", "Please paste your Python code.")
        return
    try:
        model = genai.GenerativeModel("gemini-pro")
        prompt = "Check and correct the following Python code:\\n\\n" + user_code
        response = model.generate_content(prompt)
        result_box.delete("1.0", tk.END)
        result_box.insert(tk.END, response.text)
    except Exception as e:
        messagebox.showerror("AI Error", str(e))

# PART 5: GUI Setup
root = tk.Tk()
root.title("AutoPython Installer with AI")
root.geometry("700x500")
root.config(bg="white")

tk.Label(root, text="Paste your Python code below:", bg="white", font=("Arial", 12)).pack(pady=10)
code_box = tk.Text(root, height=12, width=80, font=("Courier", 10))
code_box.pack()

tk.Button(root, text="Check Python Installation", command=check_python, bg="#28a745", fg="white", font=("Arial", 11)).pack(pady=10)
tk.Button(root, text="Check Code with AI", command=check_errors, bg="#007bff", fg="white", font=("Arial", 11)).pack(pady=5)

tk.Label(root, text="AI Feedback:", bg="white", font=("Arial", 12)).pack(pady=10)
result_box = tk.Text(root, height=8, width=80, font=("Courier", 10), bg="#f9f9f9")
result_box.pack()

root.mainloop()
