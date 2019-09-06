import launch
import launch_ros.actions

from ament_index_python.packages import get_package_share_directory

def generate_launch_description():
    camera_driver_node = launch_ros.actions.Node(
        package='camera_driver', 
        node_executable='camera_driver_node', 
        output='screen',
        parameters=[get_package_share_directory('camera_driver')+'/config/default.yaml'])
    return launch.LaunchDescription([camera_driver_node])