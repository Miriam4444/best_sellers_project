def display_books_year_range(book_list, start_year, end_year):
    books_in_range = []
    for book in book_list:
        if start_year <= int(book[3][-4:]) <= end_year:
            books_in_range.append(book)

    if books_in_range:
        print_books(books_in_range)
    else:
        print("No books found in the specified year range.")