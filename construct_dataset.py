import json

def cons_ssv2(dataset, label_list):
    ssv2_dataset = []
    for data in dataset:
        ssv2_dataset.append({
            "label_idx": label_list[data['template'].replace('[','').replace(']','')],
            "id": data['id']
        })
    return ssv2_dataset

dataset_root = "/mnt/pvc-data.common/ChenZikang/dataset/"

train_set = json.load(open(f"{dataset_root}sthv2/annotations/something-something-v2-train.json", 'r'))
val_set = json.load(open(f"{dataset_root}sthv2/annotations/something-something-v2-validation.json", 'r'))
label_list = json.load(open(f"{dataset_root}sthv2/annotations/something-something-v2-labels.json", 'r'))

with open("output/something-something-v2-train-with-label.json", 'w') as file:
    json.dump(cons_ssv2(train_set, label_list), file)
with open("output/something-something-v2-val-with-label.json", 'w') as file:
    json.dump(cons_ssv2(val_set, label_list), file)