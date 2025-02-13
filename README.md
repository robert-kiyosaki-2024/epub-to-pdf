# EPUB 转 PDF 转换工具

一个简单的命令行工具，用于将 EPUB 电子书批量转换为 PDF 格式。

## 功能描述

- 输入源文件目录路径，自动扫描该目录下所有 EPUB 格式文件
- 将扫描到的 EPUB 文件转换为 PDF 格式
- 转换后的 PDF 文件统一保存到 `output/pdf` 目录下
- 保持原文件名，仅更改扩展名为 .pdf

## 使用方法

1. 运行程序
2. 输入包含 EPUB 文件的目录路径
3. 程序自动处理所有 EPUB 文件
4. 转换完成的 PDF 文件将保存在 `output/pdf` 目录下

## 目录结构

```
epub-to-pdf/
├── epub-to-pdf.py # 主程序
├── requirements.txt # 依赖库
├── README.md # 说明文档
└── output/ # 输出目录 


## 依赖库

- ebooklib
- ebooklib-js
- ebooklib-js-cli


## 安装依赖

```bash
pip install -r requirements.txt
```


## 使用说明

```bash
python epub-to-pdf.py
```


## 注意事项

- 请确保输入的目录路径存在
- 转换过程中可能会遇到一些特殊情况，请根据错误提示进行调整
- 转换结果会保存在 `output/pdf` 目录下




## 更新日志

- 2024-01-01 初始化项目
- 2024-01-02 添加依赖库
- 2024-01-03 添加使用说明
- 2024-01-04 添加注意事项

