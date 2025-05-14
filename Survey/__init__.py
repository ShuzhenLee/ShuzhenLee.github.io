from otree.api import *
import random

doc = """
Survey
"""



class C(BaseConstants):
    NAME_IN_URL = 'Survey'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
    EXCHANGE_RATE = 0.002  # 500 ECUs = 1 GBP
    PARTICIPATION_FEE = 2  # GBP
    # Correct answers
    # GREEN_CORRECT_ANSWERS = {
    #     "green_1": "B",
    #     "green_2": "B",
    #     "green_3": "A",
    #     "green_4": "A",
    #     "green_5": "D",
    # }
    FIN_CORRECT_ANSWERS = {
        "compounding": "A",
        "inflation": "C",
        "diversification": "B",
    }


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    all_payoff = models.FloatField(label='Total payoff')
    final_donation = models.FloatField(label='final donation = portfolio donation + sustainability pref donation')
    invest_payoff = models.FloatField(label='investment payoff')
    bonus1_sus_donation = models.FloatField(label='keep xx out of 1 pound not donated')
    sus_donation_implemented = models.BooleanField(label='sustainability preference donation implemented')
    bonus2_fixed_plan = models.FloatField(label='Fixed Plan bonus - keep xx out of 50 pence not to buy fixed plan')
    selected_stage = models.IntegerField()


    # Demographics
    age = models.IntegerField(label='What is your age?', min=18, max=100)
    gender = models.StringField(label='What is your gender?', choices=['Female', 'Male', 'Other'])
    employment = models.StringField(label='What is your employment status?',
                                    choices=['Employed', 'Unemployed', 'Student', 'Retired', 'Other'])
    education = models.StringField(label='What is the highest level of education you have completed?', drop_down=True,
                                    choices=['No qualifications',
                                             'Level 1 (One to four GCSE passes, or equivalent)',
                                             'Level 2 (Five or more GCSE passes, or equivalent)',
                                             'Apprenticeships',
                                             'Level 3 (Two or more A Levels, or equivalent)',
                                             'Level 4a: Degree (BA, BSc)',
                                             'Level 4b: Higher Degree (MA, PhD, PGCE)',
                                             'Level 4c: Other Higher Qualifications (e.g. NVQ level 4 to 5, HND, BTEC)',
                                             'Other'])
    income = models.StringField(label='What was the annual disposable income (income after direct tax) of your household in 2024?', drop_down=True,
                                    choices=['Less than £16,400', # bottom (income quintile)
                                             'between £16,400 - £26,100', # 2nd
                                             'between £26,100 - £34,500', # 3rd
                                             'between £34,500 - £45,700',# 4th
                                             'between £45,700 - £68,400',# top
                                             ' More than £68,400'])
    investment = models.StringField(label='Do you have any investments in the stock market or other financial markets?',
                                    choices=['Yes', 'No'])
    investment_amount = models.StringField(
        label='What is the approximate amount of your investments? (in GBP)',
        blank=True  # Allow blank responses for participants who answered "No" to the first question
    )

    # Green Literacy
    # # Need to check exact names and add incentives
    # green_1 = models.StringField(
    #         label="A low-energy (CFL or LED) lightbulb costs more than a regular lightbulb but uses less energy. About how long does one last?",
    #         choices=[["A", "About the same as a regular lightbulb"], ["B", "About 10 times as long as a regular lightbulb"],
    #                  ["C", "About 100 times as long as a regular lightbulb"], ["D", "Don’t know/Prefer not to say"]],
    #         widget=widgets.RadioSelect)
    # green_2 = models.StringField(
    #         label="The ozone layer filters what harmful substances?",
    #         choices=[["A", "Acid rain"], ["B", "UV radiation"], ["C", "Sewage gas"],
    #                  ["D", "The Greenhouse Effect"], ["E", "Don’t know/Prefer not to say"]],
    #         widget=widgets.RadioSelect)
    # green_3 = models.StringField(
    #         label="According to the UN, around 30% of the world’s food is lost each year. When does this loss occur?",
    #         choices=[["A", "Most food is lost before it reaches the supermarket"],
    #                  ["B", "Most food is discarded at the supermarket before it is sold"],
    #                  ["C", "Most food is wasted after it is purchased from the supermarket"],
    #                  ["D", "Don’t know/Prefer not to say"]],
    #         widget=widgets.RadioSelect)
    # green_4 = models.StringField(
    #         label="Is the world spending more energy on heating homes or cooling them?",
    #         choices=[["A", "More energy on heating"],
    #                  ["B", "More energy on cooling"],
    #                  ["C", "About the same amount on both"],
    #                  ["D", "Don’t know/Prefer not to say"]],
    #         widget=widgets.RadioSelect)
    # green_5 = models.StringField(
    #         label="Why don’t polar bears eat penguins?",
    #         choices=[["A", "They have both been driven out of their natural environment"],
    #                  ["B", "Polar bears do not eat meat"],
    #                  ["C", "Penguins are only active when polar bears hibernate"],
    #                  ["D", "None of the above"],
    #                  ["E", "Don’t know/Prefer not to say"]],
    #         widget=widgets.RadioSelect)

    # Financial Literacy
    compounding = models.StringField(
            label="Suppose you had £100 in a savings account and the interest rate was 2 percent per year. "
                  "After 5 years, how much do you think you would have in the account if you left the money to grow?",
            choices=[["A", "More than £102"], ["B", "Exactly £102"],
                     ["C", "Less than £102"], ["D", "Don’t know"], ["E", "Prefer not to say"]],
            widget=widgets.RadioSelect)
    inflation = models.StringField(
            label="Imagine that the interest rate on your savings account was 1 percent per year and inflation was 2 percent per year. "
                  "After 1 year, would you be able to buy:",
            choices=[["A", "More than today with the money in this account"],
                     ["B", "The same as today with the money in this account"],
                     ["C", "Less than today with the money in this account"],
                     ["D", "Don’t know"], ["E", "	Prefer not to say"]],
            widget=widgets.RadioSelect)
    diversification = models.StringField(
        label="Do you think that the following statement is true or false? "
              "\"Buying a single company stock usually provides a safer return than a stock mutual fund.\"",
        choices=[["A", "True"], ["B", "False"],
                 ["C", "Don’t know"], ["D", "Prefer not to say"]],
        widget=widgets.RadioSelect
    )

    # Sustainability Preference
    clean_planet = models.IntegerField(
            label="1.	A clean planet is more important to me than financial welfare.",
            choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5'], [6, 'Prefer not to say']],
            widget=widgets.RadioSelectHorizontal)
    higher_return = models.IntegerField(
            label="2.	Environmentally sustainable investments generate higher returns in the long run.",
            choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5'], [6, 'Prefer not to say']],
            widget=widgets.RadioSelectHorizontal)
    higher_cost = models.IntegerField(
            label="3.	I’m willing to pay higher fees for a fund that only makes sustainable investments.",
            choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5'], [6, 'Prefer not to say']],
            widget=widgets.RadioSelectHorizontal)
    green_product = models.IntegerField(
            label="4.	I am willing to pay more for environmentally friendly products.",
            choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5'], [6, 'Prefer not to say']],
            widget=widgets.RadioSelectHorizontal)
    recycle_more = models.IntegerField(
            label="5.	I recycle a great deal more than my neighbors.",
            choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5'], [6, 'Prefer not to say']],
            widget=widgets.RadioSelectHorizontal)


    # Risk and Social Preference
    risk = models.IntegerField(
            label="1.	How willing are you to take risks?",
            choices=[ [1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5'],
                     [6, '6'], [7, '7'], [8, '8'], [9, '9'], [10, '10']],
            widget=widgets.RadioSelectHorizontal)
    time_pref = models.IntegerField(
            label="2.	How willing are you to give up something that is beneficial for you today in order to benefit more from that in the future?",
            choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5'],
                     [6, '6'], [7, '7'], [8, '8'], [9, '9'], [10, '10']],
            widget=widgets.RadioSelectHorizontal)
    # social_pref_fair = models.IntegerField(
    #         label="3.	How willing are you to punish someone who treats YOU unfairly, even if there may be costs for you?",
    #         choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5'],
    #                  [6, '6'], [7, '7'], [8, '8'], [9, '9'], [10, '10']],
    #         widget=widgets.RadioSelectHorizontal)
    # social_pref_fair_2 = models.IntegerField(
    #         label="4.	How willing are you to punish someone who treats OTHERS unfairly, even if there may be costs for you?",
    #         choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5'],
    #                  [6, '6'], [7, '7'], [8, '8'], [9, '9'], [10, '10']],
    #         widget=widgets.RadioSelectHorizontal)
    social_pref_altru = models.IntegerField(
            label="3.	How willing are you to give to good causes without expecting anything in return?",
            choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5'],
                     [6, '6'], [7, '7'], [8, '8'], [9, '9'], [10, '10']],
            widget=widgets.RadioSelectHorizontal)
    # social_pref_recip = models.IntegerField(
    #         label="6.	When someone does me a favor, I am willing to return it.",
    #         choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5'],
    #                  [6, '6'], [7, '7'], [8, '8'], [9, '9'], [10, '10']],
    #         widget=widgets.RadioSelectHorizontal)
    # social_pref_revenge = models.IntegerField(
    #         label="7.	If I am treated very unjustly, I will take revenge at the first occasion, even if there is a cost to do so.",
    #         choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5'],
    #                  [6, '6'], [7, '7'], [8, '8'], [9, '9'], [10, '10']],
    #         widget=widgets.RadioSelectHorizontal)
    # social_pref_trust = models.IntegerField(
    #         label="8.	I assume that people have only the best intentions.",
    #         choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5'],
    #                  [6, '6'], [7, '7'], [8, '8'], [9, '9'], [10, '10']],
    #         widget=widgets.RadioSelectHorizontal)

    correct_green_literacy = models.IntegerField(initial=0)
    correct_financial_literacy = models.IntegerField(initial=0)
    total_correct_number = models.IntegerField(initial=0)
    gbp_payment = models.FloatField(initial=0)


    # Calculate correct answers
    def calculate_correct_answers(self):
        # self.correct_green_literacy = sum(
        #     1 for key, correct_answer in C.GREEN_CORRECT_ANSWERS.items()
        #     if getattr(self, key) == correct_answer
        # )
        self.correct_financial_literacy = sum(
            1 for key, correct_answer in C.FIN_CORRECT_ANSWERS.items()
            if getattr(self, key) == correct_answer
        )
        self.total_correct_number = self.correct_financial_literacy
        # self.total_correct_number = self.correct_green_literacy + self.correct_financial_literacy
        self.gbp_payment = self.total_correct_number * 0.2  # Payment per correct answer


# PAGES
class Stage4(Page):
    pass


class Instruction(Page):
    pass


class DemographicsOne(Page):
    form_model = 'player'
    form_fields = ['age', 'gender', 'employment', 'education', 'income', 'investment', 'investment_amount']


# class Green_Literacy(Page):
#     form_model = 'player'
#     form_fields = ['green_1', 'green_2', 'green_3', 'green_4', 'green_5']


class Financial_Literacy(Page):
    form_model = 'player'
    form_fields = ['compounding', 'inflation', 'diversification']

    def before_next_page(player, timeout_happened):
        player.calculate_correct_answers()


class Sustainability_Preference(Page):
    form_model = 'player'
    form_fields = ['clean_planet', 'higher_return', 'higher_cost', 'green_product', 'recycle_more']



class Risk_and_Social_Preference(Page):
    form_model = 'player'
    form_fields = ['risk', 'time_pref', 'social_pref_altru']

    def before_next_page(player, timeout_happened):
        player.participant.vars['treatment_completed'] = True

class End(Page):
    def vars_for_template(player):
        # If selected_stage is not already set, assign it
        if 'selected_stage' not in player.participant.vars:
            player.participant.vars['selected_stage'] = random.choice([3, 4])

        # Use the stored selected_stage
        player.selected_stage = player.participant.vars['selected_stage']

        # Retrieve stored investment payoffs and donations
        part3_invest_payoff = round(player.participant.vars.get('payoff_real_invest', 0), 2)
        part3_donation = round(player.participant.vars.get('part3_donation', 0), 2)
        part4_invest_payoff = round(player.participant.vars.get('payoff_new_chance', 0), 2)
        part4_donation = round(player.participant.vars.get('donation_new_chance', 0), 2)

        # Determine the final donation and investment payoff based on the chosen payoff source
        if player.selected_stage == 3:
            selected_donation = part3_donation
            selected_invest_payoff = part3_invest_payoff
        else:
            selected_donation = part4_donation
            selected_invest_payoff = part4_invest_payoff

        # Always apply investment payoff
        player.invest_payoff = round(selected_invest_payoff * C.EXCHANGE_RATE, 2)

        # Base payoff before bonuses
        base = player.invest_payoff + player.gbp_payment

        # Check if treatment contains "normal_labelling"
        treatment_name = player.session.config.get('name', '').lower()
        no_donation = "normal_labelling" in treatment_name

        # Initialize final_donation and sus_donation_implemented
        player.final_donation = 0
        player.sus_donation_implemented = False
        player.bonus1_sus_donation = 0

        # Apply sustainability donation and bonus with 10% chance (if not in no-donation treatment)
        sus = player.participant.vars.get('susPref_donation')
        if not no_donation and sus is not None:
            random_value = random.random()
            print(f"Generated random value: {random_value}")
            if random_value < 0.1:
                player.sus_donation_implemented = True
                player.final_donation = round(selected_donation * C.EXCHANGE_RATE, 2) + sus/100
                player.bonus1_sus_donation = 1 - sus / 100  # keep x out of 1 pound
                base += player.bonus1_sus_donation

        # T7 fixed plan bonus
        wtp = player.participant.vars.get('wtp', 0)
        fixed = player.participant.vars.get('fixed_plan', False)
        bonus2 = 0
        if player.participant.vars.get('treatment') == 'T7':
            if fixed:
                bonus2 = 0.5 - (wtp / 100)
            else:
                bonus2 = 0.5
        player.bonus2_fixed_plan = bonus2

        player.all_payoff = round(base + bonus2, 2)

        return {
            'part4_donation': part4_donation,
            'part4_invest_payoff': part4_invest_payoff,
            'part3_donation': part3_donation,
            'part3_invest_payoff': part3_invest_payoff,
            'selected_stage': player.selected_stage,
            'invest_payoff': player.invest_payoff,
            'final_donation': player.final_donation,
            "no_donation": no_donation,
            'bonuses': player.participant.vars.get('bonuses'),
            'correct_financial_literacy': player.correct_financial_literacy,
            'total_correct_number': player.total_correct_number,
            'gbp_payment': round(player.gbp_payment, 2),
        }



page_sequence = [Stage4, Instruction, DemographicsOne, Financial_Literacy,
                 Sustainability_Preference,
                 Risk_and_Social_Preference,
                 End]
