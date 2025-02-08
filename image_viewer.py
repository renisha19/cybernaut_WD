import os
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

class ImageViewer:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Viewer")

        self.image_list = []
        self.current_index = 0

        self.label = tk.Label(root, text="Select a folder to view images", font=("Arial", 14))
        self.label.pack(pady=10)

        self.canvas = tk.Label(root)
        self.canvas.pack()

        self.btn_frame = tk.Frame(root)
        self.btn_frame.pack(pady=10)

        self.prev_button = tk.Button(self.btn_frame, text="Previous", command=self.prev_image, state=tk.DISABLED)
        self.prev_button.pack(side=tk.LEFT, padx=5)

        self.next_button = tk.Button(self.btn_frame, text="Next", command=self.next_image, state=tk.DISABLED)
        self.next_button.pack(side=tk.LEFT, padx=5)

        self.exit_button = tk.Button(self.btn_frame, text="Exit", command=root.quit)
        self.exit_button.pack(side=tk.LEFT, padx=5)

        self.open_button = tk.Button(root, text="Open Folder", command=self.load_images)
        self.open_button.pack(pady=10)

    def load_images(self):
        folder_path = filedialog.askdirectory()
        if not folder_path:
            return

        supported_formats = (".jpg", ".jpeg", ".png", ".bmp")
        self.image_list = [os.path.join(folder_path, f) 
        for f in os.listdir(folder_path) if f.lower().endswith(supported_formats)]

        if not self.image_list:
            self.label.config(text="No images found in the selected folder")
            return

        self.current_index = 0
        self.show_image()
        self.update_buttons()

    def show_image(self):
        image_path = self.image_list[self.current_index]
        image = Image.open(image_path)
        image = image.resize((500, 400))  # ANTIALIAS is no longer needed

        self.img = ImageTk.PhotoImage(image)

        self.canvas.config(image=self.img)
        self.label.config(text=os.path.basename(image_path))

    def next_image(self):
        if self.current_index < len(self.image_list) - 1:
            self.current_index += 1
            self.show_image()
        self.update_buttons()

    def prev_image(self):
        if self.current_index > 0:
            self.current_index -= 1
            self.show_image()
        self.update_buttons()

    def update_buttons(self):
        self.prev_button.config(state=tk.NORMAL if self.current_index > 0 else tk.DISABLED)
        self.next_button.config(state=tk.NORMAL if self.current_index < len(self.image_list) - 1 else tk.DISABLED)

root = tk.Tk()
app = ImageViewer(root)
root.mainloop()
