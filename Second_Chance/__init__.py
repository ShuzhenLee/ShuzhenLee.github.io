from otree.api import *
import csv
import os
import random

doc = """
Your app description
"""

# Constants
class C(BaseConstants):
    NAME_IN_URL = 'SecondChance'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
    MAX_PERIODS = 45
    CSV_FILE_PATH = os.path.join('_static', 'data', 'sequence_4.csv')


# Models
class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    payoff_new_chance = models.FloatField()
    donation_new_chance = models.FloatField()

    second_allocation = models.IntegerField()
    est_con_3 = models.FloatField(label="estimation #3 of conventional fund average return %", min=-100.0)
    est_sus_3 = models.FloatField(label="estimation #3 of sustainable fund average return %", min=-100.0)
    belief_bonus_B3 = models.FloatField()

    second_chance_avg_sus = models.FloatField()
    second_chance_avg_con = models.FloatField()


    second_chance_cumu_sus = models.FloatField(initial=100.0)  # Initialize to 100
    second_chance_cumu_con = models.FloatField(initial=100.0)  # Initialize to 100
    second_chance_cumu_portfolio = models.FloatField(initial=100.0)  # Initialize to 100


    # Method to calculate cumulative returns
    def calculate_cumulative_returns(self):
        second_allocation = self.second_allocation
        cumulative_sustainable = 100.0  # Start cumulative returns at 100
        cumulative_conventional = 100.0  # Start cumulative returns at 100
        cumulative_portfolio = 100.0  # Start cumulative returns at 100
        total_sus = 0.0
        total_con = 0.0
        count = 0  # To count the number of periods

        # Read CSV and calculate cumulative returns
        with open(C.CSV_FILE_PATH, newline='') as csvfile:
            reader = csv.DictReader(csvfile)

            # Adjusted to start period indexing from 1
            for i, row in enumerate(reader, start=1):
                try:
                    # Convert returns to float and handle any potential formatting issues
                    sustainable_return = float(row['Sustainable Fund'].strip())
                    conventional_return = float(row['Conventional Fund'].strip())
                except ValueError:
                    print(f"Error in data format at period {i}. Check the CSV values.")
                    continue

                # Calculate cumulative returns without rounding for funds and portfolio
                cumulative_sustainable *= (1 + sustainable_return)
                cumulative_conventional *= (1 + conventional_return)
                total_sus += sustainable_return
                total_con += conventional_return
                count += 1

                # Update cumulative returns
                portfolio_return = (second_allocation / 100) * sustainable_return + \
                                   ((100 - second_allocation) / 100) * conventional_return
                cumulative_portfolio *= (1 + portfolio_return)

        # Set cumulative values rounded to 2 decimal places
        self.second_chance_cumu_sus = round(cumulative_sustainable-100, 2)
        self.second_chance_cumu_con = round(cumulative_conventional-100, 2)
        self.second_chance_cumu_portfolio = round(cumulative_portfolio-100, 2)

        # Calculate and store average returns
        self.second_chance_avg_sus = 100*round(total_sus / count, 2)
        self.second_chance_avg_con = 100*round(total_con / count, 2)



# Pages
class Stage3(Page):
    def is_displayed(self):
        return self.participant.vars.get('treatment') in ['T1', 'T2', 'T5', 'T6', 'T7']


# class Belief3(Page):
#     form_model = 'player'
#     form_fields = ['est_con_3', 'est_sus_3']


class SecondChance(Page):
    form_model = 'player'
    form_fields = ['second_allocation', 'est_con_3', 'est_sus_3']
    def is_displayed(self):
        return self.participant.vars.get('treatment') in ['T1', 'T2', 'T5', 'T6', 'T7']

    def vars_for_template(player):
        # Check the session name to determine the value of frac
        treatment_name = player.session.config['name']
        if treatment_name == 'Treatment_5_Descriptive_FIX_Sustainable' or 'Treatment_6_Demo_Account_FIX_Sustainable':
            num_decision = 1
        else:
            num_decision = 5

        return {
            'decision4': player.participant.vars.get('decision4', None),
            'con_decision4': 100 - player.participant.vars.get('decision4', 0),

            'fix_decision': player.participant.vars.get('fix_decision', None),  # Previous decision
            'con_fix': 100 - player.participant.vars.get('fix_decision', 0),

            'num_decision': num_decision,
        }

    def before_next_page(player, timeout_happened):
        player.calculate_cumulative_returns()

        # Retrieve the estimated and actual average returns
        actual_sus = player.second_chance_avg_sus
        actual_con = player.second_chance_avg_con
        est_sus = player.est_sus_3
        est_con = player.est_con_3

        # Define the margin for bonus eligibility
        margin = 5.0  # ±5%
        # Initialize bonus
        player.belief_bonus_B3 = 0

        # Check if the estimations are within ±5% of actual returns
        if abs(est_sus - actual_sus) <= margin:
            player.belief_bonus_B3 += 0.50
        if abs(est_con - actual_con) <= margin:
            player.belief_bonus_B3 += 0.50

        # Store bonus in participant vars
        player.participant.vars['belief_bonus'] += round(player.belief_bonus_B3, 2)
        # Store the second allocation payoff in participant vars
        player.payoff_new_chance = round(100 + player.second_chance_cumu_portfolio,2)
        player.participant.vars['payoff_new_chance'] = player.payoff_new_chance
        # Store the second allocation donation in participant vars
        # player.participant.vars['donation_new_chance'] = round( player.second_allocation + (player.second_chance_cumu_sus * player.second_allocation/100), 2)
        player.donation_new_chance = round(player.second_allocation + (player.second_chance_cumu_sus * player.second_allocation / 100), 2)
        # Store it in participant.vars for later use
        player.participant.vars['donation_new_chance'] = player.donation_new_chance


class Result(Page):
    def is_displayed(self):
        return self.participant.vars.get('treatment') in ['T1', 'T2', 'T5', 'T6', 'T7']

    def vars_for_template(player):
        return {
            'second_allocation': player.second_allocation,
            'second_allocation_con': 100 - player.second_allocation,
            'cumu_sus': player.second_chance_cumu_sus,
            'cumu_con': player.second_chance_cumu_con,
            'cumu_portfolio': player.second_chance_cumu_portfolio,

        }


page_sequence = [Stage3, SecondChance, Result]
