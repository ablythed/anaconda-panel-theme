# Anaconda Panel Theme

Apply Anaconda branding to your own panel applications.

[![anacnoda-theme.png](https://i.postimg.cc/YC6pSMh4/anacnoda-theme.png)](https://postimg.cc/HrLGZG0H)
## Setup

### Desktop

On your desktop you will need to install either [Anaconda](https://anaconda.com/download) or
[Miniconda](https://docs.conda.io/en/latest/miniconda.html). When using Miniconda be certain
to install `anaconda-project` by running

```
conda install -n root anaconda-project
```

You can utilize this template repository by either

* Clicking the `Use this template` button to create a new repository
* Downloading an archive of this template by clicking `Code` then `Download ZIP`

After cloning a new repository from this template or extracting the downloaded ZIP
open a terminal and `cd` to the project directory.

Run `anaconda-project prepare` too create the required Conda environment.

### Anaconda Enterprise

To utilize this template on Anaconda Enterprise 

1. download an archive of this template either by
    * Clicking `Code` then `Download ZIP` above or
    * Clicking [here](https://github.com/anaconda/anaconda-panel-theme/archive/master.tar.gz) to download a `tar.gz` file.
1. Upload the archive and start an editor session.

## Development
Your Panel application can be built using either a Jupyter Notebook or Python script.

* When writing a Jupyter Notebook name your file `main.ipynb`
* When writing a Python script name your file `main.py`

Be certain to add any needed packages to the `anaconda-project.yml` file provided by running:

```
anaconda-project add-packages [package_spec [package_spec ...]]
```

See the [Anaconda Project documentation](https://anaconda-project.readthedocs.io/en/latest/#) for more details.
### Jupyter Notebook

If you are developing your Panel application in a Jupyter Notebook, you
should also add `notebook` to the `anaconda-project.yml` package list as follows

```
anaconda-project add-packages notebook
```

Then you can launch the Jupyter Notebook interface by running the following
command in the terminal:

```
anaconda-project run jupyter notebook
```

## Build your Panel application

To use the Anaconda themed Panel templated include the following code in your script
or notebook.

```python
# Import packages you need
import panel as pn

import anaconda

# uncomment if working interactively in a Notebook
# pn.extension()

my_app = pn.template.MaterialTemplate(
    logo='assets/logo.png',
    header_background='#213D5A',
    favicon='assets/favicon.png',
    theme=anaconda.AnacondaTheme
)
my_app.config.css_files.append('assets/anaconda.css')

#####################################################
# You can set the title of your Panel application
# by assigning a string to my_app.title.
#
# You can use the anaconda.AnacondaColors list as a
# cmap with HoloViews and HVPlot.
#
# Add your Panes to the main area and optionally
# add widgets to the sidebar area.
#
# See the User Guide.
# https://panel.holoviz.org/user_guide/Templates.html
#####################################################


my_app.servable()
```

## Run your application

To run your application execute the following command in your terminal

```
anaconda-project run
```
