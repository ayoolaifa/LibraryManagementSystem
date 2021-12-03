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


def genre_list(book_id):
    f = open("database.txt", "r")
    genre = ""
    book_list = []
    genre_list = []
    duplicate = ""
    for position, line in enumerate(f):
        if position == int(book_id) - 1:
            required_book_list = line.split(" | ")
            genre = required_book_list[1]
            book_list.append(line)
            duplicate = required_book_list[2]
        else:
            book_list.append(line)
    for i in book_list:
        f = i.split(" | ")
        f = [x.replace('\n', '') for x in f]
        if str(f[1]) == genre and f[2] != duplicate and f[5] == '0':
            line_appended = f[0] + " | " + f[1] + " | " + f[2] + " | " + f[3] + " | " + f[4] + " | " + f[5]
            genre_list.append(line_appended)
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
    f.write(function + " | " + str(date) + " | " + str(member_id) + " | " + str(book_id) + "\n")
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

print(genre_list(12))
