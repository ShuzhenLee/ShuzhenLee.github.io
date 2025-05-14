from otree.api import *
import csv
import os
from django.shortcuts import render
import json
from django.utils.safestring import mark_safe
import random

doc = """
Your app description
"""

# Constants
class C(BaseConstants):
    NAME_IN_URL = 'Fix_Real_Investment'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
    MAX_PERIODS = 45
    CSV_FILE_PATH = os.path.normpath(
        os.path.join(
            os.path.dirname(__file__),
            '..',  # go up one directory
            '_static', 'data', 'sequence_2.csv'
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
    payoff_real_invest = models.FloatField()

    fix_decision = models.IntegerField(label="decision that affect the portfolio return from period 1 to 45")
    fix_donation = models.FloatField()

    est_con_1 = models.FloatField(label="estimation of #1 conventional fund average return %")
    est_sus_1 = models.FloatField(label="estimation of #1 sustainable fund average return %")

    belief_bonus = models.CurrencyField()


    R_sus0 = models.FloatField(value=0.0)
    R_con0 = models.FloatField(value=0.0)
    R_port0 = models.FloatField(value=0.0)
    R_sus1 = models.FloatField()
    R_con1 = models.FloatField()
    R_port1 = models.FloatField()
    R_sus2 = models.FloatField()
    R_con2 = models.FloatField()
    R_port2 = models.FloatField()
    R_sus3 = models.FloatField()
    R_con3 = models.FloatField()
    R_port3 = models.FloatField()
    R_sus4 = models.FloatField()
    R_con4 = models.FloatField()
    R_port4 = models.FloatField()
    R_sus5 = models.FloatField()
    R_con5 = models.FloatField()
    R_port5 = models.FloatField()
    R_sus6 = models.FloatField()
    R_con6 = models.FloatField()
    R_port6 = models.FloatField()
    R_sus7 = models.FloatField()
    R_con7 = models.FloatField()
    R_port7 = models.FloatField()
    R_sus8 = models.FloatField()
    R_con8 = models.FloatField()
    R_port8 = models.FloatField()
    R_sus9 = models.FloatField()
    R_con9 = models.FloatField()
    R_port9 = models.FloatField()

    R_sus10 = models.FloatField()
    R_con10 = models.FloatField()
    R_port10 = models.FloatField()
    R_sus11 = models.FloatField()
    R_con11 = models.FloatField()
    R_port11 = models.FloatField()
    R_sus12 = models.FloatField()
    R_con12 = models.FloatField()
    R_port12 = models.FloatField()
    R_sus13 = models.FloatField()
    R_con13 = models.FloatField()
    R_port13 = models.FloatField()
    R_sus14 = models.FloatField()
    R_con14 = models.FloatField()
    R_port14 = models.FloatField()
    R_sus15 = models.FloatField()
    R_con15 = models.FloatField()
    R_port15 = models.FloatField()
    R_sus16 = models.FloatField()
    R_con16 = models.FloatField()
    R_port16 = models.FloatField()
    R_sus17 = models.FloatField()
    R_con17 = models.FloatField()
    R_port17 = models.FloatField()
    R_sus18 = models.FloatField()
    R_con18 = models.FloatField()
    R_port18 = models.FloatField()

    R_sus19 = models.FloatField()
    R_con19 = models.FloatField()
    R_port19 = models.FloatField()
    R_sus20 = models.FloatField()
    R_con20 = models.FloatField()
    R_port20 = models.FloatField()
    R_sus21 = models.FloatField()
    R_con21 = models.FloatField()
    R_port21 = models.FloatField()
    R_sus22 = models.FloatField()
    R_con22 = models.FloatField()
    R_port22 = models.FloatField()
    R_sus23 = models.FloatField()
    R_con23 = models.FloatField()
    R_port23 = models.FloatField()
    R_sus24 = models.FloatField()
    R_con24 = models.FloatField()
    R_port24 = models.FloatField()
    R_sus25 = models.FloatField()
    R_con25 = models.FloatField()
    R_port25 = models.FloatField()
    R_sus26 = models.FloatField()
    R_con26 = models.FloatField()
    R_port26 = models.FloatField()
    R_sus27 = models.FloatField()
    R_con27 = models.FloatField()
    R_port27 = models.FloatField()

    R_sus28 = models.FloatField()
    R_con28 = models.FloatField()
    R_port28 = models.FloatField()
    R_sus29 = models.FloatField()
    R_con29 = models.FloatField()
    R_port29 = models.FloatField()
    R_sus30 = models.FloatField()
    R_con30 = models.FloatField()
    R_port30 = models.FloatField()
    R_sus31 = models.FloatField()
    R_con31 = models.FloatField()
    R_port31 = models.FloatField()
    R_sus32 = models.FloatField()
    R_con32 = models.FloatField()
    R_port32 = models.FloatField()
    R_sus33 = models.FloatField()
    R_con33 = models.FloatField()
    R_port33 = models.FloatField()
    R_sus34 = models.FloatField()
    R_con34 = models.FloatField()
    R_port34 = models.FloatField()
    R_sus35 = models.FloatField()
    R_con35 = models.FloatField()
    R_port35 = models.FloatField()
    R_sus36 = models.FloatField()
    R_con36 = models.FloatField()
    R_port36 = models.FloatField()

    R_sus37 = models.FloatField()
    R_con37 = models.FloatField()
    R_port37 = models.FloatField()
    R_sus38 = models.FloatField()
    R_con38 = models.FloatField()
    R_port38 = models.FloatField()
    R_sus39 = models.FloatField()
    R_con39 = models.FloatField()
    R_port39 = models.FloatField()
    R_sus40 = models.FloatField()
    R_con40 = models.FloatField()
    R_port40 = models.FloatField()
    R_sus41 = models.FloatField()
    R_con41 = models.FloatField()
    R_port41 = models.FloatField()
    R_sus42 = models.FloatField()
    R_con42 = models.FloatField()
    R_port42 = models.FloatField()
    R_sus43 = models.FloatField()
    R_con43 = models.FloatField()
    R_port43 = models.FloatField()
    R_sus44 = models.FloatField()
    R_con44 = models.FloatField()
    R_port44 = models.FloatField()
    R_sus45 = models.FloatField()
    R_con45 = models.FloatField()
    R_port45 = models.FloatField()

    TR_sus0 = models.FloatField(value=100.0)
    TR_con0 = models.FloatField(value=100.0)
    TR_port0 = models.FloatField(value=100.0)
    TR_sus1 = models.FloatField()
    TR_con1 = models.FloatField()
    TR_port1 = models.FloatField()
    TR_sus2 = models.FloatField()
    TR_con2 = models.FloatField()
    TR_port2 = models.FloatField()
    TR_sus3 = models.FloatField()
    TR_con3 = models.FloatField()
    TR_port3 = models.FloatField()
    TR_sus4 = models.FloatField()
    TR_con4 = models.FloatField()
    TR_port4 = models.FloatField()
    TR_sus5 = models.FloatField()
    TR_con5 = models.FloatField()
    TR_port5 = models.FloatField()
    TR_sus6 = models.FloatField()
    TR_con6 = models.FloatField()
    TR_port6 = models.FloatField()
    TR_sus7 = models.FloatField()
    TR_con7 = models.FloatField()
    TR_port7 = models.FloatField()
    TR_sus8 = models.FloatField()
    TR_con8 = models.FloatField()
    TR_port8 = models.FloatField()
    TR_sus9 = models.FloatField()
    TR_con9 = models.FloatField()
    TR_port9 = models.FloatField()
    TR_sus10 = models.FloatField()
    TR_con10 = models.FloatField()
    TR_port10 = models.FloatField()
    TR_sus11 = models.FloatField()
    TR_con11 = models.FloatField()
    TR_port11 = models.FloatField()
    TR_sus12 = models.FloatField()
    TR_con12 = models.FloatField()
    TR_port12 = models.FloatField()
    TR_sus13 = models.FloatField()
    TR_con13 = models.FloatField()
    TR_port13 = models.FloatField()
    TR_sus14 = models.FloatField()
    TR_con14 = models.FloatField()
    TR_port14 = models.FloatField()
    TR_sus15 = models.FloatField()
    TR_con15 = models.FloatField()
    TR_port15 = models.FloatField()
    TR_sus16 = models.FloatField()
    TR_con16 = models.FloatField()
    TR_port16 = models.FloatField()
    TR_sus17 = models.FloatField()
    TR_con17 = models.FloatField()
    TR_port17 = models.FloatField()
    TR_sus18 = models.FloatField()
    TR_con18 = models.FloatField()
    TR_port18 = models.FloatField()
    TR_sus19 = models.FloatField()
    TR_con19 = models.FloatField()
    TR_port19 = models.FloatField()
    TR_sus20 = models.FloatField()
    TR_con20 = models.FloatField()
    TR_port20 = models.FloatField()
    TR_sus21 = models.FloatField()
    TR_con21 = models.FloatField()
    TR_port21 = models.FloatField()
    TR_sus22 = models.FloatField()
    TR_con22 = models.FloatField()
    TR_port22 = models.FloatField()
    TR_sus23 = models.FloatField()
    TR_con23 = models.FloatField()
    TR_port23 = models.FloatField()
    TR_sus24 = models.FloatField()
    TR_con24 = models.FloatField()
    TR_port24 = models.FloatField()
    TR_sus25 = models.FloatField()
    TR_con25 = models.FloatField()
    TR_port25 = models.FloatField()
    TR_sus26 = models.FloatField()
    TR_con26 = models.FloatField()
    TR_port26 = models.FloatField()
    TR_sus27 = models.FloatField()
    TR_con27 = models.FloatField()
    TR_port27 = models.FloatField()
    TR_sus28 = models.FloatField()
    TR_con28 = models.FloatField()
    TR_port28 = models.FloatField()
    TR_sus29 = models.FloatField()
    TR_con29 = models.FloatField()
    TR_port29 = models.FloatField()
    TR_sus30 = models.FloatField()
    TR_con30 = models.FloatField()
    TR_port30 = models.FloatField()
    TR_sus31 = models.FloatField()
    TR_con31 = models.FloatField()
    TR_port31 = models.FloatField()
    TR_sus32 = models.FloatField()
    TR_con32 = models.FloatField()
    TR_port32 = models.FloatField()
    TR_sus33 = models.FloatField()
    TR_con33 = models.FloatField()
    TR_port33 = models.FloatField()
    TR_sus34 = models.FloatField()
    TR_con34 = models.FloatField()
    TR_port34 = models.FloatField()
    TR_sus35 = models.FloatField()
    TR_con35 = models.FloatField()
    TR_port35 = models.FloatField()
    TR_sus36 = models.FloatField()
    TR_con36 = models.FloatField()
    TR_port36 = models.FloatField()
    TR_sus37 = models.FloatField()
    TR_con37 = models.FloatField()
    TR_port37 = models.FloatField()
    TR_sus38 = models.FloatField()
    TR_con38 = models.FloatField()
    TR_port38 = models.FloatField()
    TR_sus39 = models.FloatField()
    TR_con39 = models.FloatField()
    TR_port39 = models.FloatField()
    TR_sus40 = models.FloatField()
    TR_con40 = models.FloatField()
    TR_port40 = models.FloatField()
    TR_sus41 = models.FloatField()
    TR_con41 = models.FloatField()
    TR_port41 = models.FloatField()
    TR_sus42 = models.FloatField()
    TR_con42 = models.FloatField()
    TR_port42 = models.FloatField()
    TR_sus43 = models.FloatField()
    TR_con43 = models.FloatField()
    TR_port43 = models.FloatField()
    TR_sus44 = models.FloatField()
    TR_con44 = models.FloatField()
    TR_port44 = models.FloatField()
    TR_sus45 = models.FloatField()
    TR_con45 = models.FloatField()
    TR_port45 = models.FloatField()

    final_cumu_sus = models.FloatField(initial=1.0)
    final_average_return_sus = models.FloatField()
    final_sharpe_ratio_sus = models.FloatField()
    final_volatility_sus = models.FloatField()

    final_cumu_con = models.FloatField(initial=1.0)
    final_average_return_con = models.FloatField()
    final_sharpe_ratio_con = models.FloatField()
    final_volatility_con = models.FloatField()

    final_cumu_portfolio = models.FloatField(initial=1.0)
    final_average_return_portfolio = models.FloatField()
    final_sharpe_ratio_portfolio = models.FloatField()
    final_volatility_portfolio = models.FloatField()

    regret = models.IntegerField(
            label="How satisfied are you with your investment decision?",
            choices=[[1, '1 Completely unsatisfied'], [2, '2'], [3, '3'], [4, '4'], [5, '5'],
                     [6, '6'], [7, '7 Completely satisfied']],
            widget=widgets.RadioSelectHorizontal)


    def map_csv_data_for_this_player(self):
        # Loop over indices 1..45 (assuming you have 45 rows in the CSV)
        for i in range(1, C.MAX_PERIODS + 1):
            # CSV_DATA[i-1] is the dictionary for row i
            row = C.CSV_DATA[i - 1]

            # Retrieve R_sus and R_con from this CSV row
            R_sus_value = row['R_sus']
            R_con_value = row['R_con']

            # Build the field names for R_sus{i}, R_con{i}, and R_port{i}
            R_sus_field = f'R_sus{i}'
            R_con_field = f'R_con{i}'

            self.R_sus0 = 0
            self.R_con0 = 0
            self.R_port0 = 0

            # Assign the R_sus and R_con fields
            setattr(self, R_sus_field, R_sus_value)
            setattr(self, R_con_field, R_con_value)

    def R_sus_list(self):
        return [getattr(self, f'R_sus{i}') for i in range(0, C.MAX_PERIODS + 1)]

    def R_con_list(self):
        return [getattr(self, f'R_con{i}') for i in range(0, C.MAX_PERIODS + 1)]

    def R_port_list(self):
        result = []
        for i in range(0, C.MAX_PERIODS + 1):
            val = self.field_maybe_none(f'R_port{i}')
            if val is None or val == 0.0:
                result.append(None)
            else:
                result.append(val)
        return result

    def compute_portfolio_returns(self):
        decision_value = self.fix_decision
        for i in range(1, 46):
            # R_sus{i} and R_con{i} are stored in this player's fields:
            sus_field = f'R_sus{i}'
            con_field = f'R_con{i}'
            port_field = f'R_port{i}'

            R_sus_val = getattr(self, sus_field, 0.0)
            R_con_val = getattr(self, con_field, 0.0)

            # Calculate R_port
            R_port_val = decision_value / 100 * R_sus_val + (1 - decision_value / 100) * R_con_val
            R_port_val_rounded = round(R_port_val, 2)
            setattr(self, port_field, R_port_val_rounded)

    # calculate cumulative returns after each decision
    def calculate_cumulative_returns(self):
        # Initialize starting TR values
        TR_sus_start = 100.0
        TR_con_start = 100.0
        TR_port_start = 100.0

        # Set initial values for period 0
        self.TR_sus0 = TR_sus_start - 100  # Cumulative return starts at 0
        self.TR_con0 = TR_con_start - 100
        self.TR_port0 = TR_port_start - 100

        # Initialize cumulative values
        cumu_sus = TR_sus_start
        cumu_con = TR_con_start
        cumu_port = TR_port_start

        # Loop through each period and calculate TR and cumulative values
        for i in range(1, 46):
            R_sus_val = getattr(self, f'R_sus{i}', 0.0)
            R_con_val = getattr(self, f'R_con{i}', 0.0)
            R_port_val = getattr(self, f'R_port{i}', 0.0)

            # Update TR values based on R
            cumu_sus *= (1 + R_sus_val / 100)
            cumu_con *= (1 + R_con_val / 100)
            cumu_port *= (1 + R_port_val / 100)

            # Subtract 100 for each cumulative return
            adjusted_cumu_sus = cumu_sus - 100
            adjusted_cumu_con = cumu_con - 100
            adjusted_cumu_port = cumu_port - 100

            # Store TR values for this period
            setattr(self, f'TR_sus{i}', round(adjusted_cumu_sus, 2))
            setattr(self, f'TR_con{i}', round(adjusted_cumu_con, 2))
            setattr(self, f'TR_port{i}', round(adjusted_cumu_port, 2))

        # Store final cumulative values for the decision block
        sus_rounded = round(adjusted_cumu_sus, 2)
        con_rounded = round(adjusted_cumu_con, 2)
        port_rounded = round(adjusted_cumu_port, 2)

        self.final_cumu_sus = sus_rounded
        self.final_cumu_con = con_rounded
        self.final_cumu_portfolio = port_rounded

        # Calculate average returns

    def calculate_Average_Returns(self):
        sum_sus = 0.0
        sum_con = 0.0
        sum_port = 0.0
        count = 45

        for i in range(1, 46):
            R_sus_val = getattr(self, f'R_sus{i}', 0.0)
            R_con_val = getattr(self, f'R_con{i}', 0.0)
            R_port_val = getattr(self, f'R_port{i}', 0.0)

            sum_sus += R_sus_val
            sum_con += R_con_val
            sum_port += R_port_val

        if count > 0:
            avg_sus = sum_sus / count
            avg_con = sum_con / count
            avg_port = sum_port / count
        else:
            # If there's any odd case with zero periods
            avg_sus = 0.0
            avg_con = 0.0
            avg_port = 0.0

        avg_sus_rounded = round(avg_sus, 2)
        avg_con_rounded = round(avg_con, 2)
        avg_port_rounded = round(avg_port, 2)

        self.final_average_return_sus = avg_sus_rounded
        self.final_average_return_con = avg_con_rounded
        self.final_average_return_portfolio = avg_port_rounded

    def calculate_Sharpe_Ratios(self):
        # Prepare lists to store decimal returns for each strategy
        sus_returns = []
        con_returns = []
        port_returns = []
        rf_returns = []

        # Loop from period=1 to end_period, but remember array indexes are [period-1]
        for period in range(1, 46):
            # R_sus{i}, R_con{i}, R_port{i} are in percentage.
            sus_val_pct = getattr(self, f'R_sus{period}', 0.0)
            con_val_pct = getattr(self, f'R_con{period}', 0.0)
            port_val_pct = getattr(self, f'R_port{period}', 0.0)

            # Convert to decimal (1.23 => 0.0123)
            sus_decimal = sus_val_pct / 100
            con_decimal = con_val_pct / 100
            port_decimal = port_val_pct / 100

            sus_returns.append(sus_decimal)
            con_returns.append(con_decimal)
            port_returns.append(port_decimal)

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
        avg_port = mean(port_returns)
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
        std_port = stddev(port_returns)

        # 3) Sharpe ratio = (avgX - avgRF) / stdX
        def sharpe_ratio_proper(avg_x, avg_r, sd_x):
            if sd_x <= 1e-15:
                return 0.0
            return round((avg_x - avg_r) / sd_x, 4)

        sharpe_sus = round(sharpe_ratio_proper(avg_sus, avg_rf, std_sus), 2)
        sharpe_con = round(sharpe_ratio_proper(avg_con, avg_rf, std_con), 2)
        sharpe_port = round(sharpe_ratio_proper(avg_port, avg_rf, std_port), 2)

        # 4) Store in the relevant fields
        self.final_sharpe_ratio_sus = sharpe_sus
        self.final_sharpe_ratio_con = sharpe_con
        self.final_sharpe_ratio_portfolio = sharpe_port
        self.final_volatility_sus = round(std_sus * 100, 2)
        self.final_volatility_con = round(std_con * 100, 2)
        self.final_volatility_portfolio = round(std_port * 100, 2)


# Pages
class Stage2(Page):
    def is_displayed(self):
        return self.participant.vars.get('treatment') in ['T5', 'T6', 'T7']
    def before_next_page(self, timeout_happened):
        if 'random_sus' not in self.participant.vars:
            random_sus = random.randint(1, 100)
            self.participant.vars['random_sus'] = random_sus
            correct_compre = (random_sus / 100) * 87.3 + (1 - random_sus / 100) * 57.2
            self.participant.vars['correct_compre'] = correct_compre


class Instruction(Page):
    def is_displayed(self):
        return self.participant.vars.get('treatment') in ['T5', 'T6', 'T7']

    def vars_for_template(self):
        selected_charity = self.participant.vars.get('green_charity')
        return {
            'selected_charity': selected_charity,
            'random_sus': self.participant.vars['random_sus'],
            'random_con': 100 - self.participant.vars['random_sus'],
            'correct_compre': round(self.participant.vars['correct_compre'], 1),
        }


class Attention_Check(Page):
    def is_displayed(self):
        return self.participant.vars.get('treatment') in ['T5', 'T6', 'T7']


class Belief1(Page):
    form_model = 'player'
    form_fields = ['est_con_1', 'est_sus_1']
    def is_displayed(self):
        return self.participant.vars.get('treatment') in ['T5', 'T6', 'T7']


class Decision(Page):
    form_model = 'player'
    form_fields = ['fix_decision']
    def is_displayed(self):
        return self.participant.vars.get('treatment') in ['T5', 'T6', 'T7']

    def before_next_page(self, timeout_happened):
        self.map_csv_data_for_this_player()
        self.compute_portfolio_returns()
        self.calculate_Average_Returns()
        self.calculate_cumulative_returns()
        self.calculate_Sharpe_Ratios()

        self.payoff_real_invest = round(100 + self.final_cumu_portfolio,2)
        self.participant.vars['payoff_real_invest'] = self.payoff_real_invest
        self.fix_donation = round(self.fix_decision + self.final_cumu_sus * (self.fix_decision / 100), 2)

        self.participant.vars['part3_donation'] = self.fix_donation

        self.belief_bonus = 0
        margin = 5
        actual_sus = self.final_average_return_sus
        actual_con = self.final_average_return_con

        est_sus = self.est_sus_1
        est_con = self.est_con_1

        if abs(est_sus - actual_sus) <= margin:
            self.belief_bonus += 0.50  # 50 pence bonus

        if abs(est_con - actual_con) <= margin:
            self.belief_bonus += 0.50  # Another 50 pence bonus

        # Store the bonus for the final app
        self.participant.vars['belief_bonus'] = round(self.belief_bonus, 2)

        # for next page, store the final values in a random order
        if 'results_sequence' not in self.participant.vars:
            results = [
                {
                    'id': 'investment-result',
                    'text': f"Your Portfolio Value: {int(round(self.payoff_real_invest))} ECUs."
                },
                {
                    'id': 'con-investment-result',
                    'text': f"The final value if 100 ECUs were fully invested in the Conventional Fund: {int(round(100 + self.final_cumu_con))} ECUs."
                },
                {
                    'id': 'sus-investment-result',
                    'text': f"The final value if 100 ECUs were fully invested in the Sustainable Fund: {int(round(100 + self.final_cumu_sus))} ECUs."
                },
            ]
            random.shuffle(results)
            self.participant.vars['results_sequence'] = results


class FIX_Real_Investment(Page):
    form_model = 'player'
    form_fields = ['regret']
    def is_displayed(self):
        return self.participant.vars.get('treatment') in ['T5', 'T6', 'T7']

    def vars_for_template(self):
        sus_data = [x if x is not None else 0 for x in self.R_sus_list()]
        con_data = [x if x is not None else 0 for x in self.R_con_list()]
        port_data = [x if x is not None else 0 for x in self.R_port_list()]
        # Total returns for display (TR_sus, TR_con, TR_port for periods 0-45)
        TR_sus_data = [getattr(self, f'TR_sus{i}') for i in range(0, 46)]
        TR_con_data = [getattr(self, f'TR_con{i}') for i in range(0, 46)]
        TR_port_data = [getattr(self, f'TR_port{i}') for i in range(0, 46)]

        summary_data = {
            'cumulative': {
                'sus': self.final_cumu_sus,
                'con': self.final_cumu_con,
                'port': self.final_cumu_portfolio,
            },
            'averageReturns': {
                'sus': self.final_average_return_sus,
                'con': self.final_average_return_con,
                'port': self.final_average_return_portfolio,
            },
            'sharpeRatios': {
                'sus': self.final_sharpe_ratio_sus,
                'con': self.final_sharpe_ratio_con,
                'port': self.final_sharpe_ratio_portfolio,
            },
            'volatilities': {
                'sus': self.final_volatility_sus,
                'con': self.final_volatility_con,
                'port': self.final_volatility_portfolio,
            },
        },

        selected_charity = self.participant.vars.get('green_charity')
        results = self.participant.vars['results_sequence']

        return {
            'fix_decision': self.fix_decision,  # Previous decision
            'con_fix': 100 - self.fix_decision,

            'sus_data': mark_safe(json.dumps(sus_data)),  # Convert to JSON for template
            'con_data': mark_safe(json.dumps(con_data)),
            'port_data': mark_safe(json.dumps(port_data)),

            'TR_sus_data': mark_safe(json.dumps(TR_sus_data)),
            'TR_con_data': mark_safe(json.dumps(TR_con_data)),
            'TR_port_data': mark_safe(json.dumps(TR_port_data)),

            'summaryData': mark_safe(json.dumps(summary_data)),
            'final_cumu_portfolio': self.final_cumu_portfolio,

            'payoff_real_invest': self.payoff_real_invest,
            'results': results,
            'donation_result':  int(round(self.participant.vars['part3_donation'])),
            'fix_donation': self.fix_donation,  # Pass fix_donation to the template
            'selected_charity': selected_charity
        }

    def app_after_this_page(self, upcoming_apps):
        return "Second_Chance"


page_sequence = [Stage2, Instruction, Attention_Check, Belief1, Decision, FIX_Real_Investment]
