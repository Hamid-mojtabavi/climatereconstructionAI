import numpy as np
from torchvision import transforms
from .. import config as cfg


def img_normalization(img_data):
    img_std, img_mean, img_znorm = [], [], []
    if cfg.normalize_data:
        for i in range(len(img_data)):
            img_mean.append(np.nanmean(np.array(img_data[i])))
            img_std.append(np.nanstd(np.array(img_data[i])))
            img_znorm.append(transforms.Normalize(mean=[img_mean[-1]], std=[img_std[-1]]))

    return img_mean, img_std, img_znorm


def renormalize(img_data, img_mean, img_std):
    return img_std * img_data + img_mean


def bnd_normalization(img_mean, img_std, train_stats):

    bounds = np.ones((cfg.out_channels, 2)) * np.inf
    if train_stats is None:
        if cfg.n_target_data == 0:
            mean_val, std_val = img_mean[:cfg.out_channels], img_std[:cfg.out_channels]
        else:
            mean_val, std_val = img_mean[-cfg.n_target_data:], img_std[-cfg.n_target_data:]
    else:
        if cfg.n_target_data == 0:
            mean_val, std_val = train_stats["mean"][:cfg.out_channels], train_stats["std"][:cfg.out_channels]
        else:
            mean_val, std_val = train_stats["mean"][-cfg.n_target_data:], train_stats["std"][-cfg.n_target_data:]
    k = 0
    for bound in (cfg.min_bounds, cfg.max_bounds):
        bounds[:, k] = bound

        if cfg.normalize_data:
            bounds[:, k] = (bounds[:, k] - mean_val) / std_val

        k += 1

    return bounds
