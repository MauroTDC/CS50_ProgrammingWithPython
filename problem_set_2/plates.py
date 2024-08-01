def main():
    plate = input("Plate: ")
    if is_valid(plate): 
        print("Valid")
    else:
        print("Invalid")


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
    
    
if __name__ == "__main__":
    main()