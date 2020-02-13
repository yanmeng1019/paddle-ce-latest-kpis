#!/bin/bash
#This file is only used for continuous evaluation.
export CUDA_VISIBLE_DEVICES=0
python train.py --enable_ce True --use_multiprocess False --snapshot_iter 100 --max_iter 200 1> log_1card
cat log_1card | python _ce.py
export CUDA_VISIBLE_DEVICES=0,1,2,3,4,5,6,7
python train.py --enable_ce True --use_multiprocess False --snapshot_iter 100 --max_iter 200 1> log_8cards
cat log_8cards | python _ce.py
