from data.aligned_dataset import *
from options.train_options import TrainOptions
import os
from PIL import Image

'''
convert pix2pix images to cyclegan images

python convert_data.py --trans_yn False --phase train --data_from .\\datasets\\facades --data_to .\\datasets\\facades_cycle_gan --trans_yn False
'''

if __name__ == '__main__':
    opt = TrainOptions().parse()
    from_d = AlignedDataset(opt)
    to_dir = opt.data_to
    if not os.path.isdir(to_dir): os.mkdir(to_dir)
    to_trainA = os.path.join(to_dir,opt.phase + 'A')
    to_trainB = os.path.join(to_dir,opt.phase + 'B')
    os.mkdir(to_trainA),os.mkdir(to_trainB)
    for ddict in from_d:
        A,B,A_path,B_path = ddict['A'], ddict['B'], ddict['A_paths'],ddict['B_paths']
        (_,A_name),(_,B_name) = os.path.split(A_path),os.path.split(B_path)
        A_dir,B_dir = os.path.join(to_trainA,A_name),os.path.join(to_trainB,B_name)
        A.save(A_dir),B.save(B_dir)