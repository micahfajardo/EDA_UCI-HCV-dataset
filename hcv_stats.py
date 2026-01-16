import os
import numpy as np
import pandas as pd

from scipy import stats
import statsmodels.api as sm
from statsmodels.formula.api import ols
from statsmodels.stats.multicomp import pairwise_tukeyhsd

import scikit_posthocs as sp
import seaborn as sns
import matplotlib.pyplot as plt

from sklearn.cluster import KMeans
from sklearn.metrics import confusion_matrix, classification_report, accuracy_score

# Set seed
np.random.seed(100)

# Read CSV
dst = pd.read_csv("hcv_cleaned.csv")

# Convert Category to factor (categorical)
dst["Category"] = dst["Category"].astype("category")

# ANOVA + Tukey HSD
model_ALB = ols("ALB ~ C(Category)", data=dst).fit()
anova_ALB = sm.stats.anova_lm(model_ALB, typ=2)
print(anova_ALB)

tukey_ALB = pairwise_tukeyhsd(dst["ALB"], dst["Category"])
print(tukey_ALB)

model_CHOL = ols("CHOL ~ C(Category)", data=dst).fit()
anova_CHOL = sm.stats.anova_lm(model_CHOL, typ=2)
print(anova_CHOL)

tukey_CHOL = pairwise_tukeyhsd(dst["CHOL"], dst["Category"])
print(tukey_CHOL)

model_PROT = ols("PROT ~ C(Category)", data=dst).fit()
anova_PROT = sm.stats.anova_lm(model_PROT, typ=2)
print(anova_PROT)

tukey_PROT = pairwise_tukeyhsd(dst["PROT"], dst["Category"])
print(tukey_PROT)

# Kruskal-Wallis + Dunn’s Test (Holm)
def kruskal_dunn(var):
    groups = [g[var].values for _, g in dst.groupby("Category")]
    H, p = stats.kruskal(*groups)
    print(f"\nKruskal-Wallis for {var}: H={H:.4f}, p={p:.6f}")

    dunn = sp.posthoc_dunn(dst, val_col=var, group_col="Category", p_adjust="holm")
    print(dunn)

kruskal_dunn("ALP")
kruskal_dunn("ALT")
kruskal_dunn("AST")
kruskal_dunn("BIL")
kruskal_dunn("CHE")
kruskal_dunn("CREA")
kruskal_dunn("GGT")

# Correlation Matrix
dstNum = dst[["Age", "ALB", "ALP", "ALT", "AST", "BIL", 
              "CHE", "CHOL", "CREA", "GGT", "PROT"]]

dstMAT = dstNum.corr()

plt.figure(figsize=(10, 8))
sns.heatmap(dstMAT, annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Correlation Matrix")
plt.show()

# K-means clustering
# Remove ID and Category columns (same as R: -c(1,3))
dstUS = dst.drop(dst.columns[[0, 2]], axis=1)

kmeansDST = KMeans(n_clusters=4, n_init=100, random_state=100)
clusters = kmeansDST.fit_predict(dstUS)

dst["Cluster"] = clusters

# Confusion Matrix for Clustering
dstCat = dst.copy()
dstCat["Category"] = dstCat["Category"].cat.codes + 1

cm = confusion_matrix(dstCat["Category"], dst["Cluster"] + 1)
print(cm)

print("Accuracy:", accuracy_score(dstCat["Category"], dst["Cluster"] + 1))
print(classification_report(dstCat["Category"], dst["Cluster"] + 1))

from sklearn.decomposition import PCA

# Visualization
pca = PCA(n_components=2)
dst_pca = pca.fit_transform(dstUS)

plt.scatter(dst_pca[:, 0], dst_pca[:, 1], c=clusters)
plt.title("K-Means Clusters")
plt.xlabel("PC1")
plt.ylabel("PC2")
plt.show()
