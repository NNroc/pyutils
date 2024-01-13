from Bio import Entrez, Medline


def cmp(x):
    return int(x)


Entrez.email = "123@example.com"
term = "ebola[Title/Abstract]"

search_results1 = Entrez.read(
    Entrez.esearch(db="pubmed", term=term, reldate=50000, retmax=99999, datetype="pdat", usehistory="y",
                   mindate="2014/01/01", maxdate="2024/01/01"))
count = int(search_results1["Count"])
print("Found %i results" % count)

search_results = search_results1["IdList"]
search_results = list(set(search_results))
search_results = sorted(search_results, key=cmp)
print(len(search_results))

handle = Entrez.efetch(db="pubmed", id=search_results, rettype="medline", retmode="text")
records = list(Medline.parse(handle))
num = 0

with open('./ebola.pubtator', 'w', encoding='utf-8') as file:
    for record in records:
        try:
            i = record['PMID']
            print(record['PMID'])
            title = record['TI'] if 'TI' in record else 'nan'  # 标题
            abtxt = record['AB'] if 'AB' in record else 'nan'  # 摘要
            ebola_num = title.lower().count('ebola') + abtxt.lower().count('ebola')
            ebola_all = title.lower().count('ebola') + abtxt.lower().count('ebola') \
                        + abtxt.count('EVD') + abtxt.count('EBOV') + abtxt.count('EHF')
            if ebola_num < 2:
                print(title)
                print(abtxt)
                continue
            if ebola_all < 5:
                print(title)
                print(abtxt)
                continue
            if title == 'nan' or abtxt == 'nan' or len(abtxt) < 128:
                print(title)
                print(abtxt)
                continue
            file.write(i + "|t|" + title + '\n' + i + "|a|" + abtxt + '\n' + '\n')
            num += 1
        except ConnectionResetError:
            print(i)
