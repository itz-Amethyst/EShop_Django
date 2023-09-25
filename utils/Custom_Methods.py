from Site_Module.models import SiteBanner


def SelectSiteBanner(choice):
    return SiteBanner.objects.filter(is_active = True, position__iexact = choice)