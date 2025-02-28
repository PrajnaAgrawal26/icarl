from torchvision.datasets import CIFAR10
import numpy as np
import torch
from PIL import Image

class iCIFAR10(CIFAR10):
    def __init__(self, root,
                 classes=range(10),
                 train=True,
                 transform=None,
                 target_transform=None,
                 download=False):
        super(iCIFAR10, self).__init__(root,
                                       train=train,
                                       transform=transform,
                                       target_transform=target_transform,
                                       download=download)

        # Select subset of classes
        if self.train:
            mask = np.isin(self.targets, classes)
            self.data = self.data[mask]
            self.targets = np.array(self.targets)[mask]

        else:
            mask = np.isin(self.targets, classes)
            self.data = self.data[mask]
            self.targets = np.array(self.targets)[mask]

    def __getitem__(self, index):
        if self.train:
            img, target = self.data[index], self.targets[index]
        else:
            img, target = self.data[index], self.targets[index]

        img = Image.fromarray(img)

        if self.transform is not None:
            img = self.transform(img)

        if self.target_transform is not None:
            target = self.target_transform(target)

        return index, img, target

    def __len__(self):
        if self.train:
            return len(self.data)
        else:
            return len(self.data)

    def get_image_class(self, label):
        return self.data[np.array(self.targets) == label]

    def append(self, images, labels):
        """Append dataset with images and labels

        Args:
            images: Tensor of shape (N, C, H, W)
            labels: list of labels
        """
        self.data = np.concatenate((self.data, images), axis=0)
        self.targets = list(self.targets) + labels

class iCIFAR100(iCIFAR10):
    base_folder = 'cifar-100-python'
    url = "http://www.cs.toronto.edu/~kriz/cifar-100-python.tar.gz"
    filename = "cifar-100-python.tar.gz"
    tgz_md5 = 'eb9058c3a382ffc7106e4002c42a8d85'
    train_list = [
        ['train', '16019d7e3df5f24257cddd939b257f8d'],
    ]
    test_list = [
        ['test', 'f0ef6b0ae62326f3e7ffdfab6717acfc'],
    ]
