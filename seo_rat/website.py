# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/02_website.ipynb.

# %% auto 0
__all__ = ['Website', 'WebsiteStore']

# %% ../nbs/02_website.ipynb 1
from typing import Optional, List
from pymongo.database import Database
from pymongo.results import InsertOneResult, UpdateResult
from bson.objectid import ObjectId
from dataclasses import dataclass, asdict
from typing import Optional, Dict, Any
from datetime import datetime
import re
from urllib.parse import urlparse

# %% ../nbs/02_website.ipynb 2
@dataclass
class Website:
    """Class representing a website in our SEO analysis system"""

    url: str
    name: str
    description: Optional[str] = None
    language: str = "en"
    created_at: datetime = datetime.now()

    def __post_init__(self):
        """Validate data after initialization"""
        self.validate_url()
        self.validate_name()
        self.validate_language()

    def validate_url(self) -> None:
        """Validate URL format"""
        parsed = urlparse(self.url)
        if not all([parsed.scheme, parsed.netloc]):
            raise ValueError(f"Invalid URL format: {self.url}")

    def validate_name(self) -> None:
        """Validate website name"""
        if not self.name or len(self.name.strip()) < 2:
            raise ValueError("Name must be at least 2 characters long")

    def validate_language(self) -> None:
        """Validate language code"""
        if not re.match(r"^[a-z]{2}(-[A-Z]{2})?$", self.language):
            raise ValueError(f"Invalid language code: {self.language}")

    def to_dict(self) -> Dict[str, Any]:
        """Convert website data to dictionary for MongoDB storage"""
        return asdict(self)

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "Website":
        """Create Website instance from dictionary data"""
        return cls(**data)

# %% ../nbs/02_website.ipynb 3
class WebsiteStore:
    """Handle MongoDB operations for Website objects"""

    def __init__(self, db: Database):
        self.db = db
        self.collection = self.db.websites

    def insert_or_update_website(self, website: Website) -> str:
        """Insert website if not exists, or update if exists based on URL"""
        website_dict = website.to_dict()

        # Try to update existing website
        result = self.collection.update_one(
            {"url": website.url},  # Find by URL
            {"$set": website_dict},  # Update all fields
            upsert=True,  # Create if doesn't exist
        )

        if result.upserted_id:
            return str(result.upserted_id)
        else:
            # Get the _id of the existing document
            existing = self.collection.find_one({"url": website.url})
            return str(existing["_id"])

    def delete_website(self, website_id: str) -> bool:
        """Delete website by ID"""
        try:
            result = self.collection.delete_one({"_id": ObjectId(website_id)})
            return result.deleted_count > 0
        except Exception as e:
            print(f"Error deleting website: {e}")
            return False
