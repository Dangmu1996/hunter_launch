import os
import launch
import launch_ros

from ament_index_python.packages import get_package_share_path

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, ExecuteProcess
from launch.substitutions import LaunchConfiguration, Command
from launch_ros.actions import Node
from launch.conditions import IfCondition, UnlessCondition
from launch_ros.parameter_descriptions import ParameterValue


def generate_launch_description():
    # urdf_tutorial_path = get_package_share_path('hunter_description')
    # default_model_path = urdf_tutorial_path / 'urdf/hunter2_base_gazebo.xacro'
    use_sim_time_arg = DeclareLaunchArgument('use_sim_time', default_value='false',
                                             description='Use simulation clock if true')

    port_name_arg = DeclareLaunchArgument('port_name', default_value='can0',
                                         description='CAN bus name, e.g. can0')
    odom_frame_arg = DeclareLaunchArgument('odom_frame', default_value='odom',
                                           description='Odometry frame id')
    base_link_frame_arg = DeclareLaunchArgument('base_frame', default_value='base_link',
                                                description='Base link frame id')
    odom_topic_arg = DeclareLaunchArgument('odom_topic_name', default_value='odom',
                                           description='Odometry topic name')

    simulated_robot_arg = DeclareLaunchArgument('simulated_robot', default_value='false',
                                                   description='Whether running with simulator')
    sim_control_rate_arg = DeclareLaunchArgument('control_rate', default_value='50',
                                                 description='Simulation control loop update rate')
    # robot_description = ParameterValue(Command(['xacro ', LaunchConfiguration('model')]),
    #                                    value_type=str)
    
    # model_arg = DeclareLaunchArgument(name='model', default_value=str(default_model_path),
    #                                   description='Absolute path to robot urdf file')
    # gui_arg = DeclareLaunchArgument(name='gui', default_value='false', choices=['true', 'false'],
    #                                 description='Flag to enable joint_state_publisher_gui')
        
    # robot_state_publisher_node = Node(
    #     package='robot_state_publisher',
    #     executable='robot_state_publisher',
    #     parameters=[{'robot_description': robot_description}]
    # )
    # joint_state_publisher_node = Node(
    #     package='joint_state_publisher',
    #     executable='joint_state_publisher',
    #     condition=UnlessCondition(LaunchConfiguration('gui'))
    # )
    # joint_state_publisher_gui_node = Node(
    #     package='joint_state_publisher_gui',
    #     executable='joint_state_publisher_gui',
    #     condition=IfCondition(LaunchConfiguration('gui'))
    # )

    hunter_base_node = launch_ros.actions.Node(
        package='hunter_base',
        executable='hunter_base_node',
        output='screen',
        emulate_tty=True,
        parameters=[{
                'use_sim_time': launch.substitutions.LaunchConfiguration('use_sim_time'),
                'port_name': launch.substitutions.LaunchConfiguration('port_name'),                
                'odom_frame': launch.substitutions.LaunchConfiguration('odom_frame'),
                'base_frame': launch.substitutions.LaunchConfiguration('base_frame'),
                'odom_topic_name': launch.substitutions.LaunchConfiguration('odom_topic_name'),
                'simulated_robot': launch.substitutions.LaunchConfiguration('simulated_robot'),
                'control_rate': launch.substitutions.LaunchConfiguration('control_rate'),
        }])

    return LaunchDescription([
        use_sim_time_arg,
        port_name_arg,        
        odom_frame_arg,
        # model_arg,
        # gui_arg,
        base_link_frame_arg,
        odom_topic_arg,
        simulated_robot_arg,
        sim_control_rate_arg,
        hunter_base_node,
        # robot_state_publisher_node,
        # joint_state_publisher_node,
        # joint_state_publisher_gui_node
        
    ])
