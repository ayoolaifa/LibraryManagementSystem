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


def write_to_file(list_of_books):
    f = open("database.txt", "w")
    string_of_books = ""
    for i in list_of_books:
        string_of_books += i + "\n"
    f.write(string_of_books)
    f.close()


def write_to_log_file(function, date, member_id, book_id):
    f = open("logfile.txt", "a")
    f.write(function + "\n" + "Date: " + str(date) + "\n" + "Member ID: " + str(member_id) + "\n" + "Book ID: " + str(book_id) + "\n" + "---------------" + "\n")
    f.close()


def logfile_to_text():
    log_string = ""
    list_of_logs = []
    f = open("logfile.txt", "r")
    for l in f:
        list_of_logs += l.split("\n")
    for i in range(0, len(list_of_logs)):
        if list_of_logs[i] != '---------------':
            log_string += list_of_logs[i] + " "
        elif list_of_logs[i] == '---------------' and list_of_logs[i] != len(list_of_logs):
            list_of_logs[i] = "| "
            log_string += list_of_logs[i]
    new_list_of_logs = log_string.split(" | ")
    return new_list_of_logs


