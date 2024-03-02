# a user interface for the web scraping program


import time
import customtkinter
from customtkinter import filedialog
from tkinter import *
import Web_Scraper_for_gui
import tkinter
from tkinter import messagebox
from icecream import ic



customtkinter.set_appearance_mode('light')
customtkinter.set_default_color_theme("blue")

root = customtkinter.CTk()
root.title('Web_Scraper')
root.geometry("600x400")
root.iconbitmap(r'Scraper.ico')
root.resizable(width=False, height=False)

global tab_frame
global file_dir
global animal_frame
dir_box = customtkinter.CTkTextbox
mode = 'light'


def change(choice):
    choice = choice.split()[0]
    customtkinter.set_appearance_mode(choice)


def to_category():
    global dog_radio_var
    global cat_radio_var
    global bird_radio_var
    global small_radio_var
    radio_variable = [dog_radio_var.get(), cat_radio_var.get(), bird_radio_var.get(), small_radio_var.get()]
    global category
    temp = ['Dogs', 'Cats', 'Birds', 'Small Animals']
    global animal
    category = ''
    counter = 0
    radio = 0

    while radio < len(radio_variable):
        if radio_variable[radio] != 'other':
            counter += 1
            category = radio_variable[radio].capitalize()
            animal = temp[radio]
        radio += 1
    if counter != 1:
        err_animal()

    global animal_frame
    # switch frame and button
    frame3.forget()
    next_button.forget()
    global next_button2
    global next_button3
    next_button2 = customtkinter.CTkButton(frame4, text="Next", command=to_scrap)
    next_button2.pack(side='bottom', padx=5, pady=15)
    next_button3 = customtkinter.CTkButton(frame4, text="Home", command=home)
    next_button3.pack(side='bottom', padx=5, pady=15)

    # main frame
    animal_frame = customtkinter.CTkFrame(bottom_frame, width=400, height=300, corner_radius=0)
    animal_frame.pack(side="left", fill="both", expand=True)
    # label animal
    animal_label = customtkinter.CTkLabel(animal_frame, text=animal, corner_radius=0,
                      font=('Arial', 30, 'bold'))
    animal_label.pack(pady=20)
    # label category
    category_label = customtkinter.CTkLabel(animal_frame, text=f'Category: {category}', corner_radius=0,
                      font=('Arial', 20, 'bold'))
    category_label.pack()
    # directory
    global dir_box
    dir_box = customtkinter.CTkTextbox(animal_frame, height=20, width=300, activate_scrollbars=True, wrap='char')
    dir_box.pack(expand=True, side='top')
    dir_button = customtkinter.CTkButton(animal_frame, width=100, text="Select File Path", corner_radius=5, command=save_path, anchor='n')
    # dir_button.pack(side='top', pady=70, expand=True)
    dir_button.place(x=207, y=260, anchor='center')




def to_scrap():
    global dog_radio_var
    global cat_radio_var
    global bird_radio_var
    global small_radio_var
    global animal_frame
    global animal
    global category
    global file_dir
    animal_frame.forget()
#     new frame
#
    # main frame
    animal_frame = customtkinter.CTkFrame(bottom_frame, width=400, height=300, corner_radius=0)
    animal_frame.pack(side="left", fill="both", expand=True)
    # label animal
    animal_label = customtkinter.CTkLabel(animal_frame, text=f'Scrapping: {animal} {category}\n', corner_radius=0,
                                          font=('Arial', 14, 'bold'))
    animal_label.pack(pady=20)
    # label category
    products_done_label = customtkinter.CTkLabel(animal_frame, text=f'Products done: \n', corner_radius=0,
                                            font=('Arial', 15, 'bold'))
    products_done_label.pack()

    pages_done_label = customtkinter.CTkLabel(animal_frame, text=f'Pages done: ', corner_radius=0,
                                            font=('Arial', 15, 'bold'))
    pages_done_label.pack()


    next_button2.forget()
    next_button3.forget()
    next_button4 = customtkinter.CTkButton(frame4, text="Home", command=home)
    next_button4.pack(side='bottom', padx=5, pady=15)

    process(animal, category, file_dir, pages_done_label, products_done_label)



def process(animal, category, file_dir, pages_done_label, products_done_label):
    url = 'https://aleef.com/en/collections/' + (Web_Scraper_for_gui.section(animal, category))
    Web_Scraper_for_gui.scrap(url, animal, fr'{file_dir}', category)

    products_done_label.configure(f'Products Done: {Web_Scraper_for_gui.products_done}')
    pages_done_label.configure(f'Pages Done: {Web_Scraper_for_gui.pages_done}')


def err_animal():
    # message box
    win = Tk()
    win.eval('tk::PlaceWindow %s center' % win.winfo_toplevel())
    win.withdraw()

    messagebox.showerror('Error', 'Please select one category (max 1)')
    win.deiconify()
    win.destroy()
    win.quit()
    home()


def home():
    top_frame.forget()
    bottom_frame.forget()
    main_window()


def save_path():
    global dir_box
    global file_dir
    file_dir = filedialog.askdirectory()
    dir_box.delete('0.0', 'end')
    dir_box.insert('end', file_dir)


def main_window():
# main window
    # top frame
    sections = ['Food', 'Health & Beauty', 'Toys', 'Food Supplies', 'Treats & Supplements', 'Accesories', 'Beds & Carriers', 'Training and Cleaning',
                'Scrapers', 'Sand & its Accessories', 'Cages & Accessories', 'Reptiles']
    global top_frame
    top_frame = customtkinter.CTkFrame(root, height=100)
    top_frame.pack(side="top", fill="x", expand=False)
    # bottom frame
    global bottom_frame
    bottom_frame = customtkinter.CTkFrame(root, height=300)
    bottom_frame.pack(side="bottom", fill="both", expand=True)
    # header top left
    frame1 = customtkinter.CTkFrame(top_frame, width=450, height=100, corner_radius=0)
    frame1.pack(side="left", fill="x", expand=True)
    # bottom left
    global frame3
    frame3 = customtkinter.CTkFrame(bottom_frame, width=400, height=300, corner_radius=0)
    frame3.pack(side="left", fill="both", expand=True)
    # bottom right
    global frame4
    frame4 = customtkinter.CTkFrame(bottom_frame, fg_color='light blue', width=50, height=270, corner_radius=16)
    frame4.pack(side="right", fill="both", expand=False)
    # header
    head = customtkinter.CTkLabel(frame1, text="Web_Scraper", font=("Bebas neue", 30), width=450, anchor='w')
    head.pack(padx=10, side="left", fill="both", expand=True)
    # mode option
    modes = ['Light Mode', 'Dark Mode']
    mode_option = customtkinter.CTkOptionMenu(frame1, values=modes, command=change)
    mode_option.pack(pady=25, padx=7, fill='x', side='left')
    # credits
    credits = customtkinter.CTkLabel(frame4, text="Credits: ", font=('Bebas Neue', 15), text_color=('black', 'white'))
    credits.pack(side='top')
    credits2 = customtkinter.CTkLabel(frame4, text="This App was developed by Loai Hataba\n",font=('Helvetica', 10), text_color=('black', 'white'), anchor='s', width=75)
    credits2.pack(side='top')
    credits3 = customtkinter.CTkLabel(frame4, text="Contact me: ", font=('Bebas Neue', 15), text_color=('black', 'white'), anchor='s')
    credits3.pack(side='top')
    credits4 = customtkinter.CTkLabel(frame4, text="Email: Loaiwleed2005@hotmail.com\n\n"
                                                   "Linkedin: www.linkedin.com/in/loaihataba",
            font=('Helvetica', 10), text_color=('black', 'white'))
    credits4.pack(side='top')
    # next button
    global next_button
    next_button = customtkinter.CTkButton(frame4, text="Next", command=to_category)
    next_button.pack(side='bottom', padx=5, pady=15)
    # label animals
    font = customtkinter.CTkFont(family="Bebas neue", underline=True, weight="bold", size=25)
    animal_label = customtkinter.CTkLabel(frame3, text="Choose an animal:", font=font)
    animal_label.pack(side='top', fill='both', expand=True)
    # tab view
    global tab_frame
    tab_frame = customtkinter.CTkTabview(frame3, width=300, height=300)
    tab_frame.pack(pady=15, padx=10, fill='both', expand=True)
    # tabs
    # dogs
    tab_dog = tab_frame.add('Dogs')
    # next_dog.pack()
    dog_frame = customtkinter.CTkScrollableFrame(tab_dog)
    dog_frame.pack(pady=20, padx=10, fill='both', expand=True)


    # radio buttons
    # dog radio
    global dog_radio_var
    dog_radio_var = customtkinter.StringVar(value='other')

    rad1 = customtkinter.CTkRadioButton(dog_frame, text=sections[0], value=sections[0].lower(), variable=dog_radio_var, radiobutton_width=20, radiobutton_height=20)
    rad1.pack(pady=10, padx=60, fill='both', expand=True)

    rad2 = customtkinter.CTkRadioButton(dog_frame, text=sections[1], value=sections[1].lower(), variable=dog_radio_var, radiobutton_width=20, radiobutton_height=20)
    rad2.pack(pady=10, padx=60, fill='both', expand=True)

    rad3 = customtkinter.CTkRadioButton(dog_frame, text=sections[2], value=sections[2].lower(), variable=dog_radio_var, radiobutton_width=20, radiobutton_height=20)
    rad3.pack(pady=10, padx=60, fill='both', expand=True)

    rad4 = customtkinter.CTkRadioButton(dog_frame, text=sections[3], value=sections[3].lower(), variable=dog_radio_var, radiobutton_width=20, radiobutton_height=20)
    rad4.pack(pady=10, padx=60, fill='both', expand=True)

    rad5 = customtkinter.CTkRadioButton(dog_frame, text=sections[4], value=sections[4].lower(), variable=dog_radio_var, radiobutton_width=20, radiobutton_height=20)
    rad5.pack(pady=10, padx=60, fill='both', expand=True)

    rad6 = customtkinter.CTkRadioButton(dog_frame, text=sections[5], value=sections[5].lower(), variable=dog_radio_var, radiobutton_width=20, radiobutton_height=20)
    rad6.pack(pady=10, padx=60, fill='both', expand=True)

    rad7 = customtkinter.CTkRadioButton(dog_frame, text=sections[6], value=sections[6].lower(), variable=dog_radio_var, radiobutton_width=20, radiobutton_height=20)
    rad7.pack(pady=10, padx=60, fill='both', expand=True)

    rad8 = customtkinter.CTkRadioButton(dog_frame, text=sections[7], value=sections[7].lower(), variable=dog_radio_var, radiobutton_width=20, radiobutton_height=20)
    rad8.pack(pady=10, padx=60, fill='both', expand=True)


    # cats
    tab_cat = tab_frame.add('Cats')
    cat_frame = customtkinter.CTkScrollableFrame(tab_cat)
    cat_frame.pack(pady=20, padx=10, fill='both', expand=True)
    # radio buttons
    global cat_radio_var
    cat_radio_var = customtkinter.StringVar(value='other')


    rad1 = customtkinter.CTkRadioButton(cat_frame, text=sections[0], value=sections[0].lower(), variable=cat_radio_var, radiobutton_width=20, radiobutton_height=20)
    rad1.pack(pady=10, padx=60, fill='both', expand=True)

    rad2 = customtkinter.CTkRadioButton(cat_frame, text=sections[1], value=sections[1].lower(), variable=cat_radio_var, radiobutton_width=20, radiobutton_height=20)
    rad2.pack(pady=10, padx=60, fill='both', expand=True)

    rad3 = customtkinter.CTkRadioButton(cat_frame, text=sections[2], value=sections[2].lower(), variable=cat_radio_var, radiobutton_width=20, radiobutton_height=20)
    rad3.pack(pady=10, padx=60, fill='both', expand=True)

    rad4 = customtkinter.CTkRadioButton(cat_frame, text=sections[3], value=sections[3].lower(), variable=cat_radio_var, radiobutton_width=20, radiobutton_height=20)
    rad4.pack(pady=10, padx=60, fill='both', expand=True)

    rad5 = customtkinter.CTkRadioButton(cat_frame, text=sections[4], value=sections[4].lower(), variable=cat_radio_var, radiobutton_width=20, radiobutton_height=20)
    rad5.pack(pady=10, padx=60, fill='both', expand=True)

    rad6 = customtkinter.CTkRadioButton(cat_frame, text=sections[5], value=sections[5].lower(), variable=cat_radio_var, radiobutton_width=20, radiobutton_height=20)
    rad6.pack(pady=10, padx=60, fill='both', expand=True)

    rad7 = customtkinter.CTkRadioButton(cat_frame, text=sections[6], value=sections[6].lower(), variable=cat_radio_var, radiobutton_width=20, radiobutton_height=20)
    rad7.pack(pady=10, padx=60, fill='both', expand=True)

    rad8 = customtkinter.CTkRadioButton(cat_frame, text=sections[7], value=sections[7].lower(), variable=cat_radio_var, radiobutton_width=20, radiobutton_height=20)
    rad8.pack(pady=10, padx=60, fill='both', expand=True)

    rad9 = customtkinter.CTkRadioButton(cat_frame, text=sections[8], value=sections[8].lower(), variable=cat_radio_var, radiobutton_width=20, radiobutton_height=20)
    rad9.pack(pady=10, padx=60, fill='both', expand=True)

    rad10 = customtkinter.CTkRadioButton(cat_frame, text=sections[9], value=sections[9].lower(), variable=cat_radio_var, radiobutton_width=20, radiobutton_height=20)
    rad10.pack(pady=10, padx=60, fill='both', expand=True)



    # bird
    tab_bird = tab_frame.add('Birds')
    bird_frame = customtkinter.CTkScrollableFrame(tab_bird)
    bird_frame.pack(pady=20, padx=10, fill='both', expand=True)
    global bird_radio_var
    bird_radio_var = customtkinter.StringVar(value='other')

    rad1 = customtkinter.CTkRadioButton(bird_frame, text=sections[0], value=sections[0].lower(), variable=bird_radio_var, radiobutton_width=20, radiobutton_height=20)
    rad1.pack(pady=10, padx=60, fill='both', expand=True)

    rad2 = customtkinter.CTkRadioButton(bird_frame, text=sections[1], value=sections[1].lower(), variable=bird_radio_var, radiobutton_width=20, radiobutton_height=20)
    rad2.pack(pady=10, padx=60, fill='both', expand=True)

    rad3 = customtkinter.CTkRadioButton(bird_frame, text=sections[2], value=sections[2].lower(), variable=bird_radio_var, radiobutton_width=20, radiobutton_height=20)
    rad3.pack(pady=10, padx=60, fill='both', expand=True)

    rad4 = customtkinter.CTkRadioButton(bird_frame, text=sections[10], value=sections[10].lower(), variable=bird_radio_var, radiobutton_width=20, radiobutton_height=20)
    rad4.pack(pady=10, padx=60, fill='both', expand=True)

    # small animals
    tab_small = tab_frame.add('Small Animals')
    small_frame = customtkinter.CTkScrollableFrame(tab_small)
    small_frame.pack(pady=20, padx=10, fill='both', expand=True)
    global small_radio_var
    small_radio_var = customtkinter.StringVar(value='other')

    rad1 = customtkinter.CTkRadioButton(small_frame, text=sections[0], value=sections[0].lower(), variable=small_radio_var, radiobutton_width=20, radiobutton_height=20)
    rad1.pack(pady=10, padx=60, fill='both', expand=True)

    rad2 = customtkinter.CTkRadioButton(small_frame, text=sections[1], value=sections[1].lower(), variable=small_radio_var, radiobutton_width=20, radiobutton_height=20)
    rad2.pack(pady=10, padx=60, fill='both', expand=True)

    rad3 = customtkinter.CTkRadioButton(small_frame, text=sections[2], value=sections[2].lower(), variable=small_radio_var, radiobutton_width=20, radiobutton_height=20)
    rad3.pack(pady=10, padx=60, fill='both', expand=True)

    rad4 = customtkinter.CTkRadioButton(small_frame, text=sections[10], value=sections[10].lower(), variable=small_radio_var, radiobutton_width=20, radiobutton_height=20)
    rad4.pack(pady=10, padx=60, fill='both', expand=True)

    rad5 = customtkinter.CTkRadioButton(small_frame, text=sections[11], value=sections[11].lower(), variable=small_radio_var, radiobutton_width=20, radiobutton_height=20)
    rad5.pack(pady=10, padx=60, fill='both', expand=True)

    root.mainloop()





main_window()
