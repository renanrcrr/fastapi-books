from fastapi import FastAPI

app = FastAPI()

class Book:
    id: int
    title: str
    author: str
    desscription: str
    rating: int

    def __init__(self, id: int, title: str, author: str, description: str, rating: int):
        self.id = id
        self.title = title
        self.author = author
        self.description = description
        self.rating = rating

BOOKS = [
    Book(1, "1984", "George Orwell", "Dystopian novel set in totalitarian society", 5),
    Book(2, "To Kill a Mockingbird", "Harper Lee", "Novel about racial injustice in the Deep South", 5),
    Book(3, "The Great Gatsby", "F. Scott Fitzgerald", "Story of the Jazz Age and the American Dream", 4), 
    Book(4, "Brave New World", "Aldous Huxley", "Dystopian novel about a technologically advanced future", 4),
    Book(5, "Fahrenheit 451", "Ray Bradbury", "Novel about a future where books are banned and 'firemen' burn them", 2),
    Book(6, "The Handmaid's Tale", "Margaret Atwood", "Novel about a totalitarian society", 3)
]

@app.get("/books2")
async def read_all_books():
    return BOOKS