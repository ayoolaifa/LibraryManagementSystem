# Name: Ayokanmi Olaifa #
# Student No: F126075 #
# Date: 16 November 2021 #
# Introduction To Programming Course Work #
# Library Management System

from tkinter import *

import bookcheckout
import booksearch
import bookreturn
window = Tk()

def book_id_validation():
     while True:
        book_id = int(input("Enter the book ID: "))
        num_of_line = database.line_count()
        if book_id >= num_of_line:
            print("Book ID is not present in Library")
        else:
            return book_id
            break

def member_id_validation():
    while True:
        member_id = input("Enter members ID: ")
        if len(member_id) != 4:
            print("Not correct ID")
        else:
            return member_id
            break

def searchsubmit():
    search_list_box.delete(0,END)
    search = book_title.get()
    if(search==""):
        search_list_box.insert(0,"Please input a book title")
    else:
        Results = booksearch.search(search)
        print(Results)
        book_title.set("")
        search_show_books.config(text=search_list_box.get(ANCHOR))
        if(Results == []):
            search_list_box.insert(0,"This book is not in the library")
        else:
            search_list_box.insert(0,"Book ID | Genre | Title | Author | Purchased Date | Member ID |" )
            for i in range(0, len(Results)):
                search_list_box.insert(i+1, Results[i])

def checkoutsubmit():
    book_id_text = book_id_1.get()
    member_id_text = member_id_1.get()
    Available = bookcheckout.checkout(int(book_id_text), member_id_text)
    book_id_1.set("")
    member_id_1.set("")
    if Available:
        checkout_error_box["text"] = ("Book has been checked out")
        checkout_error_box.config(bg='green')
    else:
        checkout_error_box["text"] = ("Book is already checked out by a member")
        checkout_error_box.config(bg='red')

def returnsubmit():
    return_book_id_text = book_id_2.get()
    Returned = bookreturn.returnbook(int(return_book_id_text))
    book_id_2.set("")
    if Returned:
        return_error_box["text"] = ("Book has been returned")
        return_error_box.config(bg='green')

    else:
        return_error_box["text"] = ("Book has not been checked out by any member")
        return_error_box.config(bg='red')

def recommendsubmit():
    search = member_id_3.get()
    recommend_error_box.config(text=recommend_list_box.get(ANCHOR))
    recommend_list_box.insert(0,"hello")


DarkPurple = "#310d67"
Pink = "#c41c6d"

window.title("Library Management System")
window.geometry('1100x600')

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

search_list_box = Listbox(search_frame, width='78', height='6')

search_show_books = Label(search_frame, bg='white')
search_list_box.place(x=10, y=90)

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
recommend_frame = Frame(window, width='540', height='537', bg=Pink, highlightbackground='black', highlightthickness=2)
recommend_frame.place(x='540', y='42')

recommend_title = Label(recommend_frame, text='Book Recommend', width='59', height='1', bg=DarkPurple, fg='white', font=('Helvetica', 13))
recommend_title.place(x=0, y=0)

recommend_member_id = Label(recommend_frame, text='Member ID:', font=('calibre', 13), bg=Pink, fg='white')
recommend_member_id.place(x=80, y=40)

member_id_3=StringVar()
return_member_id_textbox = Entry(recommend_frame, font=('calibre', 11), fg='black', textvariable=member_id_3)
return_member_id_textbox.place(x=180, y=40)

recommend_submit_btn = Button(recommend_frame, text='Submit', width='10', font=('calibre', 11), fg='white', bg=DarkPurple, command=recommendsubmit)
recommend_submit_btn.place(x=400, y=35)

recommend_list_box = Listbox(recommend_frame, width='84', height='15')

recommend_error_box = Label(recommend_frame, font=('calibre', 11), bg='white')
recommend_list_box.place(x=13, y=90)

window.mainloop()

