import matplotlib.pyplot as plt
import numpy as np


populations = [
    "All populations", 
    "African", 
    "Amish", 
    "American", 
    "Ashkenazi Jewish", 
    "East Asian", 
    "Finnish", 
    "Middle Eastern", 
    "Non-Finnish European", 
    "Remaining", 
    "South Asian"
]

allele_A_freq = [
    0.859, 0.966, 0.911, 0.889, 0.881, 0.998, 0.714, 0.862, 0.794, 0.855, 0.914
]

allele_C_freq = [
    6.628e-06, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.476e-05, 0.0, 0.0
]

allele_T_freq = [
    0.141, 0.034, 0.089, 0.111, 0.118, 0.002, 0.286, 0.138, 0.206, 0.145, 0.086
]

x = np.arange(len(populations))  
width = 0.25  

fig, ax = plt.subplots(figsize=(15, 7))


ax.bar(x - width, allele_A_freq, width, label='Allele A', color='skyblue')
ax.bar(x, allele_C_freq, width, label='Allele C', color='lightcoral')
ax.bar(x + width, allele_T_freq, width, label='Allele T', color='lightgreen')


ax.set_xticks(x)
ax.set_xticklabels(populations, rotation=45, ha='right')
ax.set_ylabel('Allele Frequency')
ax.set_title('Allele Frequencies of SNP rs11803731 (TCHH) by Population')
ax.legend()

plt.tight_layout()
plt.show()

