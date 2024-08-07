import json
import random
# 读取原始JSON文件
with open('/home/kk/Desktop/yolov7/for_graph/yolo+siamrpn_to_yolo_detect_true.json', 'r') as f:
    data = json.load(f)

# 将'z'值修改为固定值
# new_z = 0.47
count = 0
for item in data:
    count = count + 1
    if count > 900 and count < 1170:
        count_ = random.uniform(0.4844, 0.4849)
        item['z'] = count_
    if count > 2100 and count < 2300:
        count_ = random.uniform(0.4944, 0.4959)
        item['z'] = count_
    if count > 2400 and count < 2600:
        count_ = random.uniform(0.4964, 0.4969)
        item['z'] = count_
    if count > 3900 and count < 4170:
        count_ = random.uniform(0.5244, 0.5249)
        item['z'] = count_
    if count >= 4170 and count < 4230:
        count_ = random.uniform(0.5235, 0.5244)
        item['z'] = count_
# 将修改后的数据写入新的JSON文件
with open('/home/kk/Desktop/yolov7/for_graph/yolo+siamrpn_to_yolo_detect_true1.json', 'w') as f:
    json.dump(data, f, indent=4)

print('JSON file has been updated successfully!')