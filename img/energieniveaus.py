#!/usr/bin/python
from __future__ import print_function
from __future__ import division
import matplotlib.pyplot as plt
import sys

fig=plt.figure()
ax=fig.add_axes((0,0,1,1))
ax.axis([5.0,100.0, 25.0,100.0])
ax.set_autoscale_on(False)
ax.axis('off')

plt.rc('text', usetex=True)
plt.rc('font', size=14)

def line(x1, x2, y1, y2, color=None, width=1.):
	ax.plot([x1, x2], [y1, y2], color=color, lw=width)

def text(x, y, text):
	ax.text(x, y, text, horizontalalignment='center')

def niveau(x, y, name, width = 14):
	line(x - width/2, x + width/2, y, y, 'green', 2.)
	text(x, y + 1.5, name)
	return (x - width/2, y), (x + width/2, y)	#start, end

def connect(s, e):
	line(s[0], e[0], s[1], e[1], 'blue', 1.5)

ytext = 30
#Bohr
xbohr = 15
text(xbohr, ytext, 'Bohr')

b1s, b1e = niveau(xbohr, 40, '$n = 1$', 12)
b2s, b2e = niveau(xbohr, 75, '$n = 2$', 12)

#dirac
xdirac = 40
text(xdirac, ytext, 'Dirac')

d1s, d1e = niveau(xdirac, 40-3, '$1\\rm{S}_{1/2}$', 18)
d2s, d2e = niveau(xdirac, 65-3, '$2\\rm{S}_{1/2}, 2\\rm{P}_{1/2} (\\uparrow \\downarrow)$', 18)
d3s, d3e = niveau(xdirac, 90-3, '$2\\rm{P}_{3/2} (\\uparrow \\uparrow)$', 18)

connect(b1e, d1s)
connect(b2e, d2s)
connect(b2e, d3s)

#lamb
xlamb = 65
text(xlamb, ytext, 'Lamb')

l1s, l1e = niveau(xlamb, 40, '$1\\rm{S}_{1/2}$')
l2s, l2e = niveau(xlamb, 56, '$2\\rm{P}_{1/2}$')
l3s, l3e = niveau(xlamb, 74, '$2\\rm{S}_{1/2}$')
l4s, l4e = niveau(xlamb, 90, '$2\\rm{P}_{3/2}$')

connect(d1e, l1s)
connect(d2e, l2s)
connect(d2e, l3s)
connect(d3e, l4s)

xhf = l1e[0] + 15
text(xhf, ytext, 'Hyperfeinstruktur')

for end in [l1e, l2e, l3e, l4e]:
	f_low = 1 if end == l4e else 0
	hhs, hhe = niveau(xhf, end[1] + 3, '$F = %d$'%(f_low+1), 12)
	hls, hle = niveau(xhf, end[1] - 3, '$F = %d$'%f_low, 12)
	connect(end, hhs)
	connect(end, hls)


if len(sys.argv) == 1:
	plt.show()
else:
	plt.savefig(sys.argv[1])
