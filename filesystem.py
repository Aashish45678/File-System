import tkinter as tk
from tkinter import filedialog, messagebox
import os
import stat
from datetime import datetime
import shutil

class FileSystemGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("File System GUI")

        # Color scheme
        self.bg_color = "#F0F0F0"  # Light gray
        self.fg_color = "black"
        self.button_bg = "#C0C0C0"  # Silver
        self.button_fg = "black"

        # Styles
        self.bold_font = ("Arial", 10, "bold")

        # Current Directory
        self.current_directory = tk.StringVar()
        self.current_directory.set(os.getcwd())

        self.directory_label = tk.Label(self.root, text="Current Directory:", font=self.bold_font)
        self.directory_label.grid(row=0, column=0, sticky="w")
        self.directory_label.configure(bg=self.bg_color, fg=self.fg_color)

        self.directory_entry = tk.Entry(self.root, textvariable=self.current_directory, width=50)
        self.directory_entry.grid(row=0, column=1, padx=10, pady=5)

        self.browse_button = tk.Button(self.root, text="Browse", command=self.browse_directory)
        self.browse_button.grid(row=0, column=2, padx=5)
        self.browse_button.configure(bg=self.button_bg, fg=self.button_fg)

        # Full Name
        self.full_name_label = tk.Label(self.root, text="Full Name:", font=self.bold_font)
        self.full_name_label.grid(row=1, column=0, sticky="w")
        self.full_name_label.configure(bg=self.bg_color, fg=self.fg_color)

        self.full_name_entry = tk.Entry(self.root, width=50)
        self.full_name_entry.grid(row=1, column=1, padx=10, pady=5)

        # Permissions
        self.permissions_label = tk.Label(self.root, text="Permissions:", font=self.bold_font)
        self.permissions_label.grid(row=2, column=0, sticky="w")
        self.permissions_label.configure(bg=self.bg_color, fg=self.fg_color)

        self.permissions_entry = tk.Entry(self.root, width=50)
        self.permissions_entry.grid(row=2, column=1, padx=10, pady=5)

        # Create buttons
        self.create_buttons()

        # Directory Management
        self.directory_management()

    def create_buttons(self):
        self.create_button = tk.Button(self.root, text="Create File", command=self.create_file)
        self.create_button.grid(row=3, column=0, padx=5, pady=5, sticky="w")
        self.create_button.configure(bg=self.button_bg, fg=self.button_fg)

        self.update_button = tk.Button(self.root, text="Update File", command=self.update_file)
        self.update_button.grid(row=3, column=1, padx=5, pady=5, sticky="w")
        self.update_button.configure(bg=self.button_bg, fg=self.button_fg)

        self.delete_button = tk.Button(self.root, text="Delete File", command=self.delete_file)
        self.delete_button.grid(row=4, column=0, padx=5, pady=5, sticky="w")
        self.delete_button.configure(bg=self.button_bg, fg=self.button_fg)

        self.read_button = tk.Button(self.root, text="Read File", command=self.read_file)
        self.read_button.grid(row=4, column=1, padx=5, pady=5, sticky="w")
        self.read_button.configure(bg=self.button_bg, fg=self.button_fg)

        self.list_button = tk.Button(self.root, text="List Directory", command=self.list_directory)
        self.list_button.grid(row=5, column=0, padx=5, pady=5, sticky="w")
        self.list_button.configure(bg=self.button_bg, fg=self.button_fg)

        self.set_permissions_button = tk.Button(self.root, text="Set Permissions", command=self.set_permissions)
        self.set_permissions_button.grid(row=5, column=1, padx=5, pady=5, sticky="w")
        self.set_permissions_button.configure(bg=self.button_bg, fg=self.button_fg)

        self.rename_label = tk.Label(self.root, text="New Name:", font=self.bold_font)
        self.rename_label.grid(row=6, column=0, sticky="w", padx=5, pady=5)
        self.rename_label.configure(bg=self.bg_color, fg=self.fg_color)

        self.rename_entry = tk.Entry(self.root, width=50)
        self.rename_entry.grid(row=6, column=1, padx=10, pady=5)

        self.rename_button = tk.Button(self.root, text="Rename File", command=self.rename_file)
        self.rename_button.grid(row=7, column=0, padx=5, pady=5, sticky="w")
        self.rename_button.configure(bg=self.button_bg, fg=self.button_fg)

        self.copy_label = tk.Label(self.root, text="Copy Name:", font=self.bold_font)
        self.copy_label.grid(row=8, column=0, sticky="w", padx=5, pady=5)
        self.copy_label.configure(bg=self.bg_color, fg=self.fg_color)

        self.copy_entry = tk.Entry(self.root, width=50)
        self.copy_entry.grid(row=8, column=1, padx=10, pady=5)

        self.copy_button = tk.Button(self.root, text="Copy File", command=self.copy_file)
        self.copy_button.grid(row=9, column=0, padx=5, pady=5, sticky="w")
        self.copy_button.configure(bg=self.button_bg, fg=self.button_fg)

    def directory_management(self):
        self.directory_label = tk.Label(self.root, text="Directory Management", font=self.bold_font)
        self.directory_label.grid(row=10, column=0, sticky="w", padx=5, pady=10, columnspan=2)
        self.directory_label.configure(bg=self.bg_color, fg=self.fg_color)

        self.create_dir_label = tk.Label(self.root, text="Create Directory:", font=self.bold_font)
        self.create_dir_label.grid(row=11, column=0, sticky="w", padx=5, pady=5)
        self.create_dir_label.configure(bg=self.bg_color, fg=self.fg_color)

        self.create_dir_entry = tk.Entry(self.root, width=50)
        self.create_dir_entry.grid(row=11, column=1, padx=10, pady=5)

        self.create_dir_button = tk.Button(self.root, text="Create", command=self.create_directory)
        self.create_dir_button.grid(row=12, column=0, padx=5, pady=5, sticky="w")
        self.create_dir_button.configure(bg=self.button_bg, fg=self.button_fg)

        self.delete_dir_label = tk.Label(self.root, text="Delete Directory:", font=self.bold_font)
        self.delete_dir_label.grid(row=13, column=0, sticky="w", padx=5, pady=5)
        self.delete_dir_label.configure(bg=self.bg_color, fg=self.fg_color)

        self.delete_dir_entry = tk.Entry(self.root, width=50)
        self.delete_dir_entry.grid(row=13, column=1, padx=10, pady=5)

        self.delete_dir_button = tk.Button(self.root, text="Delete", command=self.delete_directory)
        self.delete_dir_button.grid(row=14, column=0, padx=5, pady=5, sticky="w")
        self.delete_dir_button.configure(bg=self.button_bg, fg=self.button_fg)

    def browse_directory(self):
        directory = filedialog.askdirectory()
        if directory:
            self.current_directory.set(directory)

    def create_file(self):
        filename = self.full_name_entry.get()
        permissions = self.permissions_entry.get()
        if filename:
            filepath = os.path.join(self.current_directory.get(), filename)
            try:
                if os.path.exists(filepath):
                    raise FileExistsError(f"A file with the same name already exists in the directory: {filename}")
                with open(filepath, 'w') as file:
                    pass  # Creates an empty file
                if permissions:
                    try:
                        permissions_octal = int(permissions, 8)
                        os.chmod(filepath, permissions_octal)
                    except ValueError:
                        raise ValueError("Please enter a valid octal value for permissions.")
                self.list_directory()
                messagebox.showinfo("File Created", f"File '{filename}' created successfully.")
            except (PermissionError, FileNotFoundError, FileExistsError, ValueError) as error:
                messagebox.showerror("Error Creating File", str(error))
        else:
            messagebox.showerror("Invalid File Name", "Please enter a valid file name.")

    def update_file(self):
        filename = self.full_name_entry.get()
        if filename:
            filepath = os.path.join(self.current_directory.get(), filename)
            try:
                if os.path.exists(filepath):
                    text_editor = tk.Toplevel(self.root)
                    text_editor.title(f"Text Editor - {filename}")

                    text_widget = tk.Text(text_editor)
                    text_widget.pack()

                    with open(filepath, 'r') as file:
                        text_widget.insert(tk.END, file.read())

                    def save_changes():
                        try:
                            with open(filepath, 'w') as file:
                                file.write(text_widget.get("1.0", tk.END))
                            text_editor.destroy()
                            messagebox.showinfo("File Updated", f"File '{filename}' updated successfully.")
                        except PermissionError:
                            messagebox.showerror("Error Updating File", f"Permission denied while updating '{filename}'.")
                        except Exception as e:
                            messagebox.showerror("Error Updating File", str(e))

                    save_button = tk.Button(text_editor, text="Save", command=save_changes)
                    save_button.pack()
                else:
                    raise FileNotFoundError(f"The specified file does not exist: {filename}")
            except (PermissionError, FileNotFoundError) as error:
                messagebox.showerror("Error Updating File", str(error))
            except Exception as e:
                messagebox.showerror("Error Updating File", str(e))
        else:
            messagebox.showerror("Invalid File Name", "Please enter a valid file name.")

    def delete_file(self):
        filename = self.full_name_entry.get()
        if filename:
            filepath = os.path.join(self.current_directory.get(), filename)
            try:
                if os.path.exists(filepath):
                    os.remove(filepath)
                    self.list_directory()
                    messagebox.showinfo("File Deleted", f"File '{filename}' deleted successfully.")
                else:
                    raise FileNotFoundError(f"The specified file does not exist: {filename}")
            except (PermissionError, FileNotFoundError) as error:
                messagebox.showerror("Error Deleting File", str(error))
            except Exception as e:
                messagebox.showerror("Error Deleting File", str(e))
        else:
            messagebox.showerror("Invalid File Name", "Please enter a valid file name.")

    def read_file(self):
        filename = self.full_name_entry.get()
        if filename:
            filepath = os.path.join(self.current_directory.get(), filename)
            try:
                if os.path.exists(filepath):
                    with open(filepath, 'r') as file:
                        file_contents = file.read()
                    messagebox.showinfo("File Contents", file_contents)
                else:
                    raise FileNotFoundError(f"The specified file does not exist: {filename}")
            except (PermissionError, FileNotFoundError) as error:
                messagebox.showerror("Error Reading File", str(error))
            except Exception as e:
                messagebox.showerror("Error Reading File", str(e))
        else:
            messagebox.showerror("Invalid File Name", "Please enter a valid file name.")

    def list_directory(self):
        directory = self.current_directory.get()
        if directory:
            try:
                self.full_name_entry.delete(0, tk.END)
                files = os.listdir(directory)
                listing = "Listing Directory:\n\n"
                listing += f"{'Permission':<12}{'File/Directory':<20}{'Type':<6}{'Creation Date':<20}\n"
                for file in files:
                    filepath = os.path.join(directory, file)
                    permissions = self.get_permissions(filepath)
                    type_indicator = 'f' if os.path.isfile(filepath) else 'd'
                    creation_date = datetime.fromtimestamp(os.path.getctime(filepath))
                    creation_date_str = creation_date.strftime('%Y-%m-%d %H:%M:%S')
                    listing += f"{permissions:<12}{file:<20}{type_indicator:<6}{creation_date_str:<20}\n"

                # Create a new window for displaying the listing
                listing_window = tk.Toplevel(self.root)
                listing_window.title("Directory Listing")

                # Create a Text widget for displaying the listing
                listing_text = tk.Text(listing_window, width=80, height=20)
                listing_text.pack()

                # Insert the directory listing into the Text widget
                listing_text.insert(tk.END, listing)

                # Disable text editing in the Text widget
                listing_text.configure(state=tk.DISABLED)
            except PermissionError:
                messagebox.showerror("Error Listing Directory", "Permission denied while listing directory.")
            except Exception as e:
                messagebox.showerror("Error Listing Directory", str(e))

    def set_permissions(self):
        filename = self.full_name_entry.get()
        permissions = self.permissions_entry.get()
        if filename and permissions:
            filepath = os.path.join(self.current_directory.get(), filename)
            try:
                if os.path.exists(filepath):
                    try:
                        permissions_octal = int(permissions, 8)
                        os.chmod(filepath, permissions_octal)
                        messagebox.showinfo("Permissions Set", "File permissions have been updated.")
                    except ValueError:
                        raise ValueError("Please enter a valid octal value for permissions.")
                else:
                    raise FileNotFoundError(f"The specified file does not exist: {filename}")
            except (PermissionError, FileNotFoundError, ValueError) as error:
                messagebox.showerror("Error Setting Permissions", str(error))
            except Exception as e:
                messagebox.showerror("Error Setting Permissions", str(e))
        else:
            messagebox.showerror("Invalid File Name or Permissions", "Please enter a valid file name and permissions.")


    def rename_file(self):
        old_name = self.full_name_entry.get()
        new_name = self.rename_entry.get()
        if old_name and new_name:
            old_path = os.path.join(self.current_directory.get(), old_name)
            new_path = os.path.join(self.current_directory.get(), new_name)
            try:
                if os.path.exists(old_path):
                    os.rename(old_path, new_path)
                    self.list_directory()
                    messagebox.showinfo("File Renamed", f"File '{old_name}' renamed to '{new_name}' successfully.")
                else:
                    raise FileNotFoundError(f"The specified file does not exist: {old_name}")
            except (PermissionError, FileNotFoundError, OSError) as error:
                messagebox.showerror("Error Renaming File", str(error))
            except Exception as e:
                messagebox.showerror("Error Renaming File", str(e))
        else:
            messagebox.showerror("Invalid File Names", "Please enter valid file names.")

    def copy_file(self):
        source_name = self.full_name_entry.get()
        destination_name = self.copy_entry.get()
        if source_name and destination_name:
            source_path = os.path.join(self.current_directory.get(), source_name)
            destination_path = os.path.join(self.current_directory.get(), destination_name)
            try:
                if os.path.exists(source_path):
                    shutil.copy2(source_path, destination_path)
                    self.list_directory()
                    messagebox.showinfo("File Copied", f"File '{source_name}' copied to '{destination_name}' successfully.")
                else:
                    raise FileNotFoundError(f"The specified file does not exist: {source_name}")
            except (PermissionError, FileNotFoundError, shutil.Error) as error:
                messagebox.showerror("Error Copying File", str(error))
            except Exception as e:
                messagebox.showerror("Error Copying File", str(e))
        else:
            messagebox.showerror("Invalid File Names", "Please enter valid file names.")
    
    
    def create_directory(self):
        dirname = self.create_dir_entry.get()
        if dirname:
            dirpath = os.path.join(self.current_directory.get(), dirname)
            try:
                if os.path.exists(dirpath):
                    raise FileExistsError(f"A directory with the same name already exists: {dirname}")
                os.makedirs(dirpath)
                self.list_directory()
                messagebox.showinfo("Directory Created", f"Directory '{dirname}' created successfully.")
            except (PermissionError, FileExistsError) as error:
                messagebox.showerror("Error Creating Directory", str(error))
            except Exception as e:
                messagebox.showerror("Error Creating Directory", str(e))
        else:
            messagebox.showerror("Invalid Directory Name", "Please enter a valid directory name.")


    def delete_directory(self):
        dirname = self.delete_dir_entry.get()
        if dirname:
            dirpath = os.path.join(self.current_directory.get(), dirname)
            try:
                if os.path.exists(dirpath):
                    try:
                        os.rmdir(dirpath)
                        self.list_directory()
                        messagebox.showinfo("Directory Deleted", f"Directory '{dirname}' deleted successfully.")
                    except OSError:
                        raise OSError("The directory is not empty.")
                else:
                    raise FileNotFoundError(f"The specified directory does not exist: {dirname}")
            except (PermissionError, FileNotFoundError, OSError) as error:
                messagebox.showerror("Error Deleting Directory", str(error))
            except Exception as e:
                messagebox.showerror("Error Deleting Directory", str(e))
        else:
            messagebox.showerror("Invalid Directory Name", "Please enter a valid directory name.")

    def get_permissions(self, filepath):
        permissions = os.stat(filepath).st_mode
        permissions_string = str(oct(permissions))[-3:]
        return permissions_string

    def run(self):
        self.root.configure(bg=self.bg_color)
        self.root.mainloop()


if __name__ == '__main__':
    gui = FileSystemGUI()
    gui.run()
