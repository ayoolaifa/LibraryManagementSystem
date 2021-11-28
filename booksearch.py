import database


def search(searchterm):
    searched_list = []
    list_of_books = database.file_to_text()
    for i in range(0, len(list_of_books)):
        book_line_list = list_of_books[i].split(" | ")
        if book_line_list[2] == searchterm:
            searched_list.append(list_of_books[i])
    return searched_list

