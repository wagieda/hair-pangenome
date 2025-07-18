import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# 
data = {
    'Population_short': ['ALL', 'AFR', 'AMI', 'AMR', 'ASJ', 'EAS', 'FIN', 'MID', 'NFE', 'REM', 'SAS'],
    'Population_full': ['All', 'African', 'Amish', 'American', 'Ashkenazi Jewish', 'East Asian', 
                        'Finnish', 'Middle Eastern', 'Non-Finnish European', 'Remaining', 'South Asian'],
    'A_freq': [0.415, 0.479, 0.564, 0.410, 0.424, 0.311, 0.422, 0.431, 0.387, 0.411, 0.348],
    'G_freq': [0.585, 0.521, 0.436, 0.590, 0.576, 0.689, 0.578, 0.569, 0.613, 0.589, 0.652]
}

df = pd.DataFrame(data)

df['Population_label'] = df['Population_short'] + ' ' + df['Population_full']

#  
bar_width = 0.4
index = np.arange(len(df['Population_label']))

plt.figure(figsize=(14, 6))
plt.bar(index, df['A_freq'], bar_width, label='Allele A')
plt.bar(index + bar_width, df['G_freq'], bar_width, label='Allele G')

plt.xlabel('Population')
plt.ylabel('Allele Frequency')
plt.title('Allele Frequencies of SNP rs2981582 in FGFR2 across Populations')

# 
plt.xticks(index + bar_width / 2, df['Population_label'], rotation=45, ha='right')

plt.legend()
plt.tight_layout()
plt.show()

