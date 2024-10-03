from .postgreSql import get_connection


def create_item(name, description, price, quantity, category):
    conn = get_connection()
    if conn is None:
        return
    cursor = conn.cursor()

    insert_query = """
    INSERT INTO items (name, description, price, quantity, category) 
    VALUES (%s, %s, %s, %s, %s);
    """
    cursor.execute(insert_query, (name, description, price, quantity, category))
    conn.commit()
    print(f"Item '{name}' created successfully.")

    cursor.close()
    conn.close()

def get_item_by_id(item_id):
    conn = get_connection()
    if conn is None:
        return
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM items WHERE item_id = %s;", (item_id,))
    item = cursor.fetchone()

    if item:
        print(f"ID: {item[0]}, Name: {item[1]}, Description: {item[2]}, Price: {item[3]}, Quantity: {item[4]}, Category: {item[5]}, Created At: {item[6]}")
    else:
        print(f"No item found with ID {item_id}.")

    cursor.close()
    conn.close()
    return item

def get_item_by_name(item_name):
    conn = get_connection()
    if conn is None:
        return
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM items WHERE name = %s;", (item_name,))
    item = cursor.fetchone()

    if item:
        print(f"ID: {item[0]}, Name: {item[1]}, Description: {item[2]}, Price: {item[3]}, Quantity: {item[4]}, Category: {item[5]}, Created At: {item[6]}")
    else:
        return False

    cursor.close()
    conn.close()
    return item

def update_item(item_id, name=None, description=None, price=None, quantity=None, category=None):
    conn = get_connection()
    if conn is None:
        return
    cursor = conn.cursor()

    update_query = """
    UPDATE items SET
        name = COALESCE(%s, name),
        description = COALESCE(%s, description),
        price = COALESCE(%s, price),
        quantity = COALESCE(%s, quantity),
        category = COALESCE(%s, category)
    WHERE item_id = %s;
    """
    cursor.execute(update_query, (name, description, price, quantity, category, item_id))
    conn.commit()

    if cursor.rowcount > 0:
        print(f"Item with ID {item_id} updated successfully.")
    else:
        return False

    cursor.close()
    conn.close()
    return True

def delete_item_by_id(item_id):
    conn = get_connection()
    if conn is None:
        return
    cursor = conn.cursor()

    cursor.execute("DELETE FROM items WHERE item_id = %s;", (item_id,))
    conn.commit()

    if cursor.rowcount > 0:
        print(f"Item with ID {item_id} deleted successfully.")
    else:
        print(f"No item found with ID {item_id}.")
        return False

    cursor.close()
    conn.close()
    return True
