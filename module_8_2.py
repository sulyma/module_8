def personal_sum(numbers):
    result = 0
    incorrect_data = 0

    for item in numbers:
        try:
            result += float(item)  # Пробуем привести item к числу и прибавить к результату
        except (TypeError, ValueError):  # Обрабатываем исключения если item не числовое значение
            incorrect_data += 1

    return result, incorrect_data


def calculate_average(numbers):
    try:
        # Проверяем, является ли numbers коллекцией
        if not isinstance(numbers, (list, tuple, set, str)):
            raise TypeError('В numbers записан некорректный тип данных')

        total_sum, incorrect_count = personal_sum(numbers)
        valid_count = len(numbers) - incorrect_count  # Количество валидных значений

        # Вычисляем среднее арифметическое
        average = total_sum / valid_count if valid_count > 0 else 0
        return average

    except ZeroDivisionError:
        return 0
    except TypeError as te:
        print(te)
        return None


print(f'Результат 1: {calculate_average("1, 2, 3")}')  # Строка перебирается, но каждый символ - строковый тип
print(f'Результат 2: {calculate_average([1, "Строка", "3", "Ещё Строка"])}')  # Учитываются только 1 и 3
# print(f'Результат 3: {calculate_average(567)}')  # Передана не коллекция
# print(f'Результат 4: {calculate_average([42, 15, 36, 13])}')  # Всё должно работать
