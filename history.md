1. PetFinder train1とPetFinder No.1 inference(version 1/1) score 18.40795
  - model_name = 'swin_tiny_patch4_window7_224'
  - 学習データを[ファランクスのディスカッション](https://www.kaggle.com/c/petfinder-pawpularity-score/discussion/274303)にある切り取り済みで学習させた画像でした。
  - AugmentationはResize、HueSaturationValue、RandomBrightnessContrast、Normalize。これをベースとして考える。
  - これ以降notebookはこの命名 PetFinder udon train? ・ PetFinder udon inference?
2. score 18.29082
  - model_name = 'swin_base_patch4_window7_224'
  - 以降、1個目とモデルと値同じ
