import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import glob


def create_plot(iteration):
	patience_refill_set = [1, 2, 5, 10, 50, 100, 1000]
	patience_threshold_set = [50, 100, 250, 500, 750, 1000]
	iteration = str(iteration)
	spec_data = np.zeros((6, 7, 4))

	path = r'./data_recreate_defense_' + 'alpha'  # use your path
	all_files = glob.glob(path + "/*_iter-" + iteration + ".csv")
	for i, e in enumerate(patience_refill_set):
		for j, f in enumerate(patience_threshold_set):
			for file in all_files:
				if ("dil_incr-" + str(f // e)) in file:
					if ("dil_max-" + str(f)) in file:
						dt = np.array(pd.read_csv(file, header=None))
						modified_data = dt[-1]
						spec_data[j, i, 0] = modified_data[0]
						spec_data[j, i, 2] = modified_data[2]
						break

	path = r'./data_recreate_defense_' + 'delta'  # use your path
	all_files = glob.glob(path + "/*_iter-" + iteration + ".csv")
	for i, e in enumerate(patience_refill_set):
		for j, f in enumerate(patience_threshold_set):
			for file in all_files:
				if ("dil_incr-" + str(f // e)) in file:
					if ("dil_max-" + str(f)) in file:
						dt = np.array(pd.read_csv(file, header=None))
						modified_data = dt[-1]
						spec_data[j, i, 1] = modified_data[0]
						spec_data[j, i, 3] = modified_data[2]
						break

	# #heatmap axis
	patience_refill_set.reverse()
	patience_threshold_set.reverse()
	x = np.array(patience_threshold_set)
	y = np.array(patience_refill_set)
	x = x[::-1]
	y = y[::-1]
	color_blue = sns.color_palette("coolwarm_r", as_cmap=True)
	color_green = sns.color_palette("coolwarm_r", as_cmap=True)

	plt.clf()
	fig, axn = plt.subplots(2, 2, sharex=True, sharey=True)

	df = []

	for i in range(spec_data.shape[-1]):
		df.append(pd.DataFrame(spec_data[:, :, i]))

	for i, ax in enumerate(axn.flat):
		if (i % 2 == 0):
			df[i] = df[i].rename_axis("Threshold")  # TODO
		if (i > 1):
			df[i] = df[i].rename_axis("Refill", axis=1)
		color = color_blue if i < 2 else color_green
		# choose same scales as original paper. i = {0,1} are the top heatmaps, {2,3} the bottom ones
		vmax = 1 if i > 1 else 12
		plot = sns.heatmap(df[i], ax=ax, xticklabels=y, yticklabels=x, cmap=color, cbar=not (i % 2 == 0), vmin=0, vmax=vmax)
		plt.xticks(rotation=45)

	plot.figure.savefig("graphs/heatmap_data_recreation_defense_iteration_" + iteration + ".png")


for iteration in range(0, 3):
	create_plot(iteration)
