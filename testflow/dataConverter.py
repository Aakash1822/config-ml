import json
import pandas as pd 
from datasets import Dataset


class DataConverter:

    def __init__(self, args):
        self.args = args

    def dataloader(self, file_p):
        with open(file_p) as f:
            data = json.load(f)
        return data

    def transform(self):
        val = self.dataloader()
        df = pd.DataFrame(val)
        dataset = Dataset.from_pandas(df)
        return dataset



