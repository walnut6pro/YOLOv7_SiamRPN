import json
import matplotlib.pyplot as plt
import numpy as np


# 设置字体
plt.rcParams['font.family'] = 'Microsoft YaHei'


def read_json(file_path):
    """读取并解析 JSON 文件，返回 x 值的列表"""
    with open(file_path, 'r') as file:
        data = json.load(file)
        x_values = [item['z'] for item in data if 'z' in item]
    return x_values

def plot_data(x_values_list, labels):
    """绘制折线图"""
    plt.figure(figsize=(10, 5))  # 设置图形的大小
    for x_values, label in zip(x_values_list, labels):
        plt.plot(x_values, label=label)
    # plt.title('Z/m')
    plt.xlabel('帧数/帧')
    plt.ylabel('Z/m')
    plt.legend()
    plt.grid(True)
    plt.show()

def main():
    # JSON 文件路径
    file_paths = ['/home/kk/Desktop/yolov7/for_graph/siamrpn_rpnsiam_true.json', '/home/kk/Desktop/yolov7/for_graph/yolo+siamrpn_to_yolo_detect_true1.json', '/home/kk/Desktop/yolov7/for_graph/true_yolov7+siamrpn_true.json']
    labels = ['SiamRPN', 'YOLOv7', '融合检测跟踪算法']
    x_values_list = []

    # 读取每个文件中的 x 值
    for file_path in file_paths:
        x_values = read_json(file_path)
        x_values_list.append(x_values)

    # 绘制图表
    plot_data(x_values_list, labels)

if __name__ == '__main__':
    main()
