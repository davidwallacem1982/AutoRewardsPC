---
description: Analyzes the SEO of the Alpha Trader PWA project and generates a comprehensive report.
---

# SEO Analysis Skill

When analyzing SEO techniques and resources in a web project, follow these steps:

## Analysis Checklist

### 1. Technical SEO Foundation

- Does the site have proper semantic HTML5 structure?
- Are meta tags present and optimized (title, description, viewport, canonical)?
- Is there a single H1 per page with proper heading hierarchy?
- Are URLs clean, descriptive, and SEO-friendly?
- Does robots.txt exist and is it properly configured?
- Is sitemap.xml present and accessible?
- Is structured data (Schema markup) implemented?

### 2. Performance & Core Web Vitals

- Are images optimized with proper formats and compression?
- Do images have descriptive alt attributes?
- Are CSS and JavaScript minified and properly loaded?
- Is the site mobile-responsive and mobile-first?
- Are Core Web Vitals (LCP, FID, CLS) optimized?
- Is browser caching properly configured?

### 3. Content Quality

- Is content unique, valuable, and relevant?
- Are keywords naturally integrated in strategic locations?
- Is internal linking structure logical and optimized?
- Is content fresh and up-to-date?
- Are there content gaps or thin pages?

### 4. Accessibility & User Experience

- Does the site meet WCAG standards?
- Are ARIA labels properly used?
- Is keyboard navigation fully functional?
- Are color contrasts adequate?
- Are font sizes readable?

### 5. Security & Protocol

- Is HTTPS properly implemented?
- Are there any mixed content warnings?
- Are security headers configured (CSP, X-Frame-Options)?

### 6. Discoverability

- Are Open Graph and Twitter Card meta tags present?
- Are social sharing features implemented?
- Is local SEO data (NAP) consistent if applicable?

## How to Conduct the Analysis

### Step 1: Examine the HTML structure

- Inspect page source code
- Check meta tags in the `<head>` section
- Verify semantic HTML usage
- Map heading hierarchy

### Step 2: Test technical elements

- Validate HTML with W3C Validator
- Check robots.txt at `/robots.txt`
- Verify sitemap.xml at `/sitemap.xml`
- Test structured data with Google's Rich Results Test
- Run Lighthouse audit for performance metrics

### Step 3: Evaluate content and keywords

- Review content quality and depth
- Check keyword placement and density
- Analyze internal linking patterns
- Identify duplicate or thin content

### Step 4: Assess mobile and performance

- Test mobile responsiveness
- Check page load speed
- Analyze Core Web Vitals
- Review image optimization

## How to Provide Feedback

### Be specific about findings

- State exactly what element or page has the issue
- Reference line numbers or file paths when possible
- Use concrete examples from the actual code

### Explain the SEO impact

- Describe why this matters for search rankings
- Clarify how users are affected
- Quantify the potential impact when possible (e.g., "reduces CTR by up to 30%")

### Provide actionable recommendations

- Give exact code snippets to implement
- Suggest specific tools or techniques
- Prioritize fixes by severity (Critical, High, Medium, Low)

### Use clear formatting

- Use visual indicators: ✅ (good), ❌ (issue), ⚠️ (warning), 💡 (tip)
- Include code blocks for technical solutions
- Structure feedback consistently

## Report Structure

Your analysis report must include:

### Executive Summary

- Overall SEO health score or grade
- Top 3-5 critical issues
- Main opportunities for improvement

### What's Working Well

- List implemented best practices
- Acknowledge strong points
- Highlight competitive advantages

### Critical Issues (fix immediately)

For each issue:

- Clear description of the problem
- Location (URL, file, or element)
- SEO impact explanation
- Specific recommendation with code example
- Priority level

### High Priority Issues (significant impact)

- _Same structure as critical issues_

### Medium Priority Issues (moderate improvement)

- _Same structure as critical issues_

### Low Priority Issues (optimization opportunities)

- _Same structure as critical issues_

### Technical Recommendations

- Code changes needed
- Configuration updates
- Tools or plugins to implement

### Content Strategy

- Content gaps to fill
- Keyword opportunities
- Internal linking improves

### Performance Optimizations

- Speed improvements needed
- Resource optimization tactics
- Caching strategies

### Implementation Roadmap

- Prioritized action items
- Quick wins vs long-term projects
- Estimated effort per task

### Monitoring Setup

- Recommended SEO tools
- Google Search Console setup steps
- Key performance indicators to track

## Output Format Requirements

- Use markdown formatting throughout
- Include visual indicators for quick scanning (✅ ❌ ⚠️ 💡 🔧 📍)
- Provide code blocks with proper syntax highlighting
- Structure with clear headers and hierarchy
- Keep recommendations specific and actionable, not generic
- Focus on what matters most for the specific project analyzed
