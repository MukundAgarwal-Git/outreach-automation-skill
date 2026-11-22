---
name: outreach-skill
description: |
  General-purpose outreach automation for any campaign. Handles data enrichment, email/DM composition, and tracking across any platform. Use when the user wants to send outreach messages, find contacts, enrich profiles, or track responses. Supports customizable templates, multiple data sources, and integration with email clients, Instagram, LinkedIn, and other platforms.
---

# Outreach Automation Skill

A generic, configurable outreach workflow that works with any campaign, platform, or data source. Designed for any professional outreach scenario — speaker recruitment, job outreach, partnership proposals, product launches, and more.

## What This Skill Does

1. **Data Enrichment** - Scrape social profiles (Instagram, LinkedIn, etc.) using Apify or other methods
2. **Contact Extraction** - Parse bios for emails, handles, and contact info
3. **Template Composition** - Generate personalized messages with user-provided templates
4. **Sending Workflow** - Execute sends via Gmail, LinkedIn, Instagram DM, or other clients
5. **Tracking** - Monitor replies, log responses, update status

## When to Use This Skill

- "I need to send outreach emails to my contacts"
- "Can you find the emails for these Instagram handles?"
- "Help me send personalized messages to my prospect list"
- "Track my outreach campaign responses"
- "I have a CSV of contacts, help me send them emails"
- "Scrape LinkedIn profiles for contact info"
- Any mention of outreach, cold emailing, DM automation, prospecting, or contact research

## Configuration

Before running, you need a **config.json** file in the campaign folder:

```json
{
  "campaign_name": "Your Campaign Name",
  "data_source": {
    "type": "csv|google_sheet",
    "path": "contacts.csv",
    "spreadsheet_id": "1abc...",
    "tab": "Contacts"
  },
  "scraping": {
    "platforms": ["instagram", "linkedin"],
    "apify_actor": "instagram-profile-scraper",
    "output_csv": "data/scraped.csv"
  },
  "email": {
    "sender": "your@email.com",
    "cc": ["manager@example.com"],
    "attachment": "decks/proposal.pdf",
    "dry_run": true
  },
  "templates": {
    "male": {
      "subject": "Subject line with {name}",
      "body": "Email body with {name} and {topic}"
    },
    "female": {
      "subject": "Subject line with {name}",
      "body": "Email body with {name} and {topic}"
    },
    "neutral": {
      "subject": "Subject line with {name}",
      "body": "Email body"
    }
  },
  "sending": {
    "client": "gmail|manual|linkedIn",
    "batch_size": 40,
    "delay_minutes": 5,
    "track_column": "status"
  }
}
```

## Workflow

### Step 1: Prepare Your Data

Your contact data should have these columns (customize as needed):

| Column | Purpose |
|--------|---------|
| `platform_handle` | Instagram/LinkedIn handle |
| `profile_url` | Full profile link |
| `full_name` | Contact's name |
| `email` | Parsed email (can be empty) |
| `template` | male/female/neutral or custom template name |
| `topic` | Topic for personalization |
| `status` | to_enrich, ready, sent, replied, etc. |

### Step 2: Enrich Profiles (if needed)

Use the appropriate scraper for your platform:

```
Use Apify MCP tools to scrape profiles:
- Call actor: instagram-profile-scraper
- Input: {"username": "profile_handle"}
- Output: bio, email, external links, category
```

The skill will automatically extract emails and handles from bios.

### Step 3: Review and Prepare

The skill will:
- Show preview of enrichment data
- Validate email formats
- Check for missing critical fields
- Present ready-to-send count

### Step 4: Send Messages

Configure in config.json:
- Set `dry_run: false` when ready to send
- Review batch samples
- Skill sends with configurable limits (default: 40/day)

### Step 5: Track Responses

Run tracking command to:
- Search Gmail for replies
- Update status column
- Add reply summaries

## Platform Support

### Instagram
- Scrapes: bio, email, handles
- Extract: @mentions, email patterns
- Send: Gmail with attachment, manual DM

### LinkedIn
- Requires: Valid LinkedIn session
- Can: Scrape public profiles
- Send: LinkedIn InMail or manual DM

### Generic CSV
- Import any contact list
- Map columns to expected fields
- Auto-enrich via scrapers

## Batch Sending Rules

- Daily limit: 40 emails (configurable)
- Wait for confirmation between batches
- Log failures with error details
- Never send incomplete templates

## Safety Rules

- Work only in campaign folder
- Never delete existing data
- Always ask before sending
- Dry-run mode shows what would be sent

## Example Usage

```
Given config.json and contacts.csv in the current folder.

I want to send outreach to 100 contacts.

Run Step 2 to enrich Instagram profiles using Apify.
Run Step 3 to review the enriched data.
Run Step 4 to send emails with the male template to {name}.
Run Step 5 after 3 days to check for replies.

The campaign has a Summit Deck attached and Cc includes team@company.com.
```

## Related Files

- `scripts/enrich_contacts.py` - Scrape and enrich contact data
- `scripts/send_outreach.py` - Send emails/DMs
- `scripts/track_responses.py` - Monitor replies
- `references/platform-scraping.md` - Platform-specific scraping tips
- `references/templates.md` - Template design guidelines