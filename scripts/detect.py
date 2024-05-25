import argparse
import torch
from models.yolo import Model
from utils.datasets import LoadImages
from utils.general import non_max_suppression, scale_coords, plot_one_box
import cv2

def detect(opt):
    device = torch.device('mps' if torch.backends.mps.is_available() else 'cpu')
    model = Model(opt.cfg).to(device)
    model.load_state_dict(torch.load(opt.weights, map_location=device))
    model.eval()

    dataset = LoadImages(opt.source, img_size=opt.img_size)
   
