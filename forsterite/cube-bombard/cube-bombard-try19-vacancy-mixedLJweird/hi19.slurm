#!/bin/bash
#SBATCH --account=adam_lasp
#SBATCH --mail-user=al2vy@virginia.edu

#SBATCH --partition=parallel
#SBATCH --nodes=8
#SBATCH --ntasks-per-node=32

#SBATCH --time=3-00:00:00
#SBATCH --mem-per-cpu=1G
#SBATCH --job-name="bomb-try19"

#SBATCH --mail-type=FAIL
#SBATCH --mail-type=END

module purge
export MODULEPATH=/project/LASP/modulefiles:$MODULEPATH
module load lammps/17April2024-cpu 

srun lmp -in bombard_try19.lammps 
