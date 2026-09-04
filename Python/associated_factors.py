HR Analytics – Employee Attrition

Analysis:
Feature importance analysis using Random Forest to identify the
variables most associated with employee attrition.

Environment:
Microsoft Power BI – Python Visual

Input:
The script uses the Power BI-provided dataset DataFrame.

Method:
Random Forest Classifier

Target:
Attrition (No = 0, Yes = 1)

Output:
Top 10 features ranked by Random Forest feature importance.



import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder

# =========================================================
# 1. DATASET
# =========================================================

df = dataset.copy()

# =========================================================
# 2. VARIABLE TARGET
# =========================================================

target = 'Attrition'

df[target] = df[target].astype(str).str.strip()

df[target] = df[target].map({
    'No': 0,
    'Yes': 1
})

# Remove invalid targets
df = df.dropna(subset=[target])

# =========================================================
# 3. FEATURES
# =========================================================

features = [
    'OverTime',
    'MonthlyIncome',
    'Age',
    'TotalWorkingYears',
    'YearsAtCompany',
    'JobLevel',
    'JobSatisfaction',
    'EnvironmentSatisfaction',
    'WorkLifeBalance',
    'DistanceFromHome',
    'YearsInCurrentRole',
    'YearsSinceLastPromotion',
    'YearsWithCurrManager'
]


features = [col for col in features if col in df.columns]

X = df[features].copy()
y = df[target]

# =========================================================
# 4. TRANSFORM CATEGORICAL VALUES
# =========================================================

categorical_cols = X.select_dtypes(
    include=['object', 'category']
).columns.tolist()

X = pd.get_dummies(
    X,
    columns=categorical_cols,
    drop_first=True
)

X = X.apply(pd.to_numeric, errors='coerce')

X = X.fillna(X.median(numeric_only=True))

# =========================================================
# 5. RANDOM FOREST
# =========================================================

model = RandomForestClassifier(
    n_estimators=300,
    max_depth=6,
    min_samples_leaf=5,
    random_state=42,
    class_weight='balanced'
)

model.fit(X, y)

# =========================================================
# 6. FEATURE IMPORTANCE
# =========================================================

importance = pd.DataFrame({
    'Feature': X.columns,
    'Importance': model.feature_importances_
})

# Ordenar
importance = importance.sort_values(
    'Importance',
    ascending=False
)

# Top 10
top_features = importance.head(10).sort_values(
    'Importance',
    ascending=True
)

# =========================================================
# 7. GRAPHIC
# =========================================================

fig, ax = plt.subplots(figsize=(12, 8))

ax.barh(
    top_features['Feature'],
    top_features['Importance']
)

ax.set_title(
    'Top 10 Factors Associated with Employee Attrition',
    fontsize=14,
    fontweight='bold'
)

ax.set_xlabel('Feature Importance')
ax.set_ylabel('')

# Valores nas barras
for i, value in enumerate(top_features['Importance']):
    ax.text(
        value + 0.003,
        i,
        f'{value:.3f}',
        va='center',
        fontsize=12
    )

ax.grid(
    axis='x',
    alpha=0.1
)

plt.tight_layout()

plt.show()