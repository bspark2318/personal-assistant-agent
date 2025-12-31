import logging 
from src.agent.state import AgentState
from src.services.llm import get_llm_service
from src.services.rag import get_rag_service
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage

logger = logging.getLogger(__name__)

async def router_node(state: AgentState) -> AgentState:
    logger.info("Router Node - user: {state.user_id}")
    
    rag_service = get_rag_service()
    
    user_query = state.messages[-1].content
    
    retrieved_docs = rag_service.search_document(
        query=user_query,
        user_id=state.user_id,
        k=1
    )
    
    if retrieved_docs:
        logger.info("RAG documents found, routing to RAG node.")
        state.next_action = "rag"
    else :
        logger.info("No RAG documents found, routing to Chat node.")
        state.next_action = "chat"
        
    return state 

async def chat_node(state: AgentState) -> AgentState:
    logger.info("Chat Node - user: {state.user_id}")
    
    llm_service = get_llm_service()
    
    response = await llm_service.get_llm().ainvoke(state.messages) 
    
    state.messages.append(AIMessage(content=response.content))
    logger.info(f"AI Response: {response.content}")
    
    return state

async def rag_node(state: AgentState) -> AgentState: 
    logger.info("RAG Node - user: {state.user_id}")
    
    rag_service = get_rag_service()
    
    user_query = state.messages[-1].content
    
    retrieved_docs = rag_service.search_document(
        query=user_query,
        user_id=state.user_id,
        k=3
    )
    
    if not retrieved_docs:
        logger.info("No documents found for RAG.")
        state.context["rag_used"] = False
        state.next_action = "chat"
        return await chat_node(state)
    
    context_text = "\n\n".join(
        f"Document {i+1}:\n{doc['content']}" for i, doc in enumerate(retrieved_docs)
    )
    
    context_message = SystemMessage(
        content=f"Use the following information to answer the user's query:\n\n{context_text}"
    )
    
    messages_with_context = state.messages[:-1] + [context_message, state.messages[-1]]
    
    llm_service = get_llm_service()
    response = await llm_service.get_llm().ainvoke(messages_with_context)
    
    state.messages.append(AIMessage(content=response.content))
    state.context["rag_used"] = True
    state.context["sources"] = [doc["metadata"].get("url", "N/A") for doc in retrieved_docs]
    
    logger.info(f"AI Response with RAG: {response.content}")
    
    return state

