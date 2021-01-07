# /main.py

from books.app import app
from books.database.init_db import init_db


def main():
    init_db()
    app.run('0.0.0.0',port=5000, debug=True)


if __name__ == '__main__':
    main()
