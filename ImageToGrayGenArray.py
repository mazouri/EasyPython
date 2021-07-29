# import cv module
import cv2 as cv
import numpy  as np
# from PyQt5 import QtWidgets
import tkinter as tk
import os

basex = 5
basey = 5

from tkinter import filedialog, dialog
import os
 
window = tk.Tk()
window.title('采集灰度数据')  # 标题
window.geometry('500x500')  # 窗口尺寸
 
file_path = ''
 
file_text = ''
 
text1 = tk.Text(window, width=50, height=10, bg='orange', font=('Arial', 12))
text1.pack()

# 85个0
default_data_zero="0000000000000000000000000000000000000000000000000000000000000000000000000000000000000"
 
## 读取文件 通过CV读取gray 生成数组存入对应表情文件
def generate_gray_array():
    '''
    打开文件
    :return:
    '''
    global file_path
    global file_text
    global fo
    file_path = filedialog.askdirectory(title=u'选择文件夹', initialdir=(os.path.expanduser('～/')))
    
    output_file_name = file_path.rpartition("/")
    
    fo = open(output_file_name[len(output_file_name) - 1] + "_temp.txt", "w+")
    print('打开文件夹：', file_path)

    filename_list = os.listdir(file_path)
    for i in filename_list:
        new_name = i.replace("图层 ", "")
        os.rename(file_path+"/"+i,file_path+"/"+new_name)
        print(new_name)
    
    for root,dirs,files in os.walk(file_path):
        fo.write(str("["))
        # 文件按照标题数字排序
        files.sort(key = lambda x: int(x[:-4]))
        for name in files:
            # print("111"+name);
            # print(os.path.join(root,name))
            if os.path.join(root,name).endswith("jpg") or os.path.join(root,name).endswith("png"):
                print("cv.imread"+name);
                # read image (support bmp jpg png tiff)
                # 1 color 2 gray
                img = cv.imread(os.path.join(root,name), 1)

                # set to gray
                gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

                # fo = open(os.path.join(root,name), "w")
                getGrayValue(img, gray)
                # fo.close()
            fo.write(str(","))
        fo.write(str("]"))
            
    file_text = fo.read();
    # print(file_text);
    # text1.insert('insert', file_text)
    fo.close()


    # 将数组写入对应文件，并产生每个关键帧对应显示时间
    ret_file = open(output_file_name[len(output_file_name) - 1] + ".txt", "w+")
    fp=output_file_name[len(output_file_name) - 1]+"_temp.txt"
    if file_path is not None:
        with open(file=fp, mode='r+', encoding='utf-8') as file:
            file_text = file.read()
            # print(file_text);
            # text1.insert('insert', file_text)

            array = eval(file_text)
            # print("#############"+str(array[0]==default_data_zero))

            ret_content = ""
            last_a = ""
            last_i = 0
            during_array = "{"
            during_array_len = 0
            during_repeat = 1
            for i in range(len(array)):
                # if (array[i]==default_data_zero):
                #     array[i]='0'
                tmp_str = str(array[i])
                if last_a == tmp_str:
                    during_repeat+=1
                else:
                    if i != 0:
                        during_array+=str(during_repeat) + ","
                        during_array_len+=1
                        during_repeat = 1

                    # c语言的数组用大括号
                    tmp_str1 = tmp_str.replace("[", "{")
                    tmp_str2 = tmp_str1.replace("]", "}")
                    ret_content += "\""+tmp_str2 + "\","
                    last_a = tmp_str

                if i == 0:
                    last_a = tmp_str
            
            during_array+=str(during_repeat) + ","
            during_array_len+=1

            ret_file.write(str("char * "+output_file_name[len(output_file_name) - 1] + "_buffer["+str(during_array_len)+"] = {"+ret_content+"};"))

            ret_file.write("\n\nconst uint8_t "+output_file_name[len(output_file_name) - 1] + "_during_array["+str(during_array_len)+"] = " + during_array + "};")

            ret_text = ret_file.read();
            # print(ret_text);
            text1.insert('insert', ret_text)
    ret_file.close()
    os.remove(fp) # 删除临时文件
                

## 读取图片对应坐标 灰度值 产生数组
def getGrayValue(img, gray):
    # print("getGrayValue");
    fo.write(str('"'))

    for j in range(5):
        for i in range(17):
            img1 = img.copy()
            cx = basex + i * 10
            cy = basey + j * 10
            # print("x : "+str(cx) + ", y : " +str(cy))
            g = gray[cy][cx]

            # 以下为了减少服务端下发数据，将0-255亮度值，按照每10%透明度分为10档（其中90%没有，当作100处理）
            if g < 21:
                g = 0
            elif g >=13 and g <=39:
                g = 1
            elif g >=40 and g <=65:
                g = 2
            elif g >=65 and g <=90:
                g = 3
            elif g >=91 and g <=115:
                g = 4
            elif g >=116 and g <=140:
                g = 5
            elif g >=141 and g <=165:
                g = 6
            elif g >=166 and g <=191:
                g = 7
            elif g >=192 and g <=217:
                g = 8
            elif g >=218 and g <=255:
                g = 9

            fo.write(str(g))
    
    fo.write(str('"'))
 

#generate_gray_array()

bt1 = tk.Button(window, text='打开文件夹', width=15, height=2, command=generate_gray_array)
bt1.pack()
 
window.mainloop()  # 显示
