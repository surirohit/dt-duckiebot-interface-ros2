from setuptools import setup, find_packages

package_name = 'camera_driver'

setup(
    name=package_name,
    data_files=[
        ('share/' + package_name, ['package.xml',
                                   'launch/camera_driver_node.launch.py',
                                   ]),
        ('share/' + package_name + '/config', ['config/camera_driver_node/default.yaml']),
    ],
    version='1.0.0',
    packages=find_packages(exclude=['test']),
    zip_safe=True,
    author='Andrea Censi',
    author_email='acensi@idsc.mavt.ethz.ch',
    maintainer='Rohit Suri',
    maintainer_email='rohitsuri.nitr@gmail.com',
    keywords=['ROS2'],
    description='RPi Camera driver for ROS2 on Python3',
    license='GPLv3',
    entry_points={
        'console_scripts': [
            'camera_driver_node = src.camera_driver_node:main'
        ],
    },
)