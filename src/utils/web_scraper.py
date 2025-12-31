import logging 
from typing import List, Dict
import httpx
from bs4 import BeautifulSoup

logger = logging.getLogger(__name__)

async def fetch_webpage(url: str) -> str:
    """Fetches the content of a webpage and returns its text."""
    logger.info(f"Fetching webpage content from {url}")
    
    try:
        async with httpx.AsyncClient(timeout=30.0) as client:
            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
            }
            response = await client.get(url, headers=headers)
            response.raise_for_status()
        
        logger.info(f"Successfully fetched content from {url}")
        return response.text
    
    except Exception as e:
        logger.error(f"Error fetching {url}: {e}")
        raise 
    
def parse_html(html_content: str) -> str:
    soup = BeautifulSoup(html_content, 'lxml')
    
    for script in soup(["script", "style"]):
        script.decompose()
    
    text = soup.get_text()
    
    lines = (line.strip() for line in text.splitlines())
    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
    text = '\n'.join(chunk for chunk in chunks if chunk)
    
    return text

def chunk_text(text: str,  chunk_size: int = 1000, overlap: int = 200) -> List[str]:
    chunks = []
    start = 0
    text_length = len(text)
    
    while start < text_length:
        end = start + chunk_size
        chunk = text[start:end]
        chunks.append(chunk)
        start = end - overlap
    
    logger.info(f"Text chunked into {len(chunks)} pieces")
    
    return chunks

async def scrape_and_chunk(url: str) -> tuple[List[str], List[Dict]]: 
    html = await fetch_webpage(url=url)
    
    texts = parse_html(html_content=html)
    
    chunks = chunk_text(text=texts)
    
    metadata = [{"url": url, "chunk_index": i} for i in range(len(chunks))]
    
    return chunks, metadata

    