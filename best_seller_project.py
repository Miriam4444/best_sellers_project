#prompts
#Ask user what to do
def read_file():
    infile = open('bestsellers.txt' , 'r')
    book_list = []
    for line in infile:
        line = line.strip()
        cols = line.split('\t')
        book_list.append(cols)
        global global_book_list
        global_book_list = book_list
        #print(cols)
    #make all the lists
    title_list = []
    author_list = []
    publisher_list = []
    date_list = []
    

    #add the categories to the list
    for book in book_list:
        #make title list
        title = book[0]
        title_list.append(title)
        #make author list
        author = book[1]
        author_list.append(author)
        global global_author_list
        global_author_list = author_list
        #make publisher list
        publisher = book[2]
        publisher_list.append(publisher)
        #make date list
        date = book[3]
        date_list.append(date)
    #print(title_list)
    #print(author_list)
    #print(publisher_list)
    #print(date_list)

    #find book with author name
def search_for_author():
    search_string = input(str('Enter search string: '))
    author_count = (global_author_list.count(search_string))
    print(author_count)
    author_index_num = 0
    new_author_list = global_author_list
    for i in range(author_count):
        search_str_index = new_author_list.index(search_string)
        #print(search_str_index)
        author_spot = (new_author_list[search_str_index])
        print(author_spot)
        author_index_num = ((search_str_index) + 1)
        print(global_book_list[search_str_index])
        new_author_list = global_author_list[search_str_index:]
#I still need to figure out how to get it if the whole name isn't input

        

read_file()
search_for_author()
print("done")
'''
def user_prompts():
    print("What would you like to do? ")
    print('\t 1: Look up year range')
    print('\t 2: Look up month/year')
    print('\t 3: Search for author')
    print('\t 4: Search for title')
    print('\t Q: Quit')
    what_to_do = input('\t')

    #start running functions
    if what_to_do = "1":
        look_up_year_range
    elif what_to_do = "2":
        look_up_month_and_year
    elif what_to_do = "3":
        search_for_author
    elif what_to_do = "4":
        search_for_title
    elif what_to_do = "Q":
        break
    else:
        print("I don't understand this command")
        user_prompts

#2: look up month/year
def look_up_month_and_year():
    #get info from user (month and year)
    month = input("Enter month (1-12)")
    year = input("Enter year")
    search.

def read_file():
    infile = open('bestsellers.txt' , 'r')
    book_list = []
    for line in infile:
        print(line)

read_file
'''
    
