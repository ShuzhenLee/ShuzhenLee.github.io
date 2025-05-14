from otree.api import *
import random
import re
import logging

doc = """
General Instructions session2
"""



class C(BaseConstants):
    NAME_IN_URL = 'Instructions_session2'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


def creating_session(self):
    for p in self.get_players():
        p.participant.label = self.session.config.get('participant_label', None)


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    consent = models.BooleanField(label="Do you consent to this study?",
                                  choices=[[True, 'Yes, I consent.'], [False, 'No, I do not consent.']])
    is_mobile = models.BooleanField()
    green_charity = models.StringField(
        choices=['World Wide Fund for Nature(WWF-UK)', 'The Woodland Trust', 'BirdLife International'],
        widget=widgets.RadioSelect,
        label="Please indicate which is your MOST preferred environmental organization."
    )
    susPref_donation = models.FloatField(
            label="How much would you like to donate to the selected environmental organization?",
            min=0, max=100, initial=0)
    treatment = models.StringField(blank=True)  # blank=True allows it to be empty initially
    attention_1 = models.StringField(label="Lucy is wearing a red dress. What color is Lucy wearing?",
                                        choices=['Blue', 'Green', 'Red', 'Yellow'],
                                        widget=widgets.RadioSelect)


# PAGES
class Consent(Page):
    form_model = 'player'
    form_fields = ['consent', 'is_mobile']

    @staticmethod
    def before_next_page(player, timeout_happened):
        player.participant.vars['consent'] = player.consent

    @staticmethod
    def error_message(player, values):
        if values['is_mobile']:
            return "Sorry, this study cannot be conducted on a phone."


class General_Instructions(Page):
    # @staticmethod
    # def is_displayed(player):
    #     return player.participant.vars.get('consent', False)

    @staticmethod
    def before_next_page(player, timeout_happened):
        if 'treatment' not in player.participant.vars:
            session_name = player.session.config['name']
            treatment = None
            # Extract treatment based on session name
            if session_name == 'Treatment_5_Descriptive_FIX_Sustainable':
                treatment = 'T5'
                player.participant.vars['treatment'] = treatment
                player.treatment = treatment
                logging.info(f"Participant {player.participant.code} assigned to treatment: {treatment}")
            elif session_name == 'Treatment_6_Demo_Account_FIX_Sustainable':
                treatment = 'T6'
                player.participant.vars['treatment'] = treatment
                player.treatment = treatment
                logging.info(f"Participant {player.participant.code} assigned to treatment: {treatment}")
            elif session_name == 'Treatment_7_Demo_Account_CHOICE_Sustainable':
                treatment = 'T7'
                player.participant.vars['treatment'] = treatment
                player.treatment = treatment
                logging.info(f"Participant {player.participant.code} assigned to treatment: {treatment}")
            else:
                treatments = ['T5', 'T6', 'T7']
                max_per_treatment = player.session.config.get('max_per_treatment')
                completed_counts = {t: 0 for t in treatments}

                for participant in player.session.get_participants():
                    t = participant.vars.get('treatment')
                    if t in treatments and participant.vars.get('treatment_completed'):
                        completed_counts[t] += 1

                available_treatments = [t for t in treatments if completed_counts[t] < max_per_treatment]

                if not available_treatments:
                    assigned = random.choice(treatments)
                    print("All treatments are full. Randomly assigned:", assigned)
                else:
                    # Count how many already assigned in this session
                    assigned_so_far = [p.vars.get('treatment') for p in player.session.get_participants()
                                       if p.vars.get('treatment') in available_treatments]
                    assigned = available_treatments[len(assigned_so_far) % len(available_treatments)]

                player.participant.vars['treatment'] = assigned
                player.treatment = assigned
                print(f"Participant {player.participant.code} assigned to treatment: {assigned}")


class Thank_You(Page):
    @staticmethod
    def is_displayed(player):
        # Display only if the participant did NOT consent
        return not player.participant.vars.get('consent', False)


class Green_Charity(Page):
    form_model = 'player'
    form_fields = ['green_charity']

    @staticmethod
    def before_next_page(player, timeout_happened):
        player.participant.vars['green_charity'] = player.green_charity


class susPref_donation(Page):
    form_model = 'player'
    form_fields = ['susPref_donation']

    def vars_for_template(self):
        selected_charity = self.participant.vars.get('green_charity')
        return {
            'selected_charity': selected_charity
        }

    def before_next_page(player, timeout_happened):
        player.participant.vars['susPref_donation'] = player.susPref_donation


class Attention1(Page):
    form_model = 'player'
    form_fields = ['attention_1']

    @staticmethod
    def before_next_page(player, timeout_happened):
        player.participant.vars['attention_1'] = player.attention_1


page_sequence = [Consent, Thank_You, General_Instructions, Green_Charity, susPref_donation, Attention1]
