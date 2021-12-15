import database

def search(searchterm):
## list of books with same title as search ##
    searched_list = []

## function that gets all books in database ##
    list_of_books = database.file_to_text()

# For loop to get the individual book titles from every book in the database #

    for i in range(0, len(list_of_books)):
        book_line_list = list_of_books[i].split(" | ")

## Checks if title of book is the same as search term ##

        if book_line_list[2].lower() == searchterm.lower():
            searched_list.append(list_of_books[i])
    return searched_list

## TEST CODE
if __name__ == "__main__":
    print (search("Dune"))
## OUTPUT = ['3 | Sci-Fi | Dune | Frank Herbert | 24/04/2000 | MemberID',
##          '15 | Sci-Fi | Dune | Frank Herbert | 18/08/2000 | MemberID']
    print(search("Hello"))
## OUTPUT = []
