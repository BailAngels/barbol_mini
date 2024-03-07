def upload_cakes(instance, filename):
    return f'cakes/{instance.cake.title}/{filename}'


def upload_flour(instance, filename):
    return f'flour/{instance.flour.title}/{filename}'
