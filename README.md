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
git commit -m "Add README documentation"
git push origin main
