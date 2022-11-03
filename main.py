import uuid
import os
print(os.environ['USER_NAME'])
x = uuid.uuid1()
print(uuid.uuid5(x,"name"))
