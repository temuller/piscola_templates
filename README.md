# PISCOLA Templates

This is a repository to develop new Spectral Energy Distribution (SED) templates for [PISCOLA](https://github.com/temuller/piscola/). This also serves as a testing grounds for the templates and they might, at some point, be incorporated in PISCOLA so they comes with the installation of the package.

## Adding templates to your PISCOLA installation

To add the templates from this repository into your own PISCOLA installation, follow the steps explained below.

First, clone this repository and move into the cloned directory:

```code
git clone https://github.com/temuller/piscola_templates.git
cd piscola_templates
```

activate the environment where you have PISCOLA installed (this might vary depending on your working scheme) and run the `add_templates.py` script:

```code
conda activate piscola
python add_templates.py
```

This will copy all the templates directories under youe PISCOLA installation. The script will print the names of the copied directories. You might need to add the necessary permission to run the script. In this case, just run `chmod +x add_templates.py`.

## Developing your own templates

If you wish to develop new templates that are not already included here, you can clone the repository and follow the notebooks that are found under the existing directories. You can also make pull requests if you desire to include the newly developed templates into this repository.