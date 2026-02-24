- Using correct typed pyton code with pydantic, sqlmodel built-int typing
- Async from first approch

## Refactoir

03_seo_analysis : needs to be refactore and seprate of concernts into a more than this notebook

### 05_gsc_storage

1. the quries needs to be refactore, readable , functional

- are we using sqlmodel idomtic?
- For the Article should we just store their place and when we need them just to fetch and preprocess in the fly? or make a copy ?
- the notebook needs to be divided into multiple sperated of concernts notebook for easier remember of functions and mantain

### 08_content_mapper

- need to be better functional and modular and robust

## Test-Drive Approch

## SEO report fixes (todo)

- Notebook `.ipynb` content is counted as raw JSON (inflated word count, links, images)
- `seo_report.py` passes full metadata dict into `check_title_length` / `check_desc_length` instead of strings
- `parse_metadata` assumes frontmatter exists; files without it can error/skip
- `description` is accessed as `metadata["description"]` (KeyError when missing)

## Insights

1. Implement all the insights.canvas features and the must_ai_features also

## Quarto Specific

1. Gneral quarto specifc rules in the frontmatters  like include or exclude code cells especailly in readin .ipynb 
2.
