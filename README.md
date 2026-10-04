# Recommendation_systems


## Dataset train_test split

  # Download train and test splits

The train and test datasets are stored on Google Drive because they are too large to be stored directly in the GitHub repository.

### Download the datasets

```python
import pandas as pd
import gdown

ID_TRAIN = "1zjZe-u52WdE4obfOj8c1foCysYuJvfjB"
ID_TEST = "1y2AMXgEhL3NCT-0Z0nydxSJ6hI_wnrYK"

# Download train split
gdown.download(
    "https://drive.google.com/uc?id=" + ID_TRAIN,
    "df_train.csv",
    quiet=False
)

# Download test split
gdown.download(
    "https://drive.google.com/uc?id=" + ID_TEST,
    "df_test.csv",
    quiet=False
)

# Load datasets
df_train = pd.read_csv("df_train.csv")
df_test = pd.read_csv("df_test.csv")
```


### Files

After running the code, the following files will be available in your working directory:

```text
df_train.csv
df_test.csv
```



## MCRS
  @ala
  @zuza
  
## SASRC
  source: https://github.com/kang205/SASRec
  
  @michał



## Metrics and summary 
  
