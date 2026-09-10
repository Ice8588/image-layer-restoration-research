# FLUX.2 vs Qwen Image Edit 2511 iterative class-word prompt (oracle)

所有差值皆為 FLUX.2 − Qwen 2511。LPIPS 越低越好；PSNR／SSIM 越高越好。
每個 class 值先平均同 sample 的 seeds 0–4，再平均該 class 的 5 samples。

## Stage 1 · reveal middle

| Class | FLUX LPIPS | Qwen LPIPS | Diff | Winner | FLUX PSNR | Qwen PSNR | FLUX SSIM | Qwen SSIM |
|---|---:|---:|---:|---|---:|---:|---:|---:|
| `coin_x_padlock_x_chest` | 0.012 | 0.039 | -0.027 | FLUX.2 | 18.27 | 11.76 | 0.853 | 0.422 |
| `coin_x_potion_x_crate` | 0.014 | 0.017 | -0.003 | FLUX.2 | 20.08 | 18.79 | 0.863 | 0.830 |
| `gem_x_coin_x_chest` | 0.017 | 0.017 | -0.000 | FLUX.2 | 24.42 | 24.08 | 0.825 | 0.786 |
| `gem_x_hammer_x_anvil` | 0.008 | 0.008 | +0.001 | Qwen 2511 | 20.67 | 20.72 | 0.865 | 0.879 |
| `gem_x_sword_x_anvil` | 0.001 | 0.007 | -0.006 | FLUX.2 | 27.74 | 14.90 | 0.973 | 0.499 |
| `gem_x_sword_x_shield` | 0.001 | 0.007 | -0.006 | FLUX.2 | 29.22 | 14.12 | 0.981 | 0.501 |
| `hammer_x_sword_x_anvil` | 0.002 | 0.001 | +0.001 | Qwen 2511 | 25.29 | 21.75 | 0.808 | 0.748 |
| `key_x_coin_x_chest` | 0.005 | 0.006 | -0.001 | FLUX.2 | 23.88 | 22.90 | 0.908 | 0.868 |
| `key_x_padlock_x_chest` | 0.009 | 0.034 | -0.025 | FLUX.2 | 20.25 | 12.00 | 0.891 | 0.488 |
| `key_x_potion_x_crate` | 0.016 | 0.017 | -0.001 | FLUX.2 | 15.70 | 16.32 | 0.702 | 0.748 |

### 10-class macro

| Metric | FLUX.2 | Qwen 2511 | Diff | Winner | Paired 95% CI | Sample wins (FLUX/Qwen/tie) |
|---|---:|---:|---:|---|---|---:|
| LPIPS | 0.009 | 0.015 | -0.007 | FLUX.2 | [-0.010, -0.004] | 38/12/0 |
| PSNR | 22.55 | 17.73 | +4.819 | FLUX.2 | [+3.201, +6.523] | 38/12/0 |
| SSIM | 0.867 | 0.677 | +0.190 | FLUX.2 | [+0.123, +0.260] | 37/13/0 |

## Stage 2 chained · reveal back

| Class | FLUX LPIPS | Qwen LPIPS | Diff | Winner | FLUX PSNR | Qwen PSNR | FLUX SSIM | Qwen SSIM |
|---|---:|---:|---:|---|---:|---:|---:|---:|
| `coin_x_padlock_x_chest` | 0.042 | 0.062 | -0.020 | FLUX.2 | 16.83 | 13.68 | 0.746 | 0.526 |
| `coin_x_potion_x_crate` | 0.012 | 0.032 | -0.019 | FLUX.2 | 27.81 | 23.90 | 0.973 | 0.793 |
| `gem_x_coin_x_chest` | 0.041 | 0.072 | -0.031 | FLUX.2 | 17.38 | 12.81 | 0.773 | 0.437 |
| `gem_x_hammer_x_anvil` | 0.005 | 0.025 | -0.020 | FLUX.2 | 22.57 | 17.93 | 0.934 | 0.541 |
| `gem_x_sword_x_anvil` | 0.002 | 0.013 | -0.011 | FLUX.2 | 22.12 | 17.22 | 0.940 | 0.518 |
| `gem_x_sword_x_shield` | 0.005 | 0.021 | -0.016 | FLUX.2 | 21.42 | 13.25 | 0.910 | 0.334 |
| `hammer_x_sword_x_anvil` | 0.005 | 0.007 | -0.002 | FLUX.2 | 20.45 | 22.85 | 0.906 | 0.781 |
| `key_x_coin_x_chest` | 0.042 | 0.066 | -0.024 | FLUX.2 | 17.32 | 13.80 | 0.769 | 0.527 |
| `key_x_padlock_x_chest` | 0.044 | 0.061 | -0.017 | FLUX.2 | 16.62 | 14.08 | 0.725 | 0.553 |
| `key_x_potion_x_crate` | 0.012 | 0.040 | -0.028 | FLUX.2 | 28.34 | 22.66 | 0.974 | 0.733 |

### 10-class macro

| Metric | FLUX.2 | Qwen 2511 | Diff | Winner | Paired 95% CI | Sample wins (FLUX/Qwen/tie) |
|---|---:|---:|---:|---|---|---:|
| LPIPS | 0.021 | 0.040 | -0.019 | FLUX.2 | [-0.023, -0.015] | 47/3/0 |
| PSNR | 21.09 | 17.22 | +3.868 | FLUX.2 | [+2.652, +5.030] | 43/7/0 |
| SSIM | 0.865 | 0.574 | +0.291 | FLUX.2 | [+0.235, +0.347] | 48/2/0 |
