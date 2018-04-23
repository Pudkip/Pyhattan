import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def FormatData(path, sep = '\t', chromosome = 'chr', p_value = 'p_wald'):
    data = pd.read_table(path, sep = sep)
    data['-log10(p_value)'] = -np.log10(data[p_value])
    data[chromosome] = data[chromosome].astype('category')
    data['ind'] = range(len(data))
    data_grouped = data.groupby((chromosome))
    return data, data_grouped

def GenerateManhattan(pyhattan_object, export_path = None, significance = 6, colors = ['#E24E42', '#008F95'], refSNP = False):
    data = pyhattan_object[0]
    data_grouped = pyhattan_object[1]

    fig = plt.figure()
    ax = fig.add_subplot(111)

    x_labels = []
    x_labels_pos = []
    for num, (name, group) in enumerate(data_grouped):
        group.plot(kind='scatter', x='ind', y='-log10(p_value)', color=colors[num % len(colors)], ax=ax, s= 10000/len(data))
        x_labels.append(name)
        x_labels_pos.append((group['ind'].iloc[-1] - (group['ind'].iloc[-1] - group['ind'].iloc[0]) / 2))

    ax.set_xticks(x_labels_pos)
    ax.set_xticklabels(x_labels)
    ax.set_xlim([0, len(data)])
    ax.set_ylim([0, data['-log10(p_value)'].max() + 1])
    ax.set_xlabel('Chromosome')
    plt.axhline(y=significance, color='gray', linestyle='-', linewidth = 0.5)
    plt.xticks(fontsize=8, rotation=60)
    plt.yticks(fontsize=8)

    if refSNP:
        for index, row in data.iterrows():
            if row['-log10(p_value)'] >= significance:
                ax.annotate(str(row[refSNP]), xy = (index, row['-log10(p_value)']))

    if export_path:
        plt.savefig(export_path)

    plt.show()
