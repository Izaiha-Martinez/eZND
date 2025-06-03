#!/bin/sh
#
#SBATCH -p main
#SBATCH --qos main
#SBATCH -n 1
##SBATCH --mem=4000
##SBATCH -C C6420

#export PATH=/grps2/dmtownsley/sjboos/code/yt-conda/bin:$PATH
export PATH=/grps2/dmtownsley/iemartinez/myenv/bin:$PATH
unset PYTHONPATH

export MESA_DIR=/grps2/dmtownsley/sjboos/newBurn/mesa_8845_broxton
export OMP_NUM_THREADS=1

mkdir -p timesteps
sh ./post_process.sh  
