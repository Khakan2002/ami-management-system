import tkinter as tk
from tkinter import messagebox, simpledialog
import csv

FILENAME = "ami_records.csv"

def save_record_to_file(record):
    try:
        with open(FILENAME, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(record)
    except Exception as e:
        messagebox.showerror("Error", f"Failed to save record: {str(e)}")

def load_records_from_file():
    try:
        with open(FILENAME, newline='') as file:
            reader = csv.reader(file)
            return list(reader)
    except FileNotFoundError:
        return []

root = tk.Tk()
root.title("Academic Misconduct Investigation (AMI) Management")

def add_record():
    date = simpledialog.askstring("Input", "Enter Date of Case:")
    student_name = simpledialog.askstring("Input", "Enter Student Name:")
    module_name = simpledialog.askstring("Input", "Enter Module Name:")
    module_code = simpledialog.askstring("Input", "Enter Module Code:")
    module_leader = simpledialog.askstring("Input", "Enter Module Leader:")
    allegation = simpledialog.askstring("Input", "Enter Allegation:")
    outcome = simpledialog.askstring("Input", "Enter Outcome of Case:")
    if date and student_name and module_name and module_code and module_leader and allegation and outcome:
        record = [date, student_name, module_name, module_code, module_leader, allegation, outcome]
        save_record_to_file(record)
        messagebox.showinfo("Success", "Record Added and Saved Successfully!")
    else:
        messagebox.showerror("Error", "All fields are required!")

def view_records():
    records = load_records_from_file()
    if not records:
        messagebox.showinfo("Records", "No records found.")
    else:
        display = "\n".join(
            f"{i+1}. {record[0]} | {record[1]} | {record[2]} | {record[3]} | {record[4]} | {record[5]} | {record[6]}"
            for i, record in enumerate(records)
        )
        messagebox.showinfo("Records", display)

def update_record():
    records = load_records_from_file()
    if not records:
        messagebox.showinfo("Update", "No records found.")
        return
    try:
        record_id = simpledialog.askinteger("Input", "Enter Record ID to Update:")
        if record_id is None or not (1 <= record_id <= len(records)):
            messagebox.showerror("Error", "Invalid Record ID.")
            return
        index = record_id - 1
        record = records[index]
        date = simpledialog.askstring("Input", "Enter New Date of Case:", initialvalue=record[0])
        student_name = simpledialog.askstring("Input", "Enter New Student Name:", initialvalue=record[1])
        module_name = simpledialog.askstring("Input", "Enter New Module Name:", initialvalue=record[2])
        module_code = simpledialog.askstring("Input", "Enter New Module Code:", initialvalue=record[3])
        module_leader = simpledialog.askstring("Input", "Enter New Module Leader:", initialvalue=record[4])
        allegation = simpledialog.askstring("Input", "Enter New Allegation:", initialvalue=record[5])
        outcome = simpledialog.askstring("Input", "Enter New Outcome of Case:", initialvalue=record[6])
        if date and student_name and module_name and module_code and module_leader and allegation and outcome:
            records[index] = [date, student_name, module_name, module_code, module_leader, allegation, outcome]
            with open(FILENAME, 'w', newline='') as file:
                writer = csv.writer(file); writer.writerows(records)
            messagebox.showinfo("Success", "Record Updated Successfully!")
        else:
            messagebox.showerror("Error", "All fields must be filled.")
    except Exception as e:
        messagebox.showerror("Error", f"Something went wrong: {str(e)}")

def delete_record():
    records = load_records_from_file()
    if not records:
        messagebox.showinfo("Delete", "No records found.")
        return
    try:
        record_id = simpledialog.askinteger("Input", "Enter Record ID to Delete:")
        if record_id is None or not (1 <= record_id <= len(records)):
            messagebox.showerror("Error", "Invalid Record ID.")
            return
        index = record_id - 1
        confirm = messagebox.askyesno("Confirm Delete", f"Are you sure you want to delete record {record_id}?")
        if confirm:
            del records[index]
            with open(FILENAME, 'w', newline='') as file:
                writer = csv.writer(file); writer.writerows(records)
            messagebox.showinfo("Success", "Record Deleted Successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"Something went wrong: {str(e)}")

tk.Button(root, text="Add Record", command=add_record).pack(pady=5)
tk.Button(root, text="View Records", command=view_records).pack(pady=5)
tk.Button(root, text="Update Record", command=update_record).pack(pady=5)
tk.Button(root, text="Delete Record", command=delete_record).pack(pady=5)
tk.Button(root, text="Exit", command=root.quit).pack(pady=5)

root.mainloop()
