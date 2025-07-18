import matplotlib.pyplot as plt

# 
data = {
    "all": 0.001,
    "afr": 0.0001792,
    "amr": 0.0001789,
    "eas": 0.000,
    "fin": 0.004,
    "mid": 0.000,
    "nfe": 0.001,
    "remaining": 0.001,
    "sas": 0.0001275
}

# 
labels = {
    "all": "All populations",
    "afr": "African",
    "amr": "American",
    "eas": "East Asian",
    "fin": "Finnish",
    "mid": "Middle Eastern",
    "nfe": "Non-Finnish European",
    "remaining": "Remaining",
    "sas": "South Asian"
}

populations = list(data.keys())
frequencies = [data[pop] for pop in populations]

plt.figure(figsize=(12, 6))
plt.bar([labels[pop] for pop in populations], frequencies, color='skyblue')
plt.xlabel('Population')
plt.ylabel('Allele Frequency (A)')
plt.title('Allele Frequency for SNP rs74315329 in gene KRT17')
plt.ylim(0, max(frequencies)*1.2)
plt.xticks(rotation=45, ha='right')  
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()
