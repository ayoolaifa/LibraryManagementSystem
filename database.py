from datetime import date

## funtion count the number of line in the database
def line_count():
    f = open("database.txt", "r")
    Count = 1
    for _ in f:
        Count += 1
    return Count

## Function to change database to a string ##
def file_to_text():
    list_of_books = []
    new_list_of_books = []
    file = open("database.txt", "r")
    for line in file:
        list_of_books = list_of_books + line.split("\n")
        ## removes the \n from every line and adds to list
    file.close()
    for book in list_of_books:
        ## remove entries that is not a book in database
        if book != "":
            new_list_of_books.append(book) ## appends to new list
    return new_list_of_books

## function get the book info from database from inputing book id ##
def book_line_from_id(book_id):
    file = open("database.txt", "r")
    book_list = file_to_text()

    required_book_list = []
## for loop with gets the book line if it is equal to the book id input
    for position, line in enumerate(file):
        if position == int(book_id) - 1:
            required_book_list = line.split(" | ")
    file.close()
    if required_book_list != []:
        for i in required_book_list:
            new_required_book_list = [x.replace('\n', '') ## removes \n from line
                                      for x in required_book_list]

        return new_required_book_list
    else:
        return False

## Functions makes a list of book which has same genre as book id inputted ##
def genre_list(book_id):
    file = open("database.txt", "r")
    genre = ""
    book_list = file_to_text()
    genre_list = []
    duplicate = ""

## for loop with gets the book line if it is equal to the book id input ##
## duplicates books are removed
    for position, line in enumerate(file):
        if position == int(book_id) - 1:
            required_book_list = line.split(" | ")
            genre = required_book_list[1] ## sets genre of book
            duplicate_of_book_checkout = required_book_list[2]
            ## sets a duplicate book
    file.close()

## book_list is all the book info in database
    for book in book_list:
        single_book = book.split(" | ")
        single_book = [x.replace('\n', '') for x in single_book] ## remove \n

## if statement check:
    ## the book has the same genre
    ## not duplicate book
    ## has not been checked out
        if str(single_book[1]) == genre \
                and single_book[2] != duplicate_of_book_checkout \
                and single_book[5] == '0':
            line_appended = single_book[0] + " | " + single_book[1] + " | " \
                            + single_book[2] + " | " + single_book[3] + " | " \
                            + single_book[4] + " | " + single_book[5]
            genre_list.append(line_appended) ## appends line to list

    ## remove the formatting in each book in the genre list
    for book_info in genre_list:
        genre_line_list = book_info.split(" | ")
    return genre_list

## Function writes to database ##
def write_to_file(list_of_books):
    file = open("database.txt", "w")
    string_of_books = ""
    for book in list_of_books:
        string_of_books += book + "\n" ## adds \n to each line
    file.write(string_of_books)
    file.close()

## Function appends to log file
def write_to_log_file(function, date, member_id, book_id):
    f = open("logfile.txt", "a")
    f.write(function + " | " + str(date) +
            " | " + str(member_id) + " | " + str(book_id) + "\n")
    f.close()

## converts logfile to text
def logfile_to_text():
    list_of_logs = []
    new_list_of_logs = []
    file = open("logfile.txt", "r")
    for line in file:
        list_of_logs += line.split("\n")
        ## removes the \n from every line and adds to list ##

    file.close()
    ## remove entries that is not a log line in file
    for log_line in list_of_logs:
        if log_line != "":
            new_list_of_logs.append(log_line) # appends to list
    return new_list_of_logs

## returns every book and the number of times they have been checked out ##
def num_of_occurences_in_log():
    tuple_list_of_books = []
    count_of_occurence = 0
    logfile = logfile_to_text()

## loops through every book id ##
    for i in range(1, 17):
        for line in logfile:
            single_log = line.split(" | ")
            ## checks id the book id is the same and the entry is a checkout ##
            if int(single_log[3]) == i and single_log[0] == "CHECKOUT":
                count_of_occurence += 1

        tuple_of_books = (i, count_of_occurence)
        ## adds book id and count to a tuple ##
        count_of_occurence = 0
        ## resets count ##
        tuple_list_of_books.append(tuple_of_books)
        ## appends tuple to a list
    return tuple_list_of_books

## TEST CODE ##
if __name__ == "__main__":
    print(num_of_occurences_in_log())
## OUTPUT = [(1, 3), (2, 6), (3, 3), (4, 3), (5, 1), (6, 2), (7, 1), (8, 2),
## (9, 2), (10, 2), (11, 1), (12, 3), (13, 1), (14, 2), (15, 4), (16, 3)]

    print(genre_list(10))
## OUTPUT = ['14 | Romance | Pride & Prejudice | Jane Austen | 01/09/2021 | 0']

    print(genre_list(20))
## OUTPUT = []

    print (book_line_from_id(8))
## OUTPUT =
## ['8', 'Action', 'Lord Of The Rings', 'J. R. Tolkien', '29/11/2005', 'fefa']

    print (book_line_from_id(17))
## OUTPUT = False ##

    print(file_to_text())
## OUTPUT = [list of books in database] ##

    print(line_count())
## OUTPUT = 17 ##

    print(logfile_to_text())
## OUTPUT = the entire Log file in a list
