from datasets import load_dataset, DatasetDict, concatenate_datasets

# Load the dataset from the Hugging Face Hub
dataset_1 = load_dataset('Nuo97/Dolphin_Task1')
dataset_2 = load_dataset('Nuo97/Dolphin_Task2')
dataset_3 = load_dataset('Nuo97/Dolphin_Task3')
dataset_dpo = load_dataset("json", data_files='./DPO_Training_Data/memory_dpo_train.json')

# Create Merged, Multi-Task Dataset
multitask_dataset = DatasetDict({
    'train':concatenate_datasets([dataset_1['train'], dataset_2['train'], dataset_3['train']])
})

shuffled_multitask_dataset = DatasetDict({
    'train':multitask_dataset['train'].shuffle(seed=42)
})

# Inspect the dataset
print('Before Split')
print(dataset_1)
print(dataset_2)
print(dataset_3)
print(multitask_dataset)
print(shuffled_multitask_dataset)
print(dataset_dpo)

# Split Data
train_val_split_1 = dataset_1["train"].train_test_split(test_size=0.2)
train_val_split_2 = dataset_2["train"].train_test_split(test_size=0.2)
train_val_split_3 = dataset_3["train"].train_test_split(test_size=0.2)
multitask_train_val_split = multitask_dataset["train"].train_test_split(test_size=0.2)
shuffled_multitask_train_val_split = shuffled_multitask_dataset["train"].train_test_split(test_size=0.2)

# Split DatasetDict Creation
split_dataset_1 = DatasetDict({
    'train': train_val_split_1['train'],
    'validation': train_val_split_1['test']
})
split_dataset_2 = DatasetDict({
    'train': train_val_split_2['train'],
    'validation': train_val_split_2['test']
})
split_dataset_3 = DatasetDict({
    'train': train_val_split_3['train'],
    'validation': train_val_split_3['test']
})
split_multitask_dataset = DatasetDict({
    'train': multitask_train_val_split['train'],
    'validation':multitask_train_val_split['test']
})
split_shuffled_multitask_dataset = DatasetDict({
    'train': shuffled_multitask_train_val_split['train'],
    'validation':shuffled_multitask_train_val_split['test']
})

# Inspect the dataset
print('After Split')
print(split_dataset_1)
print(split_dataset_2)
print(split_dataset_3)
print(split_multitask_dataset)
print(split_shuffled_multitask_dataset)
print(dataset_dpo)

split_dataset_1.save_to_disk('./MultiTask_Training_Data/Dolphin_Task1')
split_dataset_2.save_to_disk('./MultiTask_Training_Data/Dolphin_Task2')
split_dataset_3.save_to_disk('./MultiTask_Training_Data/Dolphin_Task3')
split_multitask_dataset.save_to_disk('./MultiTask_Training_Data/Dolphin_MultiTask')
split_shuffled_multitask_dataset.save_to_disk('./MultiTask_Training_Data/Dolphin_MultiTask_Shuffled')