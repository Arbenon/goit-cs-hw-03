import sqlite3
from faker import Faker

# Підключення до бази даних через шлях
conn = sqlite3.connect('MyFirstDB')
cur = conn.cursor()

# Ініціалізація Faker
fake = Faker()

# Вставка користувачів
for _ in range(100):
    fullname = fake.name()
    email = fake.email()
    cur.execute(
        "INSERT INTO users (fullname, email) VALUES (?, ?)",
        (fullname, email)
    )

# Вставка статусів, якщо їх ще немає
cur.execute("SELECT COUNT(*) FROM status")
if cur.fetchone()[0] == 0:
    statuses = ['new', 'in progress', 'completed']
    for status in statuses:
        cur.execute("INSERT INTO status (name) VALUES (?)", (status,))

# Перевірка, чи статуси були успішно вставлені
cur.execute("SELECT id, name FROM status")
status_rows = cur.fetchall()
print("Status IDs:", status_rows)  # Друкуємо статуси для перевірки

status_ids = [row[0] for row in status_rows]

# Перевірка, чи користувачі були успішно вставлені
cur.execute("SELECT id, fullname FROM users")
user_rows = cur.fetchall()
print("User IDs:", user_rows)  # Друкуємо користувачів для перевірки

user_ids = [row[0] for row in user_rows]

# Вставка завдань
for _ in range(30):
    title = fake.sentence(nb_words=6)
    description = fake.paragraph(nb_sentences=3)
    status_id = fake.random_element(elements=status_ids)
    user_id = fake.random_element(elements=user_ids)
    cur.execute(
        "INSERT INTO tasks (title, description, status_id, user_id) VALUES (?, ?, ?, ?)",
        (title, description, status_id, user_id)
    )

# Коміт транзакції
conn.commit()

# Закриття підключення
cur.close()
conn.close()

