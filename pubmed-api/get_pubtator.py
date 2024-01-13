from Bio import Entrez, Medline


def cmp(x):
    return int(x)


Entrez.email = "123@example.com"

search_results1 = Entrez.read(
    Entrez.esearch(db="pubmed", term="ebola virus", reldate=50000, retmax=99999, datetype="pdat", usehistory="y",
                   mindate="1976/01/01", maxdate="2023/01/01"))
count = int(search_results1["Count"])
print("Found %i results" % count)

search_results2 = Entrez.read(
    Entrez.esearch(db="pubmed", term="ebola hemorrhagic fever", reldate=50000, retmax=99999, datetype="pdat",
                   usehistory="y", mindate="1976/01/01", maxdate="2023/01/01"))
count = int(search_results2["Count"])
print("Found %i results" % count)

search_results = search_results1["IdList"] + search_results2["IdList"]
search_results = list(set(search_results))
search_results = sorted(search_results, key=cmp)
print(len(search_results))

num = 0

with open('./ebola.pubtator', 'w', encoding='utf-8') as file:
    for i in search_results:
        try:
            print(num, i)
            handle = Entrez.efetch(db="pubmed", id=i, rettype="medline", retmode="text")
            record = list(Medline.parse(handle))[0]
            title = record['TI'] if 'TI' in record else 'nan'  # 标题
            abtxt = record['AB'] if 'AB' in record else 'nan'  # 摘要
            ebola_num = title.lower().count('ebola') + abtxt.lower().count('ebola')
            if ebola_num < 2:
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

print()