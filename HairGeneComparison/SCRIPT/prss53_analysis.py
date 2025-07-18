import pandas as pd
import matplotlib.pyplot as plt


data = {
    'Population': [
        'African/African American',
        'Admixed American',
        'Ashkenazi Jewish',
        'East Asian',
        'European (Finnish)',
        'Middle Eastern',
        'European (non-Finnish)',
        'South Asian'
    ],
    'Allele Count': [676, 14244, 339, 35269, 4976, 71, 20384, 5],
    'Allele Number': [75032, 59650, 29590, 44730, 63938, 6062, 1179630, 912]
}

df = pd.DataFrame(data)


df['Allele Frequency'] = df['Allele Count'] / df['Allele Number']


plt.figure(figsize=(12, 6))
plt.bar(df['Population'], df['Allele Frequency'], color='skyblue')
plt.xticks(rotation=45, ha='right')
plt.ylabel('Allele Frequency')
plt.title('Allele Frequency of rs11150606 in PRSS53 by Population')
plt.tight_layout()
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

