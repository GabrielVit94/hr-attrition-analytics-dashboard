HR Analytics – Employee Attrition Analysis

Analysis:
Correlation analysis between numerical employee variables.

Environment:
Microsoft Power BI – Python Visual

Input:
Power BI-provided `dataset` DataFrame.

Method:
Pearson correlation matrix.

Output:
Correlation heatmap displaying the strength and direction of
relationships between numerical variables.

Note:
Correlation indicates statistical association and should not be
interpreted as evidence of causality

""""


import matplotlib.pyplot as plt
import pandas as pd

# Only metrics columns
df = dataset.select_dtypes(include='number')

# Correlation Matrix
corr = df.corr()

# Create graphic
fig, ax = plt.subplots(figsize=(16, 12))

# Heatmap RdBu
im = ax.imshow(
    corr,
    cmap='RdBu',
    vmin=-1,
    vmax=1,
    aspect='auto'
)

# Axis Labels 
ax.set_xticks(range(len(corr.columns)))
ax.set_yticks(range(len(corr.columns)))

ax.set_xticklabels(
    corr.columns,
    rotation=45,
    ha='right',
    fontsize=12
)

ax.set_yticklabels(
    corr.columns,
    fontsize=12
)

# Cell Values
for i in range(len(corr.columns)):
    for j in range(len(corr.columns)):
        valor = corr.iloc[i, j]

        
        cor_texto = 'white' if abs(valor) > 0.6 else 'black'

        ax.text(
            j,
            i,
            f"{valor:.2f}",
            ha='center',
            va='center',
            fontsize=12,
            color=cor_texto,
            fontweight='bold'
        )

# Color Bar
cbar = plt.colorbar(im)
cbar.set_label(
    'Correlação',
    rotation=270,
    labelpad=20
)

# Title
ax.set_title(
    "Correlation Heatmap Between Numeric Variables",
    fontsize=14,
    fontweight='bold',
    pad=20
)

plt.tight_layout()
plt.show()