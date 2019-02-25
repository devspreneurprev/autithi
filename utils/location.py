def upload_location(instance, filename):
    PostModel = instance.__class__
    try:
        new_id = PostModel.objects.order_by("id").last().id + 1
    except AttributeError:  # no folder in database
        new_id = 1
    return "%s/%s" % (new_id, filename)
    