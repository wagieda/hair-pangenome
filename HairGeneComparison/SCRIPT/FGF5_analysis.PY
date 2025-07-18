import matplotlib.pyplot as plt

populations = [
    'AFRICAN', 'AMERICAN', 'AMERICAN_LATIN', 'ASIAN_SOUTH_JEWISH', 'EAST_ASIAN', 
    'FINNISH', 'MIDDLE_EASTERN', 'NON_FINNISH_EUROPEAN', 'OTHER', 'SOUTH_ASIAN', 'ALL_POPULATIONS'
]

# T 
t_freq = [0.138, 0.412, 0.435, 0.559, 0.190, 0.558, 0.576, 0.575, 0.462, 0.353, 0.418]

# A   
a_freq = [0.860, 0.589, 0.565, 0.441, 0.812, 0.443, 0.456, 0.425, 0.533, 0.649, 0.582]

#   X
x = range(len(populations))

plt.figure(figsize=(12,6))

#  T
plt.bar(x, t_freq, width=0.4, label='T allele frequency', align='center', color='blue')

#   A
plt.bar([i + 0.4 for i in x], a_freq, width=0.4, label='A allele frequency', align='center', color='orange')

#   X 
plt.xticks([i + 0.2 for i in x], populations, rotation=45, ha='right')

plt.ylabel('Allele Frequency')
plt.title('Allele Frequencies of SNP rs7680591 in FGF5 Gene by Population')
plt.legend()
plt.tight_layout()
plt.show()
