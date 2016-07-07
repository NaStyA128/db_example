import MySQLdb
import MySQLdb.cursors


def get_connection():
    connection = MySQLdb.connect(user='root',
                                 passwd='123',
                                 db='books',
                                 cursorclass=MySQLdb.cursors.DictCursor)
    return connection


def insert_books(values):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.executemany("INSERT INTO Books (title, ISBN) VALUES (%s, %s)", values)


def select(**kwargs):
    connection = get_connection()
    cursor = connection.cursor()
    query = "SELECT * FROM Books"
    if kwargs != ():
        query += ' WHERE '
        j = 1
        for i in kwargs:
            if j > 1:
                query += ' AND '
            query += str(i)
            query += ' = '
            if type(kwargs[i]) == 'str':
                query += kwargs[i]
            else:
                query += '"'
                query += str(kwargs[i])
                query += '"'
            j += 1
    print(query)
    cursor.execute(query)
    return cursor.fetchall()


# insert_books([
#     ('Book1', 'qwe-123'),
#     ('Book2', 'qwe-1212'),
# ])


print(select(book_id=1, title='Creating relational databases for fun and profit'))
