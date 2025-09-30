import sys
from traceback import format_exc

from motor.motor_asyncio import AsyncIOMotorClient

from functions.config import Var
from libs.logger import LOGS


class DataBase:
    def __init__(self):
        try:
            LOGS.info("Trying To Connect With MongoDB")
            self.client = AsyncIOMotorClient(Var.MONGO_SRV)
            self.file_info_db = self.client["ONGOINGANIME"]["fileInfo"]
            self.channel_info_db = self.client["ONGOINGANIME"]["animeChannelInfo"]
            self.opts_db = self.client["ONGOINGANIME"]["opts"]
            self.file_store_db = self.client["ONGOINGANIME"]["fileStore"]
            self.broadcast_db = self.client["ONGOINGANIME"]["broadcastInfo"]
            LOGS.info("Successfully Connected With MongoDB")
        except Exception as error:
            LOGS.exception(format_exc())
            LOGS.critical(str(error))
            sys.exit(1)

    async def add_anime(self, uid):
        data = await self.file_info_db.find_one({"_id": uid})
        if not data:
            await self.file_info_db.insert_one({"_id": uid})

    async def toggle_separate_channel_upload(self):
        data = await self.opts_db.find_one({"_id": "SEPARATE_CHANNEL_UPLOAD"})
        _data = not (data or {}).get("switch", False)
        await self.opts_db.update_one(
            {"_id": "SEPARATE_CHANNEL_UPLOAD"}, {"$set": {"switch": _data}}, upsert=True
        )

    async def is_separate_channel_upload(self):
        data = await self.opts_db.find_one({"_id": "SEPARATE_CHANNEL_UPLOAD"})
        return (data or {}).get("switch", False)

    async def toggle_original_upload(self):
        data = await self.opts_db.find_one({"_id": "OG_UPLOAD"})
        _data = not (data or {}).get("switch", False)
        await self.opts_db.update_one(
            {"_id": "OG_UPLOAD"}, {"$set": {"switch": _data}}, upsert=True
        )

    async def is_original_upload(self):
        data = await self.opts_db.find_one({"_id": "OG_UPLOAD"})
        return (data or {}).get("switch", False)

    async def toggle_button_upload(self):
        data = await self.opts_db.find_one({"_id": "BUTTON_UPLOAD"})
        _data = not (data or {}).get("switch", False)
        await self.opts_db.update_one(
            {"_id": "BUTTON_UPLOAD"}, {"$set": {"switch": _data}}, upsert=True
        )

    async def is_button_upload(self):
        data = await self.opts_db.find_one({"_id": "BUTTON_UPLOAD"})
        return (data or {}).get("switch", False)

    async def is_anime_uploaded(self, uid):
        data = await self.file_info_db.find_one({"_id": uid})
        if data:
            return True
        return False

    async def add_anime_channel_info(self, title, _data):
        await self.channel_info_db.update_one(
            {"_id": title}, {"$set": {"data": _data}}, upsert=True
        )

    async def get_anime_channel_info(self, title):
        data = await self.channel_info_db.find_one({"_id": title})
        if (data or {}).get(title):
            return data["data"]
        return {}

    async def store_items(self, _hash, _list):
        # in case
        await self.file_store_db.update_one(
            {"_id": _hash}, {"$set": {"data": _list}}, upsert=True
        )

    async def get_store_items(self, _hash):
        data = await self.file_store_db.find_one({"_id": _hash})
        if (data or {}).get("data"):
            return data["data"]
        return []

    async def add_broadcast_user(self, user_id):
        data = await self.broadcast_db.find_one({"_id": user_id})
        if not data:
            await self.broadcast_db.insert_one({"_id": user_id})

    async def get_broadcast_user(self):
        data = self.broadcast_db.find()
        return [i["_id"] for i in (await data.to_list(length=None))]

    async def toggle_ss_upload(self):
        data = await self.opts_db.find_one({"_id": "SS_UPLOAD"})
        _new = not (data or {}).get("switch", True)
        await self.opts_db.update_one(
            {"_id": "SS_UPLOAD"},
            {"$set": {"switch": _new}},
            upsert=True,
        )

    async def is_ss_upload(self):
        data = await self.opts_db.find_one({"_id": "SS_UPLOAD"})
        return (data or {}).get("switch", True)
