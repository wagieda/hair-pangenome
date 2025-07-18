import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data/EDAR_DATA.csv')
df.columns = df.columns.str.replace(r'\s+', ' ', regex=True).str.strip().str.lower()
df.rename(columns={
    'allel count': 'allele count',
    'allel number': 'allele number',
    'number of homozygot': 'number of homozygotes',
    'allel frequency': 'allele frequency'
}, inplace=True)

plt.figure(figsize=(12, 6))
plt.bar(df['genetic ancestry group'], df['allele frequency'], color='skyblue')
plt.xlabel('Genetic Ancestry Group')
plt.ylabel('Allele Frequency')
plt.title('Allele Frequency by Genetic Ancestry Group')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()
