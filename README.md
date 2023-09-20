# train-and-fine-tune-llama2
<!-- ABOUT THE PROJECT -->
## About The Project
Welcome to the "Train and Fine-Tune LLAMA2" project! This repository contains instructions and scripts for training and fine-tuning LLAMA2, a language model. Whether you're an experienced developer or new to the world of language models, this guide will help you get started and make the most of LLAMA2.

<p align="right">(<a href="#top">back to top</a>)</p>

### Prerequisites

Before you begin, make sure you have the following prerequisites installed on your development machine:
* Python3

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/a-son1028/train-and-fine-tune-llama2.git
   ```
2. Install the required dependencies
   ```sh
   pip install datasets accelerate==0.21.0 peft==0.4.0 bitsandbytes==0.40.2 transformers==4.31.0 trl==0.4.7 scipy
   ```
3. Install the NVIDIA Driver
   ```sh
   sudo apt install nvidia-driver-525 nvidia-dkms-525
   ```
   To verify a successful installation, you can use the `nvidia-smi` command.

### Usage
#### Step 1: Prepare the Dataset
To begin, create your dataset following the format specified in `train.csv`. Ensure that the file contains only one column, with the first row serving as the header.

#### Step 2: Push Your Data to Hugging Face (HF)
1. Login to HF
    ```sh
   huggingface-cli login
   ```
    Note: You'll be prompted to provide a write token, which you can obtain by following the instructions on [this page](https://huggingface.co/docs/hub/security-tokens)

2. Push to HF
   ```sh
   python3 preprocess-dataset.py
   ``` 
    Note: You can customize the desired dataset name by editing `line 15` in the `preprocess-dataset.py` file.

#### Step 3. Fine-tune your dataset
```sh
python3 finetune_llama_v2.py --new_model nghiem_model_15-9 --dataset_name tuankg1028/nghiem_dataset_15-9
```
  Note: 
  
  `--dataset_name` represents the name of the dataset on HF that you want to use for training.
  
  `--new_model` specifies the name for the new model to be created on HF.

<p align="right">(<a href="#top">back to top</a>)</p>
