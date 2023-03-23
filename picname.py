import os
import shutil

temp = r"D:\tmp"
savefile = r'D:\V320-Socket'


def getpic_num(path):
    return len(os.listdir(path))


def savepic(path, num, savepath):
    pics = os.listdir(path)
    if len(pics) < 10:
        return
    for i in range(len(pics)):
        shutil.move(path+'\\'+pics[i], savepath+"\\"+'{:0>6d}'.format(num+i+1)+'.bmp')


if __name__ == "__main__":
    savepic(temp, getpic_num(savefile), savefile)
