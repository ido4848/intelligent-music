import utilization.general_utilities.logging as logger


def apply_carefully(items, func, verbose=True):
    products = []

    for item in items:
        try:
            products.append(func(item))
        except Exception as e:
            if verbose:
                logger.log("Could not apply {} on {} with error {}".format(func, item, e))

    return products
