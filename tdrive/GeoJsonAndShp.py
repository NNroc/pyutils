import geopandas as gpd
import sys
import osgeo.ogr as ogr
import osgeo.osr as osr
import json

# 在RoadRunner生成json数据后运行
# python RoadRunner/GeoJsonAndShp.py ./lida_20220422_0411_0418/json_graph_output/lida.json ./lida_20220422_0411_0418/json_graph_output ./lida_20220422_0411_0418/rn
if __name__ == '__main__':
    # RoadRunner生成json数据的地址 ./lida_20220422_0411_0418/json_graph_output/lida.json
    # print(sys.argv[1])
    # shp文件生成的位置地址 ./lida_20220422_0411_0418/json_graph_output ./lida_20220422_0411_0418/rn
    # 对json文件的读取
    jsonFile = open('tdrive_input_original_edges_20220720.json', "r", encoding="utf-8")
    jsonFile = json.load(jsonFile)

    # 点
    # { "type": "Feature", "properties": { "FID": 0 }, "geometry": { "type": "Point", "coordinates": [ 116.3894407, 39.9062721 ] } },
    # vertices = jsonFile["vertices"]
    # nodes_data_features = []
    # # 遍历内容
    # for vertexId in range(len(vertices)):
    #     # print(vertices[str(vertexId)])
    #     lat = vertices[str(vertexId)][0]
    #     lng = vertices[str(vertexId)][1]
    #     vertex = {"type": "Feature", "properties": {"FID": vertexId},
    #               "geometry": {"type": "Point", "coordinates": [lng, lat]}}
    #     nodes_data_features.append(vertex)
    # nodes_path = sys.argv[2] + 'nodes.json'
    # nodes_data = {"type": "FeatureCollection", "features": nodes_data_features}
    # nodes = json.dumps(nodes_data)

    # 边
    # { "type": "Feature", "properties": { "eid": 0, "raw_eid": 4231222, "highway": "primary" }, "geometry": { "type": "LineString", "coordinates": [ [ 116.3894407, 39.9062721 ], [ 116.3894463, 39.9060115 ] ] } },
    # edges = jsonFile["edges"]
    # edges_data_features = []
    # # 遍历内容
    # eid = 0
    # for edgeId in edges:
    #     point1 = edgeId[0]
    #     point2 = edgeId[1]
    #     point1 = vertices[str(point1)]
    #     point2 = vertices[str(point2)]
    #     edge = {"type": "Feature", "properties": {"eid": eid, "raw_eid": 0, "highway": "primary"},
    #             "geometry": {"type": "LineString", "coordinates": [[point1[1], point1[0]], [point2[1], point2[0]]]}}
    #     # print(edge)
    #     eid += 1
    #     edges_data_features.append(edge)
    # edges_path = sys.argv[2] + 'edges.json'
    # edges_data = {"type": "FeatureCollection", "features": edges_data_features}
    # edges = json.dumps(edges_data)
    #
    # print(nodes_path)
    # print(edges_path)
    #
    # # 生成需要的json文件
    # with open(nodes_path, 'w') as f:
    #     f.write(nodes)
    # with open(edges_path, 'w') as f:
    #     f.write(edges)

    # # 将json生成到对应位置，后面通过testshp将json生成shp
    # nodes_path = 'G:/githubuse/DeepMG-nbhd_dist/data/tdrive_lida_' + date + '/rn/nodes.json'
    # edges_path = 'G:/githubuse/DeepMG-nbhd_dist/data/tdrive_lida_' + date + '/rn/edges.json'
    # with open(nodes_path, 'w') as f:
    #     f.write(nodes)
    # with open(edges_path, 'w') as f:
    #     f.write(edges)
    #
    # # shapefile = 'G:/githubuse/DeepMG-nbhd_dist/data/tdrive_sample/rn/nodes.shp'
    # # outfile = 'G:/githubuse/DeepMG-nbhd_dist/data/tdrive_sample/rn/nodes.json'
    shape_edges = './edges.shp'
    shape_nodes = './nodes.shp'
    json_edges = './edges.json'
    json_nodes = './nodes.json'
    #
    # GeoJson to shp
    data = gpd.read_file(json_edges)
    data.to_file(shape_edges, driver='ESRI Shapefile', encoding='utf-8')
    data = gpd.read_file(json_nodes)
    data.to_file(shape_nodes, driver='ESRI Shapefile', encoding='utf-8')
