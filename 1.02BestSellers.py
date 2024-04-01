def main():
    filename = "bestsellers.txt"
    read_file()

    while True:
        print("\nWhat would you like to do?")
        print("    1: Look up year range")
        print("    2: Look up month/year")
        print("    3: Search for author")
        print("    4: Search for title")
        print("    Q: Quit")

        choice = input("> ").lower()

        if choice == '1':
            look_up_year_range(book_list)
        elif choice == '2':
            look_up_month_year(book_list)
        elif choice == '3':
            search_for_author()
        elif choice == '4':
            title_search()
        elif choice == 'q':
            print("Done")
            break
        else:
            print("I don't understand this command")


def read_file():
    infile = open('bestsellers.txt', 'r')
    book_list = []
    for line in infile:
        line = line.strip()
        cols = line.split('\t')
        book_list.append(cols)
        global global_book_list
        global_book_list = book_list
        # print(cols)
        # make all the lists
    title_list = []
    author_list = []
    publisher_list = []
    date_list = []

    # add the categories to the list
    for book in book_list:
        # make title list
        title = book[0]
        title_list.append(title)
        global global_title_list
        global_title_list = title_list
        # make author list
        author = book[1]
        author_list.append(author)
        global global_author_list
        global_author_list = author_list
        # make publisher list
        publisher = book[2]
        publisher_list.append(publisher)
        global global_publisher_list
        global_publisher_list = publisher_list
        # make date list
        date = book[3]
        date_list.append(date)
        global global_date_list
        global_date_list = date_list
        # print(title_list)
        # print(author_list)
        # print(publisher_list)
        # print(date_list)


def search_for_author():
    search_string = input('Enter search string: ').lower()
    matched_authors = []
    for author, book in zip(global_author_list, global_book_list):
        if search_string in author.lower():
            matched_authors.append((author, book))
    if matched_authors:
        print("Authors matching the search string:")
        for author, book in matched_authors:
            print(f"Author: {author}, Book: {book}")
    else:
        print("No authors found matching the search string.")


def title_search():
    search_string = input("Enter search string: ").lower()
    matched_titles = []
    for title, book in zip(global_title_list, global_book_list):
        if search_string in title.lower():
            matched_titles.append((title, book))
    if matched_titles:
        for title, book in matched_titles:
            # print(title)
            print(book)
    else:
        print("No titles found matching the search string.")


if __name__ == "__main__":
    main()