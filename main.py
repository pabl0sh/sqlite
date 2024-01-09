import sqlite3

def create_table():
    conn = sqlite3.connect('user_database.db')
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER NOT NULL,
            phone TEXT NOT NULL,
            email TEXT NOT NULL
        )
    ''')

    conn.commit()
    conn.close()

def register_user(name, age, phone, email):
    conn = sqlite3.connect('user_database.db')
    cursor = conn.cursor()

    cursor.execute('''
        INSERT INTO users (name, age, phone, email)
        VALUES (?, ?, ?, ?)
    ''', (name, age, phone, email))

    conn.commit()
    conn.close()

def fetch_all_users():
    conn = sqlite3.connect('user_database.db')
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM users')
    users = cursor.fetchall()

    conn.close()
    return users

def delete_user(user_id):
    conn = sqlite3.connect('user_database.db')
    cursor = conn.cursor()

    cursor.execute('DELETE FROM users WHERE id = ?', (user_id,))

    conn.commit()
    conn.close()
    print(f"Користувач з ID {user_id} видалений успішно!")

def main():
    create_table()

    while True:
        print("\n1. Реєстрація нового користувача")
        print("2. Вивести всіх користувачів")
        print("3. Видалити користувача за ID")
        print("4. Вихід")

        choice = input("Оберіть дію: ")

        if choice == '1':
            name = input("Ім'я: ")
            age = int(input("Вік: "))
            phone = input("Номер телефону: ")
            email = input("Електронна пошта: ")

            register_user(name, age, phone, email)
            print("Користувач зареєстрований успішно!")
        elif choice == '2':
            users = fetch_all_users()
            for user in users:
                print(user)
        elif choice == '3':
            user_id = int(input("Введіть ID користувача для видалення: "))
            delete_user(user_id)
        elif choice == '4':
            break
        else:
            print("Невірний вибір. Будь ласка, виберіть ще раз.")

if __name__ == "__main__":
    main()
