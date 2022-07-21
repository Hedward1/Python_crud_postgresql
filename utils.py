import psycopg2


def connect():
    """
    Function to connect on server
    """
    try:
        conn = psycopg2.connect(
            database='ppostgresql',
            host='localhost',
            user='userlogin',
            password='userpassword',
        )
        return conn
    except psycopg2.Error as e:
        print(f'Error on connexion with PostgreSQL Server {e}')


def disconnect(conn):
    """
    Function to disconnect on server
    """
    if conn:
        conn.close()


def list():
    """
    Function to list all products on server
    """
    conn = connect()
    cursor = conn.cursor()
    cursor.execute('select * from products')
    products = cursor.fetchall()

    if len(products) > 0:
        print('List')
        print('---------------------')
        for product in products:
            print(f'ID: {product[0]}')
            print(f'Product: {product[1]}')
            print(f'Price: {product[2]}')
            print(f'Stock: {product[3]}')
            print('---------------------')
    else:
        print('No products in this table')

    disconnect(conn)
    menu()


def insert():
    """
    Function to Insert products on server
    """
    conn = connect()
    cursor = conn.cursor()

    name = input('Product Name: ')
    price = float(input('Product Price: '))
    stock = int(input('Product Stock: '))
    cursor.execute(f" insert into products (name, price, stock) values ('{name}', {price}, {stock}) ")
    conn.commit()

    if cursor.rowcount == 1:
        print(f'Product {name} has inserted successfully')
    else:
        print('cannot insert the product')
    disconnect(conn)
    menu()


def update():
    """
    Function to update products on server
    """
    conn = connect()
    cursor = conn.cursor()

    cod = int(input('Product cod.: '))
    name = input('Product Name: ')
    price = float(input('Product Price: '))
    stock = int(input('Product Stock: '))

    cursor.execute(f"Update products set name='{name}', price={price}, stock={stock} where id={cod}")
    conn.commit()

    if cursor.rowcount == 1:
        print(f'Product {name} has been updated.')
    else:
        print(f'Product with id={cod} seems not exist')
    disconnect(conn)
    menu()


def delete():
    """
    Function to delete products
    """

    conn = connect()
    cursor = conn.cursor()

    cod = int(input('Product cod.: '))

    cursor.execute(f"Delete from products where id={cod}")
    conn.commit()

    if cursor.rowcount == 1:
        print(f'Product with id={cod} has been deleted')
    else:
        print(f'Product with id={cod} seems not exists')
    disconnect(conn)
    menu()


def menu():
    """
    Function to create initial menu
    :return:
    """
    print('select an option')
    print('1 - List Products')
    print('2 - Insert Product')
    print('3 - Update Product')
    print('4 - Delete Product')
    option = int(input())
    if option in [1, 2, 3, 4]:
        if option == 1:
            list()
        elif option == 2:
            insert()
        elif option == 3:
            update()
        elif option == 4:
            delete()
        else:
            print('Invalid option')
    else:
        print('Invalid Option')


