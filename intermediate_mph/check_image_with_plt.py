import json
import matplotlib.pyplot as plt

class Keypoint:
    def __init__(self, data):
        self.x = data['x']
        self.y = data['y']
        self.covered = data['covered']

class Data:
    def __init__(self, data, root):
        self.root = root
        self.image_path = None
        self.meta = None
        self.n_hand = None
        self.hands = []
        assert type(data) == dict
        self.image_path = data['image_path'].replace('hand/', self.root + '/images/')
        self.meta = data['meta']
        hand_data = data['keypoints']
        self.n_hand = len(hand_data) #2
        for i, hand_data_ in enumerate(hand_data):
            hand = []
            for keypoint_data in hand_data_:
                hand.append(Keypoint(keypoint_data))
            self.hands.append(hand)
        assert self.n_hand == len(self.hands), 'n_hand=%d len(hands)=%d'%(self.n_hand, len(self.hands))


class DatasetForMPHTesting:
    def __init__(self, folder_path):
        self.root = folder_path
        self.meta_path = folder_path + '/meta.json'
        self.data = []
        with open(self.meta_path, 'r') as f:
            data = json.load(f)
        for dat in data:
            dat = Data(dat, self.root)
            self.data.append(dat)
        print('init %d data <- %s'%(len(self.data), self.meta_path))

    def plot_keypoint_on_image(self, index=0):
        path = self.data[index].image_path
        print(path)
        img = plt.imread(path)
        plt.imshow(img)
        plt.show()


def main():
    overlap0 = DatasetForMPHTesting('./dataset_for_mp_testing/overlap0')
    overlap0.plot_keypoint_on_image()
    print('end')


if __name__ == '__main__':
    main()
