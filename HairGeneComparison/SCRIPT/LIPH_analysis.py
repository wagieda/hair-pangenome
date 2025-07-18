import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

data = {
    'Population': ['ALL (All Populations)', 'AFR (Africa)', 'AMI (American Indigenous)', 'AMR (Admixed American)', 
                   'ASJ (Ashkenazi Jewish)', 'EAS (East Asian)', 'FIN (Finnish)', 'MID (Middle Eastern)', 
                   'NFE (Non-Finnish European)', 'Remaining (Other Populations)', 'SAS (South Asian)'],
    'T_frequency': [0.319, 0.357, 0.352, 0.330, 0.233, 0.200, 0.355, 0.344, 0.299, 0.305, 0.334],
    'A_frequency': [0.681, 0.643, 0.648, 0.670, 0.767, 0.800, 0.645, 0.656, 0.701, 0.695, 0.666]
}

df = pd.DataFrame(data)

x = np.arange(len(df['Population']))  #  
width = 0.35  # 

fig, ax = plt.subplots(figsize=(14,6))
rects1 = ax.bar(x - width/2, df['T_frequency'], width, label='T Allele Frequency')
rects2 = ax.bar(x + width/2, df['A_frequency'], width, label='A Allele Frequency')

ax.set_ylabel('Allele Frequency')
ax.set_title('Allele Frequencies of SNP rs726253 in LIPH Gene Across Populations')
ax.set_xticks(x)
ax.set_xticklabels(df['Population'], rotation=45, ha='right')
ax.legend()

plt.tight_layout()
plt.show()
