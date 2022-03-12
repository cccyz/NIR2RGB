## Optimal LED Spectral Multiplexing for NIR2RGB Translation

In this short tutorial, we will guide you through setting up the system environment for running the code, which used for nir to rgb translation

### Requirments

- Hardware: PC with NVIDIA GPU which have more than 8GB memory. 
- Software: *Ubuntu 16.04*, *CUDA 9.1*, *Anaconda3*, *pytorch 1.7.1*


### Training For TLM

1. Download the [dataset](https://drive.google.com/file/d/1IoMJ7a0LidpMywXDmfJa3m8oifGHkq8O/view?usp=sharing) you want to use and put it into `code/datasets`. More details see `data/Datasets/readme.txt`

2. Start training
    ```
    python train.py --dataroot path/to/the/datasets/icvl --name experiment_name
    ```
    
3. On training image outputs and model are stored in `checkpoints/experiment_name`, if you have multi GPUs, using `--gpu_ids 0` to specify the gpu you want to use.


### Testing

First, make sure that the data in  `code/datasets/icvl/test` folder is avaliable.

#### Pretrained models 

|  Dataset    | Camera   | Model Link     |
|-------------|------------|-------------------|
| icvl |  15S5C |[model](https://drive.google.com/file/d/12Z8x_6KEpDKzEfFSXyy0eSdfA6oFEt71/view?usp=sharing)    |


#### Translation

After the training step, or download the pretrained model and put them in `checkpoints/experiment_name` folder.

Run the following command to translate NIR images to RGB images
    
    python train.py --dataroot path/to/the/datasets/icvl --name experiment_name
    
The results are stored in `results/experiment_name` folder. 
the output contain the translation result, original nir image and rgb image

### RVM
Run the following command to see the results of RVM with 3 cameras
    
    python util/rvm.py
    