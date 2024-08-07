import matplotlib.pyplot as plt
plt.rcParams['font.family'] = 'Microsoft YaHei'
# 读取文件
def read_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    return lines

# 解析数据
def parse_data(lines):
    data = []
    for line in lines:
        line = line.strip()
        if line:
            values = line.split()
            # 取倒数3列数据并转换为浮点数
            data_point = list(map(float, values[3:5]))
            data.append(data_point)
    return data

# 计算数据总和
def calculate_sum(data):
    sums = []
    for data_point in data:
        data_sum = sum(data_point)
        sums.append(data_sum)
    return sums

# 绘制图像
def plot_graph(sums):
    plt.plot(sums)
    plt.xlabel('迭代轮次/轮')
    plt.ylabel('损失换数值')
    # plt.title('Sum of Last 3 Columns')
    plt.grid(axis="y")
    plt.show()

# 主函数
def main(file_path):
    lines = read_file(file_path)
    data = parse_data(lines)
    sums = calculate_sum(data)
    plot_graph(sums)

# 输入文件路径
file_path = r'/home/kk/Desktop/yolov7/results.txt'  # 替换为你的文件路径
main(file_path)