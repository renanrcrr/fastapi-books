from fastapi import Body, FastAPI

# Initialize FastAPI application
app = FastAPI()

# In-memory list of books
BOOKS = [
    {"title": "Title One", "author": "Author One", "category": "Category One"},
    {"title": "Title Two", "author": "Author Two", "category": "Category Two"},
    {"title": "Title Three", "author": "Author Three", "category": "Category Three"},
    {"title": "Title Four", "author": "Author Four", "category": "Category Four"},
    {"title": "Title Five", "author": "Author Two", "category": "Category Five"},
]

# Route to get all books
@app.get("/books")
async def read_all_books():
    # Return the list of all books
    return BOOKS

# Route to get a book by its title
@app.get("/books/{book_title}")
async def read_boot(book_title: str):
    # Search for a book by title (case-insensitive)
    for book in BOOKS:
        if book.get("title").casefold() == book_title.casefold():
            return book

# Route to get books by author
@app.get("/books/byauthor")
async def get_books_by_params(author: str):
    # Filter books by author (case-insensitive)
    books_by_author = []
    for i in range(len(BOOKS)):
        if BOOKS[i].get('author').casefold() == author.casefold():
            books_by_author.append(BOOKS[i])
    return books_by_author

# Route to get books by author and category
@app.get("/books/{book_author}/")
async def read_category_by_query(book_author: str, category: str):
    # Filter books by author and category (case-insensitive)
    books_to_return = []
    for book in BOOKS:
        if book.get('author').casefold() == book_author.casefold() and \
            book.get('category').casefold() == category.casefold():
            books_to_return.append(book)
    return books_to_return

# Route to create a new book
@app.post("/books/create_book")    
async def create_book(new_book=Body()):
    # Add the new book to the list
    BOOKS.append(new_book)

# Route to update an existing book
@app.put("/books/update_book")
async def update_book(new_book=Body()):
    # Update the book if the title matches (case-insensitive)
    for i in range(len(BOOKS)):
        if BOOKS[i].get('title').casefold() == new_book.get('title').casefold():
            BOOKS[i] = new_book

# Route to delete a book by its title
@app.delete("/books/delete_book/{book_title}")
async def delete_book(book_title: str):
    # Remove the book from the list if the title matches (case-insensitive)
    for i in range(len(BOOKS)):
        if BOOKS[i].get('title').casefold() == book_title.casefold():
            BOOKS.pop(i)
            break
