import pandas as pd

data_path = "hcv_cleaned.csv"
df_clean= pd.read_csv(data_path)

biomarkers=["ALB", "ALP", "ALT", "AST", "BIL", "CHE", "CHOL", "CREA", "GGT", "PROT"]
age_bins = [0, 32, 46, 60, 120]
age_labels = ['19–32', '33–46', '47–60', '61+']
df_clean['Age_Group'] = pd.cut(df_clean['Age'], bins=age_bins, labels=age_labels, right=True)

def iqr(x):
    return x.quantile(0.75) - x.quantile(0.25)

# -------------------------------------------------
#        Data Summary of Sample Population
#--------------------------------------------------

# Count per category
disease_count = df_clean['Category'].value_counts()
sex_count = df_clean['Sex'].value_counts()
age_count = df_clean['Age_Group'].value_counts().sort_index()

# Compute percentages
disease_percent = (disease_count / len(df_clean) * 100).round(1)
sex_percent = (sex_count / len(df_clean) * 100).round(1)
age_percent = (age_count / len(df_clean) * 100).round(1)

# Combine counts and percentages into a DataFrame
disease_summary = pd.DataFrame({
    'Count': disease_count,
    'Percent': disease_percent
})

sex_summary = pd.DataFrame({
    'Count': sex_count,
    'Percent': sex_percent
})

age_summary = pd.DataFrame({
    'Count': age_count,
    'Percent': age_percent
})

print("=== Disease Category ===")
print(disease_summary)
print("\n=== Sex ===")
print(sex_summary)
print("\n=== Age Group ===")
print(age_summary)

#create dataframe for measure of central tendencies and variability
table = pd.DataFrame()

# Group by disease category
grouped = df_clean.groupby('Category')

# compute Mean, SD, IQR
for marker in biomarkers:
    stats = grouped[marker].agg(['mean', 'std', iqr])
    table[marker] = stats.apply(
        lambda row: f"{row['mean']:.1f} ± {row['std']:.1f} ({row['iqr']:.1f})",
        axis=1
    )

table
