from setuptools import find_packages, setup

package_name = 'task03'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages', ['resource/task03']),
        ('share/task03', ['package.xml']),
        ('share/task03/config', ['config/task03.yaml']),
        ('share/task03/launch', ['launch/task3.launch.py']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='root',
    maintainer_email='root@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            'service_node = task03.service_node:main',
        ],
    },
)
