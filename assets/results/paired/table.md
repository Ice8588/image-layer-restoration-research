# Qwen Image Edit 2511 V2 class-word prompt (oracle) vs Qwen Image Edit 2511 V2 class-word + Lab NoiseMask 3% (oracle)

LPIPS 差值定義為 left − right，負值代表 left 較佳。PSNR／SSIM 越高越好。

| Coverage | Class | Left LPIPS | Right LPIPS | Diff | LPIPS winner | Left PSNR | Right PSNR | Left SSIM | Right SSIM |
|---|---|---:|---:|---:|---|---:|---:|---:|---:|
| cov30 | `gem_x_ring` | 0.064 | 0.042 | +0.021 | `qwen2511_class_word_prompt_v2_lab_noise_mask_oracle_3pct` | 21.27 | 22.05 | 0.849 | 0.882 |
| cov30 | `pen_x_book` | 0.110 | 0.026 | +0.083 | `qwen2511_class_word_prompt_v2_lab_noise_mask_oracle_3pct` | 25.87 | 30.10 | 0.872 | 0.954 |
| cov30 | `sword_x_shield` | 0.068 | 0.067 | +0.001 | `qwen2511_class_word_prompt_v2_lab_noise_mask_oracle_3pct` | 23.48 | 23.50 | 0.878 | 0.881 |
| cov30 | `hammer_x_anvil` | 0.032 | 0.024 | +0.008 | `qwen2511_class_word_prompt_v2_lab_noise_mask_oracle_3pct` | 29.71 | 30.20 | 0.957 | 0.970 |
| cov50 | `emblem_x_banner` | 0.021 | 0.020 | +0.001 | `qwen2511_class_word_prompt_v2_lab_noise_mask_oracle_3pct` | 31.48 | 32.65 | 0.971 | 0.977 |
| cov50 | `key_x_lock` | 0.105 | 0.103 | +0.002 | `qwen2511_class_word_prompt_v2_lab_noise_mask_oracle_3pct` | 21.67 | 21.73 | 0.925 | 0.934 |
| cov50 | `potion_x_crate` | 0.032 | 0.031 | +0.002 | `qwen2511_class_word_prompt_v2_lab_noise_mask_oracle_3pct` | 29.37 | 29.15 | 0.919 | 0.923 |
| cov70 | `coin_x_chest` | 0.162 | 0.151 | +0.011 | `qwen2511_class_word_prompt_v2_lab_noise_mask_oracle_3pct` | 17.82 | 18.43 | 0.702 | 0.736 |
| cov70 | `food_x_plate` | 0.035 | 0.031 | +0.004 | `qwen2511_class_word_prompt_v2_lab_noise_mask_oracle_3pct` | 28.92 | 29.77 | 0.951 | 0.962 |

## Overall

| Scope | Left LPIPS | Right LPIPS | Left PSNR | Right PSNR | Left SSIM | Right SSIM |
|---|---:|---:|---:|---:|---:|---:|
| 9-class macro | 0.070 | 0.055 | 25.51 | 26.40 | 0.892 | 0.913 |

Paired LPIPS mean difference: **+0.015**; 95% CI [+0.005, +0.026]; left wins 7/27, right wins 20/27.
