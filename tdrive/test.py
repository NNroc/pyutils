import sys
import json

# 对文件的读取
file = open("./tdrive_input_original_edges_20220720.txt", "r", encoding="utf-8")

# 边
edges_data_features = []
# 遍历内容
eid = 0
have = 0
point1 = []
point2 = []
for line in file:
    data = line.replace("\n", "")
    if have == 0:
        data = data.split(",")
        point1 = [data[0], data[1]]
        have += 1
        continue
    elif have == 1:
        data = data.split(",")
        point2 = [data[0], data[1]]
        have += 1
        continue
    have = 0
    edge = {"type": "Feature", "properties": {"eid": eid, "raw_eid": 0, "highway": "primary"},
            "geometry": {"type": "LineString", "coordinates": [[point1[0], point1[1]], [point2[0], point2[1]]]}}
    # print(edge)
    eid += 1
    edges_data_features.append(edge)
edges_path = "tdrive_input_original_edges_20220720.json"
edges_data = {"type": "FeatureCollection", "features": edges_data_features}
edges = json.dumps(edges_data)

print(edges_path)

with open(edges_path, 'w') as f:
    f.write(edges)
