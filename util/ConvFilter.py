import torch
from torch import nn
import torchvision.transforms as transform
import torch.nn.functional as F
import argparse
import numpy as np

import torch
from torch import nn
import torchvision.transforms as transform
import torch.nn.functional as F

class convfilter(nn.Module):
    def __init__(self,**kwargs):
        super(convfilter,self).__init__(**kwargs)
        self.select = nn.Linear(14,1,bias=True)
        
    def forward(self,x):
        test = torch.squeeze(x,dim=0).permute(1,2,3,0).view(-1,14)
        for i in self.select.parameters():
           i.data = torch.clamp(i,0)
        print(self.select.weight)
        #test = test.view(3,1,256,256).permute(1,0,2,3)
        a = torch.sum(self.select.weight,dim =1)
        test = self.select(test).view(3,256,256,1).permute(3,0,1,2)/a
        return test

    #def __init__(self,**kwargs):
        #super(convfilter,self).__init__(**kwargs)
        #self.select_1 = nn.Linear(65536,256,bias=False)
        #self.act = nn.ReLU()
        #self.select_2 = nn.Linear(256,1,bias=False)
        #self.select_3 = nn.Linear(3,1,bias=False)
        #self.soft = nn.Softmax(dim=0)
        #self.norm = nn.InstanceNorm2d(3)
        #self.select = nn.Conv1d(in_channels=14,out_channels=1,kernel_size=1,bias=False)
        #x = np.array([0.24652361, 0.32214592, 0.28686695, 0.05725322, 0.02214592,0.01090129, 0.0072103 , 0.00798283, 0.00660944, 0.00583691,0.00583691, 0.00566524, 0.00532189, 0.00497854])
        #x = torch.zeros(1,14)
        #x[0,0]=2.5
        #x[0,1]=1.4
        #x[0,2]=1
        #x = torch.unsqueeze(torch.from_numpy(x).float(),dim=0)
        #self.params = nn.Parameter(data=x,requires_grad=True)
        
    #def forward(self,x):
        #test = torch.squeeze(x,dim=0).view(14,3,-1)
        #test = self.select_1(test)
        #test = self.act(test)
        #test = self.select_2(test)
        #test = self.select_3(test.squeeze())
        #test = self.soft(test).permute(1,0)
        #test = self.select(test)
        #test = test.view(3,1,256,256).permute(1,0,2,3)
        #x = torch.squeeze(x,dim=0).view(14,-1)
        #a = torch.sum(self.params.data)
        #print(self.params)
        #print(a)
        #x = torch.mm(self.params,x).view(1,3,256,256)/a
        #return x

    #def __init__(self,**kwargs):
        #super(convfilter,self).__init__(**kwargs)
        #self.select_1 = nn.Linear(65536,256,bias=False)
        #self.act = nn.ReLU()
        #self.select_2 = nn.Linear(256,1,bias=False)
        #self.select_3 = nn.Linear(3,1,bias=False)
        #self.soft = nn.Softmax(dim=0)
        
    #def forward(self,x):
        #test = torch.squeeze(x,dim=0).view(14,3,-1)
        #test = self.select_1(test)
        #test = self.act(test)
        #test = self.select_2(test)
        #test = self.select_3(test.squeeze())
        #test = self.soft(test).permute(1,0)
        #print(test)
        #test = test.view(3,1,256,256).permute(1,0,2,3)
        #x = torch.squeeze(x,dim=0).view(14,-1)
        #x = torch.mm(test,x).view(1,3,256,256)
        #return x


    #def __init__(self,**kwargs):
        #super(convfilter,self).__init__(**kwargs)
        #self.q = torch.rand(1,14) + 0.5
        #self.q = torch.zeros(1,14)
        #self.q[0,0] = 1
        #self.q[0,1] = 1
        #self.q[0,2] = 1
        #self.params = nn.Parameter(data=self.q,requires_grad=False)

    #def forward(self, x):
        #test = x.view(x.shape[0],14,-1)
        #y = torch.zeros([x.shape[0],1,3,256,256]).cuda()
        #t = torch.nn.ReLU(inplace = False)
        #param = t(self.params).cuda()
        #param = self.params.cuda()

        #print(param)
        #a = torch.sum(param,dim =1)

        #y = torch.matmul(param,test)
        #y = y.view(x.shape[0],1,3,256,256)
        #y = torch.squeeze(y, dim=1)
        # for j in range(0,x.shape[0]):
        #   for i in range(0,256):
        #       y[j,0,0,i,:] = torch.mm(param,x[0,:,0,i,:])[0]
        #       y[j,0,1,i,:] = torch.mm(param,x[0,:,1,i,:])[0]
        #       y[j,0,2,i,:] = torch.mm(param,x[0,:,2,i,:])[0]

        #return (y/5.8)
        #return (y/a)


#class convfilter(nn.Module):
 #   def __init__(self,**kwargs):
  #      super(convfilter,self).__init__(**kwargs)
   #     self.q = torch.zeros(1,15)
    #    self.q[0,0] = 1
     #   #self.q[0,0] = 0.0713
      #  #self.q[0,1] = 0.0014
        #self.q[0,14] = 1.2985
#        self.params = nn.Parameter(data=self.q,requires_grad=False)

#    def forward(self, x):
 #       #print('X: ', x.shape[0])
#        y = torch.zeros([x.shape[0],1,3,256,256]).cuda()
        #a = torch.sum(self.params.data,dim = 1)
#        t = torch.nn.ReLU(inplace = False)
 #       param = t(self.params).cuda()
  #      a = torch.sum(param,dim =1)
        #print(param)
        #print(a)
        #print(x.shape)
        #print(self.params)
   #     for j in range(0,x.shape[0]):
    #      for i in range(0,256):
          #    y[j,0,0,i,:] = torch.mm(param,x[0,:,0,i,:])[0]
         #     y[j,0,1,i,:] = torch.mm(param,x[0,:,1,i,:])[0]
        #      y[j,0,2,i,:] = torch.mm(param,x[0,:,2,i,:])[0]
       #       
      #  y = torch.squeeze(y,dim=1)
     #   return (y/a)
