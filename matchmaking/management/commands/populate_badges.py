from django.core.management.base import BaseCommand
from matchmaking.models import Badge


class Command(BaseCommand):
    help = 'Populate the database with Theta Tau badges for the three pillars'

    def handle(self, *args, **kwargs):
        # Define all badges
        badges_data = [
            # Brotherhood badges
            {
                'name': 'Mentorship',
                'pillar': 'BROTHERHOOD',
                'description': 'Guiding and supporting fellow members',
                'icon_image': 'images/badges/mentorship.png',
                'order': 1
            },
            {
                'name': 'Social Events',
                'pillar': 'BROTHERHOOD',
                'description': 'Organizing and participating in brotherhood activities',
                'icon_image': 'images/badges/social-events.png',
                'order': 2
            },
            {
                'name': 'Team Building',
                'pillar': 'BROTHERHOOD',
                'description': 'Fostering collaboration and unity',
                'icon_image': 'images/badges/team-building.png',
                'order': 3
            },
            {
                'name': 'Networking',
                'pillar': 'BROTHERHOOD',
                'description': 'Building connections within the chapter',
                'icon_image': 'images/badges/networking.png',
                'order': 4
            },
            {
                'name': 'Tradition Keeper',
                'pillar': 'BROTHERHOOD',
                'description': 'Upholding Theta Tau traditions and values',
                'icon_image': 'images/badges/tradition-keeper.png',
                'order': 5
            },
            
            # Professionalism badges
            {
                'name': 'Leadership',
                'pillar': 'PROFESSIONALISM',
                'description': 'Leading projects and initiatives',
                'icon_image': 'images/badges/leadership.png',
                'order': 1
            },
            {
                'name': 'Career Development',
                'pillar': 'PROFESSIONALISM',
                'description': 'Focus on professional growth and skills',
                'icon_image': 'images/badges/career-development.png',
                'order': 2
            },
            {
                'name': 'Industry Expert',
                'pillar': 'PROFESSIONALISM',
                'description': 'Deep knowledge in engineering field',
                'icon_image': 'images/badges/industry-expert.png',
                'order': 3
            },
            {
                'name': 'Public Speaking',
                'pillar': 'PROFESSIONALISM',
                'description': 'Presenting and communicating effectively',
                'icon_image': 'images/badges/public-speaking.png',
                'order': 4
            },
            {
                'name': 'Resume & Interview',
                'pillar': 'PROFESSIONALISM',
                'description': 'Helping others with career preparation',
                'icon_image': 'images/badges/resume-interview.png',
                'order': 5
            },
            
            # Service badges
            {
                'name': 'Community Outreach',
                'pillar': 'SERVICE',
                'description': 'Volunteering in local community',
                'icon_image': 'images/badges/community-outreach.png',
                'order': 1
            },
            {
                'name': 'Environmental',
                'pillar': 'SERVICE',
                'description': 'Sustainability and environmental initiatives',
                'icon_image': 'images/badges/environmental.png',
                'order': 2
            },
            {
                'name': 'Education',
                'pillar': 'SERVICE',
                'description': 'Tutoring and educational programs',
                'icon_image': 'images/badges/education.png',
                'order': 3
            },
            {
                'name': 'Fundraising',
                'pillar': 'SERVICE',
                'description': 'Organizing charitable fundraising events',
                'icon_image': 'images/badges/fundraising.png',
                'order': 4
            },
            {
                'name': 'Global Impact',
                'pillar': 'SERVICE',
                'description': 'International service and awareness',
                'icon_image': 'images/badges/global-impact.png',
                'order': 5
            },
        ]
        
        # Create or update badges
        created_count = 0
        updated_count = 0
        
        for badge_data in badges_data:
            badge, created = Badge.objects.update_or_create(
                name=badge_data['name'],
                pillar=badge_data['pillar'],
                defaults={
                    'description': badge_data['description'],
                    'icon_image': badge_data['icon_image'],
                    'order': badge_data['order'],
                }
            )
            
            if created:
                created_count += 1
                self.stdout.write(
                    self.style.SUCCESS(f'✓ Created badge: {badge.name} ({badge.get_pillar_display()})')
                )
            else:
                updated_count += 1
                self.stdout.write(
                    self.style.WARNING(f'↻ Updated badge: {badge.name} ({badge.get_pillar_display()})')
                )
        
        self.stdout.write(
            self.style.SUCCESS(
                f'\nSummary: Created {created_count} badges, Updated {updated_count} badges'
            )
        )
        self.stdout.write(
            self.style.SUCCESS(f'Total badges in database: {Badge.objects.count()}')
        )

