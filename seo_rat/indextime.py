# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/07_indextime.ipynb.

# %% auto 0
__all__ = ['db', 'auth', 'router', 'app', 'get_file_names', 'create_arabic_slug_converter', 'pair_urls', 'URLInspectionRequest',
           'IndexStatusResult', 'URLInspectionResponse', 'IndexTimeDocument', 'IndexTimeStoreResponse', 'inspect_url',
           'IndexTimeQueryResponse', 'get_index_status']

# %% ../nbs/07_indextime.ipynb 1
import os
from fastapi import APIRouter, HTTPException, status, Path, Query, Depends
from typing import Optional, Dict, Any,List
from google.oauth2.credentials import Credentials
from fastapi.requests import Request as FastAPIRequest
from fastapi.responses import RedirectResponse,JSONResponse
from pydantic import BaseModel,Field
from googleapiclient.discovery import build
from fastapi import  Depends,APIRouter,FastAPI
from .fast_gsc import  require_auth
from datetime import datetime
from pydantic import BaseModel
from typing import Optional, Dict, Any
from .store_gsc import serialize_mongodb_doc
from .gsc_db import SearchConsoleDB

db = SearchConsoleDB()

# %% ../nbs/07_indextime.ipynb 2
def get_file_names(
    full_path: str = "/home/kareem/Desktop/web_dev_js/astro_hacking/emdad_gaz/emdadgaz/src/content/post",
):
    file_names = []
    for file in os.listdir(full_path):
        if file != ".obsidian":
            file_names.append(file.split(".md")[0])
    return file_names


# %% ../nbs/07_indextime.ipynb 4
from .fast_gsc import  GSCAuth
auth = GSCAuth()
router = APIRouter(prefix="/index",tags=["indexing"])

# %% ../nbs/07_indextime.ipynb 5
def create_arabic_slug_converter():
    def to_slug(arabic_text: str) -> str:
        """Convert Arabic text to URL slug."""
        # Remove extra spaces and convert to lowercase
        text = arabic_text.strip().lower()

        # Map Arabic characters to English equivalents
        char_map = {
            "ا": "a",
            "ب": "b",
            "ت": "t",
            "ث": "th",
            "ج": "j",
            "ح": "h",
            "خ": "kh",
            "د": "d",
            "ذ": "th",
            "ر": "r",
            "ز": "z",
            "س": "s",
            "ش": "sh",
            "ص": "s",
            "ض": "d",
            "ط": "t",
            "ظ": "z",
            "ع": "",
            "غ": "gh",
            "ف": "f",
            "ق": "q",
            "ك": "k",
            "ل": "l",
            "م": "m",
            "ن": "n",
            "ه": "h",
            "و": "w",
            "ي": "y",
            "ة": "h",
            "ء": "",
            "ؤ": "",
            "ئ": "",
            "أ": "a",
            "إ": "a",
            "آ": "a",
            "ى": "a",
            " ": "-",
        }

        # Convert each character
        slug = "".join(char_map.get(c, c) for c in text)

        # Remove any double dashes and clean up
        while "--" in slug:
            slug = slug.replace("--", "-")

        return slug.strip("-")

    return to_slug

# %% ../nbs/07_indextime.ipynb 6
def pair_urls(file_names):
    convert = create_arabic_slug_converter()
    sluged_urls = {}
    for arabic_name in file_names:
        slug = convert(arabic_name)
        sluged_urls[arabic_name] = slug
    return sluged_urls 

# %% ../nbs/07_indextime.ipynb 8
class URLInspectionRequest(BaseModel):
    inspection_url: str
    site_url: str
    language_code: str = "en-US"


class IndexStatusResult(BaseModel):
    verdict: str
    coverage_state: Optional[str]
    last_crawl_time: Optional[str]
    page_fetch_state: Optional[str]
    indexing_state: Optional[str]
    robots_txt_state: Optional[str]


class URLInspectionResponse(BaseModel):
    inspection_url: str
    status: str
    index_status: IndexStatusResult


# %% ../nbs/07_indextime.ipynb 9
app= FastAPI()

# %% ../nbs/07_indextime.ipynb 10
class IndexTimeDocument(BaseModel):
    """MongoDB document structure for index time data

    Attributes:
        site_url: Website URL
        page_url: Specific page URL
        verdict: Indexing verdict
        coverage_state: Coverage state
        last_crawl_time: Last time page was crawled
        indexing_state: Current indexing state
        robots_txt_state: Robots.txt status
        timestamp: Time of storage
    """

    site_url: str
    page_url: str
    verdict: str
    coverage_state: Optional[str]
    last_crawl_time: Optional[str]
    indexing_state: Optional[str]
    robots_txt_state: Optional[str]
    timestamp: datetime = Field(default_factory=datetime.now)


class IndexTimeStoreResponse(BaseModel):
    """Response model for index time storage

    Attributes:
        message: Status message
        site_url: Website URL
        page_url: Page URL
        stored_at: Time of storage
    """

    message: str
    site_url: str
    page_url: str
    stored_at: datetime


# %% ../nbs/07_indextime.ipynb 11
@router.post(
    "/inspect-url/{site_url}",
    response_model=IndexTimeStoreResponse,
    summary="Inspect and store URL indexing status",
    tags=["indexing"],
)
async def inspect_url(
    site_url: str = Path(
        ..., description="The site URL in Search Console (e.g., sc-domain:example.com)"
    ),
    page_url: str = Query(..., description="The specific page URL to inspect"),
    language_code: str = Query(
        default="en-US", description="Language code for the response"
    ),
    credentials: Credentials = Depends(require_auth),
) -> IndexTimeStoreResponse:
    """Inspect and store the indexing status of a URL"""
    try:
        search_console = build("searchconsole", "v1", credentials=credentials)

        inspection_request: Dict[str, Any] = {
            "inspectionUrl": page_url,
            "siteUrl": site_url,
            "languageCode": language_code,
        }

        response = (
            search_console.urlInspection()
            .index()
            .inspect(body=inspection_request)
            .execute()
        )

        result = response.get("inspectionResult", {}).get("indexStatusResult", {})
        if not result:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="No inspection results found for the URL",
            )

        # Create document for MongoDB
        document = IndexTimeDocument(
            site_url=site_url,
            page_url=page_url,
            verdict=result.get("verdict", "UNKNOWN"),
            coverage_state=result.get("coverageState"),
            last_crawl_time=result.get("lastCrawlTime"),
            indexing_state=result.get("indexingState"),
            robots_txt_state=result.get("robotsTxtState"),
        )

        # Store in MongoDB
        db.db.index_time.update_one(
            {"site_url": site_url, "page_url": page_url},
            {"$set": serialize_mongodb_doc(document.dict())},
            upsert=True,
        )

        return IndexTimeStoreResponse(
            message="Successfully stored index time data",
            site_url=site_url,
            page_url=page_url,
            stored_at=document.timestamp,
        )

    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Internal server error: {str(e)}",
        )


# %% ../nbs/07_indextime.ipynb 12
class IndexTimeQueryResponse(BaseModel):
    """Response model for index time queries"""
    site_url: str
    total_pages: int
    pages_data: List[IndexTimeDocument]
    query_timestamp: datetime = Field(default_factory=datetime.now)

@router.get(
    "/index-status/{site_url}",
    response_model=IndexTimeQueryResponse,
    summary="Get stored indexing status",
    description="Retrieve stored indexing status for all pages of a site",
    tags=["indexing"],
)
async def get_index_status(
    site_url: str = Path(..., description="The site URL to query (e.g., sc-domain:example.com)"),
    verdict: Optional[str] = Query(None, description="Filter by verdict (e.g., PASS, FAIL)"),
    limit: int = Query(default=100, le=1000, description="Maximum number of results to return"),
) -> IndexTimeQueryResponse:
    """Retrieve stored indexing status data for a site"""
    try:
        # Build query
        query = {"site_url": site_url}
        if verdict:
            query["verdict"] = verdict

        # Get data from MongoDB
        cursor = db.db.index_time.find(query).limit(limit)
        results = [IndexTimeDocument(**serialize_mongodb_doc(doc)) for doc in cursor]
        
        # Get total count
        total_pages = db.db.index_time.count_documents(query)

        return IndexTimeQueryResponse(
            site_url=site_url,
            total_pages=total_pages,
            pages_data=results
        )

    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Failed to retrieve index data: {str(e)}"
        )
