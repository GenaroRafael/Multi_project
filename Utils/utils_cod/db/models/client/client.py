from pydantic import BaseModel

from utils_cod.extensions.client.enums.client_type import ClientType


class Client(BaseMongoModel):
    #ID
    client_type: ClientType = ClientType.STANDART.value
    name: str
    locality: str
    plan_type: objectId
