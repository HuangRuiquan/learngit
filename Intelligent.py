import os
import shutil


path = r'D:\AI收图\Thru\芜湖中达\2022'
save_path = r'D:\AI收图\Thru\芜湖中达\2022_new'
ten_save = r'D:\AI标注\V5000\20230206\维修站_ten_pic'


def funtion(path, save_path, one_dir="ok", two_dir="oth", three_dir="00"):
    datedir_list = os.listdir(path)
    #print(datedir_list)
    for datedir in datedir_list:
        if os.path.isdir(path + "\\" + datedir):
            if datedir == "OK" or datedir == "NG":
                one_dir = datedir
                #funtion(path + "\\" + datedir, save_path)
            if datedir == "Chip" or datedir == "Other" or datedir == "IC" or datedir == 'thru':
                two_dir = datedir
            if datedir != "Land":
                funtion(path + "\\" + datedir, save_path, one_dir, two_dir, three_dir)
        if os.path.isfile(path + "\\" + datedir):
            #print(path + "\\" + datedir)
            if '.bmp' in datedir:
                three_dir = datedir.split("-")[5]
                dirpath = save_path+"\\"+one_dir+"\\"+two_dir+"\\"+three_dir+"\\"+str.split(path, "\\")[-1]
                if not os.path.exists(dirpath):
                    os.makedirs(dirpath)
                shutil.move(path + "\\" + datedir, dirpath+"\\"+datedir)
                print(dirpath+"\\"+datedir, '移动成功')


def pick_pic_one_dir(path, ten_save):
    dirlist = os.listdir(path)
    for d in dirlist:
        if os.path.isdir(path+"\\"+d):
            if os.path.isdir(path+"\\"+d + "\\" + (os.listdir(path+"\\"+d)[0])):
                pick_pic_one_dir(path+"\\"+d, ten_save)
            else:
                files = os.listdir(path+"\\"+d)
                if files.__len__() >= 10:
                    for i in range(10):
                        if not os.path.exists(ten_save+"\\" + (str.split(path+"\\"+d, ':')[1])):
                            os.makedirs(ten_save+"\\" + (str.split(path+"\\"+d, ':')[1]))
                        shutil.move(path+"\\"+d+"\\"+(files[i]), ten_save+"\\"+(str.split(path+"\\"+d, ':')[1])+"\\"+(files[i]))
                        print(files[i], '移动成功')
                else:
                    for f in files:
                        if not os.path.exists(ten_save+"\\" + (str.split(path+"\\"+d, ':')[1])):
                            os.makedirs(ten_save+"\\" + (str.split(path+"\\"+d, ':')[1]))
                        shutil.move(path+"\\"+d+"\\"+f, ten_save+"\\"+(str.split(path+"\\"+d, ':')[1])+"\\"+f)
                        print(f, '移动成功')


def move_file(src_path, dst_path):
    if not os.path.exists(dst_path):
        os.makedirs(dst_path)
    shutil.move(src_path, dst_path)
    print(dst_path, '移动成功')


if __name__ == "__main__":
    # funtion(path, save_path)
    pick_pic_one_dir(r"\\192.168.1.136\新建文件夹\new_维修站", ten_save)
