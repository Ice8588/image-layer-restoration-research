# Qualitative Results

現有 canonical 圖直接保留；未裁掉失敗 seed。以下屬 Synthetic Benchmark，來源公開許可由研究者確認。配對圖由原分析的 median-LPIPS seed 規則選取，不代表最佳 seed，也不等於人工 pass。

## Baseline → Evaluated Variant

### qual_coin_x_chest_cov70

![qual_coin_x_chest_cov70](../assets/results/paired/qual_coin_x_chest_cov70.png)

### qual_emblem_x_banner_cov50

![qual_emblem_x_banner_cov50](../assets/results/paired/qual_emblem_x_banner_cov50.png)

### qual_food_x_plate_cov70

![qual_food_x_plate_cov70](../assets/results/paired/qual_food_x_plate_cov70.png)

### qual_gem_x_ring_cov30

![qual_gem_x_ring_cov30](../assets/results/paired/qual_gem_x_ring_cov30.png)

### qual_hammer_x_anvil_cov30

![qual_hammer_x_anvil_cov30](../assets/results/paired/qual_hammer_x_anvil_cov30.png)

### qual_key_x_lock_cov50

![qual_key_x_lock_cov50](../assets/results/paired/qual_key_x_lock_cov50.png)

### qual_pen_x_book_cov30

![qual_pen_x_book_cov30](../assets/results/paired/qual_pen_x_book_cov30.png)

### qual_potion_x_crate_cov50

![qual_potion_x_crate_cov50](../assets/results/paired/qual_potion_x_crate_cov50.png)

### qual_sword_x_shield_cov30

![qual_sword_x_shield_cov30](../assets/results/paired/qual_sword_x_shield_cov30.png)

## All-seed failure / variation evidence

下面保留原始所有 seeds，需區分前景殘留、補全錯誤、幻覺與 preservation damage；這些 failure 類型不能合併成單一品質原因。

### attentive_eraser_visible_mask_0pct_coin_x_chest_cov70

![attentive_eraser_visible_mask_0pct_coin_x_chest_cov70](../assets/results/all_seeds/attentive_eraser_visible_mask_0pct_coin_x_chest_cov70.png)

### flux2_prompt_gem_x_ring_cov30

![flux2_prompt_gem_x_ring_cov30](../assets/results/all_seeds/flux2_prompt_gem_x_ring_cov30.png)

### qwen2511_class_word_prompt_v2_lab_noise_mask_oracle_3pct_coin_x_chest_cov70

![qwen2511_class_word_prompt_v2_lab_noise_mask_oracle_3pct_coin_x_chest_cov70](../assets/results/all_seeds/qwen2511_class_word_prompt_v2_lab_noise_mask_oracle_3pct_coin_x_chest_cov70.png)
