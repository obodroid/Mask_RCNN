from coco import CocoDataset

if __name__ == '__main__':
    dataset = '/mnt/nas/COCO'
    for year in ['2014','2017']:
        dataset_train = CocoDataset()
        print("dataset {}".format(dataset))
        print("year {}".format(year))
        dataset_train.load_coco(dataset, "train", year=year, auto_download=True)
        if year in '2014':
            dataset_train.load_coco(dataset, "valminusminival", year=year, auto_download=True)
        dataset_train.prepare()

        # Validation dataset
        dataset_val = CocoDataset()
        val_type = "val" if year in '2017' else "minival"
        dataset_val.load_coco(dataset, val_type, year=year, auto_download=True)
        dataset_val.prepare()