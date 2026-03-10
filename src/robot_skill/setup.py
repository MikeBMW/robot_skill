from setuptools import find_packages, setup
import os

package_name = 'robot_skill'

# --- 修改开始：使用 os 模块手动查找 launch 文件 ---
launch_dir = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'launch')
launch_files = []

if os.path.isdir(launch_dir):
    # 遍历 launch 目录，只选取 .py 结尾的文件
    launch_files = [
        os.path.join('launch', f) 
        for f in os.listdir(launch_dir) 
        if f.endswith('.py')
    ]
    # print(f"[INFO] Found launch files: {launch_files}")
else:
    # print(f"[WARNING] Launch directory not found at: {launch_dir}")
    pass
# --- 修改结束 ---

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        # 添加这一行，告诉编译器把 launch 文件夹里的东西安装到 share/robot_skill/launch 目录下    
        ('share/' + package_name + '/launch', launch_files),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='xspace',
    maintainer_email='xspace@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            'hello_skill = robot_skill.hello_skill:main',
        ],
    },
)
