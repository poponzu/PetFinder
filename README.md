# PetFinder
1. PetFinder train1とPetFinder No.1 inference(version 1/1) **score 18.40795**
  - model_name = 'swin_tiny_patch4_window7_224'
  - 学習データを[ファランクスのディスカッション](https://www.kaggle.com/c/petfinder-pawpularity-score/discussion/274303)にある切り取り済みで学習させた画像でした。
  - AugmentationはResize、HueSaturationValue、RandomBrightnessContrast、Normalize。これをベースとして考える。
  - これ以降notebookはこの命名 PetFinder udon train? ・ PetFinder udon inference? でいく
2. **score 18.29082**
  - model_name = 'swin_base_patch4_window7_224'
  - 以降、1個目とモデルと値同じ
  - モデルはlarge > base > tinyで良くなる
  - 次はAugmentationをして改善する　17.台を出したい。
3. **score  18.15736**
  - albumentations.RandomResizedCrop
  - albumentations.VerticalFlip(p=0.5), albumentations.HorizontalFlip(p=0.5)を追加した。
4. **score  18.16859**
  - albumentations.augmentations.geometric.transforms.ShiftScaleRotate(p=0.5)を追加した。
5. **CVscore 17.958034841337227 PBscore 18.13956**
  - mixupのlamdaをベータ関数のものから0.2に変更した。
  - 条件はモデル3と同じ(モデル4のアフィン変換を不採用)
