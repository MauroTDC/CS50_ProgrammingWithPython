def main():
    test_plate_length()
    test_plate_start_letters()
    test_numbers_middle()
    test_all_alphanumeric()


def is_valid(plate: str):
    digits = []
    if plate.isalnum():
        for char in plate[:2]:
            if not char.isalpha():
                return False
    
        if len(plate) > 6 or len(plate) < 2:
            return False
        
        for char in plate:
            if char in ["0","1","2","3","4","5","6","7","8","9"]:
                digits.append(char)
        if digits[0] == "0":
            return False
        
        for i in range(len(plate) - 1):
            if plate[i] in ["0","1","2","3","4","5","6","7","8","9"]:
                if plate[i+1].isalpha():
                    return False
        return True
    else:
        return False
    

def test_plate_length():
    assert is_valid("C")
    assert is_valid("AAAA000")


def test_plate_start_letters():
    assert is_valid("000C")


def test_numbers_middle():
    assert is_valid("CS50A")


def test_all_alphanumeric():
    assert is_valid("CS .0")
    
    
if __name__ == "__main__":
    main()