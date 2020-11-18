import binascii
import sys
from Crypto.Cipher import AES

#암호화할지 복호화할지 결정 
eord = input("encrypt or decrypt?: ")

class AESCBC:
    def __init__(self,key):
        self.key = key
        self.iv = '0123456789012345'
        self.BS = 16
        #패딩처리
        self.pad = lambda s: s + (self.BS - len(s) % self.BS) * chr(self.BS - len(s) % self.BS)
        self.unpad = lambda s: s[0:-ord(s[-1])]

    def encrypt(self, data): #암호화
        pad_data = self.pad(data)
        #aes cbc생성
        cipher = AES.new(self.key, AES.MODE_CBC, self.iv)
        encrypt = cipher.encrypt(pad_data)
        #바이너리데이터를 16진수문자열로변환
        result = binascii.hexlify(encrypt)
        #암호화한파일생성
        sys.stdout = open('encryptfile.txt', 'w')
        print(result)
        return

    def decrypt(self, data): #복호화
        # 16진수문자열을 바이너리데이터로반환
        enc = binascii.unhexlify(data[2:len(data)-2])
        # aes cbc생성
        cipher = AES.new(self.key, AES.MODE_CBC, self.iv)
        decrypt = cipher.decrypt(enc)
        #키값이 일치하지않으면 에러메세지출력 후, 종료됨
        try :
            decrypted_text = decrypt.decode('utf8')
        except (UnicodeDecodeError):
            print("error : 키값이 일치하지않음 ")
            return
        result = self.unpad(decrypted_text)
        sys.stdout = open('decryptfile.txt', 'w')
        print(result)
        return

if __name__ == '__main__':
    if (eord == 'e'):
        to_encrypt = input("암호화할파일명: ") #infile.txt
        key = input("key값을 입력하세요 : ") #1234567890123456
        aes = AESCBC(key)
        file = open(to_encrypt,'r')
        text = file.read()
        aes.encrypt(text)
    elif (eord =='d'):
        to_decrypt = input("복호화할 파일명: ") #encryptfile.txt
        key = input("key값을 입력하세요 : ")
        aes = AESCBC(key)
        file = open(to_decrypt, 'r')
        text = file.read()
        aes.decrypt(text)
    else:
        print("press [e or d] key")