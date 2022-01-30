import os
from setuptools import setup, find_packages


def get_package_data(directory, filetype=None):
    os.chdir("yolov5")
    paths = []
    for dirpath, dirnames, filenames in os.walk(directory):
        for filename in filenames:
            if filetype is None or filename.endswith(filetype):
                paths.append(os.path.join(dirpath, filename))
    os.chdir("..")
    return paths


package_data_paths = get_package_data("data")
package_data_paths.extend(get_package_data("models", ".yaml"))

setup(
    name='yolov5',
    version='0.0',
    packages=find_packages(),
    include_package_data=True,
    package_data={'': package_data_paths},
    license='Creative Commons Attribution-Noncommercial-Share Alike license',
    # run installation requirements file
)
