import json
import matplotlib.pyplot as plt

with open("bns_example_result.json", "r") as f:
    data = json.load(f)

#print(data.keys())

posterior = data['posterior']

#print(posterior.keys())

content = posterior['content']

#print(content.keys())

chirp_mass = content['chirp_mass']
mass_ratio = content['mass_ratio']
luminosity_distance = content['luminosity_distance']
mass_1 =  content['mass_1']
mass_2 =  content['mass_2']

print(chirp_mass)
#print(len(chirp_mass))
#print(len(mass_ratio))
#print(len(luminosity_distance))

plt.hist(chirp_mass, bins =50)
#plt.colorbar(label='Frequency')
plt.grid(True)

plt.savefig("chirp_mass_histogram.png", dpi=300)
