def calculate_checksum(nric):
    weights = [2, 7, 6, 5, 4, 3, 2]
    st = "JZIHGFEDCBA"
    fg = "XWUTRQPNMLK"
    
    if nric[0] in 'ST':
        offset = 0
    elif nric[0] in 'FG':
        offset = 4
    else:
        return False

    total = sum(int(nric[i]) * weights[i - 1] for i in range(1, 8))
    total += offset
    checksum = total % 11

    if nric[0] in 'ST':
        return nric[-1] == st[checksum]
    elif nric[0] in 'FG':
        return nric[-1] == fg[checksum]

def is_valid_nric(nric):
    if len(nric) != 9:
        return False
    if nric[0] not in 'STFG':
        return False
    if not nric[1:8].isdigit():
        return False
    return calculate_checksum(nric)

# Example usage
nric = input("Enter NRIC: ").upper()
if is_valid_nric(nric):
    print("Valid NRIC")
else:
    print("Invalid NRIC")
