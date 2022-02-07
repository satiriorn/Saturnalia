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
        self.strength = 0.6
        self.batchSize = 128
        self.textgen = textgenrnn(name='Result_model/Titles256x3',
                                weights_path='Result_model/Titles256x3_weights.hdf5',
                                vocab_path='Result_model/Titles256x3_vocab.json',
                                config_path='Result_model/Titles256x3_config.json')

    def generate(self, prefixList):
        #answer = self.textgen.generate(temperature=self.strength, return_as_list=True, max_gen_length=1000)[0]
        #while len(answer) == 0:
        #    answer = self.textgen.generate(temperature=self.strength, return_as_list=True)[0]

        answer = self.textgen.generate(temperature=self.strength, prefix=prefixList,
                                  return_as_list=True)[0]
        return answer


    def Answer(self, update, context):
        #answer = self.textgen.generate(temperature=self.strength, return_as_list=True, max_gen_length=1000)[0]
        answer = self.generate(str(update.message.text))
        if 'IMafinabot' in str(update): update.message.reply_text(answer)