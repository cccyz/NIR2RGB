import os
from data.base_dataset import BaseDataset, get_params, get_transform
from data.image_folder import make_dataset
import torch
from PIL import Image
import torchvision.transforms as transform


class AlignedDataset(BaseDataset):
    """A dataset class for paired image dataset.

    It assumes that the directory '/path/to/data/train' contains image pairs in the form of {A,B}.
    During test time, you need to prepare a directory '/path/to/data/test'.
    """

    def __init__(self, opt):
        """Initialize this dataset class.

        Parameters:
            opt (Option class) -- stores all the experiment flags; needs to be a subclass of BaseOptions
        """
        BaseDataset.__init__(self, opt)
        self.dir_AB = os.path.join(opt.dataroot, opt.phase)  # get the image directory
        #self.AB_paths = sorted(make_dataset(self.dir_AB, opt.max_dataset_size))  # get image paths
        self.AB_paths =[]
        for self.root, self.dirs, self.files in os.walk(self.dir_AB):
            for self.dir in self.dirs:
                self.full_name = os.path.join(self.root, self.dir)
                self.AB_paths.append(self.full_name)

        assert(self.opt.load_size >= self.opt.crop_size)   # crop_size should be smaller than the size of loaded image
        self.input_nc = self.opt.output_nc if self.opt.direction == 'BtoA' else self.opt.input_nc
        self.output_nc = self.opt.input_nc if self.opt.direction == 'BtoA' else self.opt.output_nc

    def __getitem__(self, index):
        #输出的是一个14的tensor
        global B, B_transform
        lisA = []
        lisB = []
        path = self.AB_paths[index]
        for i in range(1,15):
          name = 'data_%03d.png'%i
          AB = Image.open(os.path.join(path, name)).convert('RGB')
          # split AB image into A and B
          w, h = AB.size
          w2 = int(w / 2)
          A = AB.crop((0, 0, w2, h))
          B = AB.crop((w2, 0, w, h))
          # N1,N2,N3 = A.split()
  
          # apply the same transform to both A and B
          
          transform_params = get_params(self.opt, A.size)
          A_transform = get_transform(self.opt, transform_params)
          B_transform = get_transform(self.opt, transform_params)
          A = A_transform(A)
          lisA.append(A)
          

        A = torch.stack(lisA,0)
        B = B_transform(B)
        return {'A':A, 'B': B, 'A_paths': self.AB_paths[index], 'B_paths': self.AB_paths[index]}

    def __len__(self):
        """Return the total number of images in the dataset."""
        return len(self.AB_paths)
