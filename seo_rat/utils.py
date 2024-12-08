# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/01_utils.ipynb.

# %% auto 0
__all__ = ['exclude_front_matter', 'normalize_text', 'extract_frontmatter', 'extract_markdown_urls_with_tags',
           'extract_markdown_images', 'detect_numbers', 'calculate_similarity', 'get_file_paths', 'get_internal_urls',
           'get_file_name', 'get_external_urls', 'get_heads_info', 'main_keyword_in_start']

# %% ../nbs/01_utils.ipynb 3
import re
import yaml
from pathlib import Path
import glob
from typing import List, Dict, Any, Tuple
from difflib import SequenceMatcher
from urllib.parse import urlparse


# %% ../nbs/01_utils.ipynb 4
def exclude_front_matter(content: str) -> str:
    """Remove front matter from markdown content"""
    front_matter_end = content.find('---', 3)
    if front_matter_end != -1:
        return content[front_matter_end + 3:].strip()
    return content


# %% ../nbs/01_utils.ipynb 5
def normalize_text(text: str) -> str:
    """Normalize text by removing extra whitespace"""
    return re.sub(r'\s+', ' ', text).strip()


# %% ../nbs/01_utils.ipynb 6
def extract_frontmatter(md_content: str) -> Tuple[str, str, str, str, List[str]]:
    """Extract metadata from markdown frontmatter
    Returns: title, publishDate, excerpt, image, tags"""
    # Extract YAML front matter
    yaml_front_matter = md_content.split("---")[1]
    # Load YAML front matter
    front_matter_data = yaml.safe_load(yaml_front_matter)
    
    return (
        front_matter_data.get("title"),
        front_matter_data.get("publishDate"),
        front_matter_data.get("excerpt"),
        front_matter_data.get('image'),
        front_matter_data.get("tags", [])
    )


# %% ../nbs/01_utils.ipynb 7
def extract_markdown_urls_with_tags(md_content: str) -> Dict[str, Dict]:
    """Extract URLs and their metadata from markdown content"""
    markdown_urls = {}
    lines = md_content.split('\n')
    for line_number, line in enumerate(lines, start=1):
        urls = re.finditer(r'\[(.*?)\]\((.*?)\)', line)
        for match in urls:
            title = match.group(1)
            url = match.group(2)
            if url not in markdown_urls:
                markdown_urls[url] = {'titles': [], 'lines': []}
            markdown_urls[url]['titles'].append(title)
            markdown_urls[url]['lines'].append(line_number)
    return markdown_urls


# %% ../nbs/01_utils.ipynb 8
def extract_markdown_images(file_content: str) -> List[Dict[str, str]]:
    """Extract images and their alt text from markdown content"""
    image_pattern = r'\!\[(.*?)\]\((.*?)\)'
    matches = re.findall(image_pattern, file_content)
    return [{'alt_text': alt_text, 'url': url} for alt_text, url in matches]


# %% ../nbs/01_utils.ipynb 9
def detect_numbers(text: str) -> List[str]:
    """Extract phone numbers from text"""
    phone_regex = re.compile(r"(\+420)?\s*?(\d{3})\s*?(\d{3})\s*?(\d{3})")
    groups = phone_regex.findall(text)
    return ["".join(g) for g in groups]



# %% ../nbs/01_utils.ipynb 10
def calculate_similarity(text1: str, text2: str) -> float:
    """Calculate similarity ratio between two texts"""
    return SequenceMatcher(None, text1, text2).ratio()



# %% ../nbs/01_utils.ipynb 11
def get_file_paths(file_path):
    """
    get the file paths
    """

    return glob.glob(file_path)

# %% ../nbs/01_utils.ipynb 12
def get_internal_urls(urls, target_domain):
    """
    Get Internal URLs from URls
    by the target domain
    """
    related_urls = []
    for url in urls:
        parsed_url = urlparse(url)
        if (
            parsed_url.netloc == target_domain
            or parsed_url.netloc == target_domain.split(".")[0]
        ):
            related_urls.append(url)
    return related_urls

# %% ../nbs/01_utils.ipynb 13
def get_file_name(file_path):
    """get the file name"""
    return file_path.split("/")[-1][:-3]

# %% ../nbs/01_utils.ipynb 14
def get_external_urls(urls, target_domain):
    """
    Return the number of Internal Urls from markdown content by Target Domain
    """
    related_urls = []
    for url in urls:
        parsed_url = urlparse(url)
        if (
            not parsed_url.netloc == target_domain
            and not parsed_url.netloc == target_domain.split(".")[0]
            and not any(
                parsed_url.path.lower().endswith(ext)
                for ext in (".png", ".jpg", ".jpeg", ".gif", ".bmp", ".svg", ".webp")
            )
        ):
            related_urls.append(url)
    return related_urls

# %% ../nbs/01_utils.ipynb 15
def get_heads_info(file_path):
    """
    Get the Number of Headings for each type with the line number, content, and length
    """
    headings = []

    with open(file_path, "r") as file:
        for line_number, line in enumerate(file, start=1):
            line = line.strip()
            if line.startswith("# "):
                headings.append(
                    {
                        "type": "h1",
                        "line_number": line_number,
                        "content": line.strip("# ").strip(),
                        "length": len(line.strip("# ").strip()),
                    }
                )
            elif line.startswith("## "):
                headings.append(
                    {
                        "type": "h2",
                        "line_number": line_number,
                        "content": line.strip("## ").strip(),
                        "length": len(line.strip("## ").strip()),
                    }
                )
            elif line.startswith("### "):
                headings.append(
                    {
                        "type": "h3",
                        "line_number": line_number,
                        "content": line.strip("### ").strip(),
                        "length": len(line.strip("### ").strip()),
                    }
                )
            elif line.startswith("#### "):
                headings.append(
                    {
                        "type": "h4",
                        "line_number": line_number,
                        "content": line.strip("#### ").strip(),
                        "length": len(line.strip("#### ").strip()),
                    }
                )
            elif line.startswith("##### "):
                headings.append(
                    {
                        "type": "h5",
                        "line_number": line_number,
                        "content": line.strip("##### ").strip(),
                        "length": len(line.strip("##### ").strip()),
                    }
                )
            elif line.startswith("###### "):
                headings.append(
                    {
                        "type": "h6",
                        "line_number": line_number,
                        "content": line.strip("###### ").strip(),
                        "length": len(line.strip("###### ").strip()),
                    }
                )

    return headings

# %% ../nbs/01_utils.ipynb 17
def main_keyword_in_start(file_content, keyword, percent=10):
    """
    Find if the Keyword in File Content
    Default Percent is 10% of File Content
    """
    if keyword in file_content[: int(len(file_content) * percent / 100)]:
        return True
    else:
        return False