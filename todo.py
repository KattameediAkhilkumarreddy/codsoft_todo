import tkinter as tk
from tkinter import messagebox

class TodoListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List App")

        # Task list
        self.tasks = []

        # Create and set up the GUI elements
        self.task_entry = tk.Entry(root, width=30)
        self.task_entry.grid(row=0, column=0, padx=20, pady=20)

        add_button = tk.Button(root, text="Add Task", command=self.add_task,bg="Green")
        add_button.grid(row=0, column=1, padx=20, pady=20)

        self.task_listbox = tk.Listbox(root, width=50, height=15,bg="lightblue")
        self.task_listbox.grid(row=1, column=0, columnspan=2, padx=30, pady=30)

       
        delete_button = tk.Button(root, text="Delete Task", command=self.delete_task,bg="Red")
        delete_button.grid(row=2, column=1, padx=20, pady=20)

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.update_task_listbox()
            messagebox.showinfo("Task Added", f"Task '{task}' added successfully.")
            self.task_entry.delete(0, tk.END)  # Clear the entry field
        else:
            messagebox.showwarning("Empty Task", "Please enter a task.")

    def update_task_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.task_listbox.insert(tk.END, task)

    def delete_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            selected_task = self.task_listbox.get(selected_index)
            confirm = messagebox.askyesno("Delete Task", f"Do you want to delete the task '{selected_task}'?")
            if confirm:
                del self.tasks[selected_index[0]]
                self.update_task_listbox()
                messagebox.showinfo("Task Deleted", f"Task '{selected_task}' deleted.")
        else:
            messagebox.showwarning("No Task Selected", "Please select a task to delete.")

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoListApp(root)
    root.mainloop()
