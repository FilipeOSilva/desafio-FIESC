import rclpy
from rclpy.node import Node

from std_msgs.msg import String
import psutil

GIGA=1073741824

class MemoryPublisher(Node):

    def __init__(self):
        super().__init__('publish_memory')
        self.publisher_ = self.create_publisher(String, 'memory_info', 10)
        timer_period = 1  # seconds
        self.timer = self.create_timer(timer_period, self.publish_memory_info)

    def publish_memory_info(self):
        msg = String()
        memory = psutil.virtual_memory()
        msg.data = f'Memoria total: {memory.total / (GIGA):.2f} GB, Usada: {memory.used / (GIGA):.2f} GB, percentual do uso: {memory.percent}%'
        self.publisher_.publish(msg)
        self.get_logger().info('Publishing: "%s"' % msg.data)


def main(args=None):
    rclpy.init(args=args)

    memory_publisher = MemoryPublisher()

    rclpy.spin(memory_publisher)

    memory_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()