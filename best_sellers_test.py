#Cs 175
#Anthony Mendes,
#bestsellers.py
# Function to read data from file and create book list
def create_book_list():
    try:
        with open("bestsellers.txt", "r") as file:
            lines = file.readlines()
            book_list = [line.strip().split("\t") for line in lines]
        return book_list
    except FileNotFoundError:
        print("Error: File not found.")
    except Exception as e:
        print("Error:", e)
    return None

# Function to display books in a year range
def display_books_year_range(book_list, start_year, end_year):
    books_in_range = []
    for book in book_list:
        if start_year <= int(book[3][-4:]) <= end_year:
            books_in_range.append(book)

    if books_in_range:
        print_books(books_in_range)
    else:
        print("No books found in the specified year range.")

# Function to disp1lay books in a specific month and year
def display_books_month_year(book_list, month, year):
    books_in_month_year = [book for book in book_list if int(book[3][-4:]) == year and int(book[3][:2]) == month]
    if books_in_month_year:
        print_books(books_in_month_year)
    else:
        print("No books found in the specified month and year.")

# Function to search for books by author
def search_books_by_author(book_list, search_string):
    search_string = search_string.lower()
    books_by_author = [book for book in book_list if search_string in book[1].lower()]
    if books_by_author:
        print_books(books_by_author)
    else:
        print("No books found for the author search.")

# Function to search for books by title
def search_books_by_title(book_list, search_string):
    search_string = search_string.lower()
    books_by_title = [book for book in book_list if search_string in book[0].lower()]
    if books_by_title:
        print_books(books_by_title)
    else:
        print("No books found for the title search.")

# Function to print books in a readable manner
def print_books(books):
    for book in books:
        print(f"{book[0]} by: {book[1]} (pub date: {book[3]})")

# Main function to handle menu and user input
def main():
    book_list = create_book_list()
    if book_list:
        print(f"Read {len(book_list)} books")
        while True:
            print("""
            What would you like to do?
                1: Look up year range
                2: Look up month/year
                3: Search for author
                4: Search for title
                Q: Quit
            """)
            choice = input("> ").strip().lower()
            if choice == "1":
                start_year = int(input("Enter start year: "))
                end_year = int(input("Enter end year: "))
                display_books_year_range(book_list, start_year, end_year)
            elif choice == "2":
                month = int(input("Enter month (1-12): "))
                year = int(input("Enter year: "))
                display_books_month_year(book_list, month, year)
            elif choice == "3":
                search_string = input("Enter search string for author: ")
                search_books_by_author(book_list, search_string)
            elif choice == "4":
                search_string = input("Enter search string for title: ")
                search_books_by_title(book_list, search_string)
            elif choice == "q":
                print("Done")
                break
            else:
                print("Invalid input. Please try again.")

# Call the main function to start the program
if __name__ == "__main__":
    main()


