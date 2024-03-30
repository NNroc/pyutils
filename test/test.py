import spacy  # 加载英文模型

# # nlp = spacy.load("en_core_web_sm")  # 给定一个英文句子
# nlp = spacy.load('en_core_web_sm', disable=['parser', 'ner'])  # 定义一个不对单词进行拆分的Tokenizer
#
#
# class WhitespaceTokenizer:
#     def __init__(self, vocab):
#         self.vocab = vocab
#
#     def __call__(self, text):
#         words = text.split(' ')
#         return spacy.tokens.Doc(self.vocab, words=words)
#
#
# nlp.tokenizer = WhitespaceTokenizer(nlp.vocab)  # 输入英文句子
# text = 'This is a test sentence for POS tagging X-T .'  # 创建一个Doc对象
# doc = nlp(text)  # 获取每个单词的词性
# for token in doc:
#     print(token.text, token.pos_, token.tag_)

from transformers import BertTokenizer, BertForTokenClassification
from torch.optim import Adam
from torch.utils.data import DataLoader, TensorDataset
import torch

# 参数设置
max_seq_length = 128  # 可以根据需要调整
batch_size = 16
learning_rate = 2e-5
num_epochs = 3

# 预训练模型和分词器
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
model = BertForTokenClassification.from_pretrained('bert-base-uncased', num_labels=2)

# 示例文本数据（这里需要你提供真实的数据和标签）
texts = ["Steve Jobs was the CEO of Apple Inc.", "Bob Dylan is a famous singer."]
labels = [
    ["B-PER", "I-PER", "O", "B-ORG", "I-ORG", "O", "O", "B-PER", "I-PER", "O"],
    ["B-PER", "I-PER", "O", "B-ORG", "I-ORG", "O", "O", "B-PER", "I-PER", "O"]
]


# 分词和编码
def tokenize_and_encode(texts, tokenizer, max_length=max_seq_length):
    input_ids = []
    attention_masks = []
    token_type_ids = []

    for text in texts:
        bert_input = tokenizer.encode_plus(
            text,
            add_special_tokens=True,
            max_length=max_length,
            padding='max_length',
            return_attention_mask=True,
            truncation=True
        )
        input_ids.append(bert_input['input_ids'])
        attention_masks.append(bert_input['attention_mask'])
        token_type_ids.append(bert_input['token_type_ids'])

    input_ids = torch.tensor(input_ids)
    attention_masks = torch.tensor(attention_masks)
    token_type_ids = torch.tensor(token_type_ids)

    return input_ids, attention_masks, token_type_ids


# 数据集准备
input_ids, attention_masks, token_type_ids = tokenize_and_encode(texts, tokenizer)
dataset = TensorDataset(input_ids, attention_masks, token_type_ids, labels)

# 数据加载器
dataloader = DataLoader(dataset, batch_size=batch_size)

# 模型训练
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)
optimizer = Adam(model.parameters(), lr=learning_rate)

model.train()
for epoch in range(num_epochs):
    for batch in dataloader:
        # 将数据转移到相应的设备上
        batch = [item.to(device) for item in batch]
        inputs = {
            'input_ids': batch[0],
            'attention_mask': batch[1],
            'token_type_ids': batch[2],
            'labels': batch[3]
        }

        # 梯度清零
        optimizer.zero_grad()

        # 前向传播
        outputs = model(**inputs)

        # 计算损失
        loss = outputs.loss

        # 反向传播
        loss.backward()

        # 更新参数
        optimizer.step()

    print(f"Epoch {epoch + 1}/{num_epochs}, Loss: {loss.item()}")

# 模型评估（这里可以添加代码进行模型评估）
