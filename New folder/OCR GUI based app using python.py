import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import filedialog
import pytesseract as tess
import webbrowser

tess.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'

app = tk.Tk()
app.geometry('800x600')
app.title('Get Text From Image :)')
app.maxsize(800, 600)

# Load the background image (provide the correct path)
bg_image = Image.open('Screenshot 2023-09-26 225202.png')
bg_photo = ImageTk.PhotoImage(bg_image)

# Create a label to display the background image
background_label = tk.Label(app, image=bg_photo)
background_label.place(relwidth=1, relheight=1)

# Creating a notebook (tabbed interface)
notebook = ttk.Notebook(app)
notebook.pack(fill='both', expand=True)

# Creating the "Text" tab
text_tab = ttk.Frame(notebook)
notebook.add(text_tab, text='Text')

# Creating the "Readme" tab
readme_tab = ttk.Frame(notebook)
notebook.add(readme_tab, text='Readme')

# Creating outer frame with a border for the Text tab
outer_frame_text = tk.Frame(text_tab, bg='light green', borderwidth=2, relief=tk.SOLID)
outer_frame_text.pack(padx=20, pady=20, fill='both')

# Creating inner frame for the Text tab
frame_text = tk.Frame(outer_frame_text, bg='white')
frame_text.pack(padx=20, pady=20, fill='both')

# Add text
txt = tk.Label(frame_text, text="Extract Text From Image", font=('GROUPE MEDIUM', 22))
txt.pack(pady=10)

# Load an image (provide the correct path)
img = Image.open('import-37-cutout.png')

# Define function to open image
def openImage():
    progressbar["value"] = 0
    progress_txt.place(x=470, y=246)  # Adjusted coordinates

    filename = filedialog.askopenfilename()
    img1 = Image.open(filename)
    get_txt = tess.image_to_string(img1)

    progressbar["value"] = 100

    txt_box.delete('1.0', tk.END)
    txt_box.insert('1.0', get_txt)
    app.title(filename)
    progress_txt.config(text='100%')  # Update progress_txt label to show 100%

# Add button for the Text tab to clear text
def clearText():
    txt_box.delete('1.0', tk.END)

btn_text = tk.Button(frame_text, text='Add Image', font=('Arial', 20), command=openImage, bg='#900C3F', fg='white')
btn_text.pack(padx=20, pady=20)

# Add Clear Text button
clear_text_btn = tk.Button(frame_text, text='Clear Text', font=('Arial', 20), command=clearText, bg='#FF5733', fg='white')
clear_text_btn.pack(padx=20, pady=20)

# Add ProgressBar for the Text tab using ttk.Progressbar
progressbar = ttk.Progressbar(frame_text, mode='determinate', orient='horizontal', length=200)
progressbar.pack()

# Add text for progressbar for the Text tab and move it beside the progress bar
progress_txt = tk.Label(frame_text, text="0%")
progress_txt.place(x=470, y=246)  # Adjusted coordinates

# Add TextBox for the Text tab
txt_box = tk.Text(frame_text, font=('Times New Roman', 18), width=52, height=15)
txt_box.pack(pady=20)

# Create a readme label at the bottom with formatted text
readme_text = """
Proudly made by ❤️Md Tahseen Raza
GitHub: https://github.com/mdtahseenraza (click to open in browser)
"""

# Function to open URL in the default web browser
def openURL(event):
    webbrowser.open_new('https://github.com/mdtahseenraza')

readme_label = tk.Label(readme_tab, text=readme_text, font=('Arial', 16), bg='red', justify=tk.LEFT)
readme_label.pack(side='top', fill='both', expand=True, padx=20, pady=20)
readme_label.bind("<Button-3>", openURL)    # Bind right-click event to open URL

app.mainloop()