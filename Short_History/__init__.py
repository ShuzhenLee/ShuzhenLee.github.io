from otree.api import *
import csv
import os
from django.shortcuts import render
import json
from django.utils.safestring import mark_safe


doc = """
Short_History
"""



class C(BaseConstants):
    NAME_IN_URL = 'Short_History'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
    MAX_PERIODS = 10

    CSV_FILE_PATH_HISTORY = os.path.normpath(
        os.path.join(
            os.path.dirname(__file__),
            '..',  # go up one directory
            '_static', 'data', 'sequence_ShortHistory.csv'
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

    PAST_CSV_DATA, PAST_RF_DATA = load_csv_data(
        os.path.normpath(os.path.join(os.path.dirname(__file__), CSV_FILE_PATH_HISTORY))
    )


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    Belief_0 = models.StringField(
            label="Compared to the Conventional Fund, I expect the returns of the Sustainable Fund to be, in general: ",
            choices=[["A", "Much lower"], ["B", "A bit lower"],
                     ["C", "The same"], ["D", "A bit higher"],
                     ["E", "Much higher"], ["F", "I do not know"]],
            widget=widgets.RadioSelect)

    # past returns for short history
    past_R_sus1 = models.FloatField()
    past_R_con1 = models.FloatField()
    past_R_sus2 = models.FloatField()
    past_R_con2 = models.FloatField()
    past_R_sus3 = models.FloatField()
    past_R_con3 = models.FloatField()
    past_R_sus4 = models.FloatField()
    past_R_con4 = models.FloatField()
    past_R_sus5 = models.FloatField()
    past_R_con5 = models.FloatField()
    past_R_sus6 = models.FloatField()
    past_R_con6 = models.FloatField()
    past_R_sus7 = models.FloatField()
    past_R_con7 = models.FloatField()
    past_R_sus8 = models.FloatField()
    past_R_con8 = models.FloatField()
    past_R_sus9 = models.FloatField()
    past_R_con9 = models.FloatField()
    past_R_sus10 = models.FloatField()
    past_R_con10 = models.FloatField()
    # past cumulative returns for short history
    past_TR_sus0 = models.FloatField(value=100.0)
    past_TR_con0 = models.FloatField(value=100.0)
    past_TR_sus1 = models.FloatField()
    past_TR_con1 = models.FloatField()
    past_TR_sus2 = models.FloatField()
    past_TR_con2 = models.FloatField()
    past_TR_sus3 = models.FloatField()
    past_TR_con3 = models.FloatField()
    past_TR_sus4 = models.FloatField()
    past_TR_con4 = models.FloatField()
    past_TR_sus5 = models.FloatField()
    past_TR_con5 = models.FloatField()
    past_TR_sus6 = models.FloatField()
    past_TR_con6 = models.FloatField()
    past_TR_sus7 = models.FloatField()
    past_TR_con7 = models.FloatField()
    past_TR_sus8 = models.FloatField()
    past_TR_con8 = models.FloatField()
    past_TR_sus9 = models.FloatField()
    past_TR_con9 = models.FloatField()
    past_TR_sus10 = models.FloatField()
    past_TR_con10 = models.FloatField()
    # past statistics for short history
    past_final_cumu_sus = models.FloatField(initial=1.0)
    past_final_average_return_sus = models.FloatField()
    past_final_sharpe_ratio_sus = models.FloatField()
    past_final_volatility_sus = models.FloatField()

    past_final_cumu_con = models.FloatField(initial=1.0)
    past_final_average_return_con = models.FloatField()
    past_final_sharpe_ratio_con = models.FloatField()
    past_final_volatility_con = models.FloatField()

    def map_csv_data_for_this_player(self):
        for j in range(1, 11):
            past_row = C.PAST_CSV_DATA[j - 1]  # Get the correct row

            # Correctly retrieve the right keys from the CSV data
            past_R_sus_value = past_row['R_sus']
            past_R_con_value = past_row['R_con']

            # Assign values dynamically to the player's fields
            setattr(self, f'past_R_sus{j}', past_R_sus_value)
            setattr(self, f'past_R_con{j}', past_R_con_value)


    # FOR THE SHORT HISTORY DATA
    def past_R_sus_list(self):
        return [getattr(self, f'past_R_sus{i}') for i in range(1, 11)]

    def past_R_con_list(self):
        return [getattr(self, f'past_R_con{i}') for i in range(1, 11)]

    # calculate cumulative returns after each decision
    def calculate_past_cumulative_returns(self):
        start_period, end_period = [0, 10]

        # Initialize starting values for cumulative returns
        past_cumu_sus = 0.0
        past_cumu_con = 0.0

        # Initialize growth factors for compounding
        past_growth_factor_sus = 1.0
        past_growth_factor_con = 1.0

        # Loop through each period and calculate cumulative returns
        for i in range(start_period, end_period + 1):
            past_R_sus_val = getattr(self, f'past_R_sus{i}', 0.0)
            past_R_con_val = getattr(self, f'past_R_con{i}', 0.0)

            # Update growth factors
            past_growth_factor_sus *= (1 + past_R_sus_val / 100)
            past_growth_factor_con *= (1 + past_R_con_val / 100)

            # Calculate cumulative returns as percentages
            past_cumu_sus = (past_growth_factor_sus - 1) * 100  # Subtract 1 to get the return
            past_cumu_con = (past_growth_factor_con - 1) * 100  # Subtract 1 to get the return

            # Store cumulative return values for this period
            setattr(self, f'past_TR_sus{i}', round(past_cumu_sus, 2))
            setattr(self, f'past_TR_con{i}', round(past_cumu_con, 2))

        # Store final cumulative returns
        self.past_final_cumu_sus = round(past_cumu_sus, 2)
        self.past_final_cumu_con = round(past_cumu_con, 2)

        # Calculate average returns
    def calculate_past_Average_Returns (self):
        start_period, end_period = [0, 10]

        past_sum_sus = 0.0
        past_sum_con = 0.0
        past_count = end_period

        for i in range(1, end_period + 1):
            past_R_sus_val = getattr(self, f'past_R_sus{i}', 0.0)
            past_R_con_val = getattr(self, f'past_R_con{i}', 0.0)

            past_sum_sus += past_R_sus_val
            past_sum_con += past_R_con_val

        if past_count > 0:
            past_avg_sus = past_sum_sus / past_count
            past_avg_con = past_sum_con / past_count
        else:
            # If there's any odd case with zero periods
            past_avg_sus = 0.0
            past_avg_con = 0.0

        past_avg_sus_rounded = round(past_avg_sus, 2)
        past_avg_con_rounded = round(past_avg_con, 2)

        self.past_final_average_return_sus = past_avg_sus_rounded
        self.past_final_average_return_con = past_avg_con_rounded

    def calculate_past_Sharpe_Ratios(self):
        start_period, end_period = [0, 10]
        # If end_period=9 => periods 1..9 => we want indexes [0..8] in arrays

        if end_period <= 0:
            return  # no data?

        # Prepare lists to store decimal returns for each strategy
        past_sus_returns = []
        past_con_returns = []
        past_rf_returns = []

        # Loop from period=1 to end_period, but remember array indexes are [period-1]
        for period in range(1, end_period + 1):
            # R_sus{i}, R_con{i}, R_port{i} are in percentage.
            past_sus_val_pct = getattr(self, f'past_R_sus{period}', 0.0)
            past_con_val_pct = getattr(self, f'past_R_con{period}', 0.0)

            # Convert to decimal (1.23 => 0.0123)
            past_sus_decimal = past_sus_val_pct / 100
            past_con_decimal = past_con_val_pct / 100

            past_sus_returns.append(past_sus_decimal)
            past_con_returns.append(past_con_decimal)

            # risk-free for period i => index i-1
            past_rf_pct = C.PAST_RF_DATA[period - 1]  # e.g. 0.05 => +0.05%
            past_rf_decimal = past_rf_pct / 100  # => 0.0005
            past_rf_returns.append(past_rf_decimal)

        # Now compute Sharpe for each strategy
        # 1) Means
        def mean(vals):
            return sum(vals) / len(vals) if vals else 0.0

        past_avg_sus = mean(past_sus_returns)
        past_avg_con = mean(past_con_returns)
        past_avg_rf = mean(past_rf_returns)

        # 2) Standard deviations
        import math

        def stddev(vals):
            if len(vals) < 2:
                return 0.0
            m = mean(vals)
            var = sum((v - m) ** 2 for v in vals) / (len(vals) - 1)
            return math.sqrt(var)

        past_std_sus = stddev(past_sus_returns)
        past_std_con = stddev(past_con_returns)

        # 3) Sharpe ratio = (avgX - avgRF) / stdX
        def sharpe_ratio_proper(avg_x, avg_r, sd_x):
            if sd_x <= 1e-15:
                return 0.0
            return round((avg_x - avg_r) / sd_x, 4)

        past_sharpe_sus = round(sharpe_ratio_proper(past_avg_sus, past_avg_rf, past_std_sus), 2)
        past_sharpe_con = round(sharpe_ratio_proper(past_avg_con, past_avg_rf, past_std_con), 2)

        # 4) Store in the relevant fields
        self.past_final_sharpe_ratio_sus = past_sharpe_sus
        self.past_final_sharpe_ratio_con = past_sharpe_con
        self.past_final_volatility_sus = round(past_std_sus*100, 2)
        self.past_final_volatility_con = round(past_std_con*100, 2)

# PAGES
class Part1_Instructions(Page):
    def is_displayed(self):
        return self.participant.vars.get('treatment') in ['T1', 'T2', 'T5', 'T6', 'T7']

    def before_next_page(self, timeout_happened):
        self.map_csv_data_for_this_player()
        self.calculate_past_Average_Returns()
        self.calculate_past_cumulative_returns()
        self.calculate_past_Sharpe_Ratios()


class Belief0(Page):
    form_model = 'player'
    form_fields = ['Belief_0']
    def is_displayed(self):
        return self.participant.vars.get('treatment') in ['T1', 'T2', 'T5', 'T6', 'T7']


class ShortHistory(Page):
    def is_displayed(self):
        return self.participant.vars.get('treatment') in ['T1', 'T2', 'T5', 'T6', 'T7']
    def vars_for_template(self):
        past_sus_data = [x if x is not None else 0 for x in self.past_R_sus_list()]
        past_con_data = [x if x is not None else 0 for x in self.past_R_con_list()]

        past_TR_sus_data = [getattr(self, f'past_TR_sus{i}') for i in range(0, 11)]
        past_TR_con_data = [getattr(self, f'past_TR_con{i}') for i in range(0, 11)]

        past_summary_data = {
            'cumulative': {
                'sus': self.past_final_cumu_sus,
                'con': self.past_final_cumu_con,
            },
            'averageReturns': {
                'sus': self.past_final_average_return_sus,
                'con': self.past_final_average_return_con,
            },
            'sharpeRatios': {
                'sus': self.past_final_sharpe_ratio_sus,
                'con': self.past_final_sharpe_ratio_con,
            },
            'volatilities': {
                'sus': self.past_final_volatility_sus,
                'con': self.past_final_volatility_con,
            },
        },
        # no projections

        return {
            'past_sus_data': mark_safe(json.dumps(past_sus_data)),  # Convert to JSON for template
            'past_con_data': mark_safe(json.dumps(past_con_data)),

            'past_TR_sus_data': mark_safe(json.dumps(past_TR_sus_data)),
            'past_TR_con_data': mark_safe(json.dumps(past_TR_con_data)),

            'past_summaryData': mark_safe(json.dumps(past_summary_data))
        }


page_sequence = [Part1_Instructions, Belief0, ShortHistory]

