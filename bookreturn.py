import database
from datetime import date

def returnbook(book_id):
    today = date.today()

    # dd/mm/YY
    d1 = today.strftime("%d/%m/%Y")
    Returned = False
    list_of_books = database.file_to_text()
## for loop for each line in database
    for line in range(0, len(list_of_books)):

        book_line_list = list_of_books[line].split(" | ")
        member_id = book_line_list[5]

## Check if book id equals the line of the book in database
        if book_line_list[0] == str(book_id):  
            if member_id != "0":  ## Check book is already checkout
                Returned = True
                book_line_list[5] = "0" ## Resets member ID
                
                list_of_books.pop(line) ## Removes line from list of books
                new_line = ""

                ## Creation of new line in correct format
                for element in range(0, len(book_line_list)):

                    if element == 0:
                        new_line += str(book_line_list[element])
                    else:
                        new_line += " | " + str(book_line_list[element])

                ## Insert new line where previous line was deleted
                list_of_books.insert(line, new_line)

                ## Writes whole database back to file
                database.write_to_file(list_of_books)

                ## Writes returned book to log file
                database.write_to_log_file("RETURN", d1, member_id , book_id)

        ## If book has been found then loop stops
        elif int(book_line_list[0]) >= book_id:
            break

    return Returned ## return boolean variable

## TEST CODE ##
if __name__ == "__main__":
    print(returnbook(7))
## OUTPUT = True
    print(returnbook(15))
## OUTPUT = False
