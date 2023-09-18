from datasets import load_dataset

file_dict = {
  "train" : "train.csv",
}

dataset = load_dataset(
  'csv',
  data_files=file_dict,
  delimiter=',',
  column_names=['text'],
  skiprows=1
)

dataset.push_to_hub("test1", private=False)
