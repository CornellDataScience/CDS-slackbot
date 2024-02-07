from datasets import DatasetDict, Dataset
from collections import defaultdict
import itertools
import uuid
import os

directory = "data"
ds = defaultdict(list)

for filename in os.listdir(directory):
    with open(os.path.join(directory, filename)) as f:
        for l1, l2 in itertools.zip_longest(*[f]*2):
            ds["prompt"].append(l1)
            ds["prompt_id"].append(str(uuid.uuid4()))
            ds["messages"].append([{"role": "user", "content": l1}, {"role": "assitant", "content": l2}])

ds = Dataset.from_dict(ds)
print(ds)