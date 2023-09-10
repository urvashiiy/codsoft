import tkinter as tk                    # importing the tkinter module as tk  
from tkinter import ttk                 # importing the ttk module from the tkinter library  
from PIL import ImageTk, Image 
from tkinter import messagebox          # importing the messagebox module from the tkinter library  
import sqlite3 as sql                   # importing the sqlite3 module as sql  
# defining the function to add tasks to the list  
def add_task():  
    # getting the string from the entry field  
    task_string = task_field.get()  
    # checking whether the string is empty or not  
    if len(task_string) == 0:  
        # displaying a message box with 'Empty Field' message  
        messagebox.showinfo('Error', 'Field is Empty.')  
    else:  
         
        tasks.append(task_string)  
        the_cursor.execute('insert into tasks values (?)', (task_string ,))  
        list_update()                                           # calling the function to update the list   
        task_field.delete(0, 'end')                              # deleting the entry in the entry field 
   
def list_update():   
    clear_list()                                                 # calling the function to clear the list 
    for task in tasks:  
        task_listbox.insert('end', task)                         # using the insert() method to insert the tasks in the list box  
  
def delete_task():                                               # defining the function to delete a task from the list   
    try:                                                        # using the try-except method 
        the_value = task_listbox.get(task_listbox.curselection())    
        if the_value in tasks:   
            tasks.remove(the_value)                            # removing the task from the list  
            list_update()  
            the_cursor.execute('delete from tasks where title = ?', (the_value,))  
    except:   
        messagebox.showinfo('Error', 'No Task Selected. Cannot Delete.')             # displaying the message box with 'No Item Selected' message for an exception 
  
def delete_all_tasks():                                                                # function to delete all tasks from the list   
    message_box = messagebox.askyesno('Delete All', 'Are you sure?')   
    if message_box == True:     
        while(len(tasks) != 0):    
            tasks.pop()  
          
        the_cursor.execute('delete from tasks')  
        # calling the function to update the list  
        list_update()  
  

def clear_list():   
    task_listbox.delete(0, 'end')    
def close():   
    print(tasks)   
    guiWindow.destroy()                      # using the destroy() method to close the application 
def retrieve_database():                       # function to retrieve data from the database   
    while(len(tasks) != 0):    
        tasks.pop()    
    for row in the_cursor.execute('select title from tasks'): 
        tasks.append(row[0])  
   
if __name__ == "__main__":                      # main function 
    guiWindow = tk.Tk()   
    guiWindow.title("To-Do APP")    
    guiWindow.geometry("500x450+750+250")   
    guiWindow.resizable(0, 0)    
    guiWindow.configure(bg = "#8B475D")  
   
    the_connection = sql.connect('listOfTasks.db')   
    the_cursor = the_connection.cursor()    
    the_cursor.execute('create table if not exists tasks (title text)')  
    
    tasks = []                              # defining an empty list
        
    header_frame = tk.Frame(guiWindow, bg = "#FFE4C4")  
    functions_frame = tk.Frame(guiWindow, bg = "#FFE4C4")  
    listbox_frame = tk.Frame(guiWindow, bg = "#FFE4C4")  
    
    header_frame.pack(fill = "both")  
    functions_frame.pack(side = "left", expand = True, fill = "both")  
    listbox_frame.pack(side = "right", expand = True, fill = "both")  
        
    header_label = ttk.Label(  
        header_frame,  
        text = "To-Do List",  
        font = ("Brush Script MT", "30"),  
        background = "#FFE4C4",  
        foreground = "#141414"  
    )   
    header_label.pack(padx = 20, pady = 20)     # using the pack() method to place the label in the application 
    
    task_label = ttk.Label(  
        functions_frame,  
        text = "Enter the Task:",  
        font = ("Consolas", "11", "bold"),  
        background = "#FAEBD7",  
        foreground = "#000000"  
    )    
    task_label.place(x = 30, y = 40)  
       
    task_field = ttk.Entry(  
        functions_frame,  
        font = ("Consolas", "12"),  
        width = 18,  
        background = "#FFF8DC",  
        foreground = "#A52A2A"  
    )   
    task_field.place(x = 30, y = 80)  
   
    add_button = ttk.Button(                  # adding buttons to the application using the ttk.Button() widget 
        functions_frame,  
        text = "Add Task",  
        width = 24,  
        command = add_task  
    )  
    del_button = ttk.Button(  
        functions_frame,  
        text = "Delete Task",  
        width = 24,  
        command = delete_task  
    )  
    del_all_button = ttk.Button(  
        functions_frame,  
        text = "Delete All Tasks",  
        width = 24,  
        command = delete_all_tasks  
    )  
    exit_button = ttk.Button(  
        functions_frame,  
        text = "Exit",  
        width = 24,  
        command = close  
    )    
    add_button.place(x = 30, y = 120)  
    del_button.place(x = 30, y = 160)  
    del_all_button.place(x = 30, y = 200)  
    exit_button.place(x = 30, y = 240)  
   
    task_listbox = tk.Listbox(  
        listbox_frame,  
        width = 26,  
        height = 13,  
        selectmode = 'SINGLE',  
        background = "#FFFFFF",  
        foreground = "#000000",  
        selectbackground = "#CD853F",  
        selectforeground = "#FFFFFF"  
    )   
    task_listbox.place(x = 10, y = 20)  
   
    retrieve_database()                      # calling some functions 
    list_update()  
    guiWindow.mainloop()    
    the_connection.commit()  
    the_cursor.close()  
