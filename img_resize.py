# -*- coding: utf-8 -*-
import os

from PIL import Image


class ThumbnailImg:
    """
    缩略图类
    """

    def __init__(self, size):
        self.size = size
        self.loc_pwd = os.getcwd()
        self.result_path = os.path.join(self.loc_pwd, 'thumbnailimgs')
        if not os.path.exists(self.result_path):
            os.mkdir(self.result_path)
        self.origin_pwd = os.path.join(self.loc_pwd, 'imgs')
        print('正在读取文件。。。')
        self.loc_img_list = os.listdir(self.origin_pwd)
        print(f'检索到{len(self.loc_img_list)}个图片。')

    def resize(self):
        self.size = int(self.size)
        for img in self.loc_img_list:
            print(f'正在处理{img}...')
            img_path = os.path.join(self.origin_pwd, img)
            im = Image.open(img_path)
            mode = im.mode
            if mode not in ('L', 'RGB'):
                if mode == 'RGBA':
                    # 透明图片需要加白色底
                    alpha = im.split()[3]
                    bgmask = alpha.point(lambda x: 255 - x)
                    im = im.convert('RGB')
                    im.paste((255, 255, 255), None, bgmask)
                else:
                    im = im.convert('RGB')
            else:
                pass
            width, height = im.size
            reim = im.resize((int(width / self.size), int(height / self.size)), Image.ANTIALIAS)
            name, ext = img.split('.')
            savename = name + '_resize_' + str(self.size) + '.' + ext
            reim.save(os.path.join(self.result_path, savename), quality=100)

    def thumbnail(self):
        for img in self.loc_img_list:
            print(f'正在处理{img}...')
            img_path = os.path.join(self.origin_pwd, img)
            im = Image.open(img_path)
            mode = im.mode
            if mode not in ('L', 'RGB'):
                if mode == 'RGBA':
                    # 透明图片需要加白色底
                    alpha = im.split()[3]
                    bgmask = alpha.point(lambda x: 255 - x)
                    im = im.convert('RGB')
                    im.paste((255, 255, 255), None, bgmask)
                else:
                    im = im.convert('RGB')
            im = Image.open(img_path)
            reim = im.resize((int(self.size[0]), int(self.size[1])), Image.ANTIALIAS)
            name, ext = img.split('.')
            savename = name + '_thumbnail_' + str(self.size[0]) + '_' + str(self.size[1]) + '.' + ext
            reim.save(os.path.join(self.result_path, savename), quality=100)

    def main(self):
        if isinstance(self.size, list):
            self.thumbnail()
        else:
            self.resize()
        print('处理完成，请在thumbnailimgs下查看')


if __name__ == '__main__':
    print(
        """
        将要转换的图片放入 imgs 文件夹中。
        转换结果保存在程序所在目录下的thumbnailimgs下。
        
        正在初始化程序。。。
        """
    )
    loc_pwd = os.getcwd()
    origin_pwd = os.path.join(loc_pwd, 'imgs')
    if not os.path.exists(origin_pwd):
        os.mkdir(origin_pwd)
        print('创建 imgs 文件夹')
    print('请将要转换的图片放入 imgs 文件夹中，放入完成后请按任意键继续。。。')
    input()
    print("""
        请输入要转换的类型：
        
        1) 等比例缩小    2) 指定分辨率缩小
        
        """)
    flag = input('请输入：')
    if flag == '1':
        proportion = input("请输入要缩小的比例大小：")
        ThumbnailImg(size=proportion).main()
    elif flag == '2':
        proportion = input('请输入要缩小的尺寸大小用/分割，ex：x/y，请输入：')
        proportion = proportion.split('/')
        ThumbnailImg(size=proportion).main()
    else:
        print('请输入正确的类型代码！')
    input('按任意键退出。。。')
