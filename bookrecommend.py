import database
from operator import itemgetter


def bookrecommend(member_id):
    single_log = []
    member_id_log = []
    recommended_books = []
    log_file = database.logfile_to_text()
    for i in log_file:
        single_log = i.split(" | ")
        if single_log[2] == str(member_id):
            member_id_log.append(single_log)

    recommended_books = []
    tuple_list_of_books = []
    num_of_log_apps = 0
    for i in member_id_log:
        if i[0] != "RETURN":
            bookrecommended = database.genre_list(i[3])
            g = []
            tuple_of_books = ()
            for j in bookrecommended:
                g = j.split(" | ")

                for k in log_file:
                    f = k.split(" | ")
                    if f[3] == g[0] and f[0] == "CHECKOUT":
                        num_of_log_apps += 1
                tuple_of_books = (g, num_of_log_apps)
                tuple_list_of_books.append(tuple_of_books)
            num_of_log_apps = 0
    tuple_list_of_books.sort(key=lambda tup: tup[1], reverse=True)
    recommended_books = [i[0] for i in tuple_list_of_books]
    print(recommended_books)


bookrecommend("coao")
