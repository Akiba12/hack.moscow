class translate_yandex:

    def __init__ (self):
        None

    def translate_yandex(self, KEY, mytext, inLang, outLang):
        import requests

        URL = "https://translate.yandex.net/api/v1.5/tr.json/translate"  #это адрес для обращения к API


        params = {
            "key": KEY,
            "text": mytext,
            "lang": (inLang + '-' + outLang)  #Здесь мы указываем с какого языка на какой мы делаем переводим
        }
        response = requests.get(URL ,params=params)
        if response.json()['code'] != 200:
            raise Exception("It's error with translation: {}".format(response.json()))
        else:
            return response.json()['text']
