
import setuptools
import sys
import os
import re 


def build(version, requirements, long_description, entry_points=None):
  entry_points = entry_points or {}
  sys.argv[1] = "sdist"
  sys.argv.append("bdist_wheel")
  
  setuptools.setup(
      name='epyk_x_js_datepicker',
      author='',
      version=version,
      author_email='',
      description="",
      long_description=long_description,
      long_description_content_type="text/markdown",
      url="",
      packages=setuptools.find_packages(),
      install_requires=requirements, # list of scripts
      entry_points=entry_points, # {"console_scripts": entry_points}
      python_requires=">=2.7",
      classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 2.7",
        "License :: OSI Approved :: GNU General Public License (GPL)",
        "Operating System :: OS Independent",
      ],
    )


if __name__ == '__main__':
  if len(sys.argv) < 2:
    raise Exception("version number is required")
  
  res = re.match('([0-9]+).([0-9]+).([0-9]+)', sys.argv[1])
  if res is None:
    raise Exception("Invalid version number")
  
  script_path = os.path.dirname(os.path.abspath(__file__))
  project_path, name = os.path.split(script_path)
  
  with open(os.path.join(script_path, 'requirements.txt')) as f:
    requirements = f.read()
  with open(os.path.join(script_path, 'README.md')) as f:
    description = f.read()
  build(sys.argv[1], requirements, description)
