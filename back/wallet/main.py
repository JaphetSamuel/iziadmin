from fastapi import  APIRouter
from wallet.models import Wallet
from wallet.schemas import WalletPd
from pony.orm import db_session

router = APIRouter(prefix="/wallet", tags=["wallet"])


@router.get("wallet/:user_id",response_model=WalletPd)
async def getWalletByUserId(user_id:int):
    wallet = Wallet.get(user_id=user_id)


@router.get("getAllWallet/")
async def getAllWallet():
    wallets = Wallet.select()
    print(wallets)
    results = [WalletPd.from_orm(wallet) for wallet in wallets]
    return results

