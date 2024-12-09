import psycopg2
from prettytable import PrettyTable


# Підключення до БД
def display_tables():
    try:
        conn = psycopg2.connect(**DB_PARAMS)
        cursor = conn.cursor()

        # Отримання списку таблиць
        cursor.execute(
            "SELECT table_name FROM information_schema.tables WHERE table_schema = 'public';"
        )
        tables = cursor.fetchall()

        for table in tables:
            table_name = table[0]
            print(f"\n--- Таблиця: {table_name} ---")

            # Отримання структури таблиці
            cursor.execute(
                f"SELECT column_name, data_type FROM information_schema.columns WHERE table_name = '{table_name}';")
            structure = cursor.fetchall()
            print("Структура:")
            for column in structure:
                print(f"{column[0]} ({column[1]})")

            # Вивід даних
            cursor.execute(f"SELECT * FROM {table_name};")
            rows = cursor.fetchall()
            if rows:
                table = PrettyTable()
                table.field_names = [desc[0] for desc in cursor.description]
                for row in rows:
                    table.add_row(row)
                print(table)
            else:
                print("Таблиця порожня.")
    except Exception as e:
        print("Помилка:", e)
    finally:
        cursor.close()
        conn.close()


if __name__ == "__main__":
    display_tables()
