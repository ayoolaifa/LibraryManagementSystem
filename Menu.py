# Name: Ayokanmi Olaifa #
# Student No: F126075 #
# Date: 16 November 2021 #
# Introduction To Programming Course Work #
# Library Management System

from tkinter import *
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

import bookcheckout
import bookrecommend
import booksearch
import bookreturn
import database


window = Tk()

def book_id_validation(book_id):
    checkout_error_box.config(text="", bg='white')
    return_error_box.config(text="", bg='white')
    book_in_library = True
    num_of_line = database.line_count()
    if int(book_id) >= num_of_line:
           book_in_library = False
    return  book_in_library

def member_id_validation(member_id):
    checkout_error_box.config(text="", bg='white')
    return_error_box.config(text="", bg='white')
    valid_member = True
    if len(member_id) != 4:
       valid_member = False
    return  valid_member

def searchsubmit():
    search_list_box.delete(0,END)
    search = book_title.get()
    if(search==""):
        search_list_box.insert(0,"Please input a book title")
    else:
        Results = booksearch.search(search)
        book_title.set("")
        search_show_books.config(text=search_list_box.get(ANCHOR))
        if(Results == []):
            search_list_box.insert(0,"This book is not in the library")
        else:
            search_list_box.insert(0,"Book ID | Genre | Title | Author | Purchased Date | Member ID |" )
            for i in range(0, len(Results)):
                search_list_box.insert(i+1, Results[i])

def checkoutsubmit():
    checkout_error_box.config(text="", bg='white')
    return_error_box.config(text="", bg='white')
    book_id_text = book_id_1.get()
    member_id_text = member_id_1.get()
    if book_id_text == "":
        book_id_1.set("")
        member_id_1.set("")

        checkout_error_box["text"] = ("Enter Book ID")
        checkout_error_box.config(bg='red')

    elif member_id_text == "":
        checkout_error_box["text"] = ("Enter Member ID")
        checkout_error_box.config(bg='red')

        book_id_1.set("")
        member_id_1.set("")
    else:
        in_library = book_id_validation(book_id_text)
        valid_member = member_id_validation(member_id_text)

        book_id_1.set("")
        member_id_1.set("")

        if in_library and valid_member:
            Available = bookcheckout.checkout(int(book_id_text), member_id_text)
            if Available:
                checkout_error_box["text"] = ("Book Has Been Checked Out")
                checkout_error_box.config(bg='green')
            else:
                checkout_error_box["text"] = ("Book Is Not Available For Check Out")
                checkout_error_box.config(bg='red')
        elif in_library != True:
            checkout_error_box["text"] = ("Invalid Book ID")
            checkout_error_box.config(bg='red')
        elif valid_member != True:
            checkout_error_box["text"] = ("Invalid Member ID")
            checkout_error_box.config(bg='red')

    fig = plt.figure(figsize=(5.1,2.8))
    canvas = FigureCanvasTkAgg(fig, master=recommend_frame)
    canvas.get_tk_widget().place(x=13, y=230)

    tuple_list_of_books = database.num_of_occurences_in_log()
    book_id = []
    num_of_checkout = []

    print(tuple_list_of_books)
    for books in tuple_list_of_books:
        book_id.append(books[0])
        num_of_checkout.append(books[1])

def returnsubmit():
    checkout_error_box.config(text="", bg='white')
    return_error_box.config(text="", bg='white')
    return_book_id_text = book_id_2.get()
    if return_book_id_text == "":
        return_error_box["text"] = ("Enter Book ID")
        return_error_box.config(bg='red')
        book_id_2.set("")
    else:
        in_library = book_id_validation(return_book_id_text)
        if in_library:
            Returned = bookreturn.returnbook(int(return_book_id_text))
            book_id_2.set("")
            if Returned:
                return_error_box["text"] = ("Book has been returned")
                return_error_box.config(bg='green')

            else:
                return_error_box["text"] = ("Book has not been checked out by any member")
                return_error_box.config(bg='red')
        else:
            return_error_box["text"] = ("Invalid Book ID")
            return_error_box.config(bg='red')
            book_id_2.set("")

    fig = plt.figure(figsize=(5.1,2.8))
    canvas = FigureCanvasTkAgg(fig, master=recommend_frame)
    canvas.get_tk_widget().place(x=13, y=230)


    tuple_list_of_books = database.num_of_occurences_in_log()
    book_id = []
    num_of_checkout = []

    print(tuple_list_of_books)
    for books in tuple_list_of_books:
        book_id.append(books[0])
        num_of_checkout.append(books[1])

    ax1 = fig.add_subplot(1,1,1)
    ax1.bar(book_id,num_of_checkout, width=0.5)
    canvas.draw()


def recommendsubmit():
    recommend_list_box.delete(0,END)
    recommend_member_id = member_id_3.get()
    Results = bookrecommend.recommend(recommend_member_id)
    if Results != False:
        recommend_error_box.config(text=recommend_list_box.get(ANCHOR))
        for i in range(0, len(Results)):
            recommend_list_box.insert(i+1, Results[i])


        fig = plt.figure(figsize=(5.1,2.8))
        canvas = FigureCanvasTkAgg(fig, master=recommend_frame)
        canvas.get_tk_widget().place(x=13, y=230)

        tuple_list_of_books = database.num_of_occurences_in_log()
        book_id = []
        num_of_checkout = []

        for books in tuple_list_of_books:
            book_id.append(books[0])
            num_of_checkout.append(books[1])

        ax1 = fig.add_subplot(1,1,(1,16))
        ax1.bar(book_id,num_of_checkout, width=0.5)
        canvas.draw()
    else:
        recommend_error_box.config(text=recommend_list_box.get(ANCHOR))
        recommend_list_box.insert(0, "Member ID not found in log")




DarkPurple = "#310d67"
Pink = "#c41c6d"

window.title("Library Management System")
window.geometry('1100x700')

title = Label(text="Library Management System", width='600', height='1', fg='white', bg=DarkPurple, font=('Helvetica', 15), highlightbackground='black', highlightthickness =2)
title.pack()

# Search Region
search_frame = Frame(window, width='500', height='200', bg=Pink, highlightbackground='black', highlightthickness=2)
search_frame.place(x=16, y=42)

search_title = Label(search_frame, text='Book Search', width='55', height='1', bg=DarkPurple, fg='white', font=('Helvetica', 13))
search_title.place(x=0, y=0)

search_book_title = Label(search_frame, text='Book Title:', font=('calibre', 13), bg=Pink, fg='white')
search_book_title.place(x=40, y=40)

book_title = StringVar()
search_textbox = Entry(search_frame, font=('calibre', 11), fg='black', textvariable=book_title)
search_textbox.place(x=140, y=40)

search_submit_btn = Button(search_frame, text='Submit', width='10', font=('calibre', 11), fg='white', bg=DarkPurple, command=searchsubmit)
search_submit_btn.place(x=350, y=35)

search_list_box = Listbox(search_frame, width='52', height='5', font=('calibre', 12))

search_show_books = Label(search_frame, bg='white')
search_list_box.place(x=10, y=85)

# Check Region
checkout_frame = Frame(window, width='500', height='150', bg=Pink, highlightbackground='black', highlightthickness=2)
checkout_frame.place(x=16, y=260)

checkout_title = Label(checkout_frame, text='Book Checkout', width='55', height='1', bg=DarkPurple, fg='white', font=('Helvetica', 13))
checkout_title.place(x=0, y=0)

checkout_book_id = Label(checkout_frame, text='Book ID:', font=('calibre', 13), bg=Pink, fg='white')
checkout_book_id.place(x=40, y=40)

checkout_book_id = Label(checkout_frame, text='Member ID:', font=('calibre', 13), bg=Pink, fg='white')
checkout_book_id.place(x=40, y=70)

book_id_1=StringVar()
checkout_book_id_textbox = Entry(checkout_frame, font=('calibre', 11), fg='black', textvariable=book_id_1)
checkout_book_id_textbox.place(x=140, y=40)

member_id_1=StringVar()
checkout_member_id_textbox = Entry(checkout_frame, font=('calibre', 11), fg='black', textvariable=member_id_1)
checkout_member_id_textbox.place(x=140, y=70)

checkout_submit_btn = Button(checkout_frame, text='Submit', width='10', font=('calibre', 11), fg='white', bg=DarkPurple, command=checkoutsubmit)
checkout_submit_btn.place(x=350, y=53)

checkout_error_box = Label(checkout_frame, font=('calibre', 11), bg='white', width='52', height='2')
checkout_error_box.place(x=10, y=100)

#Return Region
return_frame = Frame(window, width='500', height='150', bg=Pink, highlightbackground='black', highlightthickness=2)
return_frame.place(x=16, y=430)

return_title = Label(return_frame, text='Book Return', width='55', height='1', bg=DarkPurple, fg='white', font=('Helvetica', 13))
return_title.place(x=0, y=0)

return_book_id = Label(return_frame, text='Book ID:', font=('calibre', 13), bg=Pink, fg='white')
return_book_id.place(x=40, y=40)

book_id_2=StringVar()
return_book_id_textbox = Entry(return_frame, font=('calibre', 11), fg='black', textvariable=book_id_2)
return_book_id_textbox.place(x=140, y=40)

return_submit_btn = Button(return_frame, text='Submit', width='10', font=('calibre', 11), fg='white', bg=DarkPurple, command=returnsubmit)
return_submit_btn.place(x=350, y=35)

return_error_box = Label(return_frame, font=('calibre', 11), bg='white', width='52', height='2')
return_error_box.place(x=10, y=90)

#Recommend Region
recommend_frame = Frame(window, width='540', height='538', bg=Pink, highlightbackground='black', highlightthickness=2)
recommend_frame.place(x=540, y=42)

recommend_title = Label(recommend_frame, text='Book Recommend', width='59', height='1', bg=DarkPurple, fg='white', font=('Helvetica', 13))
recommend_title.place(x=0, y=0)

recommend_member_id = Label(recommend_frame, text='Member ID:', font=('calibre', 13), bg=Pink, fg='white')
recommend_member_id.place(x=80, y=40)

member_id_3=StringVar()
return_member_id_textbox = Entry(recommend_frame, font=('calibre', 11), fg='black', textvariable=member_id_3)
return_member_id_textbox.place(x=180, y=40)

recommend_submit_btn = Button(recommend_frame, text='Submit', width='10', font=('calibre', 11), fg='white', bg=DarkPurple, command=recommendsubmit)
recommend_submit_btn.place(x=400, y=35)

recommend_list_box = Listbox(recommend_frame, width='84', height='8')
recommend_list_box.place(x=13, y=90)
recommend_error_box = Label(recommend_frame, font=('calibre', 11), bg='white')



#Check For Over 60 days
days_error_frame = Frame(window, width='850', height='97', bg=Pink, highlightbackground='black', highlightthickness=2)
days_error_frame.place(x=16, y=590)

days_error_title = Label(days_error_frame, text='Books Checkout Over 60 Days', width='94', height='1', bg=DarkPurple, fg='white', font=('Helvetica', 13))
days_error_title.place(x=0, y=0)

days_error_label = Label(days_error_frame, font=('calibre', 11), bg='white', width='92', height='3')
days_error_label.place(x=5, y=30)

#Quit Frame
quit_button_frame = Frame(window, width='200', height='77', bg=Pink, highlightbackground='black', highlightthickness=2)
quit_button_frame.place(x=880, y=600)

quit_button = Button(quit_button_frame, text='Quit', width='20', height='3', font=('calibre', 12), fg='white', bg=DarkPurple, command=window.destroy)
quit_button.place(x=2, y=2)
window.mainloop()

