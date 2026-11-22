# Outreach Automation Skill

A Python-based workflow system for automated contact outreach, designed for integration with Claude Code's skill framework.

## What This Skill Does

This skill handles the complete outreach pipeline:

- **Data Enrichment**: Scrape social profiles (Instagram, LinkedIn) for contact information
- **Contact Extraction**: Parse bios for emails, handles, and manager information
- **Template Composition**: Generate personalized messages with custom templates
- **Sending Workflow**: Execute sends via Gmail, LinkedIn, or manual DM
- **Tracking**: Monitor replies, log responses, update status

## Implementation Overview

### Architecture
The skill follows a modular pipeline architecture:
1. **Input Layer**: Reads contact data from CSV or Google Sheets
2. **Enrichment Layer**: Scrapes social profiles via Apify Actors for additional contact info
3. **Personalization Layer**: Applies gender-aware templates with dynamic placeholders
4. **Delivery Layer**: Sends messages via configured client (Gmail, LinkedIn, or manual)
5. **Tracking Layer**: Monitors replies and updates contact status

### Key Features
- MIT License for open-source distribution
- Python 3.x for robust automation
- Template-driven personalization engine
- OAuth2 integrations for secure API access
- Batch processing with configurable limits
- Dry-run mode for safe testing

## Quick Start

### 1. Install the Skill

```bash
# Package the skill
python -m scripts.package_skill outreach-skill

# Install the .skill file in Claude Code
# Settings → Skills → Install Skill → Select the .skill file
```

### 2. Set Up a Campaign

Create a new folder for your campaign:

```bash
mkdir my-outreach-campaign
cd my-outreach-campaign
```

### 3. Create config.json

```json
{
  "campaign_name": "Your Campaign Name",
  "data_source": {
    "type": "google_sheet",
    "spreadsheet_id": "YOUR_SPREADSHEET_ID_HERE",
    "tab": "Leads"
  },
  "scraping": {
    "platforms": ["instagram"],
    "apify_actor": "instagram-profile-scraper"
  },
  "email": {
    "sender": "your@email.com",
    "cc": ["manager@company.com"],
    "attachment": "attachments/proposal.pdf",
    "dry_run": true
  },
  "templates": {
    "male": {
      "subject": "Collaboration Proposal | {campaign} x Mr. {full_name}",
      "body": "Hello Mr. {full_name}..."
    },
    "female": {
      "subject": "Collaboration Proposal | {campaign} x Ms. {full_name}",
      "body": "Hello Ms. {full_name}..."
    }
  },
  "sending": {
    "client": "gmail",
    "batch_size": 40,
    "delay_minutes": 5,
    "track_column": "status"
  }
}
```

### 4. Run the Workflow

```bash
# Step 1: Enrich contact data
outreach-skill enrich

# Step 2: Review and validate
outreach-skill review

# Step 3: Send messages (dry-run first)
outreach-skill send

# Step 4: Track responses
outreach-skill track
```

## Data Format

Your data source should have these columns:

| Column | Required | Purpose |
|--------|----------|---------|
| `platform_handle` | Yes | Instagram/LinkedIn handle |
| `profile_url` | Yes | Full profile link |
| `full_name` | Yes | Contact's name |
| `email` | No | Parsed email (optional) |
| `template` | No | male/female/neutral |
| `topic` | No | Topic for personalization |
| `status` | No | to_enrich, ready, sent, replied |

## Platform Support

### Instagram
- Bio scraping (via Apify)
- Email extraction from bio
- Handle extraction (@mentions)
- Gmail sending with attachments
- Manual DM workflow

### LinkedIn
- Profile scraping (requires LinkedIn session)
- Contact info extraction
- LinkedIn InMail sending
- Manual connection requests

### Generic CSV
- Import any contact list
- Column mapping configuration
- Auto-enrichment via scrapers

## Workflow Description

The skill implements a five-stage outreach pipeline:

1. **Prepare**: Load contacts from data source (CSV/Sheets) and validate schema
2. **Enrich**: Scrape social profiles to extract additional contact information
3. **Review**: Present enriched data for validation before sending
4. **Send**: Execute email/DM delivery with template personalization
5. **Track**: Monitor replies and update contact status

Each stage is designed to be idempotent and safe for iterative execution.

## Configuration Guide

### config.json Reference

```json
{
  "campaign_name": "string",
  "data_source": {
    "type": "csv|google_sheet",
    "path": "path/to/file.csv",
    "spreadsheet_id": "abc123...",
    "tab": "Sheet1",
    "sheet_id": "1abc..."
  },
  "scraping": {
    "platforms": ["instagram", "linkedin"],
    "apify_actor": "instagram-profile-scraper",
    "output_csv": "data/scraped.csv",
    "rate_limit_delay": 10
  },
  "email": {
    "sender": "your@email.com",
    "cc": ["manager@company.com"],
    "bcc": ["archive@company.com"],
    "attachment": "path/to/file.pdf",
    "dry_run": true,
    "max_per_day": 40
  },
  "templates": {
    "male": {
      "subject": "Subject with {placeholder}",
      "body": "Body text with {placeholder}"
    },
    "female": {
      "subject": "Subject with {placeholder}",
      "body": "Body text with {placeholder}"
    },
    "neutral": {
      "subject": "Subject",
      "body": "Body text"
    }
  },
  "sending": {
    "client": "gmail|manual|linkedin",
    "batch_size": 40,
    "delay_minutes": 5,
    "track_column": "status",
    "reply_search_query": "from:your-contact@example.com"
  }
}
```

### Template Placeholders

Common placeholders available in templates:
- `{full_name}` - Contact's name
- `{first_name}` - First name only
- `{topic}` - Topic of conversation
- `{company}` - Company name
- `{campaign}` - Campaign name
- `{sender}` - Your name

## Folder Structure

```
my-outreach-campaign/
├── config.json              # Campaign configuration
├── data/                    # Scraped data, intermediate files
│   ├── scraped.csv          # Apify output
│   └── enriched.csv         # Enriched contacts
├── attachments/            # PDFs, decks, images
│   └── proposal.pdf         # Attachment for emails
├── scripts/                # Helper scripts (optional)
│   └── custom_cleaner.py    # Custom data cleaning
└── templates/              # Custom templates
    └── followup.txt         # Follow-up message
```

## Safety Features

### Dry-Run Mode
- Enabled by default (`"dry_run": true`)
- No emails are sent in dry-run mode
- Review what would be sent before enabling actual sends

### Rate Limiting
- Instagram scraping: 10-30 seconds between requests
- Email sending: 5 minutes between batches
- LinkedIn: Follow platform limits

### Platform Requirements
- **Apify**: API token configured in MCP
- **Google Sheets**: OAuth token.json in campaign folder
- **Gmail**: OAuth token.json in campaign folder
- **LinkedIn**: Valid LinkedIn session

## Example Use Cases

- Creator Outreach: Find and contact Instagram creators
- Speaker Recruitment: Reach out to potential event speakers
- Job Recruitment: Contact professionals for open positions
- Partnership Outreach: Contact potential business partners
- Product Launches: Announce new products to prospects
- Event Promotion: Invite attendees to conferences
- Fundraising: Contact potential investors or donors

## Metrics Tracked

- Contacts enriched
- Emails sent
- Replies received
- Response rate
- Bounce rate
- Conversion rate

---

**Built using Claude Code and Apify**

[GitHub Repository](https://github.com/MukundAgarwal-Git/outreach-automation-skill) | [Support](https://github.com/MukundAgarwal-Git/outreach-automation-skill/issues)