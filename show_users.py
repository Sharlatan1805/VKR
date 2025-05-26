import sqlite3

def show_users():
    conn = sqlite3.connect("users.db")
    c = conn.cursor()
    c.execute("SELECT id, login FROM users")
    users = c.fetchall()
    conn.close()

    if users:
        print("Зарегистрированные пользователи:")
        for user in users:
            print(f"ID: {user[0]}, Логин: {user[1]}")
    else:
        print("Пользователей пока нет.")

if __name__ == "__main__":
    show_users()
