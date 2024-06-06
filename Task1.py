library = {
"978-0132350884": {"title": "Clean Code", "author": "Robert C. Martin"},
"978-0201485677": {"title": "Refactoring", "author": "Martin Fowler"},
}

users = {
"Alice": [],
"Bob": [],
}


class Library:

    def __init__(self, library = library, users = users) -> None:
        self.library = library
        self.users = users

    def add_new_book(self,ISBN,title,author):
        book = {
            "title": title,
            "author": author
        }
        self.library[ISBN] = book
        return "New book added"
    
    def remove_book(self,ISBN):
        name = self.library[ISBN]["title"]
        del self.library[ISBN]
        return f"\"{name}\" has been removed from the library!"
    
    def register_user(self,name):
        self.users[name] = []
        return f"New user registered"
    
    def borrow_book(self,name,ISBN):
        self.users[name].append(ISBN)
        return f"{name} borrowed book \"{ISBN}\""
    
    def return_book(self,name,ISBN):
        self.users[name].remove(ISBN)
        return f"{name} retured book {ISBN}"
    
    def borrowed_books(self,name):
        return self.users[name]


        

miniLibrary = Library()


print(miniLibrary.add_new_book("445-6677787","Things fall apart","chidinma"))
print(miniLibrary.add_new_book("99787","Things fly apart","chidera"))
print(miniLibrary.register_user("John"))
print(miniLibrary.borrow_book("Alice","99787"))
print(miniLibrary.borrow_book("Alice","978-0201485677"))
print(miniLibrary.return_book("Alice","99787"))
print(miniLibrary.borrowed_books("Alice"))
print(miniLibrary.remove_book("978-0201485677"))
print(miniLibrary.library)

