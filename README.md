DeepVisionHTML is a comprehensive project that integrates YOLO-based object detection with dynamic HTML generation. It utilizes deep learning models to detect objects in images and videos, and automatically creates HTML pages to visualize the results, offering an efficient solution for real-time detection and web-based presentation.

# Project Structure
```
project/
├── configs/                        # 模型配置文件
│   ├── yolor_csp.cfg
│   ├── yolor_csp_x.cfg
│   ├── yolor_p6.cfg
│   ├── yolor_w6.cfg
│   ├── yolov4_csp.cfg
│   ├── yolov4_csp_x.cfg
│   ├── yolov4_p6.cfg
│   └── yolov4_p7.cfg
├── data/                           # 数据和超参数文件
│   ├── coco.names                  # 类别名称文件
│   ├── coco.yaml                   # 数据集配置文件
│   ├── hyp.finetune.1280.yaml      # 超参数配置文件
├── models/                         # 模型定义文件
│   ├── __init__.py
│   ├── export.py
│   └── models.py
├── scripts/                        # 训练和推理脚本
│   ├── train.py
│   └── detect.py
├── utils/                          # 实用工具
│   ├── __init__.py
│   ├── datasets.py
│   ├── general.py
│   ├── google_utils.py
│   ├── parse_config.py
│   └── torch_utils.py
├── inference/                      # 推理过程中使用的输入和输出文件夹
│   ├── input/
│   └── output/
├── weights/                        # 预训练和训练后的模型权重文件
│   └── yolor_p6.pt
├── requirements.txt                # 项目依赖
├── README.md                       # 项目说明
└── devops.html                     # 生成的HTML文件
```