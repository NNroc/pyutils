file_path = "cdr_20240125-0208_BSCELoss_both_s0=0.3_dropout=0.5_74.pubtator"  # 文件路径
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
            gold_re.append((line2[1], line2[2], line2[3]))
        elif len(line2) == 5:
            pre_re.append((line2[1], line2[2], line2[3]))

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
        fp += 1
fn = len(gold_re)
p = tp / (tp + fp)
r = tp / (tp + fn)
f1 = 2 * p * r / (p + r)
print()
