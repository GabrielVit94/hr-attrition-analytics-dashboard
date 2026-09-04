HR Analytics – Employee Attrition Analysis

Analysis:
Comparison of employee satisfaction profiles between employees
who left the company and employees who stayed.

Environment:
Microsoft Power BI – Python Visual

Input:
Power BI-provided `dataset` DataFrame.

Method:
Average satisfaction scores grouped by Attrition status.

Metrics:
- Job Satisfaction
- Environment Satisfaction
- Relationship Satisfaction
- Work-Life Balance

Output:
Radar chart comparing the satisfaction profiles of employees
with Attrition = Yes and Attrition = No.


"""


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# CONFIG


satisfaction_cols = [
    'JobSatisfaction',
    'EnvironmentSatisfaction',
    'RelationshipSatisfaction',
    'WorkLifeBalance'
]

labels = [
    'Job Satisfaction',
    'Environment Satisfaction',
    'Relationship Satisfaction',
    'Work-Life Balance'
]


# DATA PREPARATION


df = dataset.copy()

for col in satisfaction_cols:
    df[col] = pd.to_numeric(df[col], errors='coerce')


df['Attrition'] = df['Attrition'].astype(str).str.strip()


profile = df.groupby('Attrition')[satisfaction_cols].mean()


if 'Yes' not in profile.index or 'No' not in profile.index:
    raise ValueError(
        "A coluna Attrition precisa conter os valores 'Yes' e 'No'."
    )

yes_values = profile.loc['Yes'].values.tolist()
no_values = profile.loc['No'].values.tolist()


# RADAR CONFIG


N = len(labels)

angles = np.linspace(0, 2 * np.pi, N, endpoint=False).tolist()
angles += angles[:1]

yes_plot = yes_values + yes_values[:1]
no_plot = no_values + no_values[:1]


# FIGURE


fig, ax = plt.subplots(
    figsize=(8, 7),
    subplot_kw=dict(polar=True)
)

# Start at the top
ax.set_theta_offset(np.pi / 2)
ax.set_theta_direction(-1)


# ATTRITION GROUP = NO

ax.plot(
    angles,
    no_plot,
    linewidth=3,
    label='Attrition = No'
)

ax.fill(
    angles,
    no_plot,
    alpha=0.15
)


# ATTRITION GROUPE = YES

ax.plot(
    angles,
    yes_plot,
    linewidth=3,
    label='Attrition = Yes'
)

ax.fill(
    angles,
    yes_plot,
    alpha=0.35
)


# AXIS

ax.set_xticks(angles[:-1])
ax.set_xticklabels(
    labels,
    fontsize=10,
    fontweight='bold'
)

# Fixed scale 1–4
ax.set_ylim(1, 4)

ax.set_yticks([1, 2, 3, 4])
ax.set_yticklabels(
    ['1', '2', '3', '4'],
    fontsize=9
)


# VORTEX VALUES


for angle, value in zip(angles[:-1], yes_values):
    ax.text(
        angle,
        value + 0.12,
        f'{value:.2f}',
        ha='center',
        va='center',
        fontsize=7,
        fontweight='bold'
    )

for angle, value in zip(angles[:-1], no_values):
    ax.text(
        angle,
        value - 0.18,
        f'{value:.2f}',
        ha='center',
        va='center',
        fontsize=7,
        fontweight='bold'
    )


# TITLE

ax.set_title(
    'Satisfaction Profile: Employees Who Left vs. Stayed',
    fontsize=14,
    fontweight='bold',
    pad=25
)


# LEGEND


ax.legend(
    loc='upper right',
    bbox_to_anchor=(1.25, 1.10),
    frameon=False
)


# GRID

ax.grid(alpha=0.35)
plt.tight_layout()
plt.show()