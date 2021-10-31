from .imports import *


#Schema used to send messages in the response models
#================================#
class StatusModel(BaseModel):
    status: Optional[str]
    message: Optional[str]
#================================#