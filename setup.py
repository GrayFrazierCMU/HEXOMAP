from distutils.core import setup
setup(name='hexomap',
      version='0.2',
      package_dir={'': ''},
      packages=['hexomap'],
      package_data={'hexomap': ['data/fundamental_zone/*','data/materials/*','kernel_cuda/*']},
      scripts=['scripts/recon_mpi.py','scripts/reduction.py','scripts/recon.py'],
      )