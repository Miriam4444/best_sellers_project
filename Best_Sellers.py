# Define global variables to store book and author lists
global_book_list = []
global_author_list = []

# Function to read data from file and create book list
def read_file():
    global global_book_list, global_author_list
    infile = open('bestsellers.txt', 'r')
    book_list = []
    author_list = []
    for line in infile:
        line = line.strip()
        cols = line.split('\t')
        book_list.append(cols)
        author_list.append(cols[1])  # Assuming author name is in the second column
    global_book_list = book_list
    global_author_list = author_list
    infile.close()

# Function to search for books by author
def search_for_author(search_string):
    global global_author_list, global_book_list
    search_string = search_string.lower()
    books_by_author = [book for book in global_book_list if search_string in book[1].lower()]
    if books_by_author:
        print_books(books_by_author)
    else:
        print("No books found for the author search.")

# Function to print books in a readable manner
def print_books(books):
    for book in books:
        print(f"{book[0]} by: {book[1]} (pub date: {book[3]})")

# Function to handle user prompts and actions
def user_prompts():
    while True:
        print("What would you like to do?")
        print("\t1: Look up year range")
        print("\t2: Look up month/year")
        print("\t3: Search for author")
        print("\t4: Search for title")
        print("\tQ: Quit")
        what_to_do = input("> ").strip().lower()

        if what_to_do == "1":
            look_up_year_range()
        elif what_to_do == "2":
            look_up_month_and_year()
        elif what_to_do == "3":
            search_string = input("Enter search string for author: ")
            search_for_author(search_string)
        elif what_to_do == "4":
            search_for_title()
        elif what_to_do == "q":
            print("Done")
            break
        else:
            print("I don't understand this command")

# Function to handle looking up year range
def look_up_year_range():
    start_year = int(input("Enter start year: "))
    end_year = int(input("Enter end year: "))
    books_in_range = [book for book in global_book_list if start_year <= int(book[3][-4:]) <= end_year]
    if books_in_range:
        print_books(books_in_range)
    else:
        print("No books found in the specified year range.")

# Function to handle looking up month and year
def look_up_month_and_year():
    month = int(input("Enter month (1-12): "))
    year = int(input("Enter year: "))
    books_in_month_year = [book for book in global_book_list if int(book[3][:2]) == month and int(book[3][-4:]) == year]
    if books_in_month_year:
        print_books(books_in_month_year)
    else:
        print("No books found for the specified month and year.")

# Function to handle searching for titles
def search_for_title():
    search_string = input("Enter search string for title: ")
    books_by_title = [book for book in global_book_list if search_string.lower() in book[0].lower()]
    if books_by_title:
        print_books(books_by_title)
    else:
        print("No books found for the title search.")

# Main function to orchestrate program execution
def main():
    read_file()  # Read data from file
    user_prompts()  # Prompt user for actions

# Start the program
if __name__ == "__main__":
    main()
