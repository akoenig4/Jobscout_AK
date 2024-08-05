from delete_tables import delete_tables
from delete_queues import delete_aws_resources
import time

delete_aws_resources()
delete_tables()

#Sleep to allow for deletion of resources
print("\033[93mloading... 20 seconds remaining... \033[0m")
time.sleep(20)
