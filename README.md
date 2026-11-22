# Outreach Automation Skill

A general-purpose outreach automation skill for Claude Code that handles contact enrichment, email composition, and campaign tracking across multiple platforms.

## 🎯 What This Skill Does

This skill automates the entire outreach workflow:

✅ **Data Enrichment** - Scrape social profiles (Instagram, LinkedIn) for contact info
✅ **Contact Extraction** - Parse bios for emails, handles, and manager information  
✅ **Template Composition** - Generate personalized messages with custom templates
✅ **Sending Workflow** - Execute sends via Gmail, LinkedIn, or manual DM
✅ **Tracking** - Monitor replies, log responses, update status

## 🚀 Quick Start

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
  "campaign_name": "Creator Con 2026",
  "data_source": {
    "type": "google_sheet",
    "spreadsheet_id": "1aKThe7WMTjOl2JrQSjFIyhY6rI6sIYjF2cuyC6YTliI",
    "tab": "Leads"
  },
  "scraping": {
    "platforms": ["instagram"],
    "apify_actor": "instagram-profile-scraper"
  },
  "email": {
    "sender": "summits.nm.arithmos@gmail.com",
    "cc": ["team@example.com"],
    "attachment": "attachments/CreatorCon_Collaboration_Proposal.pdf",
    "dry_run": true
  },
  "templates": {
    "male": {
      "subject": "Creator Con - Collaboration Proposal | NM Arithmós x Mr. {full_name}",
      "body": "Hello Mr. {full_name}..."
    },
    "female": {
      "subject": "Creator Con - Collaboration Proposal | NM Arithmós x Ms. {full_name}",
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

## 📋 Data Format

Your data source should have these columns:

| Column | Required | Purpose |
|--------|----------|---------|
| `platform_handle` | ✅ | Instagram/LinkedIn handle |
| `profile_url` | ✅ | Full profile link |
| `full_name` | ✅ | Contact's name |
| `email` | ❌ | Parsed email (optional) |
| `template` | ❌ | male/female/neutral |
| `topic` | ❌ | Topic for personalization |
| `status` | ❌ | to_enrich, ready, sent, replied |

## 🛠️ Platform Support

### Instagram
- ✅ Bio scraping (via Apify)
- ✅ Email extraction from bio
- ✅ Handle extraction (@mentions)
- ✅ Gmail sending with attachments
- ✅ Manual DM workflow

### LinkedIn
- ✅ Profile scraping (requires LinkedIn session)
- ✅ Contact info extraction
- ✅ LinkedIn InMail sending
- ✅ Manual connection requests

### Generic CSV
- ✅ Import any contact list
- ✅ Column mapping configuration
- ✅ Auto-enrichment via scrapers

## 📊 Example Campaigns

### Creator Con Speaker Outreach
- Target: Instagram creators with 200K-10M followers
- Platform: Instagram
- Template: Male/Female speaker proposals
- Attachment: Summit deck PDF
- Goal: Secure keynote speakers

### Job Opportunity Outreach
- Target: LinkedIn professionals in finance
- Platform: LinkedIn
- Template: Job opportunity email
- Goal: Fill open positions

### Product Launch Campaign
- Target: Email list from CSV
- Platform: Email
- Template: Product announcement
- Goal: Drive product awareness

## 🔧 Configuration Guide

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
    "reply_search_query": "from:contact@example.com"
  }
}
```

### Template Placeholders

Common placeholders you can use in templates:
- `{full_name}` - Contact's name
- `{first_name}` - First name only
- `{topic}` - Topic of conversation
- `{company}` - Company name
- `{campaign}` - Campaign name
- `{sender}` - Your name

## 📁 Folder Structure

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

## 🎓 Tutorial: Setting Up a New Campaign

### Step 1: Create Campaign Folder

```bash
mkdir my-creator-outreach
cd my-creator-outreach
```

### Step 2: Create config.json

```bash
cat > config.json << 'EOF'
{
  "campaign_name": "NM Arithmós Summit 2026",
  "data_source": {
    "type": "google_sheet",
    "spreadsheet_id": "1aKThe7WMTjOl2JrQSjFIyhY6rI6sIYjF2cuyC6YTliI",
    "tab": "Leads"
  },
  "scraping": {
    "platforms": ["instagram"],
    "apify_actor": "instagram-profile-scraper"
  },
  "email": {
    "sender": "summits.nm.arithmos@gmail.com",
    "cc": ["arya.nmarithmos@gmail.com"],
    "attachment": "attachments/CreatorCon_Collaboration_Proposal.pdf",
    "dry_run": true
  },
  "templates": {
    "male": {
      "subject": "Creator Con - Collaboration Proposal | NM Arithmós x Mr. {full_name}",
      "body": "Hello Mr. {full_name} and Team!\n\nI'm reaching out on behalf of NM Arithmós..."
    },
    "female": {
      "subject": "Creator Con - Collaboration Proposal | NM Arithmós x Ms. {full_name}",
      "body": "Hello Ms. {full_name} and Team!\n\nI'm reaching out on behalf of NM Arithmós..."
    }
  },
  "sending": {
    "client": "gmail",
    "batch_size": 40,
    "delay_minutes": 5,
    "track_column": "status"
  }
}
EOF
```

### Step 3: Create Attachments Folder

```bash
mkdir -p attachments
# Copy your PDF deck here
```

### Step 4: Run the Workflow

```bash
# Enrich Instagram profiles
outreach-skill enrich

# Review the enriched data
outreach-skill review

# Send emails (dry-run first!)
outreach-skill send

# After 3 days, track replies
outreach-skill track
```

## 🚨 Important Notes

### Safety First
- ✅ **Dry-run mode is ON by default** - No emails are sent until you set `"dry_run": false`
- ✅ **Always review samples** before sending
- ✅ **Daily limits enforced** (default: 40 emails/day)
- ✅ **No data deletion** - Only appends and updates

### Rate Limiting
- Instagram scraping: 10-30 seconds between requests
- Email sending: 5 minutes between batches
- LinkedIn: Follow platform limits

### Platform Requirements
- **Apify**: API token configured in MCP
- **Google Sheets**: OAuth token.json in campaign folder
- **Gmail**: OAuth token.json in campaign folder
- **LinkedIn**: Valid LinkedIn session

## 🔄 Updating the Skill

```bash
# Pull latest changes
git pull origin main

# Re-package if you made changes
python -m scripts.package_skill outreach-skill
```

## 📞 Support & Issues

- Check `references/troubleshooting.md` for common issues
- Review `references/platform-scraping.md` for platform-specific tips
- Open GitHub issues for bugs or feature requests

## 🎯 Use Cases

✅ **Creator Outreach** - Find and contact Instagram creators
✅ **Speaker Recruitment** - Reach out to potential event speakers
✅ **Job Recruitment** - Contact professionals for open positions
✅ **Partnership Outreach** - Reach out to potential business partners
✅ **Product Launches** - Announce new products to prospects
✅ **Event Promotion** - Invite attendees to conferences
✅ **Fundraising** - Contact potential investors or donors

## 📊 Metrics Tracked

- Contacts enriched
- Emails sent
- Replies received
- Response rate
- Bounce rate
- Conversion rate

---

**Built with ❤️ using Claude Code and Apify**

[GitHub Repository](#) | [Documentation](#) | [Issues](#)