# import translate
#
# translator = translate.translate_yandex()
#
# text = "hello world"
# inLang = "en"
# outLang = "ru"
# KEY = "trnsl.1.1.20191026T081403Z.ef5de0c71b13b15a.3fb33a6b1dd7c9c6f937fb6ffb803e40d271a71e"
#
# print(translator.translate_yandex(KEY, text, inLang, outLang))

import speechkit
token="AgAAAAAsHJhgAATuwWbeLLogYEKyh_JmCHj_evs"

recognator = speechkit.recognize(token)
file = "rec.opus"
folder = "b1geohkpjn64hcd0bb7g"
print(recognator.recognize(file, folder))
