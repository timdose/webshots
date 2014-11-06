Webshots
========

This takes screenshots of a sitemap and places them in a hierarchical folder structure.



Installation
------------

You'll need to install some required Python modules.

**On Mac:**

1. Clone this repository.
2. If you don't already have pip installed, install it with `sudo easy_install pip`.
3. Install the Python packages required for Webshots with `sudo pip install -r requirements.txt`.
4. To be able to issue the webshots command from any folder, add it to your path
   by placing `export PATH=$PATH:path/to/folder/for/webshots` in your ~/.bash_profile file.



Usage
-----

Webshots commands take the following format:

`webshots command_name config_file output_folder`

    - **config_file:** path to yaml config file.
    - **output_folder:** path to output folder (e.g., ~/Downloads)


Currently there are two commands available

1. `urls`: Takes simple list of urls and saves resulting screenshots placed in a single, timestamped folder.
2. `sitemap` Takes hierarchical list of urls and saves resulting screenshots in a defined folder structure.


### The `urls` command 

- You'll need to pass in a YAML file defining the urls. An example is located in conf/urls.yaml
- Take screenshots with the following commmand:
  - `webshots urls config_file output_folder`
    - **config_file:** path to yaml config file.
    - **output_folder:** path to output folder (e.g., ~/Downloads).

To test this out on a Mac, you could try the following command:

`webshots urls examples/urls.yaml ~/Downloads`


### The `sitemap` command 

- You'll need to pass in a YAML file defining the urls. An example is located in conf/sitemap.yaml
- Take screenshots with the following commmand:
  - `webshots sitemap config_file output_folder`
    - **config_file:** path to yaml config file.
    - **output_folder:** path to output folder (e.g., ~/Downloads).

To test this out on a Mac, you could try the following command:

`webshots sitemap examples/sitemap.yaml ~/Downloads`




