from launch import LaunchDescription
from launch_ros.actions import Node
from launch.substitutions import LaunchConfiguration
from launch.actions import DeclareLaunchArgument
from launch_ros.descriptions import ParameterValue
import os
import yaml

def generate_launch_description():
    pkg_share = os.path.join(
        os.path.dirname(os.path.realpath(__file__)), '..', 'config'
    )
    config_file = os.path.join(pkg_share, 'task02.yaml')

    with open(config_file, 'r') as f:
        cfg = yaml.safe_load(f)
    topic_name = cfg.get('topic_name', '/spgc/receiver')

    text_arg = DeclareLaunchArgument('text', default_value='Hello, ROS2!')

    sender_node = Node(
        package='task02',
        executable='sender',
        name='sender',
        output='screen',
        parameters=[{'topic_name': topic_name, 'text': LaunchConfiguration('text')}]
    )

    return LaunchDescription([text_arg, sender_node])