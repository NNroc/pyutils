file_path = "cdr_20240330-1521_BSCELoss_tree_s0=0.3_dropout=0.5_66.pubtator"  # 文件路径
gold_re = []
pre_re = []
# 打开文件
with open(file_path, "r", encoding="utf-8") as file:
    # 逐行读取文件内容
    for line in file:
        # 处理每一行的内容
        line1 = line.strip()
        line2 = line1.split('\t')
        if len(line2) == 4:
            gold_re.append((line2[0], line2[2], line2[3]))
        elif len(line2) == 5:
            pre_re.append((line2[0], line2[2], line2[3]))

ori_re = gold_re[:]
gold_num = len(gold_re)
pre_num = len(pre_re)
tp = 0
tn = 0
fp = 0
fn = 0
for pre in pre_re:
    if (pre[0], pre[1], pre[2]) in gold_re:
        tp += 1
        gold_re.remove((pre[0], pre[1], pre[2]))
    elif (pre[0], pre[2], pre[1]) in gold_re:
        tp += 1
        gold_re.remove((pre[0], pre[2], pre[1]))
    else:

        if (pre[0], pre[1], pre[2]) in ori_re or (pre[0], pre[2], pre[1]) in ori_re:
            print(pre[0], pre[1], pre[2])
            print('print repeat tp')
        fp += 1
fn = len(gold_re)
p = tp / (tp + fp + 1e-5)
r = tp / (tp + fn + 1e-5)
f1 = 2 * p * r / (p + r)
print(p, r, f1)
