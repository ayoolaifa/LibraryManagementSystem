import database
from datetime import date


def checkout(book_id, member_id):
    today = date.today()
    # dd/mm/YY
    d1 = today.strftime("%d/%m/%Y")
    available = False
    list_of_books = database.file_to_text()

## for loop for each line in database
    for line in range(0, len(list_of_books)):
        book_line_list = list_of_books[line].split(" | ")

        ## checks if book id are the same and the book is not checked out
        if ((member_id != "") and len(member_id) == 4):
            if book_line_list[0] == str(book_id) and book_line_list[5] == "0":
                available = True
                book_line_list[5] = member_id ## changed book info with member id
                list_of_books.pop(line) ## removes list in the list of books
                new_line = ""

                ## reformats line to fit database format
                for element in range(0, len(book_line_list)):
                    if element == 0:
                        new_line += str(book_line_list[element])
                    else:
                        new_line += " | " + str(book_line_list[element])

                list_of_books.insert(line, new_line) ## adds new line to list
                database.write_to_file(list_of_books)
                ## rewrites the whole database with updated line

                database.write_to_log_file("CHECKOUT", d1, member_id, book_id)
                ## appends info to log file

            elif int(book_line_list[0]) >= book_id:
                break

    return available

## TEST CODE ##
if __name__ == "__main__":
    print(checkout(7, "coao"))
    ## OUTPUT = True ##
    print(checkout(16, ""))
    ## OUTPUT = False ##
    print(checkout(21, "afse"))
    ## OUTPUT = False ##
    print(checkout(3, "seff"))
    ## OUTPUT = False ##
    print(checkout(16, "hyrfg"))

