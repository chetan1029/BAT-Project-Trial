from settings.models import (AmazonMarket)

def marketplace(request):
    return {
        'marketplace': AmazonMarket.objects.all()
    }
