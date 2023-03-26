import tkinter.ttk as ttk, customtkinter, csv, random as r, pandas as pd, os, shutil
from tkinter import *
from tkinter import filedialog
from faker import Faker

root = Tk()
root.title('Usersator')
width = 800
height = 400
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width/2) - (width/2)
y = (screen_height/4) - (height/4)
root.geometry("%dx%d+%d+%d" % (width, height, x, y))
root.resizable(0, 0)
customtkinter.set_appearance_mode("light")

#INITIATE FAKER MODULE
fake = Faker()

#DEFINE COLUMNS NAME
fieldnames = ('first_name', 'last_name', 'email', 'age', 'phone_number', 'city', 'state', 'zip_code', 'address','company')

def generate_users(event):
    clear_frame()
    nb_users = int(nb_user_field.get())

    with open(f'{os.getcwd()}/user_info.csv','w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()

        for i in range(nb_users):
            first_name = fake.first_name()
            last_name = fake.last_name()
            domain = fake.free_email_domain()
            email = f'{first_name}.{last_name}@{domain}'
            age = r.randint(19,62)
            phone_number = f'({r.randint(100,1000)}) {r.randint(100,1000)}-{r.randint(1000,10000)}'
            city = fake.city()
            state = fake.state()
            zip_code = fake.zipcode()
            address = fake.address()
            company = fake.company()
            writer.writerow({
                'first_name':first_name,
                'last_name':last_name,
                'email':email.lower(),
                'age': age,
                'phone_number':phone_number,
                'city':city,
                'state':state,
                'zip_code':zip_code,
                'address':address,
                'company':company
            })
    display_result()

def generate_users_mul(event):
    clear_frame()

    nb_users = int(nb_user_field.get())
    nb_ss = int(nb_ss_field.get())
    occ = 1
    file = 'users_info_mul.csv'
    file_raw = os.path.splitext(file)[0]
    file_ext = os.path.splitext(file)[1]
    
    while occ < nb_ss:

        with open(f'{file_raw}%s{file_ext}' % occ,'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()

            for i in range(nb_users):
                first_name = fake.first_name()
                last_name = fake.last_name()
                domain = fake.free_email_domain()
                email = f'{first_name}.{last_name}@{domain}'
                age = r.randint(19,62)
                phone_number = f'({r.randint(100,1000)}) {r.randint(100,1000)}-{r.randint(1000,10000)}'
                city = fake.city()
                state = fake.state()
                zip_code = fake.zipcode()
                address = fake.address()
                company = fake.company()
                writer.writerow({
                    'first_name':first_name,
                    'last_name':last_name,
                    'email':email.lower(),
                    'age': age,
                    'phone_number':phone_number,
                    'city':city,
                    'state':state,
                    'zip_code':zip_code,
                    'address':address,
                    'company':company
                })
        occ += 1

def display_result():

    table = Frame(frame_right_root, width=500)
    table.pack(side=TOP)
    scrollbarx = Scrollbar(table, orient=HORIZONTAL)
    scrollbary = Scrollbar(table, orient=VERTICAL)
    tree = ttk.Treeview(table, columns=fieldnames, height=300, selectmode="extended", yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
    scrollbary.config(command=tree.yview)
    scrollbary.pack(side=RIGHT, fill=Y)
    scrollbarx.config(command=tree.xview)
    scrollbarx.pack(side=BOTTOM, fill=X)

    tree.heading('first_name', text="First Name", anchor=W)
    tree.heading('last_name', text="Last Name", anchor=W)
    tree.heading('email', text="Email", anchor=W)
    tree.heading('age', text="Age", anchor=W)
    tree.heading('phone_number', text="Phone Number", anchor=W)
    tree.heading('city', text="City", anchor=W)
    tree.heading('state', text="State", anchor=W)
    tree.heading('zip_code', text="ZIP Code", anchor=W)
    tree.heading('address', text="Address", anchor=W)
    tree.heading('company', text="Company", anchor=W)

    tree.column('#0', stretch=NO, minwidth=0, width=0)
    tree.column('#1', stretch=NO, minwidth=20, width=120)
    tree.column('#2', stretch=NO, minwidth=20, width=120)
    tree.column('#3', stretch=NO, minwidth=20, width=240)
    tree.column('#4', stretch=NO, minwidth=20, width=50, anchor=CENTER)
    tree.column('#5', stretch=NO, minwidth=20, width=150, anchor=CENTER)
    tree.column('#6', stretch=NO, minwidth=20, width=150)
    tree.column('#7', stretch=NO, minwidth=20, width=120)
    tree.column('#8', stretch=NO, minwidth=20, width=80, anchor=CENTER)
    tree.column('#9', stretch=NO, minwidth=20, width=300)
    tree.column('#10', stretch=NO, minwidth=20, width=200)

    tree.pack()

    with open(f'{os.getcwd()}/user_info.csv') as f:
        reader = csv.DictReader(f, delimiter=',')
        for row in reader:
            firstname = row['first_name']
            lastname = row['last_name']
            email = row['email']
            age = row['age']
            phone_number = row['phone_number']
            city = row['city']
            state = row['state']
            zip_code = row['zip_code']
            address = row['address']
            company = row['company']
            tree.insert("", 0, values=(firstname, 
                                        lastname,
                                        email,
                                        age,
                                        phone_number,
                                        city,
                                        state,
                                        zip_code,
                                        address,
                                        company))

def clear_frame():
    for items in frame_right_root.winfo_children():
        items.destroy()    

def quit():
    dict_ext = {'spreadsheet':('.csv','.xls')}
    try:
        for file in os.listdir():
            if file.endswith(dict_ext['spreadsheet']):
                os.remove(file)
        root.destroy()
    except FileNotFoundError:
        root.destroy()

def onclose(event):
    quit()

def save_csv():
    csv_file = f'{os.getcwd()}/user_info.csv'
    path = filedialog.askdirectory()
    full_path = f'{path}/'
    shutil.copy(csv_file, full_path)

def save_xls():
    csv_file = f'{os.getcwd()}/user_info.csv'
    path = filedialog.askdirectory()
    full_path = f'{path}/'

    read_file = pd.read_csv(csv_file)
    read_file.to_excel(f'{full_path}%s.xls' % os.path.splitext(os.path.basename(csv_file))[0], index=None, header=True)

def save_csv_mul():
    path = filedialog.askdirectory()
    full_path = f'{path}/'
    
    for file in os.listdir():
        if file.endswith('.csv'):
            shutil.copy(os.path.join(os.getcwd(),file), full_path)

def save_xls_mul():
    path = filedialog.askdirectory()
    full_path = f'{path}/'

    for file in os.listdir():
        if file.endswith('.csv'):
            read_file = pd.read_csv(file)
            read_file.to_excel(f'{full_path}%s.xls' % file,index=None, header=True)

def on_entry_change(*args):
    if nb_ss_field.get():
        btn_save_csv_mul.configure(state=NORMAL)
        btn_save_xls_mul.configure(state=NORMAL)
    else:
        btn_save_csv_mul.configure(state=DISABLED)
        btn_save_xls_mul.configure(state=DISABLED)

def clean_users_field(event):
    nb_user_field.delete(0,END)

def clean_ss_field(event):
    nb_ss_field.delete(0,END)

#TKINTER INTERFACE --- LABEL FRAME, FRAME, ENTRY, LABEL, BUTTON ---   
frame_left_root = Frame(root, width=250, bg='#adacac')
frame_left_root.pack(fill=Y,side=LEFT)
frame_right_root = Frame(root, width=550)
frame_right_root.pack(side=RIGHT, fill=Y)

open_frame = LabelFrame(frame_left_root, text='Generate and Display Datas',fg='white', background='#adacac',bd=4)
open_frame.grid(row=0, column=0, padx=5,pady=5)

open_frame2 = LabelFrame(frame_left_root, text='Generate Multiple Spreadsheets',fg='white', background='#adacac',bd=4)
open_frame2.grid(row=1,column=0, padx=5,pady=5)


lbl_intro = customtkinter.CTkLabel(open_frame,
                                   text='Usersator generates fake user\n'
                                   'informations and stores them\n'
                                   'in spreadsheets.Write a number\n'
                                   'and type Enter to display\n'
                                   'the informations.',
                                   fg_color='#adacac',
                                   text_color='Black',
                                   justify='center',
                                   font=('Georgia',int(15.0)))
lbl_intro.grid(row=0,columnspan=2,padx=5,pady=5)

lbl_user_field = customtkinter.CTkLabel(open_frame,
                                        text='Number of Users',
                                        fg_color='#adacac',
                                        text_color='Red',
                                        justify='left',
                                        font=("Georgia", int(14.0)))
lbl_user_field.grid(row=1,column=0)

nb_user_field_var = IntVar()
nb_user_field = customtkinter.CTkEntry(open_frame,
                      border_width=1,
                      height=15,
                      corner_radius=5,
                      border_color='Black',
                      text_color='Black',
                      textvariable=nb_user_field_var,
                      width=80
                      )
nb_user_field.grid(row=1,column=1,padx=5,pady=5)

btn_save_csv = customtkinter.CTkButton(open_frame,
                                   text='Save as CSV',
                                   width=100,
                                   height=10,
                                   border_color='Black',
                                   border_width=2,
                                   fg_color='#84898a',
                                   hover_color='Black',
                                   command=save_csv
                                   )
btn_save_csv.grid(row=2,column=0,padx=5,pady=5)

btn_save_xls = customtkinter.CTkButton(open_frame,
                                   text='Save as XLS',
                                   width=100,
                                   height=10,
                                   border_color='Black',
                                   border_width=2,
                                   fg_color='#84898a',
                                   hover_color='Black',
                                   command=save_xls
                                   )
btn_save_xls.grid(row=2,column=1,padx=5,pady=5)

lbl_txt = customtkinter.CTkLabel(open_frame2,
                                   text='Write a number below\n'
                                   'to generate multiple\n'
                                   'speadsheets and press Enter\n'
                                   'to be able to save them.',
                                   fg_color='#adacac',
                                   text_color='Black',
                                   justify='center',
                                   font=('Georgia',int(15.0)))
lbl_txt.grid(row=0,columnspan=2, padx=5, pady=5)

nb_ss_field_var = IntVar()
nb_ss_field_var.trace('w', on_entry_change)
nb_ss_field = customtkinter.CTkEntry(open_frame2,
                      border_width=1,
                      height=15,
                      corner_radius=5,
                      border_color='Black',
                      text_color='Black',
                      width=80,
                      textvariable=nb_ss_field_var
                      )
nb_ss_field.grid(row=1,column=1,padx=5, pady=5)

lbl_gen_field = customtkinter.CTkLabel(open_frame2,
                                        text='Number of Files',
                                        fg_color='#adacac',
                                        text_color='Red',
                                        justify='left',
                                        font=("Georgia", int(14.0)))
lbl_gen_field.grid(row=1,column=0, padx=5, pady=5)

btn_save_csv_mul = customtkinter.CTkButton(open_frame2,
                                   text='Save ... as CSV',
                                   width=100,
                                   height=10,
                                   border_color='Black',
                                   border_width=2,
                                   fg_color='#84898a',
                                   hover_color='Black',
                                   state=DISABLED,
                                   command=save_csv_mul
                                   )
btn_save_csv_mul.grid(row=2, column=0, padx=9, pady=5)

btn_save_xls_mul = customtkinter.CTkButton(open_frame2,
                                   text='Save ... as XLS',
                                   width=100,
                                   height=10,
                                   border_color='Black',
                                   border_width=2,
                                   fg_color='#84898a',
                                   hover_color='Black',
                                   state=DISABLED,
                                   command=save_xls_mul
                                   )
btn_save_xls_mul.grid(row=2, column=1, padx=5, pady=5)

btn_quit = customtkinter.CTkButton(frame_left_root,
                                   text='Quit',
                                   width=60,
                                   height=5,
                                   border_color='Black',
                                   border_width=2,
                                   fg_color='#84898a',
                                   hover_color='Black',
                                   command=quit
                                   )
btn_quit.place(x=18,y=373)

nb_user_field.bind('<Return>', generate_users)
nb_user_field.bind('<FocusIn>', clean_users_field)
nb_ss_field.bind('<Return>', generate_users_mul)
nb_ss_field.bind('<FocusIn>', clean_ss_field)

root.protocol('WM_DELETE_WINDOW', lambda: onclose(root))
root.mainloop()
