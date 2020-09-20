# Resource Catalogue Template 

This repository contains a template for a resource catalogue that can be hosted online and provide access to resources metadata, and functionality for data retrieval. If you host the resource catalogue on Github, it is possible to crowdsource the resources in the catalogue via third-party contributions. The description of resources is based on the [DCAT vocabulary](https://www.w3.org/TR/vocab-dcat-2). Resources are generic, but can be specialised on each instance of this template. 

## Usage

If you want to build a catalogue of resources, which you can host on Github, you can follow the following steps:

1. Fork this repository
1. Change the name of the fork repository to the name of your catalogue
1. For each resource you want to add to your catalogue, copy the [resource_template.yml_](./_data/resource_template.yml_), rename the file with each resource name and make sure that the extension is ```yml```.Then, include the details of your resource or generate these resource descriptions programmatically.