# Optimal LED Spectral Multiplexing for NIR2RGB Translation

[Lei Lui](https://github.com/loklz), [Yuze Chen](https://github.com/cccyz), [Junchi Yan](https://thinklab.sjtu.edu.cn), Yinqiang Zheng

This paper has been accpected by **CVPR2022**. In this short tutorial, we will guide you through setting up the system environment for running the code, which used for NIR-to-RGB translation.


## Requirments

- *Ubuntu 16.04*
- *CUDA 9.1*
- *pytorch 1.7.1*

## Datasets

1. We have released our hyperspectral images dataset [IDH](https://drive.google.com/file/d/1qDazg8VAYv8ZKpDfKjIBFiH3IHNPDMbb/view?usp=sharing), the wavelength range from 420nm to 1000nm with 10nm intervals.

2. If you only want to go through our model, we suggest to download the processed [Dataset](https://drive.google.com/file/d/1IoMJ7a0LidpMywXDmfJa3m8oifGHkq8O/view?usp=sharing) and unzip it into `datasets/`. More details see `datasets/readme.txt`.

## Target Loss Minimization (TLM)

### Training phase
1. Take ICVL for example:
    ```
    python train.py --dataroot path/to/the/datasets/icvl/train --name experiment_name
    ```
    
2. On training image outputs and model are stored in `checkpoints/experiment_name`, if you have multi GPUs, using `--gpu_ids 0` to specify the gpu you want to use.


### Testing phase

1. First, make sure that the data in `datasets/icvl/test` folder is avaliable.

2. Pretrained model:

|  Dataset    | Camera   | Model Link     |
|-------------|------------|-------------------|
| ICVL |  FLIR GS3-U3-15S5C |[model](https://drive.google.com/file/d/12Z8x_6KEpDKzEfFSXyy0eSdfA6oFEt71/view?usp=sharing)    |


3. After the training step, or download the pretrained model and put them in `checkpoints/experiment_name` folder. Run the following command to translate NIR images to RGB images:
    ```
    python test.py --dataroot path/to/the/datasets/icvl/test --name experiment_name
    ```
The results are stored in `results/experiment_name` folder. 

## RGB Variance Maximization (RVM)

Run the following command to see the results of RVM with 3 cameras:
    ```
    python util/rvm.py
    ```
    
