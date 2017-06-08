# Setup python on department linux machines

For the purposes of this class we will use an anaconda installation of python as opposed to system python. This will allow us to use additional packages and keep a consistent python experience across machines/operating systems. To get started open a terminal on a UNC linux machine type

    unc_anaconda
    
This will load you into a bash (differences with tcsh are negligible for general use) subshell with anaconda python as the default python. You should see your terminal prompt change to `(anaconda_bash)user@machine:~$` or similar. Once in this subshell you can make your own anaconda environment by typing

    conda create --name astro scikit-learn matplotlib astropy pymc spyder pandas

This will create an anaconda environment named `astro` in your home directory (`~/.conda/envs/astro`), with the packages that you need for this class. To activate this environment type

    source activate astro
    
You are now your own anaconda environment, and your terminal prompt should start with `(astro)(anaconda_bash)...`. To finish installing packages we will use for this class type the following

    conda install -c OpenAstronomy healpy
    pip install git+https://github.com/astroML/astroML
    conda install nb_conda_kernels
    
The first line installs healpy through anaconda.org, and the second installs the most up to data version of astroML through the github repository.

Note that the above steps are a one time setup. If you ever want to use the anaconda environment you have set up all you have to do is type

    unc_anaconda
    source activate astro
