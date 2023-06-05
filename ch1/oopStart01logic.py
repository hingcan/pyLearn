zenith12xp = 1
helios44 = 1

if zenith12xp == helios44:
    print('Your stuff is ready for shooting, photocowboy')
else:
    print('Sorry, you need another objective for this body')



import psycopg2

# Установка соединения с базой данных
conn = psycopg2.connect(
    host="your_host",
    port="your_port",
    database="your_database",
    user="your_username",
    password="your_password"
)

# Создание курсора для выполнения запросов
cur = conn.cursor()

# Выполнение SELECT-запроса
cur.execute("SELECT * FROM your_table")

# Получение результатов запроса
rows = cur.fetchall()

# Обработка результатов
for row in rows:
    # Доступ к значениям столбцов
    col1 = row[0]
    col2 = row[1]
    # ... и т.д.

# Закрытие курсора и соединения с базой данных
cur.close()
conn.close()
