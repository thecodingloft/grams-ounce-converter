def convert(amount: int, convert_from: str, convert_to: str):
    gram = ["g", "gr", "gram", "gramm", "grams"]
    ounce = ["oz", "ounce", "ounces"]

    if convert_from.lower() in gram and convert_to in ounce:
        converted_amount = round((amount / 28.34952), 2)
        return converted_amount, ounce[1]

    elif convert_from.lower() in ounce and convert_to in gram:
        converted_amount = round((amount * 28.34952), 2)
        return converted_amount, gram[0]

    else:
        return "Please provide a valid number and measurement"


value = convert(20, "G", "oz")
print(value)
