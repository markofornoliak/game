import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import ast
import dis
import gc

class LanguageLearningApp:
    def __init__(self, master):
        self.master = master
        self.master.title('Language Learning and Image Processing App')

        # Create UI elements
        self.label = tk.Label(self.master, text='Welcome to the Language Learning App!')
        self.label.pack()

        self.upload_button = tk.Button(self.master, text='Upload Image', command=self.upload_image)
        self.upload_button.pack()

        self.process_button = tk.Button(self.master, text='Process Code', command=self.process_code)
        self.process_button.pack()

        self.image_label = tk.Label(self.master)
        self.image_label.pack()

    def upload_image(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            img = Image.open(file_path)
            img = img.resize((250, 250), Image.ANTIALIAS)
            self.photo = ImageTk.PhotoImage(img)
            self.image_label.config(image=self.photo)
            self.image_label.image = self.photo

    def process_code(self):
        code = 'x = [1, 2, 3]\nprint(x)'
        tree = ast.parse(code)
        print(ast.dump(tree))  # Prints the code structure
        bytecode = dis.Bytecode(tree)
        for instruction in bytecode:
            print(instruction)

if __name__ == '__main__':
    root = tk.Tk()
    app = LanguageLearningApp(root)
    root.mainloop()