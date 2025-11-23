# Badge System Feature

## Overview

The badge system allows brothers to showcase their interests and skills aligned with Theta Tau's three pillars: Brotherhood, Professionalism, and Service. This helps PNMs find brothers with similar interests.

## Features

### 15 Badges Across 3 Pillars

**Brotherhood (5 badges):**
- Mentorship - Guiding and supporting fellow members
- Social Events - Organizing and participating in brotherhood activities
- Team Building - Fostering collaboration and unity
- Networking - Building connections within the chapter
- Tradition Keeper - Upholding Theta Tau traditions and values

**Professionalism (5 badges):**
- Leadership - Leading projects and initiatives
- Career Development - Focus on professional growth and skills
- Industry Expert - Deep knowledge in engineering field
- Public Speaking - Presenting and communicating effectively
- Resume & Interview - Helping others with career preparation

**Service (5 badges):**
- Community Outreach - Volunteering in local community
- Environmental - Sustainability and environmental initiatives
- Education - Tutoring and educational programs
- Fundraising - Organizing charitable fundraising events
- Global Impact - International service and awareness

## Visual Design

### Badge Display
- **Badge icons**: PNG images stored in `static/images/badges/`
- **Color coding by pillar**:
  - Brotherhood: Red gradient (#C8102E)
  - Professionalism: Gold gradient (#FFC72C)
  - Service: Green gradient (#28A745)

### User Experience

#### Brother Profile Creation
- Badges displayed in 3-column grid layout
- Large, prominent icons (80x80px) above badge names
- Vertical card layout with checkbox for selection
- Organized by pillar with color-coded headers
- Responsive: single column on mobile, 2 columns on tablets, 3 on desktop

#### Brother Success Page
- Selected badges displayed prominently with large icons (40x40px)
- Horizontal pill layout with icon + name
- Badges grouped in "My Interests & Skills" section

#### PNM Match Results
- Each brother card shows selected badges
- **Scrollable cards** (750px height) for better organization
- **Single-column badge layout** (90% width) for better visibility
- Large badge pills (32x32px icons) with pillar-specific colors
- Hover effects for interactivity

#### Admin Dashboard
- Badge count displayed for each brother
- Visual indicator of profile completion

## Database Structure

### Badge Model
```python
- name: CharField(max_length=100)
- pillar: CharField(choices=['BROTHERHOOD', 'PROFESSIONALISM', 'SERVICE'])
- description: TextField (admin reference)
- icon_image: CharField (path to PNG image)
- order: IntegerField (display order within pillar)
```

### BrotherProfile Relationship
- ManyToManyField to Badge model
- Brothers can select multiple badges
- Optional field (blank=True)

## Management Command

Populate badges in the database:

```bash
python manage.py populate_badges
```

This command:
- Creates all 15 badges automatically
- Updates existing badges if run again
- Organizes badges by pillar and order

## Badge Images

Placeholder PNG images are stored in `static/images/badges/`:
- `mentorship.png`
- `social-events.png`
- `team-building.png`
- `networking.png`
- `tradition-keeper.png`
- `leadership.png`
- `career-development.png`
- `industry-expert.png`
- `public-speaking.png`
- `resume-interview.png`
- `community-outreach.png`
- `environmental.png`
- `education.png`
- `fundraising.png`
- `global-impact.png`

**Note**: These are placeholder images. Replace with actual designed icons for production.

## CSS Styling

Custom badge styles in `static/css/badges.css`:
- `.badge-grid-3col` - 3-column responsive grid for form
- `.badge-checkbox-item-vertical` - Vertical card layout for badge selection
- `.badge-pill-large` - Large prominent badges (brother success page)
- `.badge-pill-card` - Badge display on match cards (single-column layout)
- Pillar-specific color classes
- Hover effects and transitions
- Responsive breakpoints for mobile/tablet/desktop

## Key Implementation Details

1. **Form Updates**: `BrotherProfileForm` includes `ModelMultipleChoiceField` for badge selection
2. **Template Integration**: Uses `{% regroup %}` template tag to organize badges by pillar
3. **Static Files**: Badge images loaded using `{% static badge.icon_image %}`
4. **Scrollable Cards**: PNM match cards use fixed height (750px) with `overflow-y: auto`
5. **Single-Column Layout**: Badges in match cards use `flex-direction: column` with 90% width
6. **Responsive Design**: CSS media queries adapt layout for different screen sizes

## Usage

### For Brothers
1. Create profile at `/brother/create-profile/`
2. Select badges that represent your interests
3. Badges displayed on success page and visible to PNMs

### For PNMs
1. Create profile at `/pnm/create-profile/`
2. View matched brothers with their badges in scrollable cards
3. Badges help identify shared interests with single-column layout

### For Admins
1. View badge counts in admin dashboard
2. Manage badges via Django admin panel
3. Can add/edit/delete badges as needed

## Future Enhancements

- Replace placeholder images with custom-designed icons
- Add badge search/filter functionality
- Track badge popularity statistics
- Allow brothers to explain why they selected specific badges
- Badge-based matching algorithm enhancement

