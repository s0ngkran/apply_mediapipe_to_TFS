# for i in range(5, 16):
# 	num = str(i).zfill(2)
# 	print('nohup nice python train%s.py -col -nw 3 > tr%s.col&'%(num, num))

# for i in range(15, 26):
# 	num = str(i).zfill(2)
# 	print('call python ./train%s.py -bt -nw 3 > tr%s.bt&'%(num, num))

# cnt = 0
# ep = [
#     1042,
#     1396,
#     674,
#     2592,
#     2120,
#     1884,
#     1684,
#     2194,
# ]
# for i in range(5, 16):
# 	print('nohup nice python train%s.py -col -nw 5 -bt > tr%s.bt.new.col&'%(str(i).zfill(2), str(i).zfill(2)))

ep = [
'5',
'6',
'7',
'8',
'9',
'10',
'11',
'12',
'13',
'14',
'15',
]

ep2 = [
'2066',
'2294',
'1574',
'2492',
'2632',
'1286',
'3698',
'3274',
'834',
'1656',
'2084',
]

for ep_,ep2_ in zip(ep,ep2):
    print('python train%s.py -sh -nw 2 -te %s te'%(str(ep_).zfill(2), ep2_))
# import shutil
# for i in range(16, 26):
# 	src = './train04.py'
# 	dist = './train%s.py'%(str(i).zfill(2))
# 	shutil.copyfile(src, dist)

a = [
83.60,
85.68,
83.49,
87.09,
85.01,
82.54,
85.79,
85.18,
80.69,
86.08,
85.12,
]
for i in a:
    print(i,end=',')
print()
import matplotlib.pyplot as plt
import numpy as np

dump63 = [80.35, 81.41, 80.85, 85.96, 81.58, 80.07, 81.58, 83.16, 83.44, 82.82, ]
rel_index0 = [ 83.60, 85.68, 83.49, 87.09, 85.01, 82.54, 85.79, 85.18, 80.69, 86.08, 85.12, ]
dump63 = np.array(dump63)
rel_index0 = np.array(rel_index0)
data = [dump63, rel_index0]
fig7, ax7 = plt.subplots()
# ax7.set_title('title')
bp = ax7.boxplot(data)
ax7.set_ylim(76,90)

# plt.show()
res = {}
for key, value in bp.items():
    res[key] = [v.get_data() for v in value]
    print(key, res[key])
print(res)

