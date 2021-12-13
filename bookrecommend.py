import database
from random import randint


def list_of_popular_books(book_recommended_list, books_read_by_member):
    books_read_by_member_2 = []
    for i in books_read_by_member:
        if i[0] == "RETURN":
            del i
        else:
            books_read_by_member_2.append(i)
    book_info_list = []
    for i in books_read_by_member_2:
            book_info_list.append(database.book_line_from_id(i[3]))

    no_duplicate_read_book_info = []
    for i in book_info_list:
        if i not in no_duplicate_read_book_info:
            no_duplicate_read_book_info.append(i)

    tuple_list_of_books = []
    count_of_occurence = 0
    logfile = database.logfile_to_text()
    for i in range(1, 17):
        for line in logfile:
            single_log = line.split(" | ")
            if int(single_log[3]) == i and single_log[0] == "CHECKOUT":
                count_of_occurence += 1

        tuple_of_books = (i, count_of_occurence)
        count_of_occurence = 0
        tuple_list_of_books.append(tuple_of_books)
        tuple_list_of_books.sort(key=lambda tup: tup[1], reverse=True)




    for i in tuple_list_of_books:
        random_num = randint(0,5)
        if i != random_num:
            new_book = database.book_line_from_id(i[0])
            new_book_string = new_book[0] + " | " + new_book[1] + " | " +new_book[2] + " | " + new_book[3] + " | " + new_book[4] + " | " + new_book[5]
            if book_recommended_list != []:
                for book in book_recommended_list:
                    g = book.split(" | ")
                    if i[0] != g[0] and new_book_string not in book_recommended_list:
                        for line in no_duplicate_read_book_info:
                            if i[0] != line[0] and new_book[5] == "0":
                                return new_book_string
            else:
                for line in no_duplicate_read_book_info:
                    if i[0] != line[0] and new_book[5] == "0":
                        return new_book_string


def recommend(member_id):
    final_recommended_books = []
    member_id_log = []
    log_file = database.logfile_to_text()
    for i in log_file:
        single_log = i.split(" | ")
        if single_log[2] == str(member_id):
            member_id_log.append(single_log)

    if member_id_log != []:
            tuple_list_of_books = []
            num_of_log_apps = 0
            duplicated_book = ""
            for i in member_id_log:
                if i[0] != "RETURN":
                    bookrecommended = database.genre_list(i[3])
                    for j in bookrecommended:
                        g = j.split(" | ")
                        if g[2] != duplicated_book:
                            duplicated_book = g[2]
                            for k in log_file:
                                f = k.split(" | ")
                                if f[3] == g[0] and f[0] == "CHECKOUT":
                                    num_of_log_apps += 1
                            tuple_of_books = (j, num_of_log_apps)
                            tuple_list_of_books.append(tuple_of_books)
                        num_of_log_apps = 0

            tuple_list_of_books.sort(key=lambda tup: tup[1], reverse=True)
            recommended_books = [i[0] for i in tuple_list_of_books]

            print(recommended_books)
            for i in recommended_books:
                if i not in final_recommended_books:
                    final_recommended_books.append(i)

            if len(final_recommended_books) < 3:
                num_of_books_needed = 3 - len(final_recommended_books)
                while len(final_recommended_books) < 3:
                    new_book = list_of_popular_books(final_recommended_books, member_id_log)
                    final_recommended_books.append(new_book)

            elif len(final_recommended_books) > 10:
                final_recommended_books = final_recommended_books[:10]
    else:
        final_recommended_books = False
    return final_recommended_books

