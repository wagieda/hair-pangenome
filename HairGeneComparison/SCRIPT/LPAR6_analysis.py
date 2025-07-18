import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

csv_file = 'data/lpar6_data - Sheet1.csv'

import matplotlib.pyplot as plt
import numpy as np

populations = ['African', 'American Indigenous', 'American', 'Ashkenazi Jewish', 'East Asian', 
               'Finnish', 'Middle Eastern', 'Non-Finnish European', 'Remaining', 'South Asian']

freq_T = [0.971, 0.921, 0.908, 0.744, 0.841, 0.874, 0.788, 0.853, 0.876, 0.812]

freq_G = [0.029, 0.079, 0.092, 0.256, 0.159, 0.126, 0.212, 0.147, 0.124, 0.188]

x = np.arange(len(populations))  

width = 0.35  #   

fig, ax = plt.subplots(figsize=(14,7))


rects1 = ax.bar(x - width/2, freq_T, width, label='Allele T', color='skyblue')
rects2 = ax.bar(x + width/2, freq_G, width, label='Allele G', color='orange')


ax.set_ylabel('Allele Frequency')
ax.set_title('Allele Frequencies of SNP rs13240024 in LPAR6 Gene Across Populations')
ax.set_xticks(x)
ax.set_xticklabels(populations, rotation=45, ha='right')
ax.set_ylim(0, 1)
ax.legend()


plt.tight_layout()
plt.show()

