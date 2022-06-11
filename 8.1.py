class Date:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year


    @classmethod
    def new_format_date(cls, date):
        date_list = date.split('-')
        day, month, year = date_list
        day = int(day)
        month = int(month)
        year = int(year)
        return cls(day, month, year)

    @staticmethod
    def correct_day(date_desired_format):
        if date_desired_format.day > 31:
            return '31'
        elif date_desired_format.day < 1:
            return '1'
        else:
            return date_desired_format.day

    @staticmethod
    def correct_month(date_desired_format):
        if date_desired_format.month > 12:
            return '12'
        elif date_desired_format.month < 1:
            return '1'
        else:
            return date_desired_format.month

    @staticmethod
    def correct_year(date_desired_format):
        if date_desired_format.year > 2022:
            return '2022'
        else:
            return date_desired_format.year


date = Date.new_format_date('00-00-2023')
print(f'число {date.day}, месяц {date.month}, год {date.year}')
d = Date.correct_day(date)
m = Date.correct_month(date)
y = Date.correct_year(date)
print(f'число {d}, месяц {m}, год {y}')