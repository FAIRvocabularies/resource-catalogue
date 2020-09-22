# Resource Catalogue Template 

This repository contains a template for a resource catalogue that can be hosted online and provide access to resources metadata, and functionality for data retrieval. If you host the resource catalogue on Github, it is possible to crowdsource the resources in the catalogue via third-party contributions. The description of resources is based on the [DCAT vocabulary](https://www.w3.org/TR/vocab-dcat-2). Resources are generic, but can be specialised on each instance of this template. 

## Usage

If you want to build a catalogue of resources, which you can host on Github, you can follow the following steps:

1. Fork this repository
1. Change the name of the fork repository to the name of your catalogue
1. Modify the [About page](about.md) to describe your own resource catalogue.
1. For each resource you want to add to your catalogue: 
    1. make a copy of the template for resource descriptions: [resource_template.yml_](./_data/resource_template.yml_)
    1. rename the file with the resource name and change the extension to ```yml```
    1. Then, modify the file to includ the description of your resource 
    The resources' descriptions must be in the ```./_data``` folder. Of course, you can also automate the generation of resource descriptions. 
