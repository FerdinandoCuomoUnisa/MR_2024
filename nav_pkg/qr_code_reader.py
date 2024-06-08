import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
from pyzbar.pyzbar import decode
from std_msgs.msg import String

class QRCodeReader(Node):
    def __init__(self):
        super().__init__('qr_code_reader')
        self.subscription = self.create_subscription(
            Image,
            '/oakd/rgb/preview/image_raw', 
            self.listener_callback,
            10)
        self.publisher = self.create_publisher(String, 'road_sign', 10)
        self.bridge = CvBridge()

    def listener_callback(self, data): 
        try:
            cv_image = self.bridge.imgmsg_to_cv2(data, desired_encoding='bgr8')
        except CvBridgeError as e:
            self.get_logger().error(f"Could not convert image: {e}")
            return
        
        try:
            road_sign_detected = str(decode(cv_image)[0].data.decode("utf-8"))
            self.publisher.publish(road_sign_detected)
            road_sign = road_sign_detected

        except IndexError:
            road_sign= None
            
        print("DETECTION: ",road_sign)
        
 
def main(args=None):
    rclpy.init(args=args)
    qr_code_reader = QRCodeReader()
    rclpy.spin(qr_code_reader)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
