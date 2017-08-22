import matplotlib.pyplot as plt
from matplotlib.pyplot import savefig
import numpy as np
import matplotlib.gridspec as gridspec

def read_dev_from_log(fname):
    f1 = open(fname, 'r')
    dev_list = []
    old = -1
    for l in f1:
        if 'Epoch' in l and 'dev percentage' in l:
            if int(l.split()[6]) == old:
                continue # dublicate
            dev_list.append(float(l.split()[9]))
            old = int(l.split()[6])
    return dev_list

dev_list = read_dev_from_log('adadoulstm_1')
dev_tree = read_dev_from_log('adadou_a_3')

plt.cla()   # Clear axis
plt.clf()   # Clear figure
plt.close() # Close a figure window
fig = plt.figure(figsize=(12, 6))
ax = fig.add_subplot(111)
index = xrange(60)
index_2 = xrange(0, 64, 2)
ax.plot(dev_list, 'ro')
plt.xlabel('Epochs')
plt.ylabel('Accuracy')
plt.xticks(index_2)
plt.savefig('CNN_LSTM_dev_acc', format='pdf')

plt.cla()   # Clear axis
plt.clf()   # Clear figure
plt.close() # Close a figure window
fig = plt.figure(figsize=(12, 6))
ax = fig.add_subplot(111)
index = xrange(61)
index_2 = xrange(0, 64, 2)
ax.plot(dev_tree, 'ro')
plt.xlabel('Epochs')
plt.ylabel('Accuracy')
plt.xticks(index_2)
plt.savefig('CNN_Tree_LSTM_dev_acc', format='pdf')
