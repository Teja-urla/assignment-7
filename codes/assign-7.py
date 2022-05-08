import numpy as np

#Let 1 represent a white ball and 0 represent a black ball

#When no orange is drawn
urn1 = np.array([1]*12 + [0]*3)

#When a good orange is drawn
urn2 = np.array([1]*11 + [0]*3)

#when a good orange is drawn 3rd time
urn3 = np.array([1]*10 + [0]*3)

#Sample size
N=5000

#Draw the first orange
draw1 = np.random.choice(urn1, size=N)
unique1, count1 = np.unique(draw1, return_counts=True)
bitarray1 = dict(zip(unique1, count1))

#choosing the second good orange (given that the first orange is good)
draw2 = np.random.choice(urn2, size=bitarray1[1])
unique2, count2 = np.unique(draw2, return_counts=True)
bitarray2 = dict(zip(unique2, count2))

#choosing the second good orange (given that the first and second oranges are good)
draw3 = np.random.choice(urn3, size=bitarray2[1])
unique3, count3 = np.unique(draw3, return_counts=True)
bitarray3 = dict(zip(unique3, count3))
print("Empirical probability of 2 black balls being drawn is",bitarray3[1]/N)
