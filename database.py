def line_count():
    f = open("database.txt", "r")
    Count = 1
    for line in f:
        Count += 1
    return Count


def file_to_text():
    list_of_books = []
    new_list_of_books = []
    f = open("database.txt", "r")
    for l in f:
        list_of_books = list_of_books + l.split("\n")
    f.close()
    for i in list_of_books:
        if i != "":
            new_list_of_books.append(i)
    return new_list_of_books


def write_to_file(list_of_books):
    f = open("database.txt", "w")
    string_of_books = ""
    for i in list_of_books:
        string_of_books += i + "\n"
    f.write(string_of_books)
    f.close()


def write_to_log_file(function, date, member_id, book_id):
    f = open("logfile.txt", "w")
    for i in f:
            f.write(i)
    f.write(function + "\n" + date + "\n" + member_id + "\n" + book_id + "\n" + "---------------")
    f.close()
