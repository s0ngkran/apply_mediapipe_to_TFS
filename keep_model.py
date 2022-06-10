import os
save_folder = './p_save'
if not os.path.exists(save_folder):
	os.mkdir(save_folder)

import shutil 
for _,__,fnames in os.walk('./save'):
	print('walk')

keep_model_list =[

]
training = [
16,
17,
18,
19,
20,
21,
22,
23,
24,
25,
5,
6,
7,
8,
9,
10,
11,
12,
13,
14,
15,
]
ep = [
3180,
3428,
2236,
1970,
2644,
770,
800,
2986,
3780,
3478,
2066,
2294,
1574,
2492,
2632,
1286,
3698,
3274,
834,
1656,
2084,
]
for training, ep in zip(training, ep):
	name = 'train%s.pyepoch%s.model'%(str(training).zfill(2), str(ep).zfill(10))
	keep_model_list.append(name)

print(keep_model_list)
for i in keep_model_list:
	print(i)
# for fname in fnames:
# 	if fname in keep_model_list:
# 		src = os.path.join('./save', fname)
# 		dist = os.path.join('./p_save', fname)
# 		shutil.copyfile(src, dist)
# 		print(src, dist)


