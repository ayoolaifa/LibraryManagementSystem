from datetime import date

def line_count():
    f = open("database.txt", "r")
    Count = 1
    for _ in f:
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

def book_line_from_id(book_id):
    f = open("database.txt", "r")
    book_list = file_to_text()

    for position, line in enumerate(f):
        if position == int(book_id) - 1:
            required_book_list = line.split(" | ")
    f.close()
    for i in required_book_list:
        new_required_book_list = [x.replace('\n', '') for x in required_book_list]

    return new_required_book_list

def genre_list(book_id):
    f = open("database.txt", "r")
    genre = ""
    book_list = file_to_text()
    genre_list = []
    duplicate = ""

    for position, line in enumerate(f):
        if position == int(book_id) - 1:
            required_book_list = line.split(" | ")
            genre = required_book_list[1]
            duplicate_of_book_checkout = required_book_list[2]
    f.close()


    for i in book_list:
        f = i.split(" | ")
        f = [x.replace('\n', '') for x in f]

        if str(f[1]) == genre and f[2] != duplicate_of_book_checkout and f[5] == '0':
            line_appended = f[0] + " | " + f[1] + " | " + f[2] +\
                            " | " + f[3] + " | " + f[4] + " | " + f[5]
            genre_list.append(line_appended)
    for i in genre_list:
        genre_line_list = i.split( " | ")
    return genre_list

def write_to_file(list_of_books):
    f = open("database.txt", "w")
    string_of_books = ""
    for i in list_of_books:
        string_of_books += i + "\n"
    f.write(string_of_books)
    f.close()

def write_to_log_file(function, date, member_id, book_id):
    f = open("logfile.txt", "a")
    f.write(function + " | " + str(date) +
            " | " + str(member_id) + " | " + str(book_id) + "\n")
    f.close()

def logfile_to_text():
    list_of_logs = []
    new_list_of_logs = []
    f = open("logfile.txt", "r")
    for l in f:
        list_of_logs += l.split("\n")
    f.close()
    for i in list_of_logs:
        if i != "":
            new_list_of_logs.append(i)
    return new_list_of_logs

def over_60_days():
    logfile = logfile_to_text()
    database = file_to_text()
    today = date.today()
    checkout_dates = []

    for book_info in database:
        line = book_info.split(" | ")
        if line[5] != "0":
            for i in logfile:
                logfile_line = i.split(" | ")
                if logfile_line[2] == line[5] and logfile_line[3] == line[0]:
                    checkout_dates.append(logfile_line)

    books_over_60_days = []
    for k in checkout_dates:
        print(k , "2")
        for j in checkout_dates:
            print(j)
            if k[3] == j[3] and (k[0] == "CHECKOUT" and j[0] == "RETURN"):
                print("")
    else:
        books_over_60_days.append(k)

def num_of_occurences_in_log():
    tuple_list_of_books = []
    count_of_occurence = 0
    logfile = logfile_to_text()
    for i in range(1, 17):
        for line in logfile:
            single_log = line.split(" | ")
            if int(single_log[3]) == i and single_log[0] == "CHECKOUT":
                count_of_occurence += 1

        tuple_of_books = (i, count_of_occurence)
        count_of_occurence = 0
        tuple_list_of_books.append(tuple_of_books)
    return tuple_list_of_books

