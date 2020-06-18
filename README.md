
![](https://raw.githubusercontent.com/epykure/epyk-ui/master/epyk/static/images/epyklogo_whole_big.png)

# Create an extension for Epyk


As Epyk is a collaborative project, it is possible to create your own extensions based on your favorite Javascript modules.
This will show you how to create, share and publish your packages to PYPI.

The naming convention for epyk extensions is epyk_x_%packageName%

Each package name is saved in this repository as a folder.

Some examples are available (they are already part of the core framework):

- js_datepicker
- json


## Architecture

The architecture of the framework is granular enought to be extended by bespoke compoents.
The 

<div align="center" >
    <img width=500 src="https://github.com/epykure/epyk-extensions/blob/master/static/images/extension.PNG?raw=true">
</div>


## Usage

By convention Epyk extensions are proper Python packages

You can use the setup.py script to create your package and upload it to [pypi](https://pypi.org/).
Please make sure to communicate your changes to the community to ensure your code will be added to the core framework as part of the weekly releases.

The below line of code will load the components avaiable in the package and make it available in the *page.ui* entry point
```py
from epyk.core.Page import Report

rptObj = Report()
rptObj.ui.extension('epyk_x_json', 'js')

dt = rptObj.ui.js.json_formatter({"test": 185})

rptObj.outs.html_file(path=config.OUTPUT_PATHS_LOCALS_HTML, name=config.OUT_FILENAME)
```

### Basic use of components

The structure of a basic HTML component is as below.

It is defined in a class with a __str__ method for the HTML representation.
All the CSS styles and JavaScript common definition will be inherited from the Html base class.

<div align="center">
    <img width=600 src="https://github.com/epykure/epyk-extensions/blob/master/static/images/basic_component.PNG?raw=true">
</div>


### Complex components

It is also possible to add more complex components interacting different with JavaScript.

The below will add a specific behaviour on the dom object.

<div align="center">
    <img width=500 src="https://github.com/epykure/epyk-extensions/blob/master/static/images/dom_link.PNG?raw=true">
</div>

The below will add a specific behaviour on the JS part.

<div align="center">
    <img width=600 src="https://github.com/epykure/epyk-extensions/blob/master/static/images/js_link.PNG?raw=true">
</div>


### Community

The target of this repository is more a lab with the various components implemented.
This will also keep track of the changes and the various extension which should be added to the core framework.

Feel free to propose changes and create pull requests.

Bugs in the framework should be directly raised on the main repository.