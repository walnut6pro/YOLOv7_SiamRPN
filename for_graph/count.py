import json

# 读取原始JSON文件
with open('/home/kk/Desktop/yolov7/for_graph/yolo+siamrpn_to_yolo_detect_true.json', 'r') as f:
    data = json.load(f)

count_all = 0
# 将'z'值修改为固定值
# new_z = 0.47 
for item in data:
    count_all = count_all + 1
    if count_all > 900 and count_all < 1078:
        item['z'] = count_all / 2000
    # if item['y'] < -1.0:
    #     count_y = count_y + 1

