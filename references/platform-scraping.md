# Platform-Specific Scraping Guide

This guide provides platform-specific tips for scraping contact information using Apify and other tools.

## Instagram Scraping

### Recommended Apify Actors

1. **Instagram Profile Scraper** (Most reliable)
   - Actor ID: `apify/instagram-profile-scraper`
   - Input: `{"usernames": ["handle1", "handle2"]}`
   - Output: bio, email, followers, category, external links

2. **Instagram Search Scraper**
   - Actor ID: `apify/instagram-search-scraper`
   - Input: `{"keywords": ["creator", "influencer"], "hashtags": ["#mumbai"]}`
   - Output: list of profiles matching criteria

### Scraping Tips

#### Bio Email Extraction
The scraper extracts emails from bios using regex patterns:
- Standard format: `email@example.com`
- Obfuscated format: `email [at] example [dot] com` → `email@example.com`
- Pattern: `r"@?([a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,})"`

#### Handle Extraction
Extracts @handles from bios:
- Pattern: `r"@([a-zA-Z0-9_.]{1,30})"`
- Excludes: creator's own handle, email domains, common TLDs
- Format: comma-separated list

### Rate Limiting
- **Delay**: 10-30 seconds between requests
- **Daily Limit**: ~100-200 profiles (varies by account)
- **Error Handling**: If blocked, wait 15 minutes and retry

### Alternative Methods

If Apify is unavailable:
1. **Manual CSV**: Export from Apify.com and save to `data/apify_YYYY-MM-DD.csv`
2. **Browser Extension**: Use Instagram scraping extensions
3. **Python Script**: Use `instaloader` library (requires login)

## LinkedIn Scraping

### Recommended Apify Actors

1. **LinkedIn Profile Scraper**
   - Actor ID: `apify/linkedin-profile-scraper`
   - Input: `{"startUrls": ["https://linkedin.com/in/handle"]}`
   - Output: name, headline, summary, location, experience

2. **LinkedIn Search Scraper**
   - Actor ID: `apify/linkedin-search-scraper`
   - Input: `{"keywords": ["finance", "mumbai"], "location": "Mumbai"}`
   - Output: list of profiles

### Scraping Tips

#### Contact Info Extraction
LinkedIn profiles may contain:
- Email (in summary or experience sections)
- Phone numbers
- Personal websites
- Social media links

#### Rate Limiting
- **Delay**: 30 seconds between requests
- **Daily Limit**: ~50-100 profiles (LinkedIn has strict limits)
- **Session Required**: Must be logged in

### Alternative Methods

1. **Manual Export**: Use LinkedIn's "Export Connections" feature
2. **Browser Automation**: Use Puppeteer or Playwright
3. **Sales Navigator**: If you have a premium account

## Email Scraping

### From Websites

Use these patterns to extract emails from any webpage:

```python
import re

def extract_emails(text):
    # Standard email pattern
    email_pattern = r"@?([a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,})"
    emails = re.findall(email_pattern, text)
    
    # Clean up obfuscated emails
    cleaned = []
    for e in emails:
        e = e.replace(" [at] ", "@").replace(" [dot] ", ".").replace(" (at) ", "@")
        e = e.rstrip('.')
        if e not in cleaned:
            cleaned.append(e)
    return cleaned
```

### From PDFs

Use `PyPDF2` or `pdfminer` to extract text from PDFs:

```python
import PyPDF2

def extract_text_from_pdf(pdf_path):
    text = ""
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        for page in reader.pages:
            text += page.extract_text()
    return text
```

## Scraping Best Practices

### 1. Always Check robots.txt
Before scraping any site, check `https://site.com/robots.txt` for allowed paths.

### 2. Respect Rate Limits
- Add delays between requests (10-30 seconds)
- Use exponential backoff on errors
- Don't hammer APIs

### 3. Use Proxies
If you're scraping at scale:
- Use residential proxies (Luminati, Smartproxy)
- Rotate IP addresses
- Monitor for blocks

### 4. Cache Results
Save scraped data to avoid re-scraping:
```bash
cp data/apify_2026-11-21.csv data/scraped_2026-11-21.csv
```

### 5. Handle Errors Gracefully
```python
try:
    # Scraping code
    pass
except Exception as e:
    print(f"Error scraping {handle}: {e}")
    # Log error and continue
```

## Apify Setup

### Prerequisites
1. **Apify Account**: Sign up at apify.com
2. **API Token**: Get from Settings → Integrations
3. **MCP Configuration**: Add to your MCP config

### MCP Configuration Example

```json
{
  "mcpServers": {
    "apify": {
      "command": "npx",
      "args": ["@apify/cli", "mcp"],
      "env": {
        "APIFY_TOKEN": "your-api-token-here"
      }
    }
  }
}
```

### Running Actors

```bash
# Call an actor via MCP
call-actor --actor-id apify/instagram-profile-scraper \
  --input '{"usernames": ["instagram", "creator"]}'

# Check actor run status
get-actor-run --run-id abc123

# Fetch dataset items
get-dataset-items --dataset-id xyz456
```

## Troubleshooting

### Common Issues

**Issue**: Actor not returning expected data
- **Solution**: Check actor README for input schema
- **Solution**: Verify API token has correct permissions

**Issue**: Getting blocked by Instagram
- **Solution**: Use proxies
- **Solution**: Reduce request rate
- **Solution**: Use official Instagram API if available

**Issue**: Emails not being extracted
- **Solution**: Check obfuscation patterns
- **Solution**: Verify bio contains email
- **Solution**: Add more patterns to regex

**Issue**: Handles not being extracted
- **Solution**: Check bio contains @mentions
- **Solution**: Verify handle format (@handle)
- **Solution**: Exclude creator's own handle

### Debugging Tips

1. **Log Everything**: Save raw scraped data
2. **Test with Known Data**: Use test profiles you control
3. **Validate Output**: Check CSV structure before processing
4. **Monitor Rates**: Track requests per minute

## Alternative Tools

### Python Libraries
- **instaloader**: For Instagram (requires login)
- **requests-html**: For simple scraping
- **beautifulsoup4**: For HTML parsing
- **selenium**: For JavaScript-heavy sites
- **playwright**: Modern browser automation

### Node.js Libraries
- **puppeteer**: Headless Chrome
- **cheerio**: Fast HTML parsing
- **axios**: HTTP requests

### No-Code Tools
- **ParseHub**: Visual scraping
- **Octoparse**: Point-and-click scraper
- **Apify Web Scraper**: Apify's no-code tool

## Legal Considerations

⚠️ **Important**: Always check a website's Terms of Service before scraping.

### Permissible Scraping
- Publicly available data
- Data that doesn't require login
- Data with robots.txt permission

### Prohibited Scraping
- Private user data
- Data behind login walls
- Data with explicit anti-scraping measures
- Personal contact information (may violate privacy laws)

### Best Practices
- Don't scrape personal emails without consent
- Respect opt-out requests
- Comply with GDPR/CCPA if applicable
- Consider reaching out first before scraping

---

**Last Updated**: 2026-11-22

**Next Steps**:
- [ ] Set up Apify account and API token
- [ ] Configure MCP with Apify token
- [ ] Test scraping on a small set of profiles
- [ ] Scale up based on results