import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained("D:/code/github/utils-py/FreedomIntelligence7B", use_fast=True,
                                          trust_remote_code=True)
model = AutoModelForCausalLM.from_pretrained("D:/code/github/utils-py/FreedomIntelligence7B",
                                             device_map="auto", torch_dtype=torch.bfloat16, trust_remote_code=True)
messages = []
messages.append({"role": "user", "content": "肚子疼怎么办？"})
response = model.HuatuoChat(tokenizer, messages)
print(response)
