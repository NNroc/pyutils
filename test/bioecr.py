from transformers import BertTokenizer, BertForTokenClassification
from torch.optim import Adam
from torch.utils.data import DataLoader, TensorDataset
import torch
import datetime
import os
import json
import ast

set_a = {1, 2, 3, 4}
set_b = {2, 3}

# 检查set_a是否包含set_b
contains_b = set_b.issubset(set_a)
print(contains_b)  # 输出 False，因为set_b不是set_a的子集
print()


def order_score(pos):
    return pos[0] * 100 + pos[1]


def delete_invalid_spans(src, dst):
    data = []
    tps = {"ChemicalEntity": 0, "DiseaseOrPhenotypicFeature": 0, "GeneOrGeneProduct": 0,
           "SequenceVariant": 0, "OrganismTaxon": 0, "CellLine": 0}
    fps = {"ChemicalEntity": 0, "DiseaseOrPhenotypicFeature": 0, "GeneOrGeneProduct": 0,
           "SequenceVariant": 0, "OrganismTaxon": 0, "CellLine": 0}
    fns = {"ChemicalEntity": 0, "DiseaseOrPhenotypicFeature": 0, "GeneOrGeneProduct": 0,
           "SequenceVariant": 0, "OrganismTaxon": 0, "CellLine": 0}
    tp, fp, fn = 0, 0, 0
    with open(src, 'r', encoding='utf-8') as f:
        for line in f:
            data.append(json.loads(line))
    for entry in data:
        new_spans = []
        tp += len(entry['tp'])
        fn += len(entry['fn'])
        for span in entry['fp']:
            if order_score(span[0]) >= order_score(span[1]):
                print([span[0], span[1]])
                continue
            new_spans.append(span)
            fp += 1
        entry['fp'] = new_spans
        for span in entry['tp']:
            tps[span[2]] += 1
        for span in entry['fp']:
            fps[span[2]] += 1
        for span in entry['fn']:
            fns[span[2]] += 1

    p = tp / (tp + fp)
    r = tp / (tp + fn)
    f1 = p * r * 2 / (p + r + 1e-7)
    print('tp', tp, 'fp', fp, 'fn', fn)
    print('p', p, 'r', r, 'f1', f1)

    entity_name = "ChemicalEntity"
    p = tps[entity_name] / (tps[entity_name] + fps[entity_name])
    r = tps[entity_name] / (tps[entity_name] + fns[entity_name])
    f1 = p * r * 2 / (p + r + 1e-7)
    print(entity_name, 'tp:', tps[entity_name], 'fp:', fps[entity_name], 'fn:', fns[entity_name], "p:", p, "r:", r,
          "f1:", f1)

    entity_name = "DiseaseOrPhenotypicFeature"
    p = tps[entity_name] / (tps[entity_name] + fps[entity_name])
    r = tps[entity_name] / (tps[entity_name] + fns[entity_name])
    f1 = p * r * 2 / (p + r + 1e-7)
    print(entity_name, 'tp:', tps[entity_name], 'fp:', fps[entity_name], 'fn:', fns[entity_name], "p:", p, "r:", r,
          "f1:", f1)

    entity_name = "GeneOrGeneProduct"
    p = tps[entity_name] / (tps[entity_name] + fps[entity_name])
    r = tps[entity_name] / (tps[entity_name] + fns[entity_name])
    f1 = p * r * 2 / (p + r + 1e-7)
    print(entity_name, 'tp:', tps[entity_name], 'fp:', fps[entity_name], 'fn:', fns[entity_name], "p:", p, "r:", r,
          "f1:", f1)

    entity_name = "SequenceVariant"
    p = tps[entity_name] / (tps[entity_name] + fps[entity_name])
    r = tps[entity_name] / (tps[entity_name] + fns[entity_name])
    f1 = p * r * 2 / (p + r + 1e-7)
    print(entity_name, 'tp:', tps[entity_name], 'fp:', fps[entity_name], 'fn:', fns[entity_name], "p:", p, "r:", r,
          "f1:", f1)

    entity_name = "OrganismTaxon"
    p = tps[entity_name] / (tps[entity_name] + fps[entity_name])
    r = tps[entity_name] / (tps[entity_name] + fns[entity_name])
    f1 = p * r * 2 / (p + r + 1e-7)
    print(entity_name, 'tp:', tps[entity_name], 'fp:', fps[entity_name], 'fn:', fns[entity_name], "p:", p, "r:", r,
          "f1:", f1)

    entity_name = "CellLine"
    p = tps[entity_name] / (tps[entity_name] + fps[entity_name])
    r = tps[entity_name] / (tps[entity_name] + fns[entity_name])
    f1 = p * r * 2 / (p + r + 1e-7)
    print(entity_name, 'tp:', tps[entity_name], 'fp:', fps[entity_name], 'fn:', fns[entity_name], "p:", p, "r:", r,
          "f1:", f1)


# delete_invalid_spans('/py_project/biodoc/result/BioRED/me/BioRED-me_test_9181.json', '')
# delete_invalid_spans('/py_project/biodoc/result/BioRED/me/BioRED-me_cr_re_test_9057.json', '')
# print()

def has_duplicates(lst):
    # 转换列表为元组列表，以便可以将其转换为集合
    lst_tuples = [tuple(item.values()) for item in lst]
    unique_items = set(lst_tuples)
    # 比较集合的大小和列表的大小（注意这里比较的是元组的大小）
    return len(unique_items)


def r_common_e(list1, list2):
    # 将列表中的每个元素转换为字符串表示，以便可以作为字典的键
    list1_elements = [str(element) for element in list1]
    list2_elements = [str(element) for element in list2]

    list11 = [i for i in list1_elements if i not in list2_elements]
    list22 = [i for i in list2_elements if i not in list1_elements]
    return list11, list22


def pos2sents_id(sents, pos_id):
    sent_id = 0
    sent_pos_id = pos_id
    for sent in sents:
        if sent_pos_id >= len(sent):
            sent_id += 1
            sent_pos_id -= len(sent)
        else:
            break
    return sent_id, sent_pos_id


# 读取两个实体识别结果，对比
origin_file_path = "E:/code/githubuse/utils-py/test/cdr-me.json"
now_file_path = "E:/code/githubuse/utils-py/test/CDR-me_cr_re-me_test.json"

a, b = [], []
span_data, span_gold, span_tp, span_fp, span_fn, gold_num = [], [], [], [], [], 0
tp, fp, fn = 0, 0, 0
with open(origin_file_path, 'r') as f:
    for line in f:
        span_data.append(json.loads(line))
    for span in span_data:
        if len(span['tp']) != span['stat']['tp']:
            print()
        elif len(span['fp']) != span['stat']['fp']:
            print()
        elif len(span['fn']) != span['stat']['fn']:
            print()
        span_tp.append(span['tp'])
        span_fp.append(span['fp'])
        span_fn.append(span['fn'])
        tp += len(span['tp'])
        fp += len(span['fp'])
        fn += len(span['fn'])
        span_gold.append(span['tp'] + span['fn'])
        a.append(span['tp'] + span['fp'])
        gold_num = gold_num + len(span['tp']) + len(span['fn'])
origin_gold_data = span_gold
origin_tp = span_tp
origin_fp = span_fp
origin_fn = span_fn
origin_gold_num = gold_num
print(tp, fp, fn)

span_data, span_gold, span_tp, span_fp, span_fn, gold_num = [], [], [], [], [], 0
tp, fp, fn = 0, 0, 0
with open(now_file_path, 'r') as f:
    for line in f:
        span_data.append(json.loads(line))
    for span in span_data:
        if len(span['tp']) != span['stat']['tp']:
            print()
        elif len(span['fp']) != span['stat']['fp']:
            print()
        elif len(span['fn']) != span['stat']['fn']:
            print()
        span_tp.append(span['tp'])
        span_fp.append(span['fp'])
        span_fn.append(span['fn'])
        tp += len(span['tp'])
        fp += len(span['fp'])
        fn += len(span['fn'])
        span_gold.append(span['tp'] + span['fn'])
        b.append(span['tp'] + span['fp'])
        gold_num = gold_num + len(span['tp']) + len(span['fn'])
now_gold_data = span_gold
now_tp = span_tp
now_fp = span_fp
now_fn = span_fn
now_gold_num = gold_num
print(tp, fp, fn)

# 查看好在哪了
c_num, d_num = 0, 0
for i in range(len(origin_tp)):
    a[i], b[i] = r_common_e(a[i], b[i])
    if a[i] != b[i]:
        aa = a[i]
        aaa = b[i]
        print(i, aa)
        print(i, aaa)

c_num, d_num = 0, 0
for i in range(len(origin_tp)):
    a[i], b[i] = r_common_e(a[i], b[i])
    if a[i] != b[i]:
        aa = a[i]
        aaa = b[i]
        # print(a[i], b[i])
        for test1 in aa:
            for test12 in aaa:
                t1 = test1.split('], \'')[0]
                t2 = test12.split('], \'')[0]
                t3 = test1.split('], \'')[1]
                t4 = test12.split('], \'')[1]
                if t1 == t2 and t3 != t4:
                    print(i, test1, test12)

print()

# gold span
raw_train = json.load(open('E:/code/githubuse/utils-py/test/CDR-perfect.json', 'r', encoding='utf-8'))
gold_span = []
gold_span_2 = []
for sample in raw_train:
    entity_len = []
    spans = []
    spans_2 = []
    for e in sample['entities']:
        entity_len.append(len(e))
        for m in e:
            sent_id_s, sent_pos_id_s = pos2sents_id(sample['sents'], m['pos'][0])
            sent_id_e, sent_pos_id_e = pos2sents_id(sample['sents'], m['pos'][1])
            ms = [[sent_id_s, sent_pos_id_s], [sent_id_e, sent_pos_id_e], m['type']]
            if [[sent_id_s, sent_pos_id_s], [sent_id_e, sent_pos_id_e]] not in spans_2:
                spans_2.append([[sent_id_s, sent_pos_id_s], [sent_id_e, sent_pos_id_e]])
            spans.append([ms, m['name'], m['type_id'], m['pos'], m['type'], sample['title']])
    gold_span.append(spans)
    gold_span_2.append(spans_2)

# 查看origin忽视type的实体识别性能
all_tp, all_fp, all_fn, gold_tp = 0, 0, 0, 0
for title_i in range(len(origin_gold_data)):
    tp, fp, fn = 0, 0, 0
    preds = origin_tp[title_i] + origin_fp[title_i]
    for pred in preds:
        if [pred[0], pred[1]] in gold_span_2[title_i]:
            tp += 1
        else:
            fp += 1
    fn = len(gold_span_2[title_i]) - tp
    all_tp += tp
    all_fn += fn
    all_fp += fp
    gold_tp += len(gold_span_2[title_i])
p = all_tp / (all_tp + all_fp + 1e-7)
r = all_tp / (all_tp + all_fn + 1e-7)
f1 = (p * r * 2) / (p + r + 1e-7)
print(p, r, f1)
# 查看origin忽视type的实体识别性能
all_tp, all_fp, all_fn, gold_tp = 0, 0, 0, 0
for title_i in range(len(now_gold_data)):
    tp, fp, fn = 0, 0, 0
    preds = now_tp[title_i] + now_fp[title_i]
    for pred in preds:
        if [pred[0], pred[1]] in gold_span_2[title_i]:
            tp += 1
        else:
            fp += 1
    fn = len(gold_span_2[title_i]) - tp
    all_tp += tp
    all_fn += fn
    all_fp += fp
    gold_tp += len(gold_span_2[title_i])
p = all_tp / (all_tp + all_fp + 1e-7)
r = all_tp / (all_tp + all_fn + 1e-7)
f1 = (p * r * 2) / (p + r + 1e-7)
print(p, r, f1)
