# how_to
how to configure the system


1. postgresql:

Install PostgreSQL
Install PostgreSQL using the installer linked to here: http://www.postgresql.org/download/windows/

Run through the entire install process. Keeping the defaults will work, but make note of your postgres password, as we will need this later to login to the database system. For convenience, one option is to keep the default username “postgres” and use the password “postgres”.

(Optional) Ins


2. change Jupyter Notebook start directory
https://stackoverflow.com/questions/35254852/how-to-change-the-jupyter-start-up-folder

I just had the same problem and tested the methods mentioned above. After several trials, I realized that they are partially correct and are not the complete solution. I tested the below in Windows 10 and Anaconda 4.4.0 with python 3.6.

There are two ways to do even though they have only very small difference. Follow the way marneylc suggested above: i.e.

1) Open "Anaconda Prompt" and type jupyter notebook --generate-config

2) You find the file in C:\Users\username\.jupyter\jupyter_notebook_config.py

3) Change the line of #c.NotebookApp.notebook_dir = '' to c.NotebookApp.notebook_dir = 'c:\test\your_root\'

4) Then, go to the shortcut of Jupyter Notebook located in C:\Users\User_name\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Anaconda3 (64-bit)

5) Do the right click and go to the Properties

6) In the Target field, remove %USERPROFILE% as stenlytw suggested above.

7) Then, In the field of Start in, type the same directory of c:\test\your_root\ in jupyter_notebook_config.py

8) Done!

As the simpler way, after step 3, go to C:\Users\User_name\Anaconda3\Scripts

4-2) You can see the file of jupyter-notebook.exe and click it.

5-2) Then, the Jupyter start the folder you specified in jupyter_notebook_config.py. So make the shortcut of this file.

6-2) Done.

3. change CMD home


4. insert Youtube video:
https://nbviewer.jupyter.org/github/axu2/improved-seam-carving/blob/master/Improved%20Seam%20Carving.ipynb
from IPython.lib.display import YouTubeVideo
YouTubeVideo('6NcIJXTlugc')


5. [How To Run A Python Script With Notepad++](https://www.youtube.com/watch?v=WTOVVeAD_-M)


how to export conda environment:

1. cd C:\DO_NOT_TOUCH\NMR\HTNMR\conda_env
2. conda activate HTNMR_env
3. conda env export > HTNMR_env.yml


create environment:
1. cd C:\DO_NOT_TOUCH\NMR\HTNMR\conda_env
2. conda env create --file HTNMR_env.yml

install packages in allergen.yml in the current allergen environment:        
conda env update --name allergen --file allergen.yml  

remove: 
conda env remove -n HTNMR_env


Add conda env to Jupyter Notebook Kernel

[ref](https://blog.ronin.cloud/adding-conda-environment-to-jupyter-notebook/)

conda activate myenv

pip install --user ipykernel 

python -m ipykernel install --user --name=myenv

