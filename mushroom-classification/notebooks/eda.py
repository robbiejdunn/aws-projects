# %% [markdown]
# # Mushroom classification EDA VSCode Notebook

# %%
# Imports
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
plt.style.use("ggplot")

# %%
# Read data into pandas Dataframe
data_location = "../data/mushrooms.csv"
mushrooms = pd.read_csv(data_location)
mushrooms.head(5)

# %%
# Basic dataframe analysis
mushrooms.info()

# %% [markdown]
# No null values, all features are categorical.

# %%
# Replace feature values with their full names
# mappings written manually based on Kaggle data explorer
feature_value_mappings = {
    "class": {"e": "edible", "p": "poisonous"},
    "cap-shape": {"b": "bell", "c": "conical", "x": "convex", "f": "flat", "k": "knobbed", "s": "sunken"},
    "cap-surface": {"f": "fibrous", "g": "grooves", "y": "scaly", "s": "smooth"},
    "cap-color": {"n": "brown", "b": "buff", "c": "cinnamon", "g": "gray", "r": "green", "p": "pink", "u": "purple", "e": "red", "w": "white", "y": "yellow"},
    "bruises": {"t": "bruises", "f": "no"},
    "odor": {"a": "almond", "l": "anise", "c": "creosote", "y": "fishy", "f": "foul", "m": "musty", "n": "none", "p": "pungent", "s": "spicy"},
    "gill-attachment": {"a": "attached", "d": "descending", "f": "free", "n": "notched"},
    "gill-spacing": {"c": "close", "w": "crowded", "d": "distant"},
    "gill-size": {"b": "broad", "n": "narrow"},
    "gill-color": {"k": "black", "n": "brown", "b": "buff", "h": "chocolate", "g": "gray", "r": "green", "o": "orange", "p": "pink", "u": "purple", "e": "red", "w": "white", "y": "yellow"},
    "stalk-shape": {"e": "enlarging", "t": "tapering"},
    "stalk-root": {"b": "bulbous", "c": "club", "u": "cup", "e": "equal", "z": "rhizomorphs", "r": "rooted", "?": "missing"},
    "stalk-surface-above-ring": {"f": "fibrous", "y": "scaly", "k": "silky", "s": "smooth"},
    "stalk-surface-below-ring": {"f": "fibrous", "y": "scaly", "k": "silky", "s": "smooth"},
    "stalk-color-above-ring": {"n": "brown", "b": "buff", "c": "cinnamon", "g": "gray", "o": "orange", "p": "pink", "e": "red", "w": "white", "y": "yellow"},
    "stalk-color-below-ring": {"n": "brown", "b": "buff", "c": "cinnamon", "g": "gray", "o": "orange", "p": "pink", "e": "red", "w": "white", "y": "yellow"},
    "veil-type": {"p": "partial", "u": "universal"},
    "veil-color": {"n": "brown", "o": "orange", "w": "white", "y": "yellow"},
    "ring-number": {"n": "none", "o": "one", "t": "two"},
    "ring-type": {"c": "cobwebby", "e": "evanescent", "f": "flaring", "l": "large", "n": "none", "p": "pendant", "s": "sheathing", "z": "zone"},
    "spore-print-color": {"k": "black", "n": "brown", "b": "buff", "h": "chocolate", "r": "green", "o": "orange", "u": "purple", "w": "white", "y": "yellow"},
    "population": {"a": "abundant", "c": "clustered", "n": "numerous", "s": "scattered", "v": "several", "y": "solitary"},
    "habitat": {"g": "grasses", "l": "leaves", "m": "meadows", "p": "paths", "u": "urban", "w": "waste", "d": "woods"}
}
for column, mapping in feature_value_mappings.items():
    if column in mushrooms.columns:
        mushrooms[column] = mushrooms[column].replace(mapping)
    else:
        print(f"Column {column} not found in mushrooms.csv")
mushrooms.head(5)

# %%
# Target variable analysis
print(mushrooms["class"].value_counts())
print()
print(mushrooms["class"].value_counts() / len(mushrooms))
sns.countplot(mushrooms["class"])
plt.title("target variable")

# %% [markdown]
# # Target variable analysis
#
# Fairly balanced target variable (51% edible 48% poisonous).

# %%
# All features univariate analysis
for column in mushrooms:
    if column == "class":
        continue
    plt.figure(figsize=(20,4))
    plt.subplot(121)
    mushrooms[column].value_counts().plot(kind="bar")
    plt.xlabel(column)
    plt.ylabel("count")
    plt.title(column)

# %%
# Bivariate analysis of features with the target variable
for column in mushrooms:
    if column == "class":
        continue
    plt.figure(figsize=(20,4))
    plt.subplot(121)
    sns.countplot(mushrooms, x=column, hue="class")
    plt.title(column)    
    plt.xticks(rotation=90)

# %%
