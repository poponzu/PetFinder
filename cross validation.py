def main():
    initialize()

    df = pd.read_csv("../input/sameoldfold/train_10folds.csv")
#     cv_df = df[["Id", "Pawpularity"]].copy()
#     oof_pred = np.zeros(len(df))

    for fold in range(Config.num_fold):
        with wandb_init(f"fold{fold}"):
            df_train = df.query(f"kfold != {fold}").reset_index(drop=True)
            df_valid = df.query(f"kfold == {fold}").reset_index(drop=True)
#             valid_index = df.query(f"kfold == {fold}").index

            train_img_paths = [f"../input/petfinder-pawpularity-score/train/{x}.jpg" for x in df_train["Id"].values]
            valid_img_paths = [f"../input/petfinder-pawpularity-score/train/{x}.jpg" for x in df_valid["Id"].values]

            train_dataset = PawpularDataset(
                image_paths=train_img_paths,
                dense_features=df_train[Config.dense_features].values,
                targets=df_train.Pawpularity.values,
                augmentations=Augmentation.train_aug,
            )

            valid_dataset = PawpularDataset(
                image_paths=valid_img_paths,
                dense_features=df_valid[Config.dense_features].values,
                targets=df_valid.Pawpularity.values,
                augmentations=Augmentation.valid_aug,
            )

            model = PawpularModel(Config.model_name)

            es = EarlyStopping(
                monitor="valid_rmse",
                model_path=Config.output_path / f"model{fold}.bin",
                patience=Config.patience,
                mode="min",
                save_weights_only=True,
            )
            wb = WandBCallbacks()

            callbacks = []
            if not Config.debug:
                callbacks.append(es)
                callbacks.append(wb)

            model.fit(
                train_dataset,
                valid_dataset=valid_dataset,
                train_bs=Config.batch_size,
                valid_bs=Config.batch_size,
                device="cuda",
                epochs=Config.epochs,
                callbacks=callbacks,
                fp16=True,
                n_jobs=4,

            )

#             prediction = []
#             for pred in model.predict(valid_dataset, batch_size=Config.batch_size, n_jobs=-1):
#                 prediction.extend(pred.tolist())
#             oof_pred[valid_index] = prediction

            del model
            gc.collect()

#     cv_df["cv"] = oof_pred
#     cv_df.to_csv("cross_validation.csv", index=False)
#     print("cross validation: ", eval(Config.metrics_name)(df.Pawpularity.values, oof_pred, squared=False))
