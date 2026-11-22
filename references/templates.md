# Template Design Guide

Creating effective outreach templates is crucial for campaign success. This guide provides best practices and examples.

## Template Structure

### Standard Email Template

```
Subject: [Clear, concise, personalized]

[Personalized greeting]

[Opening - 1-2 sentences, mention connection]

[Body - 3-5 sentences, explain purpose]

[Call to Action - clear next step]

[Closing - professional sign-off]

[Signature - full contact info]
```

### Template Placeholders

Use these placeholders in your templates:

| Placeholder | Description | Example |
|-------------|-------------|---------|
| `{full_name}` | Full name | John Doe |
| `{first_name}` | First name only | John |
| `{last_name}` | Last name only | Doe |
| `{company}` | Company name | Google |
| `{topic}` | Topic of conversation | AI in healthcare |
| `{campaign}` | Campaign name | Creator Con 2026 |
| `{sender}` | Your name | Mukund Agarwal |
| `{sender_title}` | Your title | Member of Department – Summits |

## Template Types

### 1. Cold Outreach Email
**Use Case**: First contact with a prospect
**Tone**: Professional, friendly
**Length**: 100-150 words

```
Subject: Collaboration opportunity with {company}

Hello {first_name},

I came across your work at {company} and was impressed by your recent project on {topic}.

I'm reaching out from [Organization] because we're looking to connect with experts like you for potential collaborations.

We're hosting {campaign} on [date] and would love to explore how we might work together. The event brings together {audience description}.

Would you be open to a quick call next week to discuss possibilities?

Looking forward to hearing your thoughts.

Best regards,
{sender}
{sender_title}
```

### 2. Follow-up Email
**Use Case**: Follow-up to unanswered emails
**Tone**: Polite, slightly more casual
**Length**: 80-120 words

```
Subject: Following up on my previous email

Hi {first_name},

I wanted to follow up on my email from [date] regarding a potential collaboration around {topic}.

I completely understand if you're busy, but I'd love to hear your thoughts when you have a moment.

The key details:
- Event: {campaign} on {date}
- Opportunity: {brief description}
- Next step: Quick 15-minute call

Would Tuesday or Thursday work for a brief conversation?

Thanks for your time!

Best,
{sender}
```

### 3. Speaker Invitation
**Use Case**: Inviting someone to speak at an event
**Tone**: Formal, flattering
**Length**: 150-200 words

```
Subject: Invitation to speak at {campaign} on {date}

Dear {full_name},

I hope this email finds you well. I'm reaching out from [Organization], where we're organizing {campaign} on {date}.

We've been following your impressive work in {topic} and believe your insights would be incredibly valuable to our audience of {audience description}.

The Summit will feature {event highlights}, bringing together {attendee count} attendees. Last year's event featured {past speaker example}.

We'd be honored if you would join us as a keynote speaker. The session would be {duration}, covering {topic areas}.

Please let us know if you'd be available, and we can discuss further details.

Looking forward to your response.

Best regards,
{sender}
{sender_title}
[Organization]
```

### 4. Partnership Proposal
**Use Case**: Proposing a business partnership
**Tone**: Professional, collaborative
**Length**: 150-200 words

```
Subject: Partnership opportunity with {company}

Hello {first_name},

I'm reaching out from [Organization] where we're exploring partnership opportunities in the {industry} space.

Your work at {company} in {topic} caught our attention, and we believe there's significant potential for collaboration between our organizations.

Specifically, we're interested in:
- {Partnership area 1}
- {Partnership area 2}
- {Partnership area 3}

We've attached a brief overview of our proposal for your review. Would you be available for a call next week to discuss this further?

Looking forward to exploring this opportunity together.

Best regards,
{sender}
{sender_title}
```

### 5. Event Promotion
**Use Case**: Promoting an event to potential attendees
**Tone**: Excited, inviting
**Length**: 120-180 words

```
Subject: Join us at {campaign} on {date} - Limited seats available!

Hi {first_name},

We're excited to invite you to {campaign}, happening on {date} at [Location]. This year's event will bring together {attendee description} for a day of {event themes}.

Highlights include:
- Keynote by {keynote speaker}
- Panel on {panel topic}
- Networking sessions
- {Other highlights}

Last year's event welcomed {past attendance} attendees, and we're expecting even more this year!

Registration is now open at [link]. Early bird tickets are available until [date].

We'd love to see you there. Let us know if you have any questions.

Best,
{sender}
[sender_title]
[Organization]
```

## Template Personalization

### Level 1: Basic Personalization
- Use `{first_name}` instead of generic greetings
- Reference their company or role
- Mention their recent work or achievements

**Example**:
```
Hi {first_name},

I've been following your work at {company} and was particularly impressed by your recent article on {topic}.
```

### Level 2: Advanced Personalization
- Reference specific projects they've worked on
- Mention mutual connections
- Reference their location or local events
- Tailor the value proposition to their industry

**Example**:
```
Hi {first_name},

I noticed your recent talk at {event} about {topic}. Your insights on {specific point} really resonated with me.

I'm reaching out because we're helping companies like yours in {industry} achieve {specific goal} through {solution}.
```

### Level 3: Hyper-Personalization
- Reference recent news about their company
- Mention their personal achievements
- Tailor the entire message to their specific situation
- Include specific metrics or results they've achieved

**Example**:
```
Hi {first_name},

Congratulations on your recent Series B funding of ${amount}! This is a huge milestone for {company}.

I wanted to reach out because we've helped similar companies like {comparable company} scale their {specific function} operations by {percentage} in just {timeframe}.
```

## Template Testing

### A/B Testing
Test different versions of your templates:

**Version A**:
```
Subject: Quick question about {topic}
```

**Version B**:
```
Subject: {first_name}, let's chat about {topic}
```

### Metrics to Track
- Open rate
- Response rate
- Click-through rate (if links included)
- Conversion rate

### Template Optimization
Based on test results:
- Keep what works
- Modify what doesn't
- Test new variations
- Iterate continuously

## Template Management

### Organizing Templates
```
templates/
├── cold-outreach/
│   ├── tech-startups.txt
│   ├── finance-professionals.txt
│   └── marketing-leads.txt
├── follow-ups/
│   ├── 1st-followup.txt
│   ├── 2nd-followup.txt
│   └── 3rd-followup.txt
└── event-specific/
    ├── creator-con.txt
    └── summit-2026.txt
```

### Template Variables
Create reusable template variables:

```json
{
  "sender_info": {
    "name": "Mukund Agarwal",
    "title": "Member of Department – Summits",
    "organization": "Arithmós | SVKM's Narsee Monjee College of Commerce & Economics",
    "email": "summits.arithmos@gmail.com",
    "phone": "+91 8217343277"
  },
  "event_details": {
    "name": "Arithmós Summit 2026",
    "date": "14 December 2026",
    "location": "Mumbai, India",
    "attendees": "600–700 students and young professionals"
  }
}
```

### Dynamic Template Loading
```python
import json

def load_template(template_name, variables):
    with open(f'templates/{template_name}.txt', 'r') as f:
        template = f.read()
    
    # Replace placeholders
    for key, value in variables.items():
        template = template.replace(f'{{{key}}}', value)
    
    return template
```

## Template Examples from Real Campaigns

### Example 1: Creator Con Speaker Invitation (Male)
```
Subject: Creator Con - Collaboration Proposal | NM Arithmós x Mr. {full_name}

Hello Mr. {full_name} and Team!

I'm reaching out on behalf of NM Arithmós, the Management & Strategy Fest of SVKM's Narsee Monjee College of Commerce & Economics, Mumbai. Ranked as India's 5th Most Popular UG College Fest on Unstop, Arithmós hosts 18+ events centred around business, management and strategy.

We're currently organising Arithmós Summit 2026, scheduled for 14 December, which will bring together 600–700 students and young professionals for insightful conversations with individuals shaping their respective industries.

For this year's edition, we would be honoured to invite you to join us as our keynote speaker. We believe that your journey and insights into {topics} would offer our audience a valuable opportunity to learn from your experiences, perspectives and work.

Our inaugural Summit last year welcomed 650+ attendees, featuring Ms. Zareen Khan as the keynote speaker, alongside a finance panel featuring Mr. Devraj Pant, Mr. Kirtan Shah and other industry professionals.

Additionally, if there is a collaboration prospect between any of his ventures, we would be more than excited to hear about it and work on it.

We've attached our Summit Deck for your reference and would love to explore the possibility of him joining us for this year's edition. Please let us know if we could connect for a brief discussion.

We look forward to hearing from you!

Regards,
Mukund Agarwal
Member of Department – Summits
Arithmós | SVKM's Narsee Monjee College of Commerce & Economics

+91 8217343277 | +91 9589969868
summits.arithmos@gmail.com
arya.nmarithmos@gmail.com
mukund.nmarithmos@gmail.com
```

### Example 2: Creator Con Speaker Invitation (Female)
```
Subject: Creator Con - Collaboration Proposal | NM Arithmós x Ms. {full_name}

Hello Ms. {full_name} and Team!

I'm reaching out on behalf of NM Arithmós, the Management & Strategy Fest of SVKM's Narsee Monjee College of Commerce & Economics, Mumbai. Ranked as India's 5th Most Popular UG College Fest on Unstop, Arithmós hosts 18+ events centred around business, management and strategy.

We're currently organising Arithmós Summit 2026, scheduled for 14 December, which will bring together 600–700 students and young professionals for insightful conversations with individuals shaping their respective industries.

For this year's edition, we would be honoured to invite you to join us as our keynote speaker. We believe that your journey and insights into {topics} would offer our audience a valuable opportunity to learn from your experiences, perspectives and work.

Our inaugural Summit last year welcomed 650+ attendees, featuring Ms. Zareen Khan as the keynote speaker, alongside a finance panel featuring Mr. Devraj Pant, Mr. Kirtan Shah and other industry professionals.

Additionally, if there is a collaboration prospect between any of her ventures, we would be more than excited to hear about it and work on it.

We've attached our Summit Deck for your reference and would love to explore the possibility of her joining us for this year's edition. Please let us know if we could connect for a brief discussion.

We look forward to hearing from you!

Regards,
Mukund Agarwal
Member of Department – Summits
Arithmós | SVKM's Narsee Monjee College of Commerce & Economics

+91 8217343277 | +91 9589969868
summits.arithmos@gmail.com
arya.nmarithmos@gmail.com
mukund.nmarithmos@gmail.com
```

### Example 3: Generic Business Outreach
```
Subject: Quick chat about {topic}?

Hi {first_name},

I came across your profile and was impressed by your work in {topic}. I'm reaching out because we're helping companies like yours achieve {specific benefit}.

We've helped similar companies:
- Increase {metric} by {percentage}
- Reduce {cost} by {amount}
- Improve {efficiency} by {percentage}

Would you be open to a quick 15-minute call next week to discuss? I'm available Tuesday or Thursday.

Looking forward to your thoughts.

Best regards,
{sender}
{sender_title}
```

## Template Best Practices

### ✅ Do
- Keep subject lines under 50 characters
- Personalize with at least `{first_name}`
- Include a clear call to action
- Keep paragraphs short (2-3 sentences)
- Use bullet points for lists
- Include social proof when possible
- Test different lengths

### ❌ Don't
- Use generic greetings like "Dear Sir/Madam"
- Write long paragraphs (more than 3-4 sentences)
- Use excessive exclamation marks!!!
- Include too many links
- Make false promises
- Copy-paste without personalization
- Forget to include your contact info

### Subject Line Tips
- **Personalized**: "{first_name}, let's chat about {topic}"
- **Curiosity**: "Quick question about your {topic}"
- **Value**: "How {company} can {benefit}"
- **Urgency**: "Last chance to {opportunity}"
- **Social Proof**: "{mutual connection} recommended I reach out"

### Length Guidelines
- **Cold Email**: 80-120 words
- **Follow-up**: 60-100 words
- **Invitation**: 120-180 words
- **Partnership**: 150-200 words

## Template Storage

### File-based Storage
```
templates/
├── speaker-invitation-male.txt
├── speaker-invitation-female.txt
├── partnership-proposal.txt
├── event-promotion.txt
└── follow-up-1.txt
```

### Database Storage
If using a database, store templates with:
- Template ID
- Name
- Subject
- Body
- Placeholders
- Category
- Language
- Status (active/inactive)

### Version Control
Track template changes with Git:
```bash
git add templates/speaker-invitation-male.txt
git commit -m "Update speaker invitation template with new event date"
```

## Template Testing Framework

### Test Matrix
Create a matrix of template variations:

| Variable | Test A | Test B | Test C |
|----------|--------|--------|--------|
| Subject | Short | Medium | Long |
| Greeting | Formal | Casual | None |
| Body | Short | Medium | Long |
| CTA | Direct | Indirect | Question |

### Success Metrics
- Open rate > 20%
- Response rate > 5%
- Positive reply rate > 70%
- Bounce rate < 2%

### Iteration Process
1. Test 2-3 variations
2. Measure results after 1 week
3. Keep the winner
4. Create new variations
5. Repeat

---

**Last Updated**: 2026-11-22  
**Next Steps**:
- [ ] Create 3-5 template variations for your campaign
- [ ] Set up A/B testing framework
- [ ] Test with a small sample (10-20 contacts)
- [ ] Scale up based on results