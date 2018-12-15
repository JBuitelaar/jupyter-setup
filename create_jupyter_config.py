import os.path
# Create the jupyter_notebook_config file.
# * set default browser to Chrome
# * set notebook folder to '%UserProfile\python\notebooks

browser_file = r'%UserProfile%\AppData\Local\Google\Chrome\Application\chrome.exe'
notebook_folder = 'repos/notebooks'
content = ''
if os.path.isfile(os.path.expandvars(browser_file)):
    content += "c.NotebookApp.browser = '{} %s'\n".format(os.path.expandvars(browser_file).replace('\\', '/'))

content += "c.NotebookApp.default_url = '/tree/{}'\n".format(notebook_folder)

# See https://github.com/Anaconda-Platform/nb_conda_kernels
content += "c.CondaKernelSpecManager.name_format = 'conda:{1}'"

config_file = os.path.expandvars(r'%UserProfile%\.jupyter\jupyter_notebook_config.py')
with open(config_file, 'w') as f:
    f.write(content)

# I couldn't get this to work (not even sure it's correct). Would be good if we get a sensible default.
# c.MultiKernelManager.default_kernel_name = 'conda env:qa1'
	
# To get the standard file back again (everything is commented out):
# jupyter notebook --generate-config
