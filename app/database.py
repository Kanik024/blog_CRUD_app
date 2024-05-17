class Database:
    client: motor.motor_asyncio.AsyncIOMotorClient = None
    database: motor.motor_asyncio.AsyncIOMotorDatabase = None

db = Database()