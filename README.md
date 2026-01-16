# EDA HCV Patient Data Analysis

## 📋 Project Overview
This project explores clinical patient data to validate the non-invasive staging of Hepatitis C Virus (HCV) related liver disease progression. By performing Exploratory Data Analysis (EDA) and inferential statistics, I identified the biochemical markers that characterize the transition from healthy states to Hepatitis, Fibrosis, and Cirrhosis.

## 📊 Dataset Description
* **Source:** <a href= "https://archive.ics.uci.edu/dataset/571/hcv+data"> UC Irvine Machine Learning Repository </a>
* **Size:** 582 instances after cleaning.
* **Composition:** 526 healthy controls and 56 confirmed HCV patients across three stages.
* **Features:** 11 clinical features (biochemical markers) and 2 demographic features (Age, Sex).

## 🛠️ Statistical & Technical Methodology

### 1. Data Cleaning & Preprocessing
* Categorical variables were converted to integers (0, 1, 2, 3) to represent disease severity.
* Handled missing values (NAs) and removed unconfirmed (suspect) donor data to ensure a clean analytical baseline.

### 2. Distribution & Normality Analysis

* **Normality Testing:** Utilized KDE plots and Histograms to assess the shape and spread of each variable.
* **Parametric Features:** ALB, CHOL, and PROT exhibited normal distributions due to homeostatic regulation.
* **Non-Parametric Features:** ALP, ALT, AST, BIL, CREA, and GGT showed right-skewed distributions.

### 3. Inferential Statistics
* **Hypothesis Testing:** Conducted ANOVA for normally distributed variables and Kruskal-Wallis tests for skewed variables.
* **Post-Hoc Analysis:** Used TukeyHSD and Dunn Tests to pinpoint significant differences between specific disease stages.
* **Findings:** All biomarkers except CREA showed statistically significant differences across categories.

### 4. Clustering & Correlation
* **Correlation:** Observed strongest positive relationships between ALB-PROT ($r \approx 0.49$) and AST-GGT.
* **K-Means Clustering:** Applied 4-cluster modeling; results showed high recall for healthy donors (97.23%) but identified significant overlap in early-stage disease attributes.

## 💡 Key Clinical Insights
* **Synthetic Function:** Cirrhosis patients showed a marked decline in Albumin (ALB) and Cholinesterase (CHE), aligning with clinical expectations of impaired liver synthesis.
* **Inflammatory Markers:** AST and Bilirubin (BIL) followed typical clinical trends, showing significant elevation during end-stage disease progression.
* **Data Challenges:** A substantial class imbalance (90.4% healthy) and the presence of severe outliers in the Cirrhosis category (specifically in CREA) limit the generalizability of standard mean-based comparisons.

## 📢 Recommendations & Conclusion
* **Recommendation:** Future predictive models should utilize **SMOTE or oversampling techniques** to address the 90.4% class imbalance and employ **non-parametric machine learning algorithms** (like Random Forests) to better handle the skewed distributions and clinical outliers identified in this study[cite: 33, 270, 271].
* **Overall Finding:** This study statistically confirms that routine biochemical markers—particularly AST, GGT, and CHE—are robust indicators for distinguishing end-stage Cirrhosis from healthy states, though clinical imaging remains necessary for early-stage Hepatitis differentiation[cite: 91, 252].

---
### 🛠 Tools Used
* **Language:** Python/R
* **Libraries:** Pandas, Matplotlib, Seaborn, Scipy, Scikit-learn
* **Statistical Tests:** ANOVA, Kruskal-Wallis, TukeyHSD, Dunn Test, K-Means
