from sparkai.llm.llm import ChatSparkLLM, ChunkPrintHandler
from sparkai.core.messages import ChatMessage

# 星火认知大模型Spark Max的URL值，其他版本大模型URL值请前往文档（https://www.xfyun.cn/doc/spark/Web.html）查看
SPARKAI_URL = 'wss://spark-api.xf-yun.com/v4.0/chat'
# 星火认知大模型调用秘钥信息，请前往讯飞开放平台控制台（https://console.xfyun.cn/services/bm35）查看
SPARKAI_APP_ID = '3322e568'
SPARKAI_API_SECRET = 'ZjhjNjU5ZDYyMTIxMjNmOTk0MjU5MjUz'
SPARKAI_API_KEY = 'a7555bcb3e1135275dfb32ec7a83cca0'
# 星火认知大模型Spark Max的domain值，其他版本大模型domain值请前往文档（https://www.xfyun.cn/doc/spark/Web.html）查看
SPARKAI_DOMAIN = '4.0Ultra'
tran = [
    "Gaoxin Hospital of The First Affilated Hospital of Anhui Medical University, Hefei, Anhui, 230088, China|Beijing Cancer Hospital, Beijing, Beijing, 100142, China|Fujian Province Oncology Hospital, Fuzhou, Fujian, 350014, China|Harbin Medical University Cancer Hospital, Harbin, Heilongjiang, 150081, China|Hunan Provincial Tumor Hospital/Division of Oncology, Changsha, Hunan, 410013, China|The first hospital of jilin university, Changchun, Jilin, 130021, China|Jilin Provincial Cancer Hospital, Changchun, Jilin, 130103, China|Tangdu Hospital of Fourth Military Medical University, Xi'an, Shanxi, 710000, China|Sichuan Province Cancer Hospital/Department of Pulmonary Tumor, Chengdu, Sichuan, 610041, China|West China Hospital, Sichuan University, Cancer center, Chengdu, Sichuan, 610041, China|The Second Affiliated Hospital of Zhejiang University College of Medicine, Hangzhou, Zhejiang, 310009, China|Sir Run Run Shaw Hospital of College of Medicine of Zhejiang University, Center for Oncology, Hangzhou, Zhejiang, 310016, China|Zhejiang Cancer Hospital, Hangzhou, Zhejiang, 310022, China|Fifth Medical Center of PLA General Hospital, Beijing, 100071, China|Beijing Chest Hospital, Capital Medical University, Beijing, 101149, China|Guangdong Provincial People's Hospital, Guangzhou, 510000, China|The First Affiliated Hospital Zhejiang University School of Medicine, Hangzhou, Zhejiang, 310003, China|General Hospital of Eastern Theater Command, Nanjing, Jiangsu, China|Shanghai Chest Hospital, Shanghai, 200030, China|Fudan University Shanghai Cancer Center, Shanghai, 200032, China|Zhongshan Hospital, Fudan University, Shanghai, 200032, China"
]

if __name__ == '__main__':
    spark = ChatSparkLLM(
        spark_api_url=SPARKAI_URL,
        spark_app_id=SPARKAI_APP_ID,
        spark_api_key=SPARKAI_API_KEY,
        spark_api_secret=SPARKAI_API_SECRET,
        spark_llm_domain=SPARKAI_DOMAIN,
        streaming=False,
    )
    for s in tran:
        # 输入内容
        system = "According to content, extract and return military related unit segments, separated by the symbol '|', such as: Tangdu Hospital of Fourth Military Medical University, Xi'an, Shanxi, 710000, China|Affiliated to the Army Medical University, Chongqing, Chongqing, 400038, China|...\n"
        content = "content: " + s
        messages = [ChatMessage(role="system", content=system),
                    ChatMessage(role="user", content=content), ]
        handler = ChunkPrintHandler()
        a = spark.generate([messages], callbacks=[handler])
        a = a.generations[0]
        a = a[0]
        a = a.message
        a = a.content
        print(a)
