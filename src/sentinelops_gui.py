import tkinter as tk
from tkinter import messagebox
import subprocess
import os
from dotenv import load_dotenv

load_dotenv()

class SentinelOpsGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("SentinelOps Tactical Dashboard")
        self.root.geometry("400x300")

        title = tk.Label(root, text="SentinelOps GUI", font=("Helvetica", 16, "bold"))
        title.pack(pady=10)

        btn_start = tk.Button(root, text="Run Main Operation", command=self.run_main)
        btn_start.pack(pady=10)

        btn_test = tk.Button(root, text="Run Unit Tests", command=self.run_tests)
        btn_test.pack(pady=10)

        btn_docs = tk.Button(root, text="Generate Docs", command=self.gen_docs)
        btn_docs.pack(pady=10)

        btn_quit = tk.Button(root, text="Exit", command=root.quit)
        btn_quit.pack(pady=10)

    def run_main(self):
        try:
            subprocess.run(["python3", "src/main.py"], check=True)
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def run_tests(self):
        try:
            subprocess.run(["pytest", "tests/"], check=True)
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def gen_docs(self):
        try:
            subprocess.run(["bash", "scripts/gen_docs.sh"], check=True)
        except Exception as e:
            messagebox.showerror("Error", str(e))

if __name__ == "__main__":
    root = tk.Tk()
    app = SentinelOpsGUI(root)
    root.mainloop()
