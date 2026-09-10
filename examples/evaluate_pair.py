"""Evaluate an already available RGB pair; no model inference."""
import argparse
import json
import numpy as np
from PIL import Image
from layer_restoration.metrics import psnr, ssim_standard

parser = argparse.ArgumentParser()
parser.add_argument("reference")
parser.add_argument("candidate")
args = parser.parse_args()
reference = np.asarray(Image.open(args.reference).convert("RGB"))
candidate = np.asarray(Image.open(args.candidate).convert("RGB"))
if candidate.shape != reference.shape:
    parser.error("reference and candidate must have identical RGB dimensions")
value = psnr(candidate, reference)
print(json.dumps({"scope": "full RGB canvas", "psnr": value if np.isfinite(value) else "infinity", "ssim_standard": ssim_standard(candidate, reference)}))
