from uuid import UUID

from app.models.lot import LotModel


class AuctionRepository:
    def __init__(self, auction_dao):
        self.auction_dao = auction_dao

    async def find_all(self):
        return await self.auction_dao.find_all()

    async def find_one(self, auction_id: UUID):
        return await self.auction_dao.find_one(auction_id)

    async def create_one(self, auction_data: LotModel.POST):
        return await self.auction_dao.create_one(auction_data)
