class Book:
    def __init__(self, title, author, price, publisher, stock):
        self.title = title
        self.author = author
        self.price = price
        self.publisher = publisher
        self.stock = stock

    def display_details(self):
        print("Title:", self.title)
        print("Author:", self.author)
        print("Price: Rs.", self.price)
        print("Publisher:", self.publisher)
        print("Stock:", self.stock)

    def sell_books(self, num_copies):
        if num_copies <= self.stock:
            total_cost = num_copies * self.price
            print(f"You have purchased {num_copies} copies of '{self.title}' for a total cost of Rs. {total_cost}.")
            self.stock -= num_copies
        else:
            print("Required copies not in stock.")

def main():
    # Creating a list of books in the inventory
    books = [
        Book("Book1", "Author1", 20, "Publisher1", 10),
        Book("Book2", "Author2", 100, "Publisher2", 5),
        Book("Book3", "Author3", 10, "Publisher3", 15),
    ]

    while True:
        print("\nBook Inventory System")
        print("1. Search for a book")
        print("2. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            title = input("Enter the title of the book: ")
            author = input("Enter the author of the book: ")

            found = False
            for book in books:
                if book.title == title and book.author == author:
                    book.display_details()
                    num_copies = int(input("Enter the number of copies you want to purchase: "))
                    book.sell_books(num_copies)
                    found = True
                    break

            if not found:
                print("Book not found in the inventory.")

        elif choice == 2:
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()





