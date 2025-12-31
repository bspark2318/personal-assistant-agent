import logging
from langgraph.checkpoint.sqlite.aio import AsyncSqliteSaver
from src.config import Config 

logger = logging.getLogger(__name__)

_saver_context = None 
_checkpointer = None

async def get_checkpointer() -> AsyncSqliteSaver:
    global _saver_context, _checkpointer
    
    if _checkpointer is not None:
        return _checkpointer

    checkpoint_path = Config.CHECKPOINTS_DIR / "checkpoints.db"
    
    logger.info(f"Using checkpoint database at: {checkpoint_path}")
    
    _saver_context = AsyncSqliteSaver.from_conn_string(str(checkpoint_path))
    
    _checkpointer = await _saver_context.__aenter__()
    
    logger.info("Checkpoint database initialized successfully.")
    
    return _checkpointer

async def close_checkpointer():
    global _saver_context, _checkpointer
    
    if _saver_context is not None and _checkpointer is not None:
        await _saver_context.__aexit__(None, None, None)
        _saver_context = None
        _checkpointer = None
        logger.info("Checkpoint database connection closed.")
