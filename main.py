import uuid
import os
if(os.environ['USER_NAME']=='Karanjit'):
  print('file is successfully encrypted')
else:
  print('file is uncessfully encrypted')
x = uuid.uuid1()
print(uuid.uuid5(x,"name"))
