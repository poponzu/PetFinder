# Soule

## 2021/11/15 
### [No.5](https://www.kaggle.com/soule50431/petfinder-no-5-inference?scriptVersionId=79935099)
#### Feature
回帰問題を分類問題として扱い、tezで動かした
MixUpを入れた
#### Model
swin_tiny_patch4_window7_224
#### Score
- CV : 
- Public : 18.37828


## 2021/11/16
### [No.6](https://www.kaggle.com/soule50431/petfinder-no-6-inference/notebook?scriptVersionId=80041165)
#### Feature
画像の情報だけで分類させた
#### Model
swin_tiny_patch4_window7_224
#### Score
- CV : 
- Public : 18.39619

## 2021/11/17
### [No.7](https://www.kaggle.com/soule50431/petfinder-no-7-inference?scriptVersionId=80128373)
#### Feature
モデルをtinyからlargeに変更した
#### Model
swin_large_patch4_window7_224
#### Score
- CV : 
- Public : 18.16206

## 2021/11/19
### [No.8](https://www.kaggle.com/soule50431/petfinder-no-8-inference/notebook?scriptVersionId=80242482)
#### Feature
オンライン画像拡張として、HorizontalFlipとVerticalFlipを確率0.5で適用させた
#### Model
swin_large_patch4_window7_224
#### Score
- CV : 
- Public : 18.05483

## 2021/11/20
### [No.9](https://www.kaggle.com/soule50431/petfinder-no-9-inference?scriptVersionId=80319055)
#### Feature
画像サイズが384のSwinTransformerを使用した
#### Model
swin_large_patch4_window12_384
#### Score
- CV : 
- Public : 18.00611


## 2021/11/21
### [No.10](https://www.kaggle.com/soule50431/petfinder-no-10-inference?scriptVersionId=80380088)
#### Feature
Resizeの代わりにRandomResizedCropを使用した
#### Model
swin_large_patch4_window12_384
#### Comment
baseの場合はRandomResizedCropを入れるとスコアが上がったが、largeでは逆に下がってしまった。
#### Score
- CV : 
- Public : 18.10817


## 2021/11/22
### [No.11](https://www.kaggle.com/soule50431/petfinder-no-11-inference?scriptVersionId=80467560)
#### Feature
画像サイズ224でもRandomResizedCropを試してみた
#### Model
swin_large_patch4_window7_224
#### Comment
画像サイズ384ではPublicが下がっていたが、224では少しだけ上がった
#### Score
- CV : 17.905690965168322
- Public : 18.02161


## 2021/11/24
### [No.13](https://www.kaggle.com/soule50431/petfinder-no-13-inference?scriptVersionId=80724674)
#### Feature
MixUpの確率を100%にして、λを0.2で固定した
#### Model
swin_large_patch4_window12_384
#### Comment
No.9よりは少し下がった
#### Score
- CV : 18.595032127165236
- Public : 18.01610

<!-- ## 0000/00/00
### [No.]()
#### Feature
#### Model
#### Score
- CV : 
- Public :  -->
