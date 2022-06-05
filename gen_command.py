# python train15.py -sh -nw 2 -te 2084 te

train = [
	26,
27,
28,
29,
30,
31,
32,
33,
34,
35,
]

ep = [
	770,
1984,
1648,
540,
1408,
770,
1126,
1924,
2180,
1802,
]

for train_, ep_ in zip(train, ep):
	print('python train%d.py -sh -nw 2 -te %d ten'%(train_, ep_))

# python train15.py -sh -nw 2 -te 2084 te
