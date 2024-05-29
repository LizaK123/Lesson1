def get_integer_from_user():
    user_input = input("Будь ласка, введіть число: ")
    try:
        user_number = int(user_input)
        print(f"Ви ввели число: {user_number}")
    except ValueError:
        print("Помилка: введені дані не є цілим числом. Спробуйте ще раз.")


get_integer_from_user()