import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class HelloSkill(Node):
    def __init__(self):
        super().__init__('hello_skill')
        self.publisher_ = self.create_publisher(String, 'skill_output', 10)
        timer_period = 1.0  # 每秒发布一次
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0

    def timer_callback(self):
        msg = String()
        msg.data = f'🤖 Skill {self.i}: Hello from robot_skill!'
        self.publisher_.publish(msg)
        self.get_logger().info(f'Publishing: "{msg.data}"')
        self.i += 1

def main(args=None):
    rclpy.init(args=args)
    hello_skill = HelloSkill()
    rclpy.spin(hello_skill)
    hello_skill.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()