# 概述
基于改进后的YOLOv7和SiamRPN算法设计融合检测跟踪算法，通过目标检测结果更新跟踪模板，结合IoU来选择 相信跟踪或者检测结果，改进后算法在跟踪过程中持续检测跟踪精度提升60%   
# 融合检测跟踪算法流程图  
![image](https://github.com/user-attachments/assets/48a6ee51-de4c-4a40-83a2-8df380810015)
# 针对地面无人车的跟踪效果
![image](https://github.com/user-attachments/assets/cd31b40c-a3ea-4d2c-a9ed-aaf2a81751c3)
![image](https://github.com/user-attachments/assets/5b72d371-d2dd-4daa-9637-633da8c1a7b9)
# 检测成功率对比
![image](https://github.com/user-attachments/assets/7541a101-d075-46f9-9e97-8f047c8397b4)
# 结论
通过对比结果可知，单独SiamRPN算法处理速度最快但由于易受图像尺度变化的影响，短暂跟踪后容易丢失目标的中心位置。本文提出的融合检测跟踪算法综合了改进YOLOv7算法的高精度和SiamRPN跟踪算法的高实时性，在略微牺牲处理速度的情况下，将成功率提升至95%，在TX2平台上实现了13.15fps的帧率，满足了无人机着陆的实时性和准确性要求
