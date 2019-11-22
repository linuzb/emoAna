set -eux

home_ernie=$PWD
home_ERNIE=$PWD

export TASK_DATA_PATH=$home_ernie/task_data
export MODEL_PATH=$home_ernie/model

sh $home_ERNIE/run_ChnSentiCorp.sh
