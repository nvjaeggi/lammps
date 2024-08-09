#!/bin/bash
#SBATCH --account=adam_lasp
#SBATCH --mail-user=al2vy@virginia.edu

#SBATCH --partition=parallel
#SBATCH --nodes=4
#SBATCH --ntasks-per-node=32

#SBATCH --time=3-00:00:00
#SBATCH --mem-per-cpu=1G
#SBATCH --job-name="bomb-try24"
#SBATCH --array=1-9

#SBATCH --mail-type=FAIL
#SBATCH --mail-type=END

module purge
module load gcc
module load openmpi
export MODULEPATH=/project/LASP/modulefiles:$MODULEPATH
module load lammps/17April2024-cpu 

srun lmp -in bombard_try24.lammps -v param_file ${SLURM_ARRAY_TASK_ID}
