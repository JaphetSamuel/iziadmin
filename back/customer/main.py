from config.db  import db
from customer.models import Customers
from fastapi import APIRouter
from customer.schemas import CustomersPd
from pony.orm import db_session

router = APIRouter(prefix="/customers", tags=["customers"])



@router.get("/db_test")
async def test():
    with db_session:
        customers = Customers.select()
        result = [CustomersPd.from_orm(customer) for customer in customers]
    return  result

@router.get("/{id}")
async  def get_customer_by_id(id:int):
    with db_session:
        customer = Customers[id]
    return CustomersPd.from_orm(customer)

