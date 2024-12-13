from fastapi import FastAPI
import os
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from seo_rat.fast_gsc import app as search_api_app
from seo_rat.store_gsc import store_router  # Import the storage router
from seo_rat.indextime import router as index_router

os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

app = FastAPI(
    title="Search Console Analytics API",
    description="API for Google Search Console Analytics",
    version="1.0.0",
)
# add CORS middleware with specific origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost",
        "http://localhost:8000",
        "http://127.0.0.1",
        "http://127.0.0.1:8000",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routes from search_api_app
app.include_router(search_api_app.router)
app.include_router(store_router)
app.include_router(index_router)

# Add callback URL configuration
os.environ["OAUTH_CALLBACK_URL"] = "http://localhost:8000/callback"

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)