def get_percentage(number, round_digits=None):
    percent_ = round(number * 100, ndigits=round_digits)
    return f'{percent_}%'

