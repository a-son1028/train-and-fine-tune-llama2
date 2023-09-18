# train-and-fine-tune-llama2
<!-- ABOUT THE PROJECT -->
## About The Project
...
<p align="right">(<a href="#top">back to top</a>)</p>

### Prerequisites

Make sure you have installed all of the following prerequisites on your development machine:
* Python3

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/a-son1028/train-and-fine-tune-llama2.git
   ```
2. Install dependencies
   ```sh
   pip install accelerate==0.21.0 peft==0.4.0 bitsandbytes==0.40.2 transformers==4.31.0 trl==0.4.7 scipy
   ```
### Usage
#### Step 1: Prepare the dataset
Follow the `train.csv` to create your own dataset 

Note: the file must contain only one column and the first row is the header

#### Step 2: Push your data to HF
1. Login to HF
    ```sh
   huggingface-cli login
   ```
    Note: it will ask you for a write token, you can get the token by following [this page](https://huggingface.co/docs/hub/security-tokens)

2. Push to HF
   ```sh
   python3 preprocess-dataset.py
   ``` 
    Note: You can edit the dataset name you want at `line 15` in `preprocess-dataset.py` file

3. Fine-tune your dataset
  ```sh
   python3 finetune_llama_v2.py --new_model nghiem_model_15-9 --dataset_name tuankg1028/nghiem_dataset_15-9
   ```
  Note: 
  
  `--dataset_name` is a dataset name on HF that you want to train your model
  
  `--new_model` is a new model name that will be created on HF

<p align="right">(<a href="#top">back to top</a>)</p>
