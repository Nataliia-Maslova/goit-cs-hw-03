from pymongo import MongoClient
from pymongo.errors import PyMongoError, ConnectionFailure


# Підключення до MongoDB
try:
    client = MongoClient("mongodb://localhost:27017/")  # Вкажіть свій URL до MongoDB
    db = client["cats_db"]  # Створення бази даних "cats_db"
    collection = db["cats"]  # Створення колекції "cats"
    # Перевірка з'єднання
    client.admin.command('ismaster')
    print("MongoDB підключено успішно")
except ConnectionFailure:
    print("Не вдалося підключитися до MongoDB, перевірте з'єднання")


# Функція для створення нового документа
def create_document():
    try:
        name = input("Введіть ім'я кота: ")
        age = int(input("Введіть вік кота: "))
        features = input("Введіть характеристики через кому: ").split(',')

        document = {
            "name": name,
            "age": age,
            "features": [feature.strip() for feature in features]
        }

        collection.insert_one(document)
        print("Документ створено.")
    except PyMongoError as e:
        print(f"Помилка при роботі з MongoDB: {e}")
    except ValueError as e:
        print(f"Помилка введення: {e}")


# Функція для читання всіх документів
def read_all_documents():
    try:
        documents = collection.find()
        for doc in documents:
            print(doc)
    except PyMongoError as e:
        print(f"Помилка при роботі з MongoDB: {e}")


# Функція для пошуку кота за ім'ям
def read_document_by_name():
    try:
        name = input("Введіть ім'я кота: ")
        document = collection.find_one({"name": name})
        if document:
            print(document)
        else:
            print("Кіт не знайдений.")
    except PyMongoError as e:
        print(f"Помилка при роботі з MongoDB: {e}")


# Функція для оновлення віку кота за ім'ям
def update_document_age():
    try:
        name = input("Введіть ім'я кота для оновлення віку: ")
        new_age = int(input("Введіть новий вік: "))
        result = collection.update_one({"name": name}, {"$set": {"age": new_age}})
        if result.matched_count > 0:
            print("Вік оновлено успішно.")
        else:
            print("Кіт не знайдений.")
    except PyMongoError as e:
        print(f"Помилка при роботі з MongoDB: {e}")
    except ValueError as e:
        print(f"Помилка введення: {e}")


# Функція для додавання нової характеристики до списку features
def add_feature_to_document():
    try:
        name = input("Введіть ім'я кота для додавання характеристики: ")
        new_feature = input("Введіть нову характеристику: ")
        result = collection.update_one({"name": name}, {"$push": {"features": new_feature}})
        if result.matched_count > 0:
            print("Характеристика додана.")
        else:
            print("Кіт не знайдений.")
    except PyMongoError as e:
        print(f"Помилка при роботі з MongoDB: {e}")


# Функція для видалення кота за ім'ям
def delete_document():
    try:
        name = input("Введіть ім'я кота для видалення: ")
        result = collection.delete_one({"name": name})
        if result.deleted_count > 0:
            print("Кіт видалений.")
        else:
            print("Кіт не знайдений.")
    except PyMongoError as e:
        print(f"Помилка при роботі з MongoDB: {e}")


# Функція для видалення всіх документів
def delete_all_documents():
    try:
        confirmation = input("Ви впевнені, що хочете видалити всі документи? (так/ні): ")
        if confirmation.lower() == "так":
            collection.delete_many({})
            print("Всі документи видалені.")
        else:
            print("Операція скасована.")
    except PyMongoError as e:
        print(f"Помилка при роботі з MongoDB: {e}")


# Основна функція програми
def main():
    while True:
        print("\nДоступні дії:")
        print("1 - Створити запис про тварину")
        print("2 - Показати всі записи")
        print("3 - Пошук запису за ім'ям тварини")
        print("4 - Оновити вік тварини")
        print("5 - Додати особливість до тварини")
        print("6 - Видалити запис про тварину")
        print("7 - Видалити всі записи")
        print("8 - Вийти")
        choice = input("Виберіть дію: ")

        if choice == "1":
            create_document()
        elif choice == "2":
            read_all_documents()
        elif choice == "3":
            read_document_by_name()
        elif choice == "4":
            update_document_age()
        elif choice == "5":
            add_feature_to_document()
        elif choice == "6":
            delete_document()
        elif choice == "7":
            delete_all_documents()
        elif choice == "8":
            break
        else:
            print("Некоректний вибір. Спробуйте ще раз.")


if __name__ == "__main__":
    main()
