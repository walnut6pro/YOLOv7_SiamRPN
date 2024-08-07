import json
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # 用于3D绘图
plt.rcParams['font.family'] = 'Microsoft YaHei'

def read_json(file_path):
    """读取并解析 JSON 文件，返回 x, y, z 值的列表"""
    with open(file_path, 'r') as file:
        data = json.load(file)
        x_values = [item['x'] for item in data if 'x' in item]
        y_values = [item['y'] for item in data if 'y' in item]
        z_values = [item['z'] for item in data if 'z' in item]
    return x_values, y_values, z_values

def plot_data(x_values_list, y_values_list, z_values_list, labels):
    """绘制三维散点图"""
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')  # 创建3D绘图区域

    for x_values, y_values, z_values, label in zip(x_values_list, y_values_list, z_values_list, labels):
        ax.scatter(x_values, y_values, z_values, label=label)  # 正确使用label参数

    ax.set_xlabel('X/m')
    ax.set_ylabel('Y/m')
    ax.set_zlabel('Z/m')
    # ax.set_title('3D Scatter Plot of X, Y, and Z Values from JSON Files')
    ax.legend()
    plt.show()

def main():
    # JSON 文件路径
    file_paths = [
        '/home/kk/Desktop/yolov7/for_graph/siamrpn_rpnsiam_true.json', 
        '/home/kk/Desktop/yolov7/for_graph/yolo+siamrpn_to_yolo_detect_true.json', 
        '/home/kk/Desktop/yolov7/for_graph/true_yolov7+siamrpn_true.json'
    ]
    labels = ['SiamRPN', 'YOLOv7', '融合检测跟踪算法']
    x_values_list = []
    y_values_list = []
    z_values_list = []

    for file_path in file_paths:
        x_values, y_values, z_values = read_json(file_path)
        x_values_list.append(x_values)
        y_values_list.append(y_values)
        z_values_list.append(z_values)

    plot_data(x_values_list, y_values_list, z_values_list, labels)

if __name__ == '__main__':
    main()
