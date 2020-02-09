from .intake import ReferralFactory


# def create_pending_clients(factory.):


def populate_fake_db(factory=ReferralFactory, size=25):
    """
        Helper function to create fake Models instances.
    """

    factory.create_batch(size)


def delete_factory_inventory(factory=ReferralFactory):

    model = factory._meta.model
    inventory = model.objects.all()
    for each in inventory:
        each.delete()

    return f'{len(inventory)} objects deleted'