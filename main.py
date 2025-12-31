import asyncio 
import logging 
from src.config import Config 
from src.telegram_bot.bot import start_bot

logging.basicConfig(
    level=Config.LOG_LEVEL,
    format="%(asctime)s - %(levelname)s - %(name)s:%(lineno)d - %(message)s"
)
logger = logging.getLogger(__name__)

async def main(): 
    try:
        Config.validate()
        logger.info("Configuration validated successfully.")
        
        await start_bot()
        
    except Exception as e:
        logger.exception("Failed while executing main function: %s", e)
        raise
    
if __name__ == "__main__": 
    asyncio.run(main()) 

