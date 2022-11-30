import tkinter as tk
from tkinter import *
from tkinter import ttk
import datab as db

todo = db.getFromDB()
taskEdit=''

def delete():
    global todo
    selection = todo_listbox.curselection()
    todo_listbox.delete(selection[0])
    s=todo[selection[0]]
    db.deleteTask(s)
    todo = db.getFromDB()
 
def add():
    new_task = task_entry.get()
    todo.insert(0, new_task)
    todo_var.set(todo)
    db.addToDb(new_task)

def edit():
    global todo
    global taskEdit
    selection = todo_listbox.curselection()
    taskEdit=todo[selection[0]]
    task_entry.delete(0,END)
    task_entry.insert(0, todo[selection[0]])
    btn_save.grid(column=1, row=3, padx=6, pady=6)    

def save():
    global todo
    global taskEdit
    btn_save.grid_remove()
    taskUpdated=task_entry.get()
    db.updateTask(taskOld=taskEdit, task=taskUpdated)
    todo = db.getFromDB()
    todo_var.set(todo)

def exit():
    window.destroy()


window = tk.Tk()
window.title('ToDo list')
frame_add = tk.Frame(window, width=500, height=20, bg='#CC99FF')
frame_list = tk.Frame(window, width=350, height=150, bg="#66FF99")
frame_control = tk.Frame(window, width=150, height=150, bg='#FFFF99')

frame_add.place(relx=0, rely=0, relwidth=1, relheight=0.1)
frame_list.place(relx=0, rely=0.1, relwidth=0.8, relheight=0.9)
frame_control.place(relx=0.8, rely=0.1, relwidth=0.2, relheight=0.9)
todo_var = Variable(value=todo)
todo_listbox = Listbox(frame_list, listvariable=todo_var)
todo_listbox.configure(background="#66FF99", font="mincho 13")
todo_listbox.pack(anchor=NW, fill=X, padx=5, pady=15)

task_entry = ttk.Entry(frame_add, width=80)
task_entry.grid(column=0, row=0, padx=6, pady=6, sticky=EW)

btn_add = Button(frame_control,text="Добавить", command=add)
btn_delete = Button(frame_control,text="Удалить", command=delete)
btn_edit = Button(frame_control,text="Изменить", command=edit)
btn_save = Button(frame_control,text="Сохранить", command=save)
btn_exit = Button(frame_control,text="Выйти", command=exit)
btn_add.grid(column=1, row=0, padx=6, pady=6, sticky=W)
btn_delete.grid(column=1, row=1, padx=6, pady=6, sticky=W)
btn_edit.grid(column=1, row=2, padx=6, pady=6, sticky=W)
btn_exit.grid(column=1, row=7, padx=6, pady=6, sticky=W)

window.geometry('500x300')
window.resizable(width=False, height=False)
window.mainloop()