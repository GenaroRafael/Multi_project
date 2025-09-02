from utils_cod.extensions.plan.enums.plan_type import PlanType
from utils_cod.extensions.plan.enums.price import Price
from utils_cod.extensions.plan.enums.velocity import Velocity

class Plan(BaseMongoModel):
    #ID
    plan_type: PlanType = PlanType.BASIC.value
    price: Price = Price.PLAN_BASIC_PRICE.value
    velocity: Velocity = Velocity.PLAN_BASIC_VELOCITY.value
