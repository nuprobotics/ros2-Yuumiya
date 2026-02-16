from launch import LaunchDescription
from launch_ros.actions import Node
import os
import yaml

def generate_launch_description():
    pkg_share = os.path.join(
        os.path.dirname(os.path.realpath(__file__)), '..', 'config'
    )
    config_file = os.path.join(pkg_share, 'task03.yaml')

    with open(config_file, 'r') as f:
        cfg = yaml.safe_load(f)

    service_name = cfg.get('service_name', '/trigger_service')
    default_string = cfg.get('default_string', 'No service available')

    service_node = Node(
        package='task03',
        executable='service_node',
        name='service_node',
        output='screen',
        parameters=[{'service_name': service_name, 'default_string': default_string}]
    )

    return LaunchDescription([service_node])