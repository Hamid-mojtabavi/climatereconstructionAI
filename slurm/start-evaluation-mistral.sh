#!/usr/bin/env bash

#SBATCH -J JohannesMeuer
#SBATCH -p gpu
#SBATCH -A bb1152
#SBATCH -n 1
#SBATCH --cpus-per-task=64
#SBATCH --time=12:00:00
#SBATCH --mem=256G
#SBATCH --nodelist=mg201

module load cuda/10.0.130
module load singularity/3.6.1-gcc-9.1.0

singularity run --bind /work/bb1152/k204233/ --nv /work/bb1152/k204233/climatereconstructionAI/torch_img_mistral.sif python /work/bb1152/k204233/climatereconstructionAI/climatereconstructionAI/evaluate.py