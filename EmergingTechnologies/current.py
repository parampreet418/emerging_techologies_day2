def cur_date():
    from datetime import date
    today = date.today()
    current_date = today.strftime("%d/%m/%y")
    date = print("The current date is =", current_date)


