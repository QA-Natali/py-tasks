# validate_pin - ky7 - kata
# https://www.codewars.com/kata/55f8a9c06c018a0d6e000132/train/python

def validate_pin(pin):
    if len(pin) == 4 or len(pin)==6:
        if pin.isdigit() == True and int(pin) >= 0:
            return True
        else:
            return False
    else:
        return False