set -ex
python train.py --dataroot ./datasets/facades --name facades_cycle --model cycle_gan --pool_size 50 --no_dropout
