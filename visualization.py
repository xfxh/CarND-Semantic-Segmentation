#!/usr/bin/env python3
import csv
import matplotlib.pyplot as plt
import numpy as np

epochs = []
with open('./data/test.csv') as data:
	reader = csv.reader(data)
	for row in reader:
		epoch = []
		for value in row:
			epoch.append(float(value))
		epochs.append(epoch)

fig, ax =plt.subplots(figsize=(20,10))
ax.violinplot(epochs, showmeans=True)
ax.yaxis.grid(True)
ax.set_xticks([y+1 for y in range(len(epochs))])
ax.set_xlabel("Epochs")
ax.set_ylabel("Loss")
ax.set_title("50 Epochs")
plt.show()