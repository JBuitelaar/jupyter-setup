# Introduction
I've been having some problems setting up Jupyter the way I want, but finally figured it out. This repo makes that reproducible.

You don't need to install Jupyter in every environment. As long as there is one where you can run jupyter from, the other ones just need to install ipykernel. To make sure they are discoverable you need ```nb_conda_kernels```.

# How?
To create one environment with jupyter in it, install from the file:
> conda env create -f jupyter.yml

Next, you can configure some settings, using:
> python create_jupyter_config.py

It will change the file ```jupyter_notebook_config.py```

# What didn't work?

## not using ```nb_conda```
It should be possible to just add new kernels using this in the relevant environment:
> python -m ipykernel install --user --name XYZ

However, I couldn't get that to work. The problem is that $PATH (```os.environ['PATH']```) still points to the jupyter environment instead of the environment. That means that DLLs (like you need for numpy) couldn't be found (unless you install them in the jupyter folder)
