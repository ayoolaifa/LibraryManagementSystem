import database
from datetime import date


def checkout(book_id, member_id):
    today = date.today()
    # dd/mm/YY
    d1 = today.strftime("%d/%m/%Y")
    available = False
    list_of_books = database.file_to_text()
    for i in range(0, len(list_of_books)):
        book_line_list = list_of_books[i].split(" | ")
        if book_line_list[0] == str(book_id) and book_line_list[5] == "0":
            available = True
            book_line_list[5] = member_id
            list_of_books.pop(i)
            line = ""
            for j in range(0, len(book_line_list)):
                if j == 0:
                    line += str(book_line_list[j])
                else:
                    line += " | " + str(book_line_list[j])
            list_of_books.insert(i, line)
            database.write_to_file(list_of_books)
            database.write_to_log_file("CHECKOUT", d1, member_id, book_id)
        elif int(book_line_list[0]) >= book_id:
            break

    return available
