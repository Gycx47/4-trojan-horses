import json
from nltk_utils import tokenize, stem, bag_of_words
import numpy as np

import torch
import torch.nn as nn
from torch.utils.data import Dataset, DataLoader

from model import NeuralNet

with open('intents.json','r') as f:
    intents = json.load(f)
    #print(intents) --> first test, must be able to print out the entire json file

all_words = []
tags = []
xy = []

#tokenization steps below
for intent in intents['intents']:
    tag = intent['tag']
    tags.append(tag) 
    for pattern in intent['patterns']:
        w = tokenize(pattern)
        all_words.extend(w)
        xy.append((w, tag))
        #print(xy) --> can test again (for tokenization)
        #or with print(all_words)

#stemming steps below
ignore_words = ['?', '.', ',', '!']
all_words = [stem(w) for w in all_words if w not in ignore_words] #the "w" variable here is a different/seperate -temporary- variable from the "w" in the previous loop, we just used used the letter "w" bc its short for "word"
#print(all_words) --> test out stemming and ignore_words when stemming
all_words = sorted(set(all_words))
tags = sorted(set(tags))
#print(tags) --> visual ref

#bag of words steps below
x_train = [] #lowercase x & y btw
y_train = [] 
for (pattern_sentence, tag) in xy: #explanation for future self lol: since up to this point the xy variable now stores the value (w, tag), u are assigning variable names thru this loop to those values (so w is pattern_sentence and tag is tag), these 2 variables will only exist inside the loop block (this is a self-indulgent comment sorry im slowly learning this)
    bag = bag_of_words(pattern_sentence, all_words)
    x_train.append(bag)

    label = tags.index(tag)#note to self:here
    y_train.append(label)

x_train = np.array(x_train)
y_train = np.array(y_train)

class ChatDataset(Dataset):
    def __init__(self):
        self.n_samples = len(x_train)
        self.x_data = x_train
        self.y_data = y_train

    #dataset[idx]
    def __getitem__(self, index):
        return self.x_data[index], self.y_data[index]
        
    def __len__(self):
        return self.n_samples
        
        
#hyperparameters
batch_size = 8
hidden_size = 8
output_size = len(tags)
input_size = len(x_train[0])
learning_rate = 0.001
num_epochs = 1000
#test if input size matches the length of all_words and if output size is the number of all tags)
#print(input_size, len(all_words))
#print(output_size, tags)

dataset = ChatDataset()
train_loader = DataLoader(dataset=dataset, batch_size=batch_size, shuffle=True, num_workers=0) #set to '2' if u get an error

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
model = NeuralNet(input_size, hidden_size, output_size).to(device)

#loss and optimizer
criterion = nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(model.parameters(), lr=learning_rate)

for epoch in range(num_epochs):
    for (words, labels) in train_loader:
        words = words.to(device)
        labels = labels.to(device)

        #forward
        outputs = model(words)
        loss = criterion(outputs, labels)

        #backward and optimizer step
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

    if (epoch +1) % 100 == 0:
        print(f'epoch {epoch+1}/{num_epochs}, loss={loss.item():.4f}')

print(f'final loss, loss={loss.item():.4f}')