---
name: SEO Analysis
description: Analyzes the SEO of the AutoRewardsPC project and generates a comprehensive report following a specific template.
---

# SEO Analysis Instructions

You are an expert SEO analyst. Your goal is to analyze the codebase (Python, HTML, templates, etc.) and generate a report following the exact template below.
Fill in all placeholders with real data from the project.

---

# SEO Analysis Report - AutoRewardsPC

**Analysis Date:** 12/02/2026
**Project Type:** Python Desktop Application

---

## Executive Summary

[2-3 paragraphs covering:]

- Overall SEO maturity level
- Key strengths found
- Critical gaps identified

---

## 1. Meta Tags Analysis

### ✅ Implemented Features

- [Feature 1] - Found in `file.py:line_number`
- [Feature 2] - Found in `file.py:line_number`

### ❌ Missing Features

- [Missing feature 1] - **Impact: High/Medium/Low**
- [Missing feature 2] - **Impact: High/Medium/Low**

### 💡 Recommendations

[Specific actionable improvements with code examples]

```python
# Example: Adding meta description
meta_description = '<meta name="description" content="Your page description">'
```

---

## 2. Content Structure

### ✅ Implemented Features

[List with file references]

### ❌ Missing Features

[List with impact assessment]

### 💡 Recommendations

[Improvements with code examples]

---

## 3. Technical SEO

### ✅ Implemented Features

[List with file references]

### ❌ Missing Features

[List with impact assessment]

### 💡 Recommendations

[Improvements with code examples]

---

## 4. Performance Optimization

### ✅ Implemented Features

[List with file references]

### ❌ Missing Features

[List with impact assessment]

### 💡 Recommendations

[Improvements with code examples]

---

## 5. SEO Tools & Integration

### ✅ Implemented Features

[List with file references]

### ❌ Missing Features

[List with impact assessment]

### 💡 Recommendations

[Improvements with code examples]

---

## Priority Action Items

### 🔴 High Priority (Immediate Action Required)

1. [Critical issue with explanation]
2. [Critical issue with explanation]

### 🟡 Medium Priority (Address Soon)

1. [Important issue with explanation]
2. [Important issue with explanation]

### 🟢 Low Priority (Future Enhancement)

1. [Enhancement with explanation]
2. [Enhancement with explanation]

---

## Implementation Examples

### Adding Meta Tags

```python
def generate_meta_tags(title, description, url, image=None):
    meta_tags = f'''
    <title>{title}</title>
    <meta name="description" content="{description}">
    <meta property="og:title" content="{title}">
    <meta property="og:description" content="{description}">
    <meta property="og:url" content="{url}">
    '''
    if image:
        meta_tags += f'<meta property="og:image" content="{image}">\n'
    return meta_tags
```

### Generating XML Sitemap

```python
from xml.etree.ElementTree import Element, SubElement, tostring
from datetime import datetime

def generate_sitemap(urls):
    urlset = Element('urlset', xmlns="http://www.sitemaps.org/schemas/sitemap/0.9")

    for url_data in urls:
        url = SubElement(urlset, 'url')
        loc = SubElement(url, 'loc')
        loc.text = url_data['url']
        lastmod = SubElement(url, 'lastmod')
        lastmod.text = datetime.now().strftime('%Y-%m-%d')
        priority = SubElement(url, 'priority')
        priority.text = str(url_data.get('priority', 0.5))

    return tostring(urlset, encoding='utf-8', method='xml')
```

[Add more relevant examples based on findings]

---

## SEO Score Summary

| Category          | Score    | Status       |
| ----------------- | -------- | ------------ |
| Meta Tags         | X/10     | ⭐⭐⭐       |
| Content Structure | X/10     | ⭐⭐         |
| Technical SEO     | X/10     | ⭐⭐⭐⭐     |
| Performance       | X/10     | ⭐⭐         |
| Tools Integration | X/10     | ⭐           |
| **Overall**       | **X/10** | **[Status]** |

**Status Legend:**

- ⭐⭐⭐⭐⭐ (9-10): Excellent
- ⭐⭐⭐⭐ (7-8): Good
- ⭐⭐⭐ (5-6): Fair
- ⭐⭐ (3-4): Poor
- ⭐ (0-2): Critical

---

## Additional Resources

**SEO Best Practices:**

- [Google SEO Starter Guide](https://developers.google.com/search/docs/beginner/seo-starter-guide)
- [Schema.org Documentation](https://schema.org/)
- [Open Graph Protocol](https://ogp.me/)

**Python SEO Libraries:**

- BeautifulSoup4: https://www.crummy.com/software/BeautifulSoup/
- Python Sitemap Generator: https://github.com/c4software/python-sitemap
- Django SEO Framework: https://github.com/jazzband/django-meta

**Validation Tools:**

- Google Rich Results Test: https://search.google.com/test/rich-results
- Facebook Sharing Debugger: https://developers.facebook.com/tools/debug/
- Twitter Card Validator: https://cards-dev.twitter.com/validator

---

## Conclusion

[Final summary covering:]

- Overall assessment
- Most critical improvements needed
- Expected impact of implementing recommendations
- Next steps for the user
