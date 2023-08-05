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