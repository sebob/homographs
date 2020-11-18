import tldextract
import idna
import random
from library import domain as domains_tool

class Unicodes:

    def __init__(self, url, show_all=0):
        self.show_all = show_all
        self.url = url
        self.url_extract = tldextract.extract(self.url.lower())
        self.full_url = self.domain = self.url_extract.domain
        self.chars = []

        # copy & past from https://github.com/elceef/dnstwist/blob/e7857e7e63def12cc457a96dc76cf405c614a85e/dnstwist.py#L244
        self.glyphs = {
            'a': [u'à', u'á', u'â', u'ã', u'ä', u'å', u'ɑ', u'ạ', u'ǎ', u'ă', u'ȧ', u'ą'],
            'b': ['d', 'lb', u'ʙ', u'ɓ', u'ḃ', u'ḅ', u'ḇ', u'ƅ'],
            'c': ['e', u'ƈ', u'ċ', u'ć', u'ç', u'č', u'ĉ'],
            'd': ['b', 'cl', 'dl', u'ɗ', u'đ', u'ď', u'ɖ', u'ḑ', u'ḋ', u'ḍ', u'ḏ', u'ḓ'],
            'e': ['c', u'é', u'è', u'ê', u'ë', u'ē', u'ĕ', u'ě', u'ė', u'ẹ', u'ę', u'ȩ', u'ɇ', u'ḛ'],
            'f': [u'ƒ', u'ḟ'],
            'g': ['q', u'ɢ', u'ɡ', u'ġ', u'ğ', u'ǵ', u'ģ', u'ĝ', u'ǧ', u'ǥ'],
            'h': ['lh', u'ĥ', u'ȟ', u'ħ', u'ɦ', u'ḧ', u'ḩ', u'ⱨ', u'ḣ', u'ḥ', u'ḫ', u'ẖ'],
            'i': ['1', 'l', u'í', u'ì', u'ï', u'ı', u'ɩ', u'ǐ', u'ĭ', u'ỉ', u'ị', u'ɨ', u'ȋ', u'ī'],
            'j': [u'ʝ', u'ɉ'],
            'k': ['lk', 'ik', 'lc', u'ḳ', u'ḵ', u'ⱪ', u'ķ'],
            'l': ['1', 'i', u'ɫ', u'ł'],
            'm': ['n', 'nn', 'rn', 'rr', u'ṁ', u'ṃ', u'ᴍ', u'ɱ', u'ḿ'],
            'n': ['m', 'r', u'ń', u'ṅ', u'ṇ', u'ṉ', u'ñ', u'ņ', u'ǹ', u'ň', u'ꞑ'],
            'o': ['0', u'ȯ', u'ọ', u'ỏ', u'ơ', u'ó', u'ö'],
            'p': [u'ƿ', u'ƥ', u'ṕ', u'ṗ'],
            'q': ['g', u'ʠ'],
            'r': [u'ʀ', u'ɼ', u'ɽ', u'ŕ', u'ŗ', u'ř', u'ɍ', u'ɾ', u'ȓ', u'ȑ', u'ṙ', u'ṛ', u'ṟ'],
            's': [u'ʂ', u'ś', u'ṣ', u'ṡ', u'ș', u'ŝ', u'š'],
            't': [u'ţ', u'ŧ', u'ṫ', u'ṭ', u'ț', u'ƫ'],
            'u': [u'ᴜ', u'ǔ', u'ŭ', u'ü', u'ʉ', u'ù', u'ú', u'û', u'ũ', u'ū', u'ų', u'ư', u'ů', u'ű', u'ȕ', u'ȗ', u'ụ'],
            'v': [u'ṿ', u'ⱱ', u'ᶌ', u'ṽ', u'ⱴ'],
            'w': ['vv', u'ŵ', u'ẁ', u'ẃ', u'ẅ', u'ⱳ', u'ẇ', u'ẉ', u'ẘ'],
            'y': [u'ʏ', u'ý', u'ÿ', u'ŷ', u'ƴ', u'ȳ', u'ɏ', u'ỿ', u'ẏ', u'ỵ'],
            'z': [u'ʐ', u'ż', u'ź', u'ᴢ', u'ƶ', u'ẓ', u'ẕ', u'ⱬ']
        }

        for char in self.glyphs:
            if char in self.domain:
                self.chars.append(char)

    def get_unicodes(self):
        return self.glyphs

    def gen(self):
        full_url = self.full_url

        for char in self.domain:
            if char in self.glyphs:
                full_url = full_url.replace(char, "[{} x {}]".format(char, len(self.glyphs[char])))
                special_chars = self.glyphs[char]
                for special_char in special_chars:
                    full_domain = "{}.{}".format(
                        idna.encode(self.domain.replace(char, "{}".format(special_char)), uts46=True).decode('utf8'),
                        self.url_extract.suffix)
                    ip = domains_tool.Domain.check_ip(full_domain)
                    if ip:
                        hopp = domains_tool.Domain.check_hopp(full_domain)
                    else:
                        hopp = '?'

                    if self.show_all:
                        print("sign: {}, {}.{} => {} [{}], {}".format(
                            char,
                            self.domain.replace(char, "{}".format(special_char)),
                            self.url_extract.suffix,
                            full_domain,
                            ip,
                            hopp
                        ))
                    elif ip:
                        print("sign: {}, {}.{} => {} [{}], {}".format(
                            char,
                            self.domain.replace(char, "{}".format(special_char)),
                            self.url_extract.suffix,
                            full_domain,
                            ip,
                            hopp
                        ))


    def random_domain(self, n):
        random_special_char = []
        for char in self.chars:
            if char in self.domain:
                random_special_char.append([char, random.choice(self.glyphs[char])])

        domain = self.domain

        for char in range(n):
            p = random.choice(random_special_char)
            random_special_char.remove(p)
            domain = domain.replace(p[0], p[1])

        full_domain = "{}.{}".format(domain, self.url_extract.suffix)
        ip = domains_tool.Domain.check_ip(full_domain)

        print("\n------------------------------------------------------\ndomain:{}, IDN: {}.{}, [{}]".format(
            full_domain,
            idna.encode(domain, uts46=True).decode('utf8'),
            self.url_extract.suffix,
            ip
        ))