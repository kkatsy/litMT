import os
# GPU to fine-tune on
os.environ["CUDA_DEVICE_ORDER"] = "PCI_BUS_ID"
os.environ["CUDA_VISIBLE_DEVICES"] = "1"

import torch
from helpers import preprocess_data, fine_tune


# data settings
alignment = 'aligned'       # aligned or random
context_type = 'src+tgt'    # tgt256, tgt512, src+tgt
batch_size = 12

# dataset dirs
dir = "/home/kkatsy/litMT/"
dataset_dir = dir + "experiment_dataset/"
aligned_train_file = dataset_dir + 'aligned_train_df.pickle'
random_train_file = dataset_dir + 'random_train_df.pickle'

train_file = aligned_train_file if alignment=='align' else random_train_file
val_file = dataset_dir + 'experiment_val_df.pickle'
test_file = dataset_dir + 'experiment_test_df.pickle'

# model info
model = "bert-base-multilingual-cased"
classes = ["Garnett", "McDuff", "PV", "Katz", "Hogarth"]

# fine-tune settings
epochs = 30
lr = 2e-8
eps = 0
wd = 0.0
train_args = {'epochs': epochs, 'lr': lr, 'eps': eps, 'wd': wd}

# logging settings
proj_name = "param_exps"
run_name = "vanilla 2e-8"
model_save_pth = "/home/kkatsy/pretrained/" + run_name

def main():
    train_set, val_set, test_set = preprocess_data(model, train_file, val_file, test_file, context_type, batch_size)
    data = {'train' : train_set, 'val' : val_set, 'test' : test_set}
    
    fine_tune(model, classes, data, train_args, proj_name, run_name, model_save_pth)

if __name__ == "__main__":
    main()