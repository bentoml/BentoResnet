import random
from locust import HttpUser
from locust import between
from locust import task

with open("cat1.jpg", "rb") as f:
    IMAGE_DATA = f.read()


class BentoHttpUser(HttpUser):
    """
        Start locust load testing client with:

            locust --class-picker -H http://localhost:3000

        Open browser at http://0.0.0.0:8089, adjust desired number of users and spawn
        rate for the load test from the Web UI and start swarming.
    """

    @task
    def classify(self):
        self.client.post("/classify", files={"images": IMAGE_DATA})

    wait_time = between(0.01, 2)
