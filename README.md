Webshots
========

This takes screenshots of a sitemap and places them in a hierarchical folder structure.



Installation
------------

You'll need to install some required Python modules.

**On Mac:**

1. `sudo easy_install pip`
2. `sudo pip install -r requirements.txt`
3. Add `export PATH=$PATH:path/to/folder/for/webshots` to ~/.bash_profile



Usage
-----

- You'll need to pass in a YAML file defining the sitemap's structure. An example is located in conf/sitemap.yaml
- Take screenshots with the following commmand:
  - `webshots sitemap config_file output_folder`
    - **config_file:** path to yaml config file.
    - **output_folder:** path to output folder (e.g., ~/Downloads).




