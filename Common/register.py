def gen_mobile():
    import random
    while True:
        phone = "187"
        for i in range(8):
            num = random.randint(0, 8)
            phone += str(num)
        return phone
