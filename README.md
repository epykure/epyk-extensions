
![](https://raw.githubusercontent.com/epykure/epyk-ui/master/epyk/static/images/epyklogo_whole_big.png)

# Create an extension for Epyk


As Epyk is a collaborative project, it is possible to create your own extensions based on your favorite Javascript modules.
This will show you how to create, share and publish your packages to PYPI.

The naming convention for epyk extensions is epyk_x_%packageName%

Each package name is saved in this repository as a folder.

For example js_datepicker

## Architecture

<div align="center" >
    <img width=500 src="https://github.com/epykure/epyk-extensions/blob/master/static/images/extension.PNG?raw=true">
</div>

## Usage

### Basic use of components

It is possible to add quick extension to the framework

<div align="center">
    <img width=400 src="https://github.com/epykure/epyk-extensions/blob/master/static/images/basic_component.PNG?raw=true">
</div>

```py
from epyk.core.Page import Report

rptObj = Report()
rptObj.ui.extension('epyk_x_json', 'js')

dt = rptObj.ui.js.json_formatter({"test": 185})

rptObj.outs.html_file(path=config.OUTPUT_PATHS_LOCALS_HTML, name=config.OUT_FILENAME)
```

### Complex components

It is also possible to add more complex components interacting with various

<div align="center">
    <img width=400 src="https://github.com/epykure/epyk-extensions/blob/master/static/images/dom_link.PNG?raw=true">
</div>


<div align="center">
    <img width=400 src="https://github.com/epykure/epyk-extensions/blob/master/static/images/js_link.PNG?raw=true">
</div>