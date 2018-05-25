# Setup Python on your laptop

We will use python bundled with a number of scientific libraries (Numpy, Scipy, matplotlib, etc) in an installation called "Anaconda". Follow the instructions to [download and install Anaconda for your operating system from the official documentation](https://docs.continuum.io/anaconda/install). To determine whether your system has a 32-bit or 64-bit processor, see the following links: [Mac Users](http://support.apple.com/kb/HT3696) or [Windows Users](http://support.microsoft.com/kb/827218).

After you have installed Anaconda, open up the Anaconda terminal/command prompt and ensure Anaconda is installed and up to date by typing

    conda update conda
    conda update anaconda
    
The default scipy stack is already installed on the with anaconda, all we have to do is install some additional modules

    conda install -c OpenAstronomy healpy   # does not work on windows
    conda install pymc

Though there are version of AstroML available through the conda channels, it is a little outdated, we will instead install the latest version available through github. To do this type

    conda install git
    pip install git+https://github.com/astroML/astroML
    
To verify you have the appropriate packages installed you can run

    conda list
