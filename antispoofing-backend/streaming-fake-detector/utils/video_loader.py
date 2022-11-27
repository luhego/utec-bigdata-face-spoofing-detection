import torch
import torchvision.transforms as transforms

BATCH_SIZE = 64


class VideoLoader:
    def process(self, dataset):
        print(f"Generating video loader: {dataset.shape}")
        transform = transforms.Compose([transforms.ToPILImage(), transforms.ToTensor()])
        train_set = CustomDataset((torch.Tensor(dataset),), transform=transform)
        loader = torch.utils.data.DataLoader(
            dataset=train_set, batch_size=BATCH_SIZE, shuffle=True
        )
        return loader


class CustomDataset(torch.utils.data.Dataset):
    def __init__(self, tensors, transform=None):
        assert all(tensors[0].size(0) == tensor.size(0) for tensor in tensors)
        self.tensors = tensors
        self.transform = transform

    def __getitem__(self, index):
        x = self.tensors[0][index]

        if self.transform:
            x = self.transform(x)

        return x

    def __len__(self):
        return self.tensors[0].size(0)
