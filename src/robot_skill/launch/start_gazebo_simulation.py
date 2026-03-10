import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, ExecuteProcess, IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration, PathJoinSubstitution
from launch_ros.actions import Node


def generate_launch_description():
    # 1. 获取当前包 (robot_skill) 和 turtlebot3_gazebo 包的路径
    robot_skill_dir = get_package_share_directory('robot_skill')
    turtlebot3_gazebo_dir = get_package_share_directory('turtlebot3_gazebo')
    
    # 2. 定义要使用的模型 (burger, waffle, waffle_pi)
    # 这里默认使用 burger，你也可以通过命令行参数修改
    model_name = 'burger'
    os.environ['TURTLEBOT3_MODEL'] = model_name

    # 3. 定义要加载的世界文件路径 (使用 turtlebot3 自带的空世界或标准世界)
    # 你可以修改这里指向你自己写的 .world 文件
    world_file_name = 'turtlebot3_world.world' 
    world_path = os.path.join(turtlebot3_gazebo_dir, 'worlds', world_file_name)

    # 4. 定义 Gazebo 启动参数
    gazebo_server_args = [
        '-s',  # 启动 gzserver (物理引擎)
        world_path
    ]
    
    gazebo_client_args = [
        '-g'   # 启动 gzclient (图形界面)
    ]

    # 5. 定义生成实体的节点 (Spawn Entity)
    # 这个节点负责把小车模型“变”进 Gazebo 世界里
    spawn_entity_node = Node(
        package='gazebo_ros',
        executable='spawn_entity.py',
        name='spawn_turtlebot',
        arguments=[
            '-topic', 'robot_description', # 从哪个话题获取模型描述 (通常由 urdf 节点发布，但 turtlebot3 启动文件内部处理了)
            '-entity', 'turtlebot3_burger', # 在 Gazebo 里的名字
            '-x', '0.0', '-y', '0.0', '-z', '0.0', # 初始坐标
            '-R', '0.0', '-P', '0.0', '-Y', '0.0'  # 初始姿态
        ],
        output='screen'
    )
    
    # ⚠️ 重要提示：
    # 上面的 spawn_entity_node 是通用写法。
    # 但为了简单起见，我们直接复用 turtlebot3_gazebo 官方写好的启动逻辑，
    # 因为里面已经包含了加载 URDF、发布 robot_description 和 spawn 的所有复杂逻辑。
    # 下面的 IncludeLaunchDescription 是最稳健的做法。

    return LaunchDescription([
        # 方法 A: 直接包含官方的启动文件 (推荐，最稳定)
        # 这会启动 gzserver, gzclient, 并且自动把小车放进去
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(
                os.path.join(turtlebot3_gazebo_dir, 'launch', 'turtlebot3_world.launch.py')
            ),
            launch_arguments={
                'x_pos': '0.0',
                'y_pos': '0.0',
                'z_pos': '0.0'
            }.items()
        ),

        # 如果你想在这个 launch 文件里额外启动你自己的节点（比如一个控制脚本），可以在下面加：
        # Node(
        #     package='robot_skill',
        #     executable='your_control_script.py',
        #     name='my_controller',
        #     output='screen'
        # ),
    ])