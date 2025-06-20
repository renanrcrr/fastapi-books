# FastAPI Book Project

This project demonstrates the use of FastAPI for building RESTful APIs. Follow the instructions below to set up and run the application.

## Prerequisites

- Python 3.7 or higher installed on your system.

## Setup Instructions

### 1. Install `virtualenv`

To isolate the project dependencies, install `virtualenv`:

```bash
pip install virtualenv
```

### 2. Create a Virtual Environment

Create a virtual environment named `fastapienv`:

```bash
virtualenv fastapienv
```

Activate the virtual environment:

- On Windows:
  ```bash
  fastapienv\Scripts\activate
  ```
- On macOS/Linux:
  ```bash
  source fastapienv/bin/activate
  ```

### 3. Install Dependencies

Install FastAPI and Uvicorn:

```bash
pip install fastapi uvicorn
```

### 4. Start the Application

Run the FastAPI application using Uvicorn:

```bash
uvicorn books.books:app --reload
```

- `books.books:app` specifies the module and the FastAPI instance.
- `--reload` enables auto-reloading for development.

### 5. Access the API

Once the application is running, you can access the API at:

- Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- ReDoc: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

## Project Structure

```
code/
├── books/
│   └── books.py  # FastAPI routes for managing books
├── .gitignore    # Git ignore file
└── README.md     # Project documentation
```

## License

This project is licensed under the MIT License.