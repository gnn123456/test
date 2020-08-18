from common.mysql import mysqlni

def gen_mobile():
    import random
    while True:
        phone = "18"
        for i in range(9):
            num = random.randint(0, 9)
            phone += str(num)

        # mysql = mysqlni(retu_dict=True)
        # ww = mysql.fet_all("select * from ab_member where mobile=to_base64(AES_ENCRYPT('{}','19549303ghdyoscc'))".format(18735571533))
        # if not ww:
        #     mysql.close()
        return phone
