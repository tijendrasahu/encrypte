class Encrypt:
    def __init__(self, login_id,
                 const='0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ! "#$%&\'()*+,-./:;<=>?@['
                       '\\]^_`{|}~'
                 ):
        self.login_id = login_id
        self.const = const

    def enc(self):
        new_encrypt = ''
        for i in self.login_id:
            for j in range(0, len(self.const)-6):
                if i == self.const[j]:
                    new_encrypt = new_encrypt + self.const[j + 6]
                else:
                    pass
        return new_encrypt

    def decrypt(self, encrypted_data):
        new_decrypt = ''
        for i in encrypted_data:
            for j in range(0, len(self.const) - 6):
                if i == self.const[j]:
                    new_decrypt = new_decrypt + self.const[j - 6]
                else:
                    pass
        return new_decrypt
