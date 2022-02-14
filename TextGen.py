from textgenrnn import textgenrnn
import random
class TextGeneration:
    _instance, _mafina = None, None
    def __new__(cls, M):
        if not hasattr(cls, '_inst'):
            TextGeneration._instance = super(TextGeneration, cls).__new__(cls)
            TextGeneration._mafina = M
            return TextGeneration._instance

    def __init__(self, M):
        self.strength = 0.55
        self.batchSize = 128
        self.textgen = textgenrnn(name='Result_model/Titles256x3',
                                weights_path='Result_model/Titles256x3_weights.hdf5 ',
                                vocab_path='Result_model/Titles256x3_vocab.json',
                                config_path='Result_model/Titles256x3_config.json')
        self.kharkiv_prefix_list = ['У Харкові ', 'Жителі харківщини ', 'На харківщині ', 'Харківська ', 'Під харковом ',
                      'Жителі Харкова ', 'В харківській області ', 'Харківські ', 'Харківський ']
        self.kyiv_prefix_list = ['У Київі ', 'Жителі харківщини ', 'На київщині ', "Київська ", "Під києвом ",
                                 "Жителі Київа ", "В київській області ", "Київські ", "Київський "]

    def generate_by_prefix(self, prefixList):
        return self.textgen.generate(temperature=self.strength, prefix=prefixList, return_as_list=True)[0]

    def generate_random(self):
        return self.textgen.generate(temperature=self.strength, return_as_list=True)[0]

    def generate_by_prefix_city(self, update, context, text):
        city = {
            '/kh': lambda: update.message.reply_text(
                self.generate_by_prefix(self.kharkiv_prefix_list[random.randrange(len(self.kharkiv_prefix_list)-1)])),
            '/kv': lambda: update.message.reply_text(
                self.generate_by_prefix(self.kyiv_prefix_list[random.randrange(len(self.kyiv_prefix_list)-1)]))
        }
        if text in city.keys():
            city[text]()
            return True
        else: return False
