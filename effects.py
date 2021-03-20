# I
import main


def health_effect(amount, add, effect_on):
    """
    :param effect_on: str
    :param amount: int
    :param add: boolean
    :return:
    """
    for point in range(amount):
        if add:
            if effect_on.currentlifespan < effect_on.maxlifespan:
                effect_on.currentlifespan = effect_on.currentlifespan + 1
            if effect_on.currentlifespan > effect_on.maxlifespan:
                effect_on.currentlifespan = effect_on.maxlifespan
        else:
            effect_on.currentlifespan = effect_on.currentlifespan - 1
