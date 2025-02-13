import os
import ebooklib
from ebooklib import epub
from pathlib import Path
from bs4 import BeautifulSoup
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.pdfbase.pdfmetrics import stringWidth
from reportlab.lib.units import inch
from datetime import datetime

def get_epub_files(directory):
    """扫描目录，返回所有 EPUB 文件的路径"""
    epub_files = []
    try:
        dir_path = Path(directory)
        if not dir_path.exists():
            raise FileNotFoundError(f"目录 '{directory}' 不存在")
        
        epub_files = list(dir_path.glob("**/*.epub"))
        if not epub_files:
            print(f"在目录 '{directory}' 中未找到 EPUB 文件")
            
    except Exception as e:
        print(f"扫描目录时出错: {str(e)}")
    
    return epub_files

def register_chinese_font():
    """注册中文字体"""
    try:
        # 尝试使用系统中文字体
        windows_font_paths = [
            "C:/Windows/Fonts/simsun.ttc",  # 宋体
            "C:/Windows/Fonts/simhei.ttf",  # 黑体
            "C:/Windows/Fonts/msyh.ttc"     # 微软雅黑
        ]
        
        for font_path in windows_font_paths:
            if os.path.exists(font_path):
                if "simsun" in font_path.lower():
                    pdfmetrics.registerFont(TTFont('SimSun', font_path))
                    return 'SimSun'
                elif "simhei" in font_path.lower():
                    pdfmetrics.registerFont(TTFont('SimHei', font_path))
                    return 'SimHei'
                elif "msyh" in font_path.lower():
                    pdfmetrics.registerFont(TTFont('MicrosoftYaHei', font_path))
                    return 'MicrosoftYaHei'
        
        raise Exception("未找到合适的中文字体")
        
    except Exception as e:
        print(f"注册中文字体时出错: {str(e)}")
        return None

def extract_text_from_epub(epub_path):
    """从 EPUB 文件中提取文本内容"""
    book = epub.read_epub(str(epub_path))
    chapters = []
    
    for item in book.get_items():
        if item.get_type() == ebooklib.ITEM_DOCUMENT:
            # 解析 HTML 内容
            soup = BeautifulSoup(item.get_content(), 'lxml')
            # 获取文本，保留基本段落结构
            text = soup.get_text('\n', strip=True)
            chapters.append(text)
    
    return '\n\n'.join(chapters)

def convert_epub_to_pdf(epub_path, output_dir):
    """将单个 EPUB 文件转换为 PDF"""
    try:
        # 创建输出目录
        output_dir = Path(output_dir)
        output_dir.mkdir(parents=True, exist_ok=True)
        
        # 生成带时间戳的文件名
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        output_filename = f"{epub_path.stem}_{timestamp}.pdf"
        output_path = output_dir / output_filename
        
        print(f"正在转换: {epub_path.name}")
        
        # 注册中文字体
        chinese_font = register_chinese_font()
        if not chinese_font:
            raise Exception("未能注册中文字体，无法继续转换")
        
        # 提取文本内容
        content = extract_text_from_epub(epub_path)
        
        # 创建 PDF 文档
        doc = SimpleDocTemplate(
            str(output_path),
            pagesize=A4,
            rightMargin=72,
            leftMargin=72,
            topMargin=72,
            bottomMargin=72
        )
        
        # 创建中文样式
        styles = getSampleStyleSheet()
        chinese_style = ParagraphStyle(
            'ChineseStyle',
            parent=styles['Normal'],
            fontName=chinese_font,
            fontSize=12,
            leading=16,
            wordWrap='CJK'  # 支持中文换行
        )
        
        # 将内容分段
        paragraphs = []
        for text in content.split('\n'):
            if text.strip():
                # 使用中文样式创建段落
                p = Paragraph(text, chinese_style)
                paragraphs.append(p)
        
        # 生成 PDF
        doc.build(paragraphs)
        
        print(f"转换完成: {output_path}")
        return True
        
    except Exception as e:
        print(f"转换文件 '{epub_path.name}' 时出错: {str(e)}")
        return False

def main():
    """主函数"""
    print("EPUB 转 PDF 转换工具")
    print("-" * 20)
    
    # 获取用户输入的目录路径
    input_dir = input("请输入包含 EPUB 文件的目录路径: ").strip()
    
    # 设置输出目录
    output_dir = Path("output/pdf")
    
    # 获取所有 EPUB 文件
    epub_files = get_epub_files(input_dir)
    
    if not epub_files:
        print("未找到需要转换的文件，程序退出")
        return
    
    print(f"\n找到 {len(epub_files)} 个 EPUB 文件")
    print("-" * 20)
    
    # 转换文件
    success_count = 0
    for epub_file in epub_files:
        if convert_epub_to_pdf(epub_file, output_dir):
            success_count += 1
    
    print("\n转换完成!")
    print(f"成功转换: {success_count}/{len(epub_files)} 个文件")
    print(f"转换后的文件保存在: {output_dir}")

if __name__ == "__main__":
    main() 