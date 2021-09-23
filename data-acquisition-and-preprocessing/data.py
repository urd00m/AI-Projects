import pandas as pd

import torch
import torch.nn.functional as F
from torch.utils.data import Dataset, DataLoader

from transformers import AutoModel, AutoTokenizer


class TweetDataset(Dataset):
    def __init__(self, df, size=1000):
        
        self.tokenizer = AutoTokenizer.from_pretrained("vinai/bertweet-base", use_fast=False)
        self.bertweet = AutoModel.from_pretrained("vinai/bertweet-base")

        self.inputs = tokenizer(list(df['content'][:size]), return_tensors="pt", padding=True, truncation=True)
        self.authors = pd.get_dummies(df['author']).loc[:size].values
        
        # Run BERT forward pass to get embeddings
        with torch.no_grad():
            features = bertweet(self.inputs.input_ids)
            
        self.embeddings = features.pooler_output
        self.labels = torch.tensor(self.authors).float()

    def __len__(self):
        return len(self.labels)

    def __getitem__(self, idx):
        
        x = # YOUR CODE HERE!
        y = # YOUR CODE HERE!
        
        return x, y
    

if __name__ == '__main__':
    df = pd.read_csv("data/tweets.csv")
    ds = TweetDataset(df, size=10)
    assert ds[0][0].shape[1] == 768