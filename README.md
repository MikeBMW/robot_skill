# 🤖 Robot Skill

一个简单的 ROS 2 (Robot Operating System 2) 功能包示例，用于演示基础的机器人技能开发。

## 📋 项目简介

本项目包含一个基础的 ROS 2 Python 节点 `hello_skill`，旨在展示如何：
- 创建标准的 ROS 2 Python 包 (`ament_python`)
- 编写并发布/订阅话题或提供服务的节点
- 使用 `colcon` 构建系统编译工作空间
- 配置 `.gitignore` 以保持仓库整洁

此项目适合作为 ROS 2 初学者的入门模板或开发新技能的起点。

## 🛠️ 环境要求

- **操作系统**: Ubuntu 20.04 / 22.04 (或其他支持 ROS 2 的系统)
- **ROS 2 版本**: Humble Hawksbill (推荐) 或 Iron/Irwi
- **Python**: 3.8+
- **构建工具**: colcon-common-extensions

## 🚀 快速开始

### 1. 克隆仓库

首先，将本仓库克隆到您的 ROS 2 工作空间的 `src` 目录下：

```bash
cd ~/ros2_ws/src
git clone https://github.com/MikeBMW/robot_skill.git

cd ~/ros2_ws
rosdep install -i --from-path src --rosdistro humble -y

colcon build
source install/setup.bash

ros2 run robot_skill hello_skill

robot_skill/
├── README.md
├── .gitignore
├── package.xml
├── setup.py
└── robot_skill/
    ├── __init__.py
    └── hello_skill.py

Author: MikeBMW
Repository: https://github.com/MikeBMW/robot_skill

执行 Git 上传操作
紧接着，**复制下方这 4 行命令**，粘贴并回车，即可自动完成添加、提交和推送：

```bash
git add README.md
git add .
git commit -m "Add README documentation"
git push origin main


# Gazebo

这是一个基于 ROS 2 的功能包，主要用于演示机器人技能控制及 Gazebo 仿真集成。

## 📦 功能特性

- **Hello Skill 节点**: 基础技能演示节点。
- **Gazebo 仿真**: 包含启动 Gazebo 仿真的 Launch 文件。
- **模块化设计**: 易于扩展新的技能节点。

source ~/ros2_ws/install/setup.bash
echo "source ~/ros2_ws/install/setup.bash" >> ~/.bashrc
source ~/.bashrc
ros2 run robot_skill hello_skill
ros2 launch robot_skill start_gazebo_simulation.py

📂 项目结构
robot_skill/
├── README.md               # 本说明文件
├── package.xml             # 包依赖描述文件
├── setup.py                # Python 包构建配置
├── resource/               # Ament 资源索引
├── launch/                 # Launch 启动文件
│   └── start_gazebo_simulation.py
└── robot_skill/            # Python 源代码目录
    ├── __init__.py
    └── hello_skill.py      # 主节点代码