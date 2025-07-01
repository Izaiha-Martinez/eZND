#!/bin/bash
#SBATCH -p main
#SBATCH --qos main
#SBATCH -n 1
#SBATCH --cpus-per-task=2


export MESASDK_ROOT=/grps2/dmtownsley/iemartinez/mesa_dir/mesasdk-23.7.3
export MESA_DIR=/grps2/dmtownsley/iemartinez/mesa_dir/mesa-r23.05.1

export OMP_NUM_THREADS=2

./run_new