import string
import random as r

class pwd_generator:
    files = ["data/list_a.txt", "data/list_b.txt", "data/countries.txt"]


    list_a = []
    list_b = []
    countries = []

    ab_lower = list(string.ascii_lowercase)
    ab_upper = list(string.ascii_uppercase)
    digits = list(string.digits)
    special_chars = list("$£%&#?")

    def __init__(self):
        self.readin_word_list(self.files[0], self.files[1], self.files[2])
        # print(self.leet_password())

    def readin_word_list(self, file_a, file_b, countries):

        file = open(file_a, "r")
        content = file.read()
        self.list_a = content.split("\n")
        file.close()
        # print("nouns: {}".format(self.nouns))

        file = open(file_b, "r")
        content = file.read()
        self.list_b = content.split("\n")
        file.close()
        # print("verbs: {}".format(self.verbs))

        file = open(countries, "r")
        content = file.read()
        self.countries = content.split("\n")
        file.close()

    def leet_password(self):
        s = []
        n = 2

        s.append(r.choice(self.list_a))
        s.append(r.choice(self.list_b).capitalize())

        for i in range(n):
            s.append(r.choice(self.digits))

        for i in range(n):
            s.append(r.choice(self.special_chars))

        password = "".join(s)
        # leet = {'a': '4', 'i': '1', 'o': '0', 'A': '4', 'I': '1', 'O': '0'}
        # password = "".join(leet.get(char, char) for char in generated)
        return password

    def random_password(self, pwd_length):

        pwd = []

        lc = 0
        uc = 0
        sc = 0
        nc = 0

        if pwd_length == 8:
            lc = 2
            uc = 2
            sc = 2
            nc = 2
        elif pwd_length == 10:
            lc = 3
            uc = 2
            sc = 2
            nc = 3
        elif pwd_length == 12:
            lc = 4
            uc = 3
            sc = 2
            nc = 3

        for i in range(lc):
            pwd.append(r.choice(self.ab_lower))

        for i in range(uc):
            pwd.append(r.choice(self.ab_upper))

        for i in range(sc):
            pwd.append(r.choice(self.special_chars))

        for i in range(nc):
            pwd.append(r.choice(self.digits))

        # print("".join(pwd) + " " + str(pwd_length))

        r.shuffle(pwd)
        password = "".join(pwd)
        return password

    def country_name_password(self):
        pwd = []
        n = 2

        pwd.append(r.choice(self.countries).capitalize())

        for i in range(n):
            pwd.append(r.choice(self.digits))

        for i in range(n):
            pwd.append(r.choice(self.special_chars))

        password = "".join(pwd)
        return password
