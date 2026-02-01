from datetime import datetime

def get_sign(date_str):
    date = datetime.strptime(date_str, "%Y-%m-%d").date()

    match(date.month):
        case 1: 
            return "Capricorn" if date.day < 20 else "Aquarius"
        case 2:
            return "Aquarius" if date.day < 19 else "Pisces"
        case 3:
            return "Pisces" if date.day < 21 else "Aries"
        case 4:
            return "Aries" if date.day < 20 else "Taurus"
        case 5:
            return "Taurus" if date.day < 21 else "Gemini"
        case 6:
            return "Gemini" if date.day < 21 else "Cancer"
        case 7:
            return "Cancer" if date.day < 23 else "Leo"
        case 8:
            return "Leo" if date.day < 23 else "Virgo"
        case 9:
            return "Virgo" if date.day < 23 else "Libra"
        case 10:
            return "Libra" if date.day < 23 else "Scorpio"
        case 11:
            return "Scorpio" if date.day < 22 else "Sagittarius"
        case 12:
            return "Sagittarius" if date.day < 22 else "Capricorn"

    return "Invalid date"

print(get_sign("1985-12-06"))