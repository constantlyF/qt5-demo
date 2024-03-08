from PIL import Image

# 打开图片文件
image = Image.open('datasource.png')

# 将图片保存为 SVG 格式
image.save('datasource.svg')
