from utils.utils import load_operations
from utils.utils import make_list_executed_operations


if __name__ == '__main__':

    # Получаем данные и файла и формируем список выполненных операций
    filename = "operations.json"
    data = load_operations(filename)
    list_of_executed_operations = make_list_executed_operations(data)

    # Сортируем список по дате, от последней операции к первой и получаем последние 5 операций
    sorted_list_by_date = sorted(list_of_executed_operations, key=lambda x: x.date, reverse=True)
    latest_five = sorted_list_by_date[:5]

    # Выводим последние 5 операций в требуемом формате
    for item in latest_five:
        print(f"""{item.format_date()} {item.description}
{item.return_from_card_name()} {item.mask_from_account()} -> {item.to_card_name} {item.mask_to_account()}
{item.summa} {item.currency}\n""")
