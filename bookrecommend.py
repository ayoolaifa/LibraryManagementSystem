import database
from random import randint


def list_of_popular_books(book_recommended_list, books_read_by_member):

    books_read_by_member_2 = [] ## log of books read by member (no return log)

    ## for loop remove line where member returns books
    for line in books_read_by_member:
        if line[0] == "RETURN":
            del line
        else:
            books_read_by_member_2.append(line )

    ## for loop gets the book info from database using book id
    book_info_list = []
    for line in books_read_by_member_2:
            book_info_list.append(database.book_line_from_id(line[3]))

    ## This removes any duplicated books in list
    no_duplicate_read_book_info = []
    for line in book_info_list:
        if line not in no_duplicate_read_book_info:
            no_duplicate_read_book_info.append(line)

    tuple_list_of_books = database.num_of_occurences_in_log()
    tuple_list_of_books.sort(key=lambda tup: tup[1], reverse=True)

    ## This returns the top read books by every member
    for book_id in tuple_list_of_books:
        random_num = randint(0,5)
        if random_num != 3:
            ## new_book is the book info for the book id being checked.
            new_book = database.book_line_from_id(book_id[0])
            new_book_string = new_book[0] + " | " + new_book[1] + " | " \
                              + new_book[2] + " | " + new_book[3] + " | "\
                              + new_book[4] + " | " + new_book[5]

            ## makes sure recommend list is not empty
            ## if it is, skips check is new_book_string in in that list.
            if book_recommended_list != []:
                for recommend_book in book_recommended_list:
                    single_recommend_book = recommend_book.split(" | ")

                 ## If the book is already in the members recommended book list
                 ## It is not returned

                    if book_id[0] != single_recommend_book[0] \
                            and new_book_string not in book_recommended_list:

                        for line in no_duplicate_read_book_info:
                            if book_id[0] != line[0] and new_book[5] == "0":
                                return new_book_string

            else:
                for line in no_duplicate_read_book_info:
                    if book_id[0] != line[0] and new_book[5] == "0":
                        return new_book_string

def recommend(member_id):
    final_recommended_books = [] ## final list of recommended books
    member_id_log = [] ## list of logs with member id

    ## for loop that gets lines of log with member id in
    log_file = database.logfile_to_text()
    for line in log_file:
        # split the log line into its different variables
        single_log_line = line.split(" | ")
        if single_log_line[2] == str(member_id):
            member_id_log.append(single_log_line)

    ## makes sure the member has checkout a book
    if member_id_log != []:
            tuple_list_of_books = []
## A list that contains recommend book
## and the number of times they have been checked out
            num_of_log_apps = 0
            duplicated_book = "" ## varible of duplicated books

## for loop to make the recommended book list
            for member_log_line in member_id_log:
                ## checks log line is not a return log line
                ## only count number of checkouts the book has got
                if member_log_line[0] != "RETURN":
                    book_recommended = database.genre_list(member_log_line[3])
                    for book_recommend_line in book_recommended:
                        single_book_line = book_recommend_line.split(" | ")

## makes sure no duplicated books (same title but book id) appear
                        if single_book_line[2] != duplicated_book:
                            duplicated_book = single_book_line[2]

## loop that counts how many times book has been checked out by all members
                            for line in log_file:
                                log_line = line.split(" | ")
                                if log_line[3] == single_log_line[0] \
                                        and log_line[0] == "CHECKOUT":
                                    num_of_log_apps += 1

                        ## tuple_of_books is the book being recommened
                        ## and the number of apperances in logfile in a tuple
                            tuple_of_books = (book_recommend_line,
                                              num_of_log_apps)

                            tuple_list_of_books.append(tuple_of_books)
                            ## append tuple to list of tuple
                        num_of_log_apps = 0  ## reset counter

            tuple_list_of_books.sort(key=lambda tup: tup[1], reverse=True)
            ## arranges list of tuples by thier second element in each tuple
            ## second element in tuples is the number of appearances in logfile

            recommended_books = [book[0] for book in tuple_list_of_books]
            ## only recommend books info from list of tuples

            ## removes duplicate books in list
            for book in recommended_books:
                if book not in final_recommended_books:
                    final_recommended_books.append(book)


            ## if statements that add or remove books
            ## depending on the number in list already
            if len(final_recommended_books) < 3:
                num_of_books_needed = 3 - len(final_recommended_books)
                while len(final_recommended_books) < 3:
                    new_book = list_of_popular_books(final_recommended_books,
                                                     member_id_log)
                    final_recommended_books.append(new_book)

            elif len(final_recommended_books) > 10:
                final_recommended_books = final_recommended_books[:10]
    else:
        final_recommended_books = False
    return final_recommended_books

## TEST CODE ##
if __name__ == "__main__":
    print(recommend("coao"))
## OUTPUT = [list of recommended books] ##
    print(recommend("mnil"))
## OUTPUT = False ##


