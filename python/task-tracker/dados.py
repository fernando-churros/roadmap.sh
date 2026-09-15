from datetime import datetime

def create_date():
    x: datetime = datetime.now()
    date = x.strftime('%d/%m/%y ás %H:%M')

    return date

