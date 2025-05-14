from otree.api import *
import csv
import os
from django.shortcuts import render
import json
from django.utils.safestring import mark_safe


doc = """
Descriptive_Information
"""



class C(BaseConstants):
    NAME_IN_URL = 'Descriptive_Information'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
    MAX_PERIODS = 45
    CSV_FILE_PATH = os.path.normpath(
        os.path.join(
            os.path.dirname(__file__),
            '..',  # go up one directory
            '_static', 'data', 'sequence_1.csv'
        )
    )

    # Load the whole CSV data when the first page of sampling is submitted
    def load_csv_data(file_path):
        rows = []
        rf_list = []  # store risk-free data in a parallel list
        with open(file_path, newline='') as f:
            reader = csv.DictReader(f)
            for row in reader:
                sus_raw = float(row.get('Sustainable Fund', '0'))
                con_raw = float(row.get('Conventional Fund', '0'))
                rf_raw = float(row.get('R_f', '0'))  # risk-free

                # Multiply by 100 and round to 2 decimal places
                sus_pct = round(sus_raw * 100, 2)
                con_pct = round(con_raw * 100, 2)
                rf_pct = round(rf_raw * 100, 4)  # keep maybe 4 decimals for R_f

                rows.append({'R_sus': sus_pct, 'R_con': con_pct})
                rf_list.append(rf_pct)
        return rows, rf_list

    CSV_DATA, RF_DATA = load_csv_data(
        os.path.normpath(os.path.join(os.path.dirname(__file__), CSV_FILE_PATH))
    )


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    # returns for the stage 1
    R_sus1 = models.FloatField()
    R_con1 = models.FloatField()
    R_sus2 = models.FloatField()
    R_con2 = models.FloatField()
    R_sus3 = models.FloatField()
    R_con3 = models.FloatField()
    R_sus4 = models.FloatField()
    R_con4 = models.FloatField()
    R_sus5 = models.FloatField()
    R_con5 = models.FloatField()
    R_sus6 = models.FloatField()
    R_con6 = models.FloatField()
    R_sus7 = models.FloatField()
    R_con7 = models.FloatField()
    R_sus8 = models.FloatField()
    R_con8 = models.FloatField()
    R_sus9 = models.FloatField()
    R_con9 = models.FloatField()

    R_sus10 = models.FloatField()
    R_con10 = models.FloatField()
    R_sus11 = models.FloatField()
    R_con11 = models.FloatField()
    R_sus12 = models.FloatField()
    R_con12 = models.FloatField()
    R_sus13 = models.FloatField()
    R_con13 = models.FloatField()
    R_sus14 = models.FloatField()
    R_con14 = models.FloatField()
    R_sus15 = models.FloatField()
    R_con15 = models.FloatField()
    R_sus16 = models.FloatField()
    R_con16 = models.FloatField()
    R_sus17 = models.FloatField()
    R_con17 = models.FloatField()
    R_sus18 = models.FloatField()
    R_con18 = models.FloatField()

    R_sus19 = models.FloatField()
    R_con19 = models.FloatField()
    R_sus20 = models.FloatField()
    R_con20 = models.FloatField()
    R_sus21 = models.FloatField()
    R_con21 = models.FloatField()
    R_sus22 = models.FloatField()
    R_con22 = models.FloatField()
    R_sus23 = models.FloatField()
    R_con23 = models.FloatField()
    R_sus24 = models.FloatField()
    R_con24 = models.FloatField()
    R_sus25 = models.FloatField()
    R_con25 = models.FloatField()
    R_sus26 = models.FloatField()
    R_con26 = models.FloatField()
    R_sus27 = models.FloatField()
    R_con27 = models.FloatField()

    R_sus28 = models.FloatField()
    R_con28 = models.FloatField()
    R_sus29 = models.FloatField()
    R_con29 = models.FloatField()
    R_sus30 = models.FloatField()
    R_con30 = models.FloatField()
    R_sus31 = models.FloatField()
    R_con31 = models.FloatField()
    R_sus32 = models.FloatField()
    R_con32 = models.FloatField()
    R_sus33 = models.FloatField()
    R_con33 = models.FloatField()
    R_sus34 = models.FloatField()
    R_con34 = models.FloatField()
    R_sus35 = models.FloatField()
    R_con35 = models.FloatField()
    R_sus36 = models.FloatField()
    R_con36 = models.FloatField()

    R_sus37 = models.FloatField()
    R_con37 = models.FloatField()
    R_sus38 = models.FloatField()
    R_con38 = models.FloatField()
    R_sus39 = models.FloatField()
    R_con39 = models.FloatField()
    R_sus40 = models.FloatField()
    R_con40 = models.FloatField()
    R_sus41 = models.FloatField()
    R_con41 = models.FloatField()
    R_sus42 = models.FloatField()
    R_con42 = models.FloatField()
    R_sus43 = models.FloatField()
    R_con43 = models.FloatField()
    R_sus44 = models.FloatField()
    R_con44 = models.FloatField()
    R_sus45 = models.FloatField()
    R_con45 = models.FloatField()

    TR_sus0 = models.FloatField(value=100.0)
    TR_con0 = models.FloatField(value=100.0)
    TR_sus1 = models.FloatField()
    TR_con1 = models.FloatField()
    TR_sus2 = models.FloatField()
    TR_con2 = models.FloatField()
    TR_sus3 = models.FloatField()
    TR_con3 = models.FloatField()
    TR_sus4 = models.FloatField()
    TR_con4 = models.FloatField()
    TR_sus5 = models.FloatField()
    TR_con5 = models.FloatField()
    TR_sus6 = models.FloatField()
    TR_con6 = models.FloatField()
    TR_sus7 = models.FloatField()
    TR_con7 = models.FloatField()
    TR_sus8 = models.FloatField()
    TR_con8 = models.FloatField()
    TR_sus9 = models.FloatField()
    TR_con9 = models.FloatField()

    TR_sus10 = models.FloatField()
    TR_con10 = models.FloatField()
    TR_sus11 = models.FloatField()
    TR_con11 = models.FloatField()
    TR_sus12 = models.FloatField()
    TR_con12 = models.FloatField()
    TR_sus13 = models.FloatField()
    TR_con13 = models.FloatField()
    TR_sus14 = models.FloatField()
    TR_con14 = models.FloatField()
    TR_sus15 = models.FloatField()
    TR_con15 = models.FloatField()
    TR_sus16 = models.FloatField()
    TR_con16 = models.FloatField()
    TR_sus17 = models.FloatField()
    TR_con17 = models.FloatField()
    TR_sus18 = models.FloatField()
    TR_con18 = models.FloatField()

    TR_sus19 = models.FloatField()
    TR_con19 = models.FloatField()
    TR_sus20 = models.FloatField()
    TR_con20 = models.FloatField()
    TR_sus21 = models.FloatField()
    TR_con21 = models.FloatField()
    TR_sus22 = models.FloatField()
    TR_con22 = models.FloatField()
    TR_sus23 = models.FloatField()
    TR_con23 = models.FloatField()
    TR_sus24 = models.FloatField()
    TR_con24 = models.FloatField()
    TR_sus25 = models.FloatField()
    TR_con25 = models.FloatField()
    TR_sus26 = models.FloatField()
    TR_con26 = models.FloatField()
    TR_sus27 = models.FloatField()
    TR_con27 = models.FloatField()

    TR_sus28 = models.FloatField()
    TR_con28 = models.FloatField()
    TR_sus29 = models.FloatField()
    TR_con29 = models.FloatField()
    TR_sus30 = models.FloatField()
    TR_con30 = models.FloatField()
    TR_sus31 = models.FloatField()
    TR_con31 = models.FloatField()
    TR_sus32 = models.FloatField()
    TR_con32 = models.FloatField()
    TR_sus33 = models.FloatField()
    TR_con33 = models.FloatField()
    TR_sus34 = models.FloatField()
    TR_con34 = models.FloatField()
    TR_sus35 = models.FloatField()
    TR_con35 = models.FloatField()
    TR_sus36 = models.FloatField()
    TR_con36 = models.FloatField()

    TR_sus37 = models.FloatField()
    TR_con37 = models.FloatField()
    TR_sus38 = models.FloatField()
    TR_con38 = models.FloatField()
    TR_sus39 = models.FloatField()
    TR_con39 = models.FloatField()
    TR_sus40 = models.FloatField()
    TR_con40 = models.FloatField()
    TR_sus41 = models.FloatField()
    TR_con41 = models.FloatField()
    TR_sus42 = models.FloatField()
    TR_con42 = models.FloatField()
    TR_sus43 = models.FloatField()
    TR_con43 = models.FloatField()
    TR_sus44 = models.FloatField()
    TR_con44 = models.FloatField()
    TR_sus45 = models.FloatField()
    TR_con45 = models.FloatField()

    final_cumu_sus = models.FloatField(initial=1.0)
    final_average_return_sus = models.FloatField()
    final_sharpe_ratio_sus = models.FloatField()
    final_volatility_sus = models.FloatField()

    final_cumu_con = models.FloatField(initial=1.0)
    final_average_return_con = models.FloatField()
    final_sharpe_ratio_con = models.FloatField()
    final_volatility_con = models.FloatField()

    attention_2 = models.StringField(label="I regularly ride a unicorn to work.",
                                        choices=['Strongly Agree', 'Agree', 'Disagree', 'Strongly Disagree'],
                                        widget=widgets.RadioSelect)

    def map_csv_data_for_this_player(self):
        # Loop over indices 1..45 (assuming you have 45 rows in the CSV)
        for i in range(1, 45 + 1):
            # CSV_DATA[i-1] is the dictionary for row i
            row = C.CSV_DATA[i - 1]

            # Retrieve R_sus and R_con from this CSV row
            R_sus_value = row['R_sus']
            R_con_value = row['R_con']

            # Build the field names for R_sus{i}, R_con{i}, and R_port{i}
            R_sus_field = f'R_sus{i}'
            R_con_field = f'R_con{i}'

            # Assign the R_sus and R_con fields
            setattr(self, R_sus_field, R_sus_value)
            setattr(self, R_con_field, R_con_value)


    # FOR THE COMPLETE STAGE 1 DATA
    def R_sus_list(self):
        return [getattr(self, f'R_sus{i}') for i in range(1, 45 + 1)]

    def R_con_list(self):
        return [getattr(self, f'R_con{i}') for i in range(1, 45 + 1)]

    # calculate cumulative returns after each decision
    def calculate_cumulative_returns(self):
        start_period, end_period = [0, 45]

        # Initialize starting values for cumulative returns
        cumu_sus = 0.0
        cumu_con = 0.0

        # Initialize growth factors for compounding
        growth_factor_sus = 1.0
        growth_factor_con = 1.0

        # Loop through each period and calculate cumulative returns
        for i in range(start_period, end_period + 1):
            R_sus_val = getattr(self, f'R_sus{i}', 0.0)
            R_con_val = getattr(self, f'R_con{i}', 0.0)

            # Update growth factors
            growth_factor_sus *= (1 + R_sus_val / 100)
            growth_factor_con *= (1 + R_con_val / 100)

            # Calculate cumulative returns as percentages
            cumu_sus = (growth_factor_sus - 1) * 100  # Subtract 1 to get the return
            cumu_con = (growth_factor_con - 1) * 100  # Subtract 1 to get the return

            # Store cumulative return values for this period
            setattr(self, f'TR_sus{i}', round(cumu_sus, 2))
            setattr(self, f'TR_con{i}', round(cumu_con, 2))

        # Store final cumulative returns
        self.final_cumu_sus = round(cumu_sus, 2)
        self.final_cumu_con = round(cumu_con, 2)

        # Calculate average returns
    def calculate_Average_Returns (self):
        start_period, end_period = [0, 45]

        sum_sus = 0.0
        sum_con = 0.0
        count = end_period

        for i in range(1, end_period + 1):
            R_sus_val = getattr(self, f'R_sus{i}', 0.0)
            R_con_val = getattr(self, f'R_con{i}', 0.0)

            sum_sus += R_sus_val
            sum_con += R_con_val

        if count > 0:
            avg_sus = sum_sus / count
            avg_con = sum_con / count
        else:
            # If there's any odd case with zero periods
            avg_sus = 0.0
            avg_con = 0.0

        avg_sus_rounded = round(avg_sus, 2)
        avg_con_rounded = round(avg_con, 2)

        self.final_average_return_sus = avg_sus_rounded
        self.final_average_return_con = avg_con_rounded

    def calculate_Sharpe_Ratios(self):
        start_period, end_period = [0, 45]
        # If end_period=9 => periods 1..9 => we want indexes [0..8] in arrays

        if end_period <= 0:
            return  # no data?

        # Prepare lists to store decimal returns for each strategy
        sus_returns = []
        con_returns = []
        rf_returns = []

        # Loop from period=1 to end_period, but remember array indexes are [period-1]
        for period in range(1, end_period + 1):
            # R_sus{i}, R_con{i}, R_port{i} are in percentage.
            sus_val_pct = getattr(self, f'R_sus{period}', 0.0)
            con_val_pct = getattr(self, f'R_con{period}', 0.0)

            # Convert to decimal (1.23 => 0.0123)
            sus_decimal = sus_val_pct / 100
            con_decimal = con_val_pct / 100

            sus_returns.append(sus_decimal)
            con_returns.append(con_decimal)

            # risk-free for period i => index i-1
            rf_pct = C.RF_DATA[period - 1]  # e.g. 0.05 => +0.05%
            rf_decimal = rf_pct / 100  # => 0.0005
            rf_returns.append(rf_decimal)

        # Now compute Sharpe for each strategy
        # 1) Means
        def mean(vals):
            return sum(vals) / len(vals) if vals else 0.0

        avg_sus = mean(sus_returns)
        avg_con = mean(con_returns)
        avg_rf = mean(rf_returns)

        # 2) Standard deviations
        import math

        def stddev(vals):
            if len(vals) < 2:
                return 0.0
            m = mean(vals)
            var = sum((v - m) ** 2 for v in vals) / (len(vals) - 1)
            return math.sqrt(var)

        std_sus = stddev(sus_returns)
        std_con = stddev(con_returns)

        # 3) Sharpe ratio = (avgX - avgRF) / stdX
        def sharpe_ratio_proper(avg_x, avg_r, sd_x):
            if sd_x <= 1e-15:
                return 0.0
            return round((avg_x - avg_r) / sd_x, 4)

        sharpe_sus = round(sharpe_ratio_proper(avg_sus, avg_rf, std_sus), 2)
        sharpe_con = round(sharpe_ratio_proper(avg_con, avg_rf, std_con), 2)

        # 4) Store in the relevant fields
        self.final_sharpe_ratio_sus = sharpe_sus
        self.final_sharpe_ratio_con = sharpe_con
        self.final_volatility_sus = round(std_sus*100, 2)
        self.final_volatility_con = round(std_con*100, 2)


# PAGES
class Stage1(Page):
    def is_displayed(self):
        return self.participant.vars.get('treatment') in ['T1', 'T5']


class Instructions(Page):
    def is_displayed(self):
        return self.participant.vars.get('treatment') in ['T1', 'T5']

    def before_next_page(self, timeout_happened):
        self.map_csv_data_for_this_player()
        self.calculate_Average_Returns()
        self.calculate_cumulative_returns()
        self.calculate_Sharpe_Ratios()


class Belief0(Page):
    form_model = 'player'
    form_fields = ['Belief_0']
    def is_displayed(self):
        return self.participant.vars.get('treatment') in ['T1', 'T5']


class Table_Graph(Page):
    def is_displayed(self):
        return self.participant.vars.get('treatment') in ['T1', 'T5']

    def vars_for_template(self):
        sus_data = [x if x is not None else 0 for x in self.R_sus_list()]
        con_data = [x if x is not None else 0 for x in self.R_con_list()]
        # Total returns for display (TR_sus, TR_con, TR_port for periods 0-45)
        TR_sus_data = [getattr(self, f'TR_sus{i}') for i in range(0, 46)]
        TR_con_data = [getattr(self, f'TR_con{i}') for i in range(0, 46)]

        summary_data = {
            'cumulative': {
                'sus': self.final_cumu_sus,
                'con': self.final_cumu_con,
            },
            'averageReturns': {
                'sus': self.final_average_return_sus,
                'con': self.final_average_return_con,
            },
            'sharpeRatios': {
                'sus': self.final_sharpe_ratio_sus,
                'con': self.final_sharpe_ratio_con,
            },
            'volatilities': {
                'sus': self.final_volatility_sus,
                'con': self.final_volatility_con,
            },
        },
        # no projections

        return {
            'sus_data': mark_safe(json.dumps(sus_data)),  # Convert to JSON for template
            'con_data': mark_safe(json.dumps(con_data)),

            'TR_sus_data': mark_safe(json.dumps(TR_sus_data)),
            'TR_con_data': mark_safe(json.dumps(TR_con_data)),

            'summaryData': mark_safe(json.dumps(summary_data))
        }


class Attention2(Page):
    form_model = 'player'
    form_fields = ['attention_2']

    def is_displayed(self):
        return self.participant.vars.get('treatment') in ['T1', 'T5']

    @staticmethod
    def before_next_page(player, timeout_happened):
        # Store the response for attention_2
        player.participant.vars['attention_2'] = player.attention_2

        # Check if both attention_1 and attention_2 are incorrect
        attention_1_correct = player.participant.vars.get('attention_1') == 'Red'
        attention_2_correct = player.attention_2 == 'Strongly Disagree' or player.attention_2 == 'Disagree'

        if not attention_1_correct and not attention_2_correct:
            # Mark the participant as having failed the attention checks
            player.participant.vars['attention_failed'] = True


class Thank_You(Page):
    @staticmethod
    def is_displayed(player):
        # Show only if both attention checks failed
        return player.participant.vars.get('attention_failed', False) and player.participant.vars.get('treatment') in ['T1', 'T5']


page_sequence = [Stage1, Instructions, Table_Graph, Attention2]

