from otree.api import *

import random

doc = """
Choice between Fixed and Adjustable Investment Plans
"""


# Constants
class C(BaseConstants):
    NAME_IN_URL = 'Choice'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
    MAX_PRICE = 50  # Maximum possible random price (in pence)


# Models
class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    wtp = models.IntegerField(
        label='Willingness to pay for the Fixed Plan (in pence)',
        min=0, max=C.MAX_PRICE
    )
    random_price = models.IntegerField()  # Random price between 0 and 50
    fixed_plan = models.BooleanField()  # True if player gets Fixed Plan, False if Adjustable Plan

    def set_plan(self):
        """Generate random price and determine which plan is implemented."""
        self.random_price = random.randint(0, C.MAX_PRICE)  # Generate random price between 0 and 50
        self.fixed_plan = self.wtp >= self.random_price  # Compare and assign the plan

        # Store values in participant.vars
        self.participant.vars['wtp'] = self.wtp
        self.participant.vars['fixed_plan'] = self.fixed_plan

# Pages
class Choice(Page):
    form_model = 'player'
    form_fields = ['wtp']
    def is_displayed(self):
        return self.participant.vars.get('treatment') in ['T7']

    def before_next_page(self, timeout_happened):
        """Set the random price and determine plan assignment before moving to the next page."""
        self.set_plan()


class Result(Page):
    def is_displayed(self):
        return self.participant.vars.get('treatment') in ['T7']

    @staticmethod
    def vars_for_template(player: Player):
        return {
            "random_price": player.random_price,
            "wtp": player.wtp,
            "fixed_plan": "Fixed Plan" if player.fixed_plan else "Adjustable Plan",
        }

    def app_after_this_page(self, upcoming_apps):
        """Redirect to Fix_App if the player chose Fixed Plan, otherwise redirect to Flex_App."""
        if self.fixed_plan:
            return "FIX_Real_Investment"
        else:
            return "FLEX_Real_Investment"


page_sequence = [Choice, Result]

