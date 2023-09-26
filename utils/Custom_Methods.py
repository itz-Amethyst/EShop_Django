from Site_Module.models import SiteBanner


def SelectSiteBanner(choice):
    return SiteBanner.objects.filter(is_active = True, position__iexact = choice)


def Group_List(custom_list, size=4):
    grouped_list = []
    group_size = size

    for i in range(0, len(custom_list), size):
        grouped_list.append(custom_list[i:i + size])
    return grouped_list