import sys
import os


for i in range(1, 5):
    os.system("python demo/demoFull.py configs/faster_rcnn_r50_augfpn_1x.py work_dirs/faster_rcnn_r50_augfpn_1x/latest.pth demo/results/huanjiao{}.txt ../../huanjiao/segImgFull/huanjiao{}/".format(i, i))
