import os , shutil, zipfile

def zip_display_in_train():
    model_root = './checkpoints'
    for models in os.listdir(model_root):
        path_to_models = os.path.join(model_root,models)
        checks = list(os.listdir(path_to_models))
        if 'display_in_train' not in checks:
            print("There is no display in train in {} !".format(models))
            continue

        path_to_display = os.path.join(path_to_models, 'display_in_train')
        copy_to = os.makedirs(os.path.join('./display_in_train',models))
        shutil.copytree(path_to_display, copy_to)
    
    f = zipfile.ZipFile('display_in_train.zip','w',zipfile.ZIP_DEFLATED)

    startdir = "./display_in_train"
    for dirpath, dirnames, filenames in os.walk(startdir):
        for filename in filenames:
            f.write(os.path.join(dirpath,filename))
    f.close()

zip_display_in_train()
