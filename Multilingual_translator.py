from tkinter import *
import tkinter as tk
from tkinter import ttk
from googletrans import Translator,LANGUAGES
from tkinter import messagebox
from tkinter import PhotoImage
root = tk.Tk()
# Create a PhotoImage from the image file
img_path = PhotoImage(file=r"C:\Users\hi\Downloads\map2 (1).png")
# Create a canvas to place the background image
canvas = Canvas(root, width=root.winfo_screenwidth(), height=root.winfo_screenheight())
canvas.pack(fill="both",expand=True)
# Place the background image on the canvas
canvas.create_image(0, 0, anchor="nw", image=img_path)
# Title for GUI display
root.title('Language Translator')
# Maximize the window
root.state('zoomed')
# Create a grid layout
root.grid_rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)
# Title dimensions
#set background color to an empty string(it uses default background color)
frame1 = Frame(canvas, width=root.winfo_screenwidth(), height=root.winfo_screenheight(), bg='')
frame1.place(relx=0.5, rely=0.5, anchor="center")
Label(frame1, text='Language Translator', font=("helvetica", 24)).grid(row=0, column=1, columnspan=2, pady=10)
# Function to translate text to multiple languages
def translate_text(text, target_languages):
    translator = Translator()
    translations = {}
    for lang_code in target_languages:
        try:
            output = translator.translate(text, dest=lang_code)
            translations[lang_code] = output.text
        except ValueError as e:
            translations[lang_code] = f"Error: {e}"
    return translations
# Function to display translations
def display_translations(translations):
    text_output.delete(1.0, 'end')
    for lang_code, translation in translations.items():
        text_output.insert('end', f'{lang_code}: {translation}\n')
# Translate button click event
def translate():
    lang_in = text_input.get("1.0", "end-1c")
    selected_languages = listbox.curselection()
    if not lang_in:
        messagebox.showerror('Language Translator', 'Enter text to translate')
    elif not selected_languages:
        messagebox.showerror('Language Translator', 'Select at least one language')
    else:
        selected_languages = [listbox.get(i) for i in selected_languages]
        translations = translate_text(lang_in, selected_languages)
        display_translations(translations)
        translator=Translator()
        detected_language = translator.detect(lang_in).lang
        detected_language_name = LANGUAGES[detected_language].title()
        # Print the selected input language in the label
        selected_lang_label.config(text=f"Selected Input Language: {detected_language_name}")
# Clear button click event
def clear():
    text_input.delete(1.0, 'end')
    text_output.delete(1.0, 'end')
# Function to update the auto-selected language
def update_auto_selected_language(selected_languages):
    if selected_languages:
        auto_select.set(selected_languages[0])
#auto-select button
a = tk.StringVar()
auto_select = ttk.Combobox(frame1, width=20, textvariable=a, state='readonly', font=('arial', 15, 'bold'))
auto_select['values'] = ('Auto Select',)
auto_select.grid(row=1, column=1, padx=10, pady=10)
# List of languages for the Listbox
languages = [
    'Afrikaans','Albanian','Amharic','Arabic','Armenian','Azerbaijani','Basque','Belarusian','Bengali',
    'Bosnian','Bulgarian','Catalan','Cebuano','chichewa','Chinese','Corsican','Croatian','Czech','Danish','Dutch',
    'English','Esperanto','Estonian','Filipino','Finnish','French','Frisian','Galician','Georgian',
    'German','Greek','Gujarati','Haitian creole','Hausa','Hawaiian','Hebrew','Hindi','Hmong','Hungarian',
    'Icelandic','Igbo','Indonesian','Irish','Italian','Japanese','Kannada','Kazakh','Khmer','Korean',
    'Kurdish','Kyrgyz','Lao','Latin','Latvian','Lithuanian','Luxembourgish','Macedonian','Malagasy',
    'Malay','Malayalam','Maltese','Maori','Marathi','Mongolian','Myanmar (Burmese)','Nepali','Norwegian',
    'Odia (Oriya)','Pashto','Persian','Polish','Portuguese (Portugal, Brazil)','Punjabi','Romanian',
    'Russian','Samoan','Scots Gaelic','Serbian','Sesotho','Shona','Sindhi','Sinhala (Sinhalese)','Slovak',
    'Slovenian','Somali','Spanish','Sundanese','Swahili','Swedish','Tajik','Tamil','Telugu','Thai','Turkish',
    'Ukrainian','Urdu','Uyghur','Uzbek','Vietnamese','Welsh','Xhosa','Yiddish','Yoruba','Zulu'
]
text_box={ 
    'font':('arial',15),
    'borderwidth':0,
    'highlightbackground':'black',
    'highlightthickness': 2
}
# Input text
text_input = Text(frame1, width=30, height=10, **text_box)
text_input.grid(row=2, column=0, columnspan=2, padx=10, pady=10,sticky="ew")
# Output text
text_output = Text(frame1, width=35, height=10,**text_box)
text_output.grid(row=2, column=2, columnspan=2, padx=10, pady=10,sticky="ew")
# Languages Listbox
listbox = Listbox(frame1, selectmode=tk.MULTIPLE, font=('arial',12, 'bold'))
for i, lang in enumerate(languages):
    listbox.insert(i, lang)
listbox.grid(row=1, column=2, columnspan=4, padx=10, pady=10,sticky="ew")
# Style for the buttons
button_style = {
    'font': ('arial', 15, 'bold'),
    'borderwidth':0,
    'highlightbackground': '#17202A',
    'highlightthickness': 4
}
# Translate button
btn_in = Button(frame1, command=translate, text="Translate", **button_style)
btn_in.grid(row=4, column=1, padx=10, pady=10)
# Clear button
btn_op = Button(frame1, command=clear, text="Clear", **button_style)
btn_op.grid(row=4, column=2, padx=10, pady=10)
#name text
name = Label(root, text="SIRI \n bs22eeb0b49@student.nitw.ac.in", font=("helvetica",10), borderwidth=5)
name.place(relx=1.0, rely=1.0, anchor='se')
#selected language label
selected_lang_label =Label(frame1, text='Selected Language:', font=("arial", 12, "bold"))
selected_lang_label.grid(row=5, column=0, columnspan=2,pady=10)
root.mainloop()