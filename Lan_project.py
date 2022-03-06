import pandas as pd
import json
import numpy  as np

# with open("./input/topics.txt","r") as f,  open("./output/topics50.txt","w") as f_out:
#     lines = f.readlines()
#     for line in lines:
#         line_list = line.split(" ")
#         for i in range(15):
#             print(line_list[i]+" ",file=f_out,end = "")
#         print("",file=f_out)

#exit()
topics_to_labels = np.load("./output/topics_to_labels.npz",allow_pickle=True) #['probs', 'label']
print(topics_to_labels.files, topics_to_labels["probs"].shape)

beta = np.load("./output/beta.npz",allow_pickle=True)
print(beta.files,beta["beta"].shape)

theta = np.load("./output/theta.train.npz",allow_pickle=True)
print(theta.files, theta["theta"].shape, theta["ids"])


exit()

# Load the xlsx file
excel_data = pd.read_excel('review texts.xlsx')
meta_data = pd.read_excel('meta data.xlsx')
# Read the values of the file in the dataframe
data = pd.DataFrame(excel_data, columns=['ProductID','ReviewText'])
meta_data = pd.DataFrame(meta_data, columns=['ID','rating','review_age','helpfulscore','votes','impact','dummy_helpful'])
# Print the content
#print("The content of the file is:\n", data.loc[0],dict(data.loc[0]))
#print("data.loc[0]", data.loc[32232], dict(meta_data))
json_all = []
for i in range(32233):
    if i == 0:
        continue
    json_ = {}
    text_ = data.loc[i]
    meta_ = meta_data.loc[i]
    id = text_["ProductID"]
    assert id == meta_['ID']
    
    json_["id"] = str(id)
    json_["orig"] = str(id)
    json_["sentiment"] = "neg"
    json_["text"] = text_["ReviewText"]
    json_["rating"] = str(meta_["rating"])
    json_all.append(json_)

with open('train.json', mode='w') as f:
    for dict_ in json_all:
        json.dump(dict_, f)
        f.write('\n')
#meta_data.to_excel('test.xlsx', index=False)