import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Removes limit of columns displayed when run

pd.set_option('display.max_columns', None)

# Loads data

df = pd.read_csv('hcv_cleaned.csv')

# Maps numeric codes to disease labels
category_labels = {
    0: 'Healthy',
    1: 'Hepatitis',
    2: 'Fibrosis',
    3: 'Cirrhosis'
}
df['Category'] = df['Category'].map(category_labels)

# Biomarker columns
biomarkers = ['ALB', 'ALP', 'ALT', 'AST', 'BIL',
              'CHE', 'CHOL', 'CREA', 'GGT', 'PROT']

print("Dataset shape:", df.shape)
print("\nDisease categories distribution:")
print(df['Category'].value_counts())
print("\nBiomarker columns:", biomarkers)

# Defines explicit category order
category_order = ['Healthy', 'Hepatitis', 'Fibrosis', 'Cirrhosis']


#Plotting Kde and histogram to show distribution of samples
for marker in biomarkers:
    plt.figure(figsize=(8,5))
    sns.histplot(df_clean[marker], bins=20, color='skyblue', kde=False, stat='density')  # Density histogram
    sns.kdeplot(df_clean[marker], color='red', linewidth=2, bw_adjust=1)               # KDE
    plt.title(f'Distribution of {marker}')
    plt.xlabel(marker)
    plt.ylabel('Density')
    plt.show()

#  Boxplot

# Creates color palette for each disease category
colors = { 'Healthy': 'green','Hepatitis': 'yellow', 'Fibrosis': 'orange', 'Cirrhosis': 'red'}

plt.style.use('seaborn-v0_8')

fig, axes = plt.subplots(2, 5, figsize=(20, 10))
axes = axes.ravel()

for i, biomarker in enumerate(biomarkers):
    sns.boxplot(data=df, x='Category', y=biomarker, ax=axes[i], hue='Category', palette=colors, legend=False, order=category_order)
    axes[i].set_title(f'{biomarker} by Disease Category')
    axes[i].set_xlabel('Disease category')
    axes[i].set_ylabel(biomarker)

    # Adds median values to the boxplot
    medians = df.groupby('Category')[biomarker].median().reindex(category_order)
    for j, category in enumerate(category_order):
        axes[i].text(j, medians[category], f'{medians[category]:.1f}', ha='center', va='bottom', fontweight='bold', color='black')

plt.tight_layout()
plt.show()


