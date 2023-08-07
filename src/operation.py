from datetime import datetime


class Operation:

    def __init__(self, id, description, summa, currency, date, to_card_name,
                 to_account, from_card_name=None, from_account=None):
        self.id = id
        self.description = description
        self.summa = summa
        self.currency = currency
        self.date = date
        self.to_card_name = to_card_name
        self.to_account = to_account
        self.from_card_name = from_card_name
        self.from_account = from_account

    def __repr__(self):
        return f'Operation({self.id}, {self.description}, {self.summa}, {self.currency}, ' \
               f'{self.date}, {self.to_card_name}, {self.to_account}, {self.from_card_name}, {self.from_account})'

    def format_date(self):
        """
        Приводит дату к формату ДД.ММ.ГГГГ (пример: 14.10.2018) и возвращает её
        """
        self.date = datetime.strptime(self.date[0], '%Y-%m-%d')
        self.date = self.date.strftime('%d.%m.%Y')
        return self.date

    def mask_to_account(self):
        """
        Маскирует номер карты/счёта получателя, возвращает в формате  **XXXX
        (видны только последние 4 цифры номера счета).
        """
        self.to_account = str(self.to_account)
        return f"**{self.to_account[-4:]}"

    def mask_from_account(self):
        """
        Маскирует номер карты/счёта отправителя, возвращает в формате  XXXX XX** **** XXXX
        (видны первые 6 цифр и последние 4, разбито по блокам по 4 цифры, разделенных пробелом).
        """
        if self.from_account is None:
            return "Не указано"
        else:
            self.from_account = str(self.from_account)
            return f"{self.from_account[:4]} {self.from_account[4:6]}** **** {self.from_account[-4:]}"

    def return_from_card_name(self):
        """
        Возвращает название карты отправителя, либо фразу "Не указано", если self.card.name = None
        """
        if self.from_card_name is None:
            return "Не указано"
        else:
            return self.from_card_name
