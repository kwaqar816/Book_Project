from book import Book


class bookActivity:
    booklist = []

    def execute(self, ch):
        if ch == 1:
            id = int(input('Enter id of book: '))
            name = input('Enter book name: ')
            author = input('Enter auhtor name: ')
            price = int(input('Enter price of book: '))
            b = Book(id, name, author, price)
            bookActivity.booklist.append(b)
        elif ch == 2:
            for b in bookActivity.booklist:
                print('Book info is')
                print(
                    'Id: {}  Name: {}  Author: {}  Price: {}'.format(
                        b.getId(), b.getName(), b.getAuthor(), b.getPrice()))

        elif ch == 3:
            def update_info():
                for b in bookActivity.booklist:
                    print('What do you want to update')
                    choice = int(
                        input('1.Book name \n 2.Author name \n 3.Price : '))
                    if choice == 1:
                        name = input('Enter new name: ')
                        b.setName(name)
                    elif choice == 2:
                        author = input("Enter new author name: ")
                        b.setAuthor(author)
                    elif choice == 3:
                        price = int(input('Enter new price: '))
                        b.setPrice(price)
                    else:
                        print('Please enter correct option')
                        update_info()
            update_info()

        elif ch == 4:
            def search():
                for b in bookActivity.booklist:
                    id1 = input('Enter book id you want: ')
                    if b.getId() == id1:
                        print(
                            'Id: {}  Name: {}  Author: {}  Price: {}'.format(
                                b.getId(), b.getName(), b.getAuthor(), b.getPrice()))
                    else:
                        print('Please enter correct id')
                        search()
            search()

        elif ch == 5:
            for b in bookActivity.booklist:
                id2 = input('Enter book id you want to delete: ')
                if b.getId == id2:
                    bookActivity.booklist.remove(b)

        elif ch == 6:
            exit()

        else:
            pass


b = bookActivity()
while True:
    print('Welcome')
    print(' 1)Add Book \n 2) Show book list \n 3) Update book info \n 4) Search books by id \n 5) Delete book \n 6) Exit')
    choice = int(input('Enter your choice: '))

    b.execute(choice)
