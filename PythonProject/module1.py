from datetime import datetime,timedelta
def returned(date):
    original = datetime.strptime(date, '%d/%m/%y')
    return_date = original + timedelta(days=7)
    current_date = datetime.today()
    if return_date >= current_date:
        return 1
    else:
        return 0