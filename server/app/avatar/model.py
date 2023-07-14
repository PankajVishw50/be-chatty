from multiavatar.multiavatar import multiavatar


def generate_multiavatar(id):
    """Returns svg of avatar

    :param id: string
    :return: svg
    """
    return multiavatar(id, None, None)
