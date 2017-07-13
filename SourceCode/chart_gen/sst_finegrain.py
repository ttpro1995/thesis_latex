import matplotlib.pyplot as plt
from matplotlib.pyplot import savefig
import numpy as np
import matplotlib.gridspec as gridspec

labels = ["Very negative", "Negative", "Neutral", "Positive", "Very positive"]
dev_sentences = [139, 289, 229, 279, 165]
test_sentences = [279, 633, 389, 510, 399]
train_sentences = [1092, 2218, 1624, 2322, 1288]
plt.clf()
plt.cla()
plt.close()
gs = gridspec.GridSpec(2, 2)
ax1= plt.subplot(gs[0, 0])
ax1.pie(train_sentences,  autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')
ax1.set_title("Train")

ax2= plt.subplot(gs[0, 1])
ax2.pie(dev_sentences, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax2.axis('equal')
ax2.set_title("Dev")

ax3 = plt.subplot(gs[1, 1])
ax3.pie(test_sentences, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax3.axis('equal')
ax3.set_title("Test")

ax3.legend(labels=labels, bbox_to_anchor=(-1,1), loc="upper left")
plt.savefig('fine_grain', format='pdf')
