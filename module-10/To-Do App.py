"""
Brijette Baboolal
Assignment 10.2
To-Do App.py

This program is a To-Do application built using Tkinter GUI library. 
It allows users to manage tasks within a pop up window. Users can type new 
tasks into a text box and press Enter to add them to the list. To delete a task, 
the user right-clicks on the task and confirms the deletion. The app includes a 
menu bar with a "File → Exit" option that allows users to safely close the application.
"""
import tkinter as tk
import tkinter.messagebox as msg

class TodoApp(tk.Tk):
    def __init__(self, tasks=None):
        super().__init__()

        self.tasks = tasks if tasks else []

        # Title with your last name
        self.title('Baboolal To-Do App')  
        self.geometry('300x400')

        # Menu bar
        menubar = tk.Menu(self)
        file_menu = tk.Menu(menubar, tearoff=0, bg='pink', fg='white')  # complementary colors
        file_menu.add_command(label="Exit", command=self.quit)
        menubar.add_cascade(label="File", menu=file_menu)
        self.config(menu=menubar)

        # Canvas and frames
        self.tasks_canvas = tk.Canvas(self)
        self.tasks_frame = tk.Frame(self.tasks_canvas)
        self.text_frame = tk.Frame(self)

        self.scrollbar = tk.Scrollbar(self.tasks_canvas, orient="vertical", command=self.tasks_canvas.yview)
        self.tasks_canvas.configure(yscrollcommand=self.scrollbar.set)
        self.canvas_frame = self.tasks_canvas.create_window((0, 0), window=self.tasks_frame, anchor="nw")

        self.task_create = tk.Text(self.text_frame, height=3, bg='white', fg='black')
        self.task_create.pack(side=tk.BOTTOM, fill=tk.X)
        self.text_frame.pack(side=tk.BOTTOM, fill=tk.X)

        self.tasks_canvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Instruction label
        instruction = tk.Label(self.tasks_frame, text='--- Right-click to delete a task ---', bg="skyblue", fg="black", pady=10)
        instruction.bind("<Button-3>", self.remove_task)  
        instruction.pack(side=tk.TOP, fill=tk.X)
        self.tasks.append(instruction)

        self.task_create.bind("<Return>", self.add_task)
        self.task_create.bind("<Button-1>", self.clear_text)
        self.tasks_canvas.bind("<Configure>", self.configure_canvas)

        self.colour_schemes = [{'bg': 'skyblue', 'fg': 'black'}, {'bg': 'lightcoral', 'fg': 'white'}]
    
    def add_task(self, event=None):
        task_text = self.task_create.get("1.0", tk.END).strip()
        if task_text:
            new_task = tk.Label(self.tasks_frame, text=task_text, pady=10)
            self.set_task_colour(len(self.tasks), new_task)
            new_task.bind("<Button-3>", self.remove_task)  # Right click to delete
            new_task.pack(side=tk.TOP, fill=tk.X)
            self.tasks.append(new_task)
            self.task_create.delete("1.0", tk.END)
        return "break"  

    def remove_task(self, event):
        task = event.widget
        if msg.askyesno("Delete Task", f"Delete '{task.cget('text')}'?"):
            self.tasks.remove(task)
            task.destroy()
            self.recolour_tasks()

    def recolour_tasks(self):
        for index, task in enumerate(self.tasks):
            self.set_task_colour(index, task)

    def set_task_colour(self, position, task):
        style = self.colour_schemes[position % 2]
        task.configure(bg=style['bg'], fg=style['fg'])

    def configure_canvas(self, event):
        canvas_width = event.width
        self.tasks_canvas.itemconfig(self.canvas_frame, width=canvas_width)
        self.tasks_canvas.configure(scrollregion=self.tasks_canvas.bbox("all"))

    def clear_text(self, event):
        self.task_create.delete(1.0, tk.END)

if __name__ == "__main__":
    app = TodoApp()
    app.mainloop()
