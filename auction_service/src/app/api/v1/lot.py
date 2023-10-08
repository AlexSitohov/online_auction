from uuid import UUID

from fastapi import APIRouter, Depends

from app.models.lot import LotModel
from app.repositories.auction_repository import AuctionRepository
from app.repositories.providers import provide_auction_repository_stub

lot_router = APIRouter(tags=["Auction"], prefix="/auction/api/v1")


@lot_router.post("/lots", response_model=LotModel.GET)
async def create_lot(
    auction_data: LotModel.POST,
    auction_repository: AuctionRepository = Depends(provide_auction_repository_stub),
):
    return await auction_repository.create_one(auction_data)


@lot_router.get("/lots", response_model=list[LotModel.GET])
async def get_lots(
    auction_repository: AuctionRepository = Depends(provide_auction_repository_stub),
):
    return await auction_repository.find_all()


@lot_router.get("/lots/{auction_id}", response_model=LotModel.GET)
async def get_lot(
    auction_id: UUID,
    auction_repository: AuctionRepository = Depends(provide_auction_repository_stub),
):
    return await auction_repository.find_one(auction_id)
