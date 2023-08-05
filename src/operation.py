from datetime import datetime


class Operation:

    def __init__(self, id, description, summa, currency, date, to_card_name,
                 to_account, from_card_name="None", from_account="None"):
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
