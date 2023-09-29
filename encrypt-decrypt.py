import random, string

allowed_chars = list(' ' + string.ascii_letters + string.digits + string.punctuation)

def process_msg(msg, oper):
    random.seed(int(input("Enter key: ")))
    shuffled_chars = allowed_chars.copy()
    random.shuffle(shuffled_chars)

    print("".join(shuffled_chars[allowed_chars.index(ele)] for ele in msg)) if oper == 1 else print("".join(allowed_chars[shuffled_chars.index(ele)] for ele in msg))
    
process_msg(input("Enter message: "), int(input("Input (1) to encrypt and (2) to decrypt: ")))

