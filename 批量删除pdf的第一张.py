import os
from PyPDF2 import PdfReader, PdfWriter
def remove_first_page(pdf_path, output_path):
    with open(pdf_path, 'rb') as infile:
        reader = PdfReader(infile)
        writer = PdfWriter()
        num_pages = len(reader.pages)
        if num_pages > 1:
            for page_num in range(1, num_pages):  # Skip the first page (page_num=0)
                writer.add_page(reader.pages[page_num])
            with open(output_path, 'wb') as outfile:
                writer.write(outfile)
        else:
            print(f'Warning: {pdf_path} has only one page. Skipping.')
def batch_remove_first_page(input_folder, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    for filename in os.listdir(input_folder):
        if filename.endswith('.pdf'):
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, filename)
            try:
                remove_first_page(input_path, output_path)
                print(f'Successfully removed first page from {filename}')
            except Exception as e:
                print(f'Error processing {filename}: {str(e)}')
# 示例用法
input_folder = r'C:\Users\Administrator\Desktop\shiyan'  # 输入文件夹路径
output_folder = r'C:\Users\Administrator\Desktop\shiyan'  # 输出文件夹路径
batch_remove_first_page(input_folder, output_folder)
