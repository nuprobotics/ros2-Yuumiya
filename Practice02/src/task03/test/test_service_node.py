import os
import pytest
import rclpy
from rclpy.node import Node
from std_srvs.srv import Trigger
from rclpy.task import Future


@pytest.fixture
def rclpy_init():
    rclpy.init()
    yield
    rclpy.shutdown()


@pytest.fixture
def create_test_trigger_service(rclpy_init):
    node = Node('test_trigger_server')

    def handle_request(req, res):
        res.success = True
        res.message = "Hello from /spgc/trigger"
        return res

    srv = node.create_service(Trigger, '/spgc/trigger', handle_request)
    yield node
    node.destroy_node()


def test_task3_service(rclpy_init, create_test_trigger_service):
    from task03.service_node import ServiceNode

    node = ServiceNode()
    rclpy.spin_once(create_test_trigger_service, timeout_sec=0.1)

    client = node.create_client(Trigger, node.service_name)
    while not client.wait_for_service(timeout_sec=1.0):
        pass

    req = Trigger.Request()
    future = client.call_async(req)
    rclpy.spin_until_future_complete(node, future)

    assert future.result() is not None
    assert future.result().success is True
    assert future.result().message == "Hello from /spgc/trigger"

    node.destroy_node()