def main():
    try:
        user_input = input("Будь ласка, введіть число: ")
        number = int(user_input)
        print(f"Ви ввели число: {number}")
    except ValueError:
        print("Помилка: введені дані не можна конвертувати в ціле число.")

if __name__ == "main":
    main()