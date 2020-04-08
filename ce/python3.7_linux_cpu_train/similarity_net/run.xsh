#!/bin/bash
export models_dir=$PWD/../../models_repo
#copy models files
rm -rf ${models_dir}/PaddleNLP/similarity_net/.run_ce.sh
rm -rf ${models_dir}/PaddleNLP/similarity_net/_ce.py
cp -r ${models_dir}/PaddleNLP/similarity_net/. ./
cd ..
if [ -d "shared_modules" ];then rm -rf shared_modules
fi
cp -r ${models_dir}/PaddleNLP/shared_modules .
cd similarity_net
if [ -d "data" ];then rm -rf data
fi
ln -s ${dataset_path}/similarity_net/data data
./.run_ce.sh
