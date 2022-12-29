import numpy as np
import tensorflow as tf
import torch
import sklearn
from tensorflow.python.client import device_lib

if __name__ == '__main__':
    print(f'numpy version : {np.__version__}')
    print(f'tensorflow version : {tf.__version__}')
    print(f'torch version : {torch.__version__}')
    print(f'sklearn version : {sklearn.__version__}')
    print(f'이 PC에 설치된 디바이스 상세보기 : {device_lib.list_local_devices()}')
    print(f'CUDA 프로그래밍 가능여부 :  {torch.cuda.is_available()}')
    print(f'CUDA 프로그래밍 가능여부 : {torch.cuda.get_device_name()}')
    print(f'사용 가능 GPU 갯수 :  {torch.cuda.device_count()}')
    '''
    numpy version : 1.21.5
    tensorflow version : 2.11.0
    torch version : 1.7.1+cu110
    sklearn version : 1.1.3
    이 PC에 설치된 디바이스 상세보기 : [name: "/device:CPU:0"
    device_type: "CPU"
    memory_limit: 268435456
    locality {
    }
    incarnation: 1293823082114439000
    xla_global_id: -1
    ]
    2022-12-08 15:57:25.475705: I tensorflow/core/platform/cpu_feature_guard.cc:193] This TensorFlow binary is optimized with oneAPI Deep Neural Network Library (oneDNN) to use the following CPU instructions in performance-critical operations:  AVX AVX2
    To enable them in other operations, rebuild TensorFlow with the appropriate compiler flags.
    CUDA 프로그래밍 가능여부 :  True
    CUDA 프로그래밍 가능여부 : NVIDIA GeForce RTX 2080
    사용 가능 GPU 갯수 :  1
    '''