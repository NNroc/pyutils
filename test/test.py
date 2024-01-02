import spacy  # 加载英文模型

# nlp = spacy.load("en_core_web_sm")  # 给定一个英文句子
nlp = spacy.load('en_core_web_sm', disable=['parser', 'ner'])  # 定义一个不对单词进行拆分的Tokenizer


class WhitespaceTokenizer:
    def __init__(self, vocab):
        self.vocab = vocab

    def __call__(self, text):
        words = text.split(' ')
        return spacy.tokens.Doc(self.vocab, words=words)


nlp.tokenizer = WhitespaceTokenizer(nlp.vocab)  # 输入英文句子
text = 'This is a test sentence for POS tagging X-T .'  # 创建一个Doc对象
doc = nlp(text)  # 获取每个单词的词性
for token in doc:
    print(token.text, token.pos_, token.tag_)
