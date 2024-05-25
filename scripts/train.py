import argparse
import torch
from models.models import Darknet
from utils.datasets import LoadImagesAndLabels
from utils.general import check_img_size, non_max_suppression, scale_coords, xyxy2xywh, plot_one_box
from utils.loss import compute_loss

def train():
    parser = argparse.ArgumentParser()
    parser.add_argument('--epochs', type=int, default=300)
    parser.add_argument('--batch-size', type=int, default=16)
    parser.add_argument('--img-size', type=int, default=1280)
    parser.add_argument('--data', type=str, default='data/coco.yaml')
    parser.add_argument('--cfg', type=str, default='configs/yolor_p6.cfg')
    parser.add_argument('--weights', type=str, default='weights/yolor_p6.pt')
    parser.add_argument('--hyp', type=str, default='data/hyp.finetune.1280.yaml')
    opt = parser.parse_args()

    device = torch.device('mps' if torch.backends.mps.is_available() else 'cpu')
    model = Darknet(opt.cfg, opt.img_size).to(device)
    if opt.weights.endswith('.pt'):
        model.load_state_dict(torch.load(opt.weights, map_location=device)['model'])

    dataset = LoadImagesAndLabels(opt.data, opt.img_size)
    optimizer = torch.optim.SGD(model.parameters(), lr=opt.lr0, momentum=opt.momentum, weight_decay=opt.weight_decay)

    for epoch in range(opt.epochs):
        for batch_i, (imgs, targets, paths, _) in enumerate(dataset):
            imgs = imgs.to(device)
            targets = targets.to(device)

            pred = model(imgs)
            loss, _ = compute_loss(pred, targets, model)

            optimizer.zero_grad()
            loss.backward()
            optimizer.step()

            print(f"Epoch [{epoch}/{opt.epochs}], Step [{batch_i}/{len(dataset)}], Loss: {loss.item()}")

    torch.save(model.state_dict(), 'weights/yolor_p6_finetuned.pt')

if __name__ == '__main__':
    train()
