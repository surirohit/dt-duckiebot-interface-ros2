import rclpy

def main():
    rclpy.init()
    node = rclpy.create_node('camera_driver_node')
    print("Success")
    rclpy.spin(node)

if __name__ == '__main__':
    main()