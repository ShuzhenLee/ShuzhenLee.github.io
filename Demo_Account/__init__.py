from otree.api import *
import csv
import os
from django.shortcuts import render
import json
from django.utils.safestring import mark_safe


doc = """
DemoAccount"""




class C(BaseConstants):
    NAME_IN_URL = 'DemoAccount'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
    MAX_PERIODS = 45
    CSV_FILE_PATH = os.path.normpath(
        os.path.join(
            os.path.dirname(__file__),  # FLEX_Real_Investment folder
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
                rf_raw  = float(row.get('R_f', '0'))  # risk-free

                # Multiply by 100 and round to 2 decimal places
                sus_pct = round(sus_raw * 100, 2)
                con_pct = round(con_raw * 100, 2)
                rf_pct  = round(rf_raw * 100, 4)  # keep maybe 4 decimals for R_f

                rows.append({'R_sus': sus_pct, 'R_con': con_pct})
                rf_list.append(rf_pct)
        return rows, rf_list

    CSV_DATA, RF_DATA = load_csv_data(
        os.path.normpath(os.path.join(os.path.dirname(__file__), CSV_FILE_PATH))
    )


    PERIOD_RANGES = {
        'decision0': (0, 9),
        'decision1': (10, 18),
        'decision2': (19, 27),
        'decision3': (28, 36),
        'decision4': (37, 45)
    }


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    payoff_demo = models.FloatField()

    decision0 = models.IntegerField(label="first decision that affect the portfolio return from period 1 to 9")

    # Returns for the stage 1 with 45 periods
    R_sus0 = models.FloatField()
    R_con0 = models.FloatField()
    R_port0 = models.FloatField()
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
    fix_R_port0 = models.FloatField()
    fix_R_port1 = models.FloatField()
    fix_R_port2 = models.FloatField()
    fix_R_port3 = models.FloatField()
    fix_R_port4 = models.FloatField()
    fix_R_port5 = models.FloatField()
    fix_R_port6 = models.FloatField()
    fix_R_port7 = models.FloatField()
    fix_R_port8 = models.FloatField()
    fix_R_port9 = models.FloatField()

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

    fix_TR_port0 = models.FloatField(value=100.0)
    fix_TR_port1 = models.FloatField()
    fix_TR_port2 = models.FloatField()
    fix_TR_port3 = models.FloatField()
    fix_TR_port4 = models.FloatField()
    fix_TR_port5 = models.FloatField()
    fix_TR_port6 = models.FloatField()
    fix_TR_port7 = models.FloatField()
    fix_TR_port8 = models.FloatField()
    fix_TR_port9 = models.FloatField()

    cumu_sus1 = models.FloatField(initial=1.0)
    average_return_sus1 = models.FloatField()
    sharpe_ratio_sus1 = models.FloatField()
    volatility_sus1 = models.FloatField()
    projected_return_sus1 = models.FloatField()

    cumu_con1 = models.FloatField(initial=1.0)
    average_return_con1 = models.FloatField()
    sharpe_ratio_con1 = models.FloatField()
    volatility_con1 = models.FloatField()
    projected_return_con1 = models.FloatField()

    cumu_portfolio1 = models.FloatField(initial=1.0)
    average_return_portfolio1 = models.FloatField()
    sharpe_ratio_portfolio1 = models.FloatField()
    volatility_portfolio1 = models.FloatField()
    projected_return_portfolio1 = models.FloatField()

    cumu_fix_portfolio1 = models.FloatField(initial=1.0)
    average_return_fix_portfolio1 = models.FloatField()
    sharpe_ratio_fix_portfolio1 = models.FloatField()
    volatility_fix_portfolio1 = models.FloatField()
    projected_return_fix_portfolio1 = models.FloatField()


    decision1 = models.IntegerField()

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
    fix_R_port10 = models.FloatField()
    fix_R_port11 = models.FloatField()
    fix_R_port12 = models.FloatField()
    fix_R_port13 = models.FloatField()
    fix_R_port14 = models.FloatField()
    fix_R_port15 = models.FloatField()
    fix_R_port16 = models.FloatField()
    fix_R_port17 = models.FloatField()
    fix_R_port18 = models.FloatField()

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

    fix_TR_port10 = models.FloatField()
    fix_TR_port11 = models.FloatField()
    fix_TR_port12 = models.FloatField()
    fix_TR_port13 = models.FloatField()
    fix_TR_port14 = models.FloatField()
    fix_TR_port15 = models.FloatField()
    fix_TR_port16 = models.FloatField()
    fix_TR_port17 = models.FloatField()
    fix_TR_port18 = models.FloatField()

    cumu_sus2 = models.FloatField(initial=1.0)
    average_return_sus2 = models.FloatField()
    sharpe_ratio_sus2 = models.FloatField()
    volatility_sus2 = models.FloatField()
    projected_return_sus2 = models.FloatField()

    cumu_con2 = models.FloatField(initial=1.0)
    average_return_con2 = models.FloatField()
    sharpe_ratio_con2 = models.FloatField()
    volatility_con2 = models.FloatField()
    projected_return_con2 = models.FloatField()

    cumu_portfolio2 = models.FloatField(initial=1.0)
    average_return_portfolio2 = models.FloatField()
    sharpe_ratio_portfolio2 = models.FloatField()
    volatility_portfolio2 = models.FloatField()
    projected_return_portfolio2 = models.FloatField()

    cumu_fix_portfolio2 = models.FloatField(initial=1.0)
    average_return_fix_portfolio2 = models.FloatField()
    sharpe_ratio_fix_portfolio2 = models.FloatField()
    volatility_fix_portfolio2 = models.FloatField()
    projected_return_fix_portfolio2 = models.FloatField()

    decision2 = models.IntegerField()

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
    fix_R_port19 = models.FloatField()
    fix_R_port20 = models.FloatField()
    fix_R_port21 = models.FloatField()
    fix_R_port22 = models.FloatField()
    fix_R_port23 = models.FloatField()
    fix_R_port24 = models.FloatField()
    fix_R_port25 = models.FloatField()
    fix_R_port26 = models.FloatField()
    fix_R_port27 = models.FloatField()

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

    fix_TR_port19 = models.FloatField()
    fix_TR_port20 = models.FloatField()
    fix_TR_port21 = models.FloatField()
    fix_TR_port22 = models.FloatField()
    fix_TR_port23 = models.FloatField()
    fix_TR_port24 = models.FloatField()
    fix_TR_port25 = models.FloatField()
    fix_TR_port26 = models.FloatField()
    fix_TR_port27 = models.FloatField()

    cumu_sus3 = models.FloatField(initial=1.0)
    average_return_sus3 = models.FloatField()
    sharpe_ratio_sus3 = models.FloatField()
    volatility_sus3 = models.FloatField()
    projected_return_sus3 = models.FloatField()

    cumu_con3 = models.FloatField(initial=1.0)
    average_return_con3 = models.FloatField()
    sharpe_ratio_con3 = models.FloatField()
    volatility_con3 = models.FloatField()
    projected_return_con3 = models.FloatField()

    cumu_portfolio3 = models.FloatField(initial=1.0)
    average_return_portfolio3 = models.FloatField()
    sharpe_ratio_portfolio3 = models.FloatField()
    volatility_portfolio3 = models.FloatField()
    projected_return_portfolio3 = models.FloatField()

    cumu_fix_portfolio3 = models.FloatField(initial=1.0)
    average_return_fix_portfolio3 = models.FloatField()
    sharpe_ratio_fix_portfolio3 = models.FloatField()
    volatility_fix_portfolio3 = models.FloatField()
    projected_return_fix_portfolio3 = models.FloatField()

    decision3 = models.IntegerField()

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
    fix_R_port28 = models.FloatField()
    fix_R_port29 = models.FloatField()
    fix_R_port30 = models.FloatField()
    fix_R_port31 = models.FloatField()
    fix_R_port32 = models.FloatField()
    fix_R_port33 = models.FloatField()
    fix_R_port34 = models.FloatField()
    fix_R_port35 = models.FloatField()
    fix_R_port36 = models.FloatField()

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

    fix_TR_port28 = models.FloatField()
    fix_TR_port29 = models.FloatField()
    fix_TR_port30 = models.FloatField()
    fix_TR_port31 = models.FloatField()
    fix_TR_port32 = models.FloatField()
    fix_TR_port33 = models.FloatField()
    fix_TR_port34 = models.FloatField()
    fix_TR_port35 = models.FloatField()
    fix_TR_port36 = models.FloatField()

    cumu_sus4 = models.FloatField(initial=1.0)
    average_return_sus4 = models.FloatField()
    sharpe_ratio_sus4 = models.FloatField()
    volatility_sus4 = models.FloatField()
    projected_return_sus4 = models.FloatField()

    cumu_con4 = models.FloatField(initial=1.0)
    average_return_con4 = models.FloatField()
    sharpe_ratio_con4 = models.FloatField()
    volatility_con4 = models.FloatField()
    projected_return_con4 = models.FloatField()

    cumu_portfolio4 = models.FloatField(initial=1.0)
    average_return_portfolio4 = models.FloatField()
    sharpe_ratio_portfolio4 = models.FloatField()
    volatility_portfolio4 = models.FloatField()
    projected_return_portfolio4 = models.FloatField()

    cumu_fix_portfolio4 = models.FloatField(initial=1.0)
    average_return_fix_portfolio4 = models.FloatField()
    sharpe_ratio_fix_portfolio4 = models.FloatField()
    volatility_fix_portfolio4 = models.FloatField()
    projected_return_fix_portfolio4 = models.FloatField()

    decision4 = models.IntegerField()

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
    fix_R_port37 = models.FloatField()
    fix_R_port38 = models.FloatField()
    fix_R_port39 = models.FloatField()
    fix_R_port40 = models.FloatField()
    fix_R_port41 = models.FloatField()
    fix_R_port42 = models.FloatField()
    fix_R_port43 = models.FloatField()
    fix_R_port44 = models.FloatField()
    fix_R_port45 = models.FloatField()

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

    fix_TR_port37 = models.FloatField()
    fix_TR_port38 = models.FloatField()
    fix_TR_port39 = models.FloatField()
    fix_TR_port40 = models.FloatField()
    fix_TR_port41 = models.FloatField()
    fix_TR_port42 = models.FloatField()
    fix_TR_port43 = models.FloatField()
    fix_TR_port44 = models.FloatField()
    fix_TR_port45 = models.FloatField()

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

    final_cumu_fix_portfolio = models.FloatField(initial=1.0)
    final_average_return_fix_portfolio = models.FloatField()
    final_sharpe_ratio_fix_portfolio = models.FloatField()
    final_volatility_fix_portfolio = models.FloatField()

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

            self.R_sus0 = 0
            self.R_con0 = 0
            self.R_port0 = 0

            # Assign the R_sus and R_con fields
            setattr(self, R_sus_field, R_sus_value)
            setattr(self, R_con_field, R_con_value)

    # FOR THE COMPLETE STAGE 1 DATA
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

    def fix_R_port_list(self):
        result = []
        for i in range(0, C.MAX_PERIODS + 1):
            val = self.field_maybe_none(f'fix_R_port{i}')
            if val is None or val == 0.0:
                result.append(None)
            else:
                result.append(val)
        return result

    def compute_portfolio_returns(self, start_period, end_period, decision_field):
        # Grab the decision (0 or 1)
        decision_value = getattr(self, decision_field, 0)
        for i in range(start_period, end_period + 1):
            # R_sus{i} and R_con{i} are stored in this player's fields:
            sus_field = f'R_sus{i}'
            con_field = f'R_con{i}'
            port_field = f'R_port{i}'

            R_sus_val = getattr(self, sus_field, 0.0)
            R_con_val = getattr(self, con_field, 0.0)

            # Calculate R_port
            R_port_val = decision_value/100 * R_sus_val + (1 - decision_value/100) * R_con_val
            R_port_val_rounded = round(R_port_val, 2)
            setattr(self, port_field, R_port_val_rounded)

    def compute_fixed_portfolio_returns(self):
        # Grab the initial decision (0 or 1) from decision_0
        decision_value = getattr(self, 'decision0')

        for i in range(0, 46):
            # R_sus{i} and R_con{i} are stored in this player's fields:
            sus_field = f'R_sus{i}'
            con_field = f'R_con{i}'
            fix_field = f'fix_R_port{i}'  # Fixed total return storage

            R_sus_val = getattr(self, sus_field, 0.0)
            R_con_val = getattr(self, con_field, 0.0)

            # Calculate fixed portfolio return
            fix_R_val = decision_value / 100 * R_sus_val + (1 - decision_value / 100) * R_con_val
            fix_R_val_rounded = round(fix_R_val, 2)

            setattr(self, fix_field, fix_R_val_rounded)

    # calculate cumulative returns after each decision
    def calculate_cumulative_returns(self, decision_name):
        start_period, end_period = C.PERIOD_RANGES[decision_name]

        # Initialize starting TR values
        if decision_name == 'decision0':
            TR_sus_start = 100.0
            TR_con_start = 100.0
            TR_port_start = 100.0
            fix_TR_port_start = 100.0
        elif decision_name == 'decision1':
            TR_sus_start = getattr(self, 'TR_sus9', 100.0) + 100
            TR_con_start = getattr(self, 'TR_con9', 100.0) + 100
            TR_port_start = getattr(self, 'TR_port9', 100.0) + 100
            fix_TR_port_start = getattr(self, 'fix_TR_port9', 100.0) + 100
        elif decision_name == 'decision2':
            TR_sus_start = getattr(self, 'TR_sus18', 100.0) + 100
            TR_con_start = getattr(self, 'TR_con18', 100.0) + 100
            TR_port_start = getattr(self, 'TR_port18', 100.0) + 100
            fix_TR_port_start = getattr(self, 'fix_TR_port18', 100.0) + 100
        elif decision_name == 'decision3':
            TR_sus_start = getattr(self, 'TR_sus27', 100.0) + 100
            TR_con_start = getattr(self, 'TR_con27', 100.0) + 100
            TR_port_start = getattr(self, 'TR_port27', 100.0) + 100
            fix_TR_port_start = getattr(self, 'fix_TR_port27', 100.0) + 100
        else:  # decision_name == 'decision4'
            TR_sus_start = getattr(self, 'TR_sus36', 100.0) + 100
            TR_con_start = getattr(self, 'TR_con36', 100.0) + 100
            TR_port_start = getattr(self, 'TR_port36', 100.0) + 100
            fix_TR_port_start = getattr(self, 'fix_TR_port36', 100.0) + 100

        # Initialize cumulative values
        cumu_sus = TR_sus_start
        cumu_con = TR_con_start
        cumu_port = TR_port_start
        cumu_fix_port = fix_TR_port_start

        # Loop through each period and calculate TR and cumulative values
        for i in range(start_period, end_period + 1):
            R_sus_val = getattr(self, f'R_sus{i}', 0.0)
            R_con_val = getattr(self, f'R_con{i}', 0.0)
            R_port_val = getattr(self, f'R_port{i}', 0.0)
            fix_R_port_val = getattr(self, f'fix_R_port_{i}', 0.0)


            # Update TR values based on R
            cumu_sus *= (1 + R_sus_val / 100)
            cumu_con *= (1 + R_con_val / 100)
            cumu_port *= (1 + R_port_val / 100)
            cumu_fix_port *= (1 + fix_R_port_val / 100)

            # Subtract 100 for each cumulative return
            adjusted_cumu_sus = cumu_sus - 100
            adjusted_cumu_con = cumu_con - 100
            adjusted_cumu_port = cumu_port - 100
            adjusted_cumu_fix_port = cumu_fix_port - 100

            # Store TR values for this period
            setattr(self, f'TR_sus{i}', round(adjusted_cumu_sus, 2))
            setattr(self, f'TR_con{i}', round(adjusted_cumu_con, 2))
            setattr(self, f'TR_port{i}', round(adjusted_cumu_port, 2))
            setattr(self, f'fix_TR_port{i}', round(adjusted_cumu_fix_port, 2))

        # Store final cumulative values for the decision block
        sus_rounded = round(adjusted_cumu_sus, 2)
        con_rounded = round(adjusted_cumu_con, 2)
        port_rounded = round(adjusted_cumu_port, 2)
        fix_port_rounded = round(adjusted_cumu_fix_port, 2)

        if decision_name == 'decision0':
            self.cumu_sus1 = sus_rounded
            self.cumu_con1 = con_rounded
            self.cumu_portfolio1 = port_rounded
            self.cumu_fix_portfolio1 = fix_port_rounded
        elif decision_name == 'decision1':
            self.cumu_sus2 = sus_rounded
            self.cumu_con2 = con_rounded
            self.cumu_portfolio2 = port_rounded
            self.cumu_fix_portfolio2 = fix_port_rounded
        elif decision_name == 'decision2':
            self.cumu_sus3 = sus_rounded
            self.cumu_con3 = con_rounded
            self.cumu_portfolio3 = port_rounded
            self.cumu_fix_portfolio3 = fix_port_rounded
        elif decision_name == 'decision3':
            self.cumu_sus4 = sus_rounded
            self.cumu_con4 = con_rounded
            self.cumu_portfolio4 = port_rounded
            self.cumu_fix_portfolio4 = fix_port_rounded
        else:  # decision_name == 'decision4'
            self.final_cumu_sus = sus_rounded
            self.final_cumu_con = con_rounded
            self.final_cumu_portfolio = port_rounded
            self.final_cumu_fix_portfolio = fix_port_rounded

    def calculate_fix_cumulative_returns(self, decision_name):
        fix_TR_port_start = 100.0
        cumu_fix_port = fix_TR_port_start
        # Loop through each period and calculate TR and cumulative values

        if decision_name == 'decision0':
            for i in range(0, 10):
                fix_R_port_val = getattr(self, f'fix_R_port{i}')
                # Update TR values based on R
                cumu_fix_port *= (1 + fix_R_port_val / 100)
                # Subtract 100 for each cumulative return
                adjusted_cumu_fix_port = cumu_fix_port - 100
                setattr(self, f'fix_TR_port{i}', round(adjusted_cumu_fix_port, 2))
            # Store final cumulative values for the decision block
            fix_port_rounded = round(adjusted_cumu_fix_port, 2)
            self.cumu_fix_portfolio1 = fix_port_rounded
        elif decision_name == 'decision1':
            for i in range(0, 19):
                fix_R_port_val = getattr(self, f'fix_R_port{i}')
                # Update TR values based on R
                cumu_fix_port *= (1 + fix_R_port_val / 100)
                # Subtract 100 for each cumulative return
                adjusted_cumu_fix_port = cumu_fix_port - 100
                setattr(self, f'fix_TR_port{i}', round(adjusted_cumu_fix_port, 2))
            fix_port_rounded = round(adjusted_cumu_fix_port, 2)
            self.cumu_fix_portfolio2 = fix_port_rounded
        elif decision_name == 'decision2':
            for i in range(0, 28):
                fix_R_port_val = getattr(self, f'fix_R_port{i}')
                # Update TR values based on R
                cumu_fix_port *= (1 + fix_R_port_val / 100)
                # Subtract 100 for each cumulative return
                adjusted_cumu_fix_port = cumu_fix_port - 100
                setattr(self, f'fix_TR_port{i}', round(adjusted_cumu_fix_port, 2))
            fix_port_rounded = round(adjusted_cumu_fix_port, 2)
            self.cumu_fix_portfolio3 = fix_port_rounded
        elif decision_name == 'decision3':
            for i in range(0, 37):
                fix_R_port_val = getattr(self, f'fix_R_port{i}')
                # Update TR values based on R
                cumu_fix_port *= (1 + fix_R_port_val / 100)
                # Subtract 100 for each cumulative return
                adjusted_cumu_fix_port = cumu_fix_port - 100
                setattr(self, f'fix_TR_port{i}', round(adjusted_cumu_fix_port, 2))
            fix_port_rounded = round(adjusted_cumu_fix_port, 2)
            self.cumu_fix_portfolio4 = fix_port_rounded
        else:  # decision_name == 'decision4'
            for i in range(0, 46):
                fix_R_port_val = getattr(self, f'fix_R_port{i}')
                # Update TR values based on R
                cumu_fix_port *= (1 + fix_R_port_val / 100)
                # Subtract 100 for each cumulative return
                adjusted_cumu_fix_port = cumu_fix_port - 100
                setattr(self, f'fix_TR_port{i}', round(adjusted_cumu_fix_port, 2))
            fix_port_rounded = round(adjusted_cumu_fix_port, 2)
            self.final_cumu_fix_portfolio = fix_port_rounded


    def calculate_final_cumulative_returns(self):
        self.calculate_cumulative_returns('decision4')

        # Calculate average returns
    def calculate_Average_Returns (self, decision_name):
        start_period, end_period = C.PERIOD_RANGES[decision_name]

        sum_sus = 0.0
        sum_con = 0.0
        sum_port = 0.0
        sum_fix_port = 0.0
        count = end_period

        for i in range(1, end_period + 1):
            R_sus_val = getattr(self, f'R_sus{i}', 0.0)
            R_con_val = getattr(self, f'R_con{i}', 0.0)
            R_port_val = getattr(self, f'R_port{i}', 0.0)
            fix_R_port_val = getattr(self, f'fix_R_port{i}', 0.0)

            sum_sus += R_sus_val
            sum_con += R_con_val
            sum_port += R_port_val
            sum_fix_port += fix_R_port_val

        if count > 0:
            avg_sus = sum_sus / count
            avg_con = sum_con / count
            avg_port = sum_port / count
            avg_fix_port = sum_fix_port/ count
        else:
            # If there's any odd case with zero periods
            avg_sus = 0.0
            avg_con = 0.0
            avg_port = 0.0
            avg_fix_port = 0.0

        avg_sus_rounded = round(avg_sus, 2)
        avg_con_rounded = round(avg_con, 2)
        avg_port_rounded = round(avg_port, 2)
        avg_fix_port_rounded = round(avg_fix_port, 2)

        if decision_name == 'decision0':
            # For block 1
            self.average_return_sus1 = avg_sus_rounded
            self.average_return_con1 = avg_con_rounded
            self.average_return_portfolio1 = avg_port_rounded
            self.average_return_fix_portfolio1 = avg_fix_port_rounded
        elif decision_name == 'decision1':
            # For block 2
            self.average_return_sus2 = avg_sus_rounded
            self.average_return_con2 = avg_con_rounded
            self.average_return_portfolio2 = avg_port_rounded
            self.average_return_fix_portfolio2 = avg_fix_port_rounded
        elif decision_name == 'decision2':
            # For block 3
            self.average_return_sus3 = avg_sus_rounded
            self.average_return_con3 = avg_con_rounded
            self.average_return_portfolio3 = avg_port_rounded
            self.average_return_fix_portfolio3 = avg_fix_port_rounded
        elif decision_name == 'decision3':
            # For block 4
            self.average_return_sus4 = avg_sus_rounded
            self.average_return_con4 = avg_con_rounded
            self.average_return_portfolio4 = avg_port_rounded
            self.average_return_fix_portfolio4 = avg_fix_port_rounded
        else:
            # For block 5 (final)
            self.final_average_return_sus = avg_sus_rounded
            self.final_average_return_con = avg_con_rounded
            self.final_average_return_portfolio = avg_port_rounded
            self.final_average_return_fix_portfolio = avg_fix_port_rounded

    def calculate_Sharpe_Ratios(self, decision_name):
        start_period, end_period = C.PERIOD_RANGES[decision_name]
        # If end_period=9 => periods 1..9 => we want indexes [0..8] in arrays

        if end_period <= 0:
            return  # no data?

        # Prepare lists to store decimal returns for each strategy
        sus_returns = []
        con_returns = []
        port_returns = []
        fix_port_returns = []
        rf_returns = []

        # Loop from period=1 to end_period, but remember array indexes are [period-1]
        for period in range(1, end_period + 1):
            # R_sus{i}, R_con{i}, R_port{i} are in percentage.
            sus_val_pct = getattr(self, f'R_sus{period}', 0.0)
            con_val_pct = getattr(self, f'R_con{period}', 0.0)
            port_val_pct = getattr(self, f'R_port{period}', 0.0)
            fix_port_val_pct = getattr(self, f'fix_R_port{period}', 0.0)

            # Convert to decimal (1.23 => 0.0123)
            sus_decimal = sus_val_pct / 100
            con_decimal = con_val_pct / 100
            port_decimal = port_val_pct / 100
            fix_port_decimal = fix_port_val_pct / 100

            sus_returns.append(sus_decimal)
            con_returns.append(con_decimal)
            port_returns.append(port_decimal)
            fix_port_returns.append(fix_port_decimal)

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
        avg_fix_port = mean(fix_port_returns)
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
        std_fix_port = stddev(fix_port_returns)

        # 3) Sharpe ratio = (avgX - avgRF) / stdX
        def sharpe_ratio_proper(avg_x, avg_r, sd_x):
            if sd_x <= 1e-15:
                return 0.0
            return round((avg_x - avg_r) / sd_x, 4)

        sharpe_sus = round(sharpe_ratio_proper(avg_sus, avg_rf, std_sus), 2)
        sharpe_con = round(sharpe_ratio_proper(avg_con, avg_rf, std_con), 2)
        sharpe_port = round(sharpe_ratio_proper(avg_port, avg_rf, std_port), 2)
        sharpe_fix_port = round(sharpe_ratio_proper(avg_fix_port, avg_rf, std_fix_port), 2)

        # 4) Store in the relevant fields
        if decision_name == 'decision0':
            self.sharpe_ratio_sus1 = sharpe_sus
            self.sharpe_ratio_con1 = sharpe_con
            self.sharpe_ratio_portfolio1 = sharpe_port
            self.sharpe_ratio_fix_portfolio1 = sharpe_fix_port

            self.volatility_sus1 = round(std_sus*100, 2)
            self.volatility_con1 = round(std_con*100, 2)
            self.volatility_portfolio1 = round(std_port*100, 2)
            self.volatility_fix_portfolio1 = round(std_fix_port*100, 2)
        elif decision_name == 'decision1':
            self.sharpe_ratio_sus2 = sharpe_sus
            self.sharpe_ratio_con2 = sharpe_con
            self.sharpe_ratio_portfolio2 = sharpe_port
            self.sharpe_ratio_fix_portfolio2 = sharpe_fix_port

            self.volatility_sus2 = round(std_sus*100, 2)
            self.volatility_con2 = round(std_con*100, 2)
            self.volatility_portfolio2 = round(std_port*100, 2)
            self.volatility_fix_portfolio2 = round(std_fix_port*100, 2)
        elif decision_name == 'decision2':
            self.sharpe_ratio_sus3 = sharpe_sus
            self.sharpe_ratio_con3 = sharpe_con
            self.sharpe_ratio_portfolio3 = sharpe_port
            self.sharpe_ratio_fix_portfolio3 = sharpe_fix_port

            self.volatility_sus3 = round(std_sus*100, 2)
            self.volatility_con3 = round(std_con*100, 2)
            self.volatility_portfolio3 = round(std_port*100, 2)
            self.volatility_fix_portfolio3 = round(std_fix_port*100, 2)
        elif decision_name == 'decision3':
            self.sharpe_ratio_sus4 = sharpe_sus
            self.sharpe_ratio_con4 = sharpe_con
            self.sharpe_ratio_portfolio4 = sharpe_port
            self.sharpe_ratio_fix_portfolio4 = sharpe_fix_port

            self.volatility_sus4 = round(std_sus*100, 2)
            self.volatility_con4 = round(std_con*100, 2)
            self.volatility_portfolio4 = round(std_port*100, 2)
            self.volatility_fix_portfolio4 = round(std_fix_port*100, 2)
        else:  # decision4 => final
            self.final_sharpe_ratio_sus = sharpe_sus
            self.final_sharpe_ratio_con = sharpe_con
            self.final_sharpe_ratio_portfolio = sharpe_port
            self.final_sharpe_ratio_fix_portfolio = sharpe_fix_port

            self.final_volatility_sus = round(std_sus*100, 2)
            self.final_volatility_con = round(std_con*100, 2)
            self.final_volatility_portfolio = round(std_port*100, 2)
            self.final_volatility_fix_portfolio = round(std_fix_port*100, 2)


    def calculate_Projected_Returns(self, decision_name):
        start_period, end_period = C.PERIOD_RANGES[decision_name]
        if decision_name == 'decision0':
            avg_sus_pct = self.average_return_sus1
            avg_con_pct = self.average_return_con1
            avg_port_pct = self.average_return_portfolio1
            avg_fix_port_pct = self.average_return_fix_portfolio1

        elif decision_name == 'decision1':
            avg_sus_pct = self.average_return_sus2
            avg_con_pct = self.average_return_con2
            avg_port_pct = self.average_return_portfolio2
            avg_fix_port_pct = self.average_return_fix_portfolio2

        elif decision_name == 'decision2':
            avg_sus_pct = self.average_return_sus3
            avg_con_pct = self.average_return_con3
            avg_port_pct = self.average_return_portfolio3
            avg_fix_port_pct = self.average_return_fix_portfolio3

        else:   # decision_name == 'decision3'
            avg_sus_pct = self.average_return_sus4
            avg_con_pct = self.average_return_con4
            avg_port_pct = self.average_return_portfolio4
            avg_fix_port_pct = self.average_return_fix_portfolio4

            # 3) Convert average returns from percentage to decimal
            #    e.g. 1.23 => 0.0123
        avg_sus_dec = avg_sus_pct / 100.0
        avg_con_dec = avg_con_pct / 100.0
        avg_port_dec = avg_port_pct / 100.0
        avg_fix_port_dec = avg_fix_port_pct / 100.0

        # 4) Project from end_period+1 up to period 45
        #    That is, for each future period, multiply by (1 + avg_return_decimal)
        future_periods = 45 - end_period
        proj_sus = 100.0 * ((1 + avg_sus_dec) ** future_periods)-100
        proj_con = 100.0 * ((1 + avg_con_dec) ** future_periods)-100
        proj_port = 100.0 * ((1 + avg_port_dec) ** future_periods)-100
        proj_fix_port = 100.0 * ((1 + avg_fix_port_dec) ** future_periods)-100

        # 6) Round once at the end
        proj_sus_rounded = round(proj_sus, 2)
        proj_con_rounded = round(proj_con, 2)
        proj_port_rounded = round(proj_port, 2)
        proj_fix_port_rounded = round(proj_fix_port, 2)

        # 6) Store in projected_return_susN, etc.
        if decision_name == 'decision0':
            self.projected_return_sus1 = proj_sus_rounded
            self.projected_return_con1 = proj_con_rounded
            self.projected_return_portfolio1 = proj_port_rounded
            self.projected_return_fix_portfolio1 = proj_fix_port_rounded
        elif decision_name == 'decision1':
            self.projected_return_sus2 = proj_sus_rounded
            self.projected_return_con2 = proj_con_rounded
            self.projected_return_portfolio2 = proj_port_rounded
            self.projected_return_fix_portfolio2 = proj_fix_port_rounded
        elif decision_name == 'decision2':
            self.projected_return_sus3 = proj_sus_rounded
            self.projected_return_con3 = proj_con_rounded
            self.projected_return_portfolio3 = proj_port_rounded
            self.projected_return_fix_portfolio3 = proj_fix_port_rounded
        else: # decision_name == 'decision3', decision4 has no projected returns as it is the final decision
            self.projected_return_sus4 = proj_sus_rounded
            self.projected_return_con4 = proj_con_rounded
            self.projected_return_portfolio4 = proj_port_rounded
            self.projected_return_fix_portfolio4 = proj_fix_port_rounded


        # PAGES
class Stage1(Page):
    def is_displayed(self):
        return self.participant.vars.get('treatment') in ['T2', 'T6', 'T7']



class Instruction(Page):
    def is_displayed(self):
        return self.participant.vars.get('treatment') in ['T2', 'T6', 'T7']
    def before_next_page(self, timeout_happened):
        self.map_csv_data_for_this_player()


class Decision_P0(Page):
    form_model = 'player'
    form_fields = ['decision0']
    def is_displayed(self):
        return self.participant.vars.get('treatment') in ['T2', 'T6', 'T7']

    def before_next_page(self, timeout_happened):
        self.participant.vars['decision0'] = self.decision0
        self.compute_portfolio_returns(1, 9, 'decision0')
        self.compute_fixed_portfolio_returns()
        self.calculate_Average_Returns('decision0')
        self.calculate_cumulative_returns('decision0')
        self.calculate_fix_cumulative_returns('decision0')
        self.calculate_Sharpe_Ratios('decision0')
        self.calculate_Projected_Returns('decision0')



class Decision_P1(Page):
    form_model = 'player'
    form_fields = ['decision1']
    def is_displayed(self):
        return self.participant.vars.get('treatment') in ['T2', 'T6', 'T7']

    def vars_for_template(self):
        sus_data = [x if x is not None else 0 for x in self.R_sus_list()]
        con_data = [x if x is not None else 0 for x in self.R_con_list()]
        port_data = [x if x is not None else 0 for x in self.R_port_list()]
        fix_port_data = [x if x is not None else 0 for x in self.fix_R_port_list()]

        # Total returns for display (TR_sus, TR_con, TR_port for periods 0-9)
        TR_sus_data = [getattr(self, f'TR_sus{i}') for i in range(0, 10)]
        TR_con_data = [getattr(self, f'TR_con{i}') for i in range(0, 10)]
        TR_port_data = [getattr(self, f'TR_port{i}') for i in range(0, 10)]
        fix_TR_port_data = [getattr(self, f'fix_TR_port{i}') for i in range(0, 10)]

        summary_data = {
            'cumulative': {
                'sus': self.cumu_sus1,
                'con': self.cumu_con1,
                'port': self.cumu_portfolio1,
                'fix_port': self.cumu_fix_portfolio1,
            },
            'averageReturns': {
                'sus': self.average_return_sus1,
                'con': self.average_return_con1,
                'port': self.average_return_portfolio1,
                'fix_port': self.average_return_fix_portfolio1,
            },
            'sharpeRatios': {
                'sus': self.sharpe_ratio_sus1,
                'con': self.sharpe_ratio_con1,
                'port': self.sharpe_ratio_portfolio1,
                'fix_port': self.sharpe_ratio_fix_portfolio1,
            },
            'volatilities': {
                'sus': self.volatility_sus1,
                'con': self.volatility_con1,
                'port': self.volatility_portfolio1,
                'fix_port': self.volatility_fix_portfolio1,
            },
            'projectedReturns': {
                'sus': self.projected_return_sus1,
                'con': self.projected_return_con1,
                'port': self.projected_return_portfolio1,
                'fix_port': self.projected_return_fix_portfolio1,
            },
        },
        # Calculate projections for each period (starting from maxPeriods+1 to 45)
        base_value = 100.0
        avg_return_sus = self.average_return_sus1 / 100  # Convert percentage to decimal
        avg_return_con = self.average_return_con1 / 100
        avg_return_port = self.average_return_portfolio1 / 100
        avg_return_fix_port = self.average_return_fix_portfolio1 / 100

        projections_sus = [round((base_value * (1 + avg_return_sus) ** (i - 9))-100, 2) for i in range(10, 46)]
        projections_con = [round((base_value * (1 + avg_return_con) ** (i - 9))-100, 2) for i in range(10, 46)]
        projections_port = [round((base_value * (1 + avg_return_port) ** (i - 9))-100, 2) for i in range(10, 46)]
        projections_fix_port = [round((base_value * (1 + avg_return_fix_port) ** (i - 9))-100, 2) for i in range(10, 46)]

        return {
            'decision0': self.decision0,  # Previous decision
            'con_decision0': 100 - self.decision0,

            'sus_data': mark_safe(json.dumps(sus_data)),  # Convert to JSON for template
            'con_data': mark_safe(json.dumps(con_data)),
            'port_data': mark_safe(json.dumps(port_data)),
            'fix_port_data': mark_safe(json.dumps(fix_port_data)),

            'TR_sus_data': mark_safe(json.dumps(TR_sus_data)),
            'TR_con_data': mark_safe(json.dumps(TR_con_data)),
            'TR_port_data': mark_safe(json.dumps(TR_port_data)),
            'fix_TR_port_data': mark_safe(json.dumps(fix_TR_port_data)),

            'summaryData': mark_safe(json.dumps(summary_data)),
            'projections_sus': mark_safe(json.dumps(projections_sus)),
            'projections_con': mark_safe(json.dumps(projections_con)),
            'projections_port': mark_safe(json.dumps(projections_port)),
            'projections_fix_port': mark_safe(json.dumps(projections_fix_port))
        }

    def before_next_page(self, timeout_happened):
        self.participant.vars['decision1'] = self.decision1
        self.compute_portfolio_returns(10, 18, 'decision1')
        self.calculate_cumulative_returns('decision1')
        self.calculate_fix_cumulative_returns('decision1')
        self.calculate_Average_Returns('decision1')
        self.calculate_Sharpe_Ratios('decision1')
        self.calculate_Projected_Returns('decision1')



class Decision_P2(Page):
    form_model = 'player'
    form_fields = ['decision2']
    def is_displayed(self):
        return self.participant.vars.get('treatment') in ['T2', 'T6', 'T7']

    def vars_for_template(self):
        sus_data = [x if x is not None else 0 for x in self.R_sus_list()]
        con_data = [x if x is not None else 0 for x in self.R_con_list()]
        port_data = [x if x is not None else 0 for x in self.R_port_list()]
        fix_port_data = [x if x is not None else 0 for x in self.fix_R_port_list()]
        # Total returns for display (TR_sus, TR_con, TR_port for periods 0-18)
        TR_sus_data = [getattr(self, f'TR_sus{i}') for i in range(0, 19)]
        TR_con_data = [getattr(self, f'TR_con{i}') for i in range(0, 19)]
        TR_port_data = [getattr(self, f'TR_port{i}') for i in range(0, 19)]
        fix_TR_port_data = [getattr(self, f'fix_TR_port{i}') for i in range(0, 19)]

        summary_data = {
            'cumulative': {
                'sus': self.cumu_sus2,
                'con': self.cumu_con2,
                'port': self.cumu_portfolio2,
                'fix_port': self.cumu_fix_portfolio2,
            },
            'averageReturns': {
                'sus': self.average_return_sus2,
                'con': self.average_return_con2,
                'port': self.average_return_portfolio2,
                'fix_port': self.average_return_fix_portfolio2,
            },
            'sharpeRatios': {
                'sus': self.sharpe_ratio_sus2,
                'con': self.sharpe_ratio_con2,
                'port': self.sharpe_ratio_portfolio2,
                'fix_port': self.sharpe_ratio_fix_portfolio2,
            },
            'volatilities': {
                'sus': self.volatility_sus2,
                'con': self.volatility_con2,
                'port': self.volatility_portfolio2,
                'fix_port': self.volatility_fix_portfolio2,
            },
            'projectedReturns': {
                'sus': self.projected_return_sus2,
                'con': self.projected_return_con2,
                'port': self.projected_return_portfolio2,
                'fix_port': self.projected_return_fix_portfolio2,
            },
        },
        # Calculate projections for each period (starting from maxPeriods+1 to 45)
        base_value = 100.0
        avg_return_sus = self.average_return_sus2 / 100  # Convert percentage to decimal
        avg_return_con = self.average_return_con2 / 100
        avg_return_port = self.average_return_portfolio2 / 100
        avg_return_fix_port = self.average_return_fix_portfolio2 / 100

        projections_sus = [round((base_value * (1 + avg_return_sus) ** (i - 18))-100, 2) for i in range(19, 46)]
        projections_con = [round((base_value * (1 + avg_return_con) ** (i - 18))-100, 2) for i in range(19, 46)]
        projections_port = [round((base_value * (1 + avg_return_port) ** (i - 18))-100, 2) for i in range(19, 46)]
        projections_fix_port = [round((base_value * (1 + avg_return_fix_port) ** (i - 18))-100, 2) for i in range(19, 46)]

        return {
            'decision0': self.decision0,  # Previous decision
            'decision1': self.decision1,
            'con_decision0': 100 - self.decision0,
            'con_decision1': 100 - self.decision1,

            'sus_data': mark_safe(json.dumps(sus_data)),  # Convert to JSON for template
            'con_data': mark_safe(json.dumps(con_data)),
            'port_data': mark_safe(json.dumps(port_data)),
            'fix_port_data': mark_safe(json.dumps(fix_port_data)),

            'TR_sus_data': mark_safe(json.dumps(TR_sus_data)),
            'TR_con_data': mark_safe(json.dumps(TR_con_data)),
            'TR_port_data': mark_safe(json.dumps(TR_port_data)),
            'fix_TR_port_data': mark_safe(json.dumps(fix_TR_port_data)),

            'summaryData': mark_safe(json.dumps(summary_data)),
            'projections_sus': mark_safe(json.dumps(projections_sus)),
            'projections_con': mark_safe(json.dumps(projections_con)),
            'projections_port': mark_safe(json.dumps(projections_port)),
            'projections_fix_port': mark_safe(json.dumps(projections_fix_port))
        }

    def before_next_page(self, timeout_happened):
        self.participant.vars['decision2'] = self.decision2
        self.compute_portfolio_returns(19, 27, 'decision2')
        self.calculate_cumulative_returns('decision2')
        self.calculate_fix_cumulative_returns('decision2')
        self.calculate_Average_Returns('decision2')
        self.calculate_Sharpe_Ratios('decision2')
        self.calculate_Projected_Returns('decision2')


class Decision_P3(Page):
    form_model = 'player'
    form_fields = ['decision3']
    def is_displayed(self):
        return self.participant.vars.get('treatment') in ['T2', 'T6', 'T7']

    def vars_for_template(self):
        sus_data = [x if x is not None else 0 for x in self.R_sus_list()]
        con_data = [x if x is not None else 0 for x in self.R_con_list()]
        port_data = [x if x is not None else 0 for x in self.R_port_list()]
        fix_port_data = [x if x is not None else 0 for x in self.fix_R_port_list()]
        # Total returns for display (TR_sus, TR_con, TR_port for periods 0-27)
        TR_sus_data = [getattr(self, f'TR_sus{i}') for i in range(0, 28)]
        TR_con_data = [getattr(self, f'TR_con{i}') for i in range(0, 28)]
        TR_port_data = [getattr(self, f'TR_port{i}') for i in range(0, 28)]
        fix_TR_port_data = [getattr(self, f'fix_TR_port{i}') for i in range(0, 28)]

        summary_data = {
            'cumulative': {
                'sus': self.cumu_sus3,
                'con': self.cumu_con3,
                'port': self.cumu_portfolio3,
                'fix_port': self.cumu_fix_portfolio3,
            },
            'averageReturns': {
                'sus': self.average_return_sus3,
                'con': self.average_return_con3,
                'port': self.average_return_portfolio3,
                'fix_port': self.average_return_fix_portfolio3,
            },
            'sharpeRatios': {
                'sus': self.sharpe_ratio_sus3,
                'con': self.sharpe_ratio_con3,
                'port': self.sharpe_ratio_portfolio3,
                'fix_port': self.sharpe_ratio_fix_portfolio3,
            },
            'volatilities': {
                'sus': self.volatility_sus3,
                'con': self.volatility_con3,
                'port': self.volatility_portfolio3,
                'fix_port': self.volatility_fix_portfolio3,
            },
            'projectedReturns': {
                'sus': self.projected_return_sus3,
                'con': self.projected_return_con3,
                'port': self.projected_return_portfolio3,
                'fix_port': self.projected_return_fix_portfolio3,
            },
        },
        # Calculate projections for each period (starting from maxPeriods+1 to 45)
        base_value = 100.0
        avg_return_sus = self.average_return_sus3 / 100  # Convert percentage to decimal
        avg_return_con = self.average_return_con3 / 100
        avg_return_port = self.average_return_portfolio3 / 100
        avg_return_fix_port = self.average_return_fix_portfolio3 / 100

        projections_sus = [round((base_value * (1 + avg_return_sus) ** (i - 27))-100, 2) for i in range(28, 46)]
        projections_con = [round((base_value * (1 + avg_return_con) ** (i - 27))-100, 2) for i in range(28, 46)]
        projections_port = [round((base_value * (1 + avg_return_port) ** (i - 27))-100, 2) for i in range(28, 46)]
        projections_fix_port = [round((base_value * (1 + avg_return_fix_port) ** (i - 27))-100, 2) for i in range(28, 46)]

        return {
            'min_percent': self.participant.vars.get('min_percent', 0),  # Default 0 if not set
            'decision0': self.decision0,  # Previous decision
            'decision1': self.decision1,
            'decision2': self.decision2,
            'con_decision0': 100 - self.decision0,
            'con_decision1': 100 - self.decision1,
            'con_decision2': 100 - self.decision2,

            'sus_data': mark_safe(json.dumps(sus_data)),  # Convert to JSON for template
            'con_data': mark_safe(json.dumps(con_data)),
            'port_data': mark_safe(json.dumps(port_data)),
            'fix_port_data': mark_safe(json.dumps(fix_port_data)),

            'TR_sus_data': mark_safe(json.dumps(TR_sus_data)),
            'TR_con_data': mark_safe(json.dumps(TR_con_data)),
            'TR_port_data': mark_safe(json.dumps(TR_port_data)),
            'fix_TR_port_data': mark_safe(json.dumps(fix_TR_port_data)),

            'summaryData': mark_safe(json.dumps(summary_data)),
            'projections_sus': mark_safe(json.dumps(projections_sus)),
            'projections_con': mark_safe(json.dumps(projections_con)),
            'projections_port': mark_safe(json.dumps(projections_port)),
            'projections_fix_port': mark_safe(json.dumps(projections_fix_port))
        }

    def before_next_page(self, timeout_happened):
        self.participant.vars['decision3'] = self.decision3
        self.compute_portfolio_returns(28, 36, 'decision3')
        self.calculate_cumulative_returns('decision3')
        self.calculate_fix_cumulative_returns('decision3')
        self.calculate_Average_Returns('decision3')
        self.calculate_Sharpe_Ratios('decision3')
        self.calculate_Projected_Returns('decision3')


class Decision_P4(Page):
    form_model = 'player'
    form_fields = ['decision4']
    def is_displayed(self):
        return self.participant.vars.get('treatment') in ['T2', 'T6', 'T7']

    def vars_for_template(self):
        sus_data = [x if x is not None else 0 for x in self.R_sus_list()]
        con_data = [x if x is not None else 0 for x in self.R_con_list()]
        port_data = [x if x is not None else 0 for x in self.R_port_list()]
        fix_port_data = [x if x is not None else 0 for x in self.fix_R_port_list()]

        # Total returns for display (TR_sus, TR_con, TR_port for periods 0-36)
        TR_sus_data = [getattr(self, f'TR_sus{i}') for i in range(0, 37)]
        TR_con_data = [getattr(self, f'TR_con{i}') for i in range(0, 37)]
        TR_port_data = [getattr(self, f'TR_port{i}') for i in range(0, 37)]
        fix_TR_port_data = [getattr(self, f'fix_TR_port{i}') for i in range(0, 37)]

        summary_data = {
            'cumulative': {
                'sus': self.cumu_sus4,
                'con': self.cumu_con4,
                'port': self.cumu_portfolio4,
                'fix_port': self.cumu_fix_portfolio4,
            },
            'averageReturns': {
                'sus': self.average_return_sus4,
                'con': self.average_return_con4,
                'port': self.average_return_portfolio4,
                'fix_port': self.average_return_fix_portfolio4,
            },
            'sharpeRatios': {
                'sus': self.sharpe_ratio_sus4,
                'con': self.sharpe_ratio_con4,
                'port': self.sharpe_ratio_portfolio4,
                'fix_port': self.sharpe_ratio_fix_portfolio4,
            },
            'volatilities': {
                'sus': self.volatility_sus4,
                'con': self.volatility_con4,
                'port': self.volatility_portfolio4,
                'fix_port': self.volatility_fix_portfolio4,
            },
            'projectedReturns': {
                'sus': self.projected_return_sus4,
                'con': self.projected_return_con4,
                'port': self.projected_return_portfolio4,
                'fix_port': self.projected_return_fix_portfolio4,
            },
        },
        # Calculate projections for each period (starting from maxPeriods+1 to 45)
        base_value = 100.0
        avg_return_sus = self.average_return_sus4 / 100  # Convert percentage to decimal
        avg_return_con = self.average_return_con4 / 100
        avg_return_port = self.average_return_portfolio4 / 100
        avg_return_fix_port = self.average_return_fix_portfolio4 / 100

        projections_sus = [round((base_value * (1 + avg_return_sus) ** (i - 36))-100, 2) for i in range(37, 46)]
        projections_con = [round((base_value * (1 + avg_return_con) ** (i - 36))-100, 2) for i in range(37, 46)]
        projections_port = [round((base_value * (1 + avg_return_port) ** (i - 36))-100, 2) for i in range(37, 46)]
        projections_fix_port = [round((base_value * (1 + avg_return_fix_port) ** (i - 36))-100, 2) for i in range(37, 46)]

        return {
            'min_percent': self.participant.vars.get('min_percent', 0),  # Default 0 if not set
            'decision0': self.decision0,  # Previous decision
            'decision1': self.decision1,
            'decision2': self.decision2,
            'decision3': self.decision3,
            'con_decision0': 100 - self.decision0,
            'con_decision1': 100 - self.decision1,
            'con_decision2': 100 - self.decision2,
            'con_decision3': 100 - self.decision3,

            'sus_data': mark_safe(json.dumps(sus_data)),  # Convert to JSON for template
            'con_data': mark_safe(json.dumps(con_data)),
            'port_data': mark_safe(json.dumps(port_data)),
            'fix_port_data': mark_safe(json.dumps(fix_port_data)),

            'TR_sus_data': mark_safe(json.dumps(TR_sus_data)),
            'TR_con_data': mark_safe(json.dumps(TR_con_data)),
            'TR_port_data': mark_safe(json.dumps(TR_port_data)),
            'fix_TR_port_data': mark_safe(json.dumps(fix_TR_port_data)),

            'summaryData': mark_safe(json.dumps(summary_data)),
            'projections_sus': mark_safe(json.dumps(projections_sus)),
            'projections_con': mark_safe(json.dumps(projections_con)),
            'projections_port': mark_safe(json.dumps(projections_port)),
            'projections_fix_port': mark_safe(json.dumps(projections_fix_port))
        }

    def before_next_page(self, timeout_happened):
        self.participant.vars['decision4'] = self.decision4
        self.compute_portfolio_returns(37, 45, 'decision4')
        self.calculate_cumulative_returns('decision4')
        self.calculate_fix_cumulative_returns('decision4')
        self.calculate_Average_Returns('decision4')
        self.calculate_Sharpe_Ratios('decision4')

        # Set the real investment payoff
        self.payoff_demo = round(100 + self.final_cumu_portfolio,2)
        self.participant.vars['payoff_demo'] = self.payoff_demo


class Decision_P5(Page):
    def is_displayed(self):
        return self.participant.vars.get('treatment') in ['T2', 'T6', 'T7']

    def vars_for_template(self):
        sus_data = [x if x is not None else 0 for x in self.R_sus_list()]
        con_data = [x if x is not None else 0 for x in self.R_con_list()]
        port_data = [x if x is not None else 0 for x in self.R_port_list()]
        fix_port_data = [x if x is not None else 0 for x in self.fix_R_port_list()]

        # Total returns for display (TR_sus, TR_con, TR_port for periods 0-36)
        TR_sus_data = [getattr(self, f'TR_sus{i}') for i in range(0, 46)]
        TR_con_data = [getattr(self, f'TR_con{i}') for i in range(0, 46)]
        TR_port_data = [getattr(self, f'TR_port{i}') for i in range(0, 46)]
        fix_TR_port_data = [getattr(self, f'fix_TR_port{i}') for i in range(0, 46)]

        summary_data = {
            'cumulative': {
                'sus': self.final_cumu_sus,
                'con': self.final_cumu_con,
                'port': self.final_cumu_portfolio,
                'fix_port': self.final_cumu_fix_portfolio,
            },
            'averageReturns': {
                'sus': self.final_average_return_sus,
                'con': self.final_average_return_con,
                'port': self.final_average_return_portfolio,
                'fix_port': self.final_average_return_fix_portfolio,
            },
            'sharpeRatios': {
                'sus': self.final_sharpe_ratio_sus,
                'con': self.final_sharpe_ratio_con,
                'port': self.final_sharpe_ratio_portfolio,
                'fix_port': self.final_sharpe_ratio_fix_portfolio,
            },
            'volatilities': {
                'sus': self.final_volatility_sus,
                'con': self.final_volatility_con,
                'port': self.final_volatility_portfolio,
                'fix_port': self.final_volatility_fix_portfolio,
            },
        },
        # no projections

        return {
            'min_percent': self.participant.vars.get('min_percent', 0),  # Default 0 if not set
            'decision0': self.decision0,  # Previous decision
            'decision1': self.decision1,
            'decision2': self.decision2,
            'decision3': self.decision3,
            'decision4': self.decision4,
            'con_decision0': 100 - self.decision0,
            'con_decision1': 100 - self.decision1,
            'con_decision2': 100 - self.decision2,
            'con_decision3': 100 - self.decision3,
            'con_decision4': 100 - self.decision4,

            'sus_data': mark_safe(json.dumps(sus_data)),  # Convert to JSON for template
            'con_data': mark_safe(json.dumps(con_data)),
            'port_data': mark_safe(json.dumps(port_data)),
            'fix_port_data': mark_safe(json.dumps(fix_port_data)),

            'TR_sus_data': mark_safe(json.dumps(TR_sus_data)),
            'TR_con_data': mark_safe(json.dumps(TR_con_data)),
            'TR_port_data': mark_safe(json.dumps(TR_port_data)),
            'fix_TR_port_data': mark_safe(json.dumps(fix_TR_port_data)),

            'summaryData': mark_safe(json.dumps(summary_data)),
            'final_cumu_portfolio': self.final_cumu_portfolio,
            'final_cumu_fix_portfolio': self.final_cumu_fix_portfolio,
            'payoff_demo': self.payoff_demo,
        }

    def before_next_page(self, timeout_happened):
        self.participant.vars['final_cumu_portfolio'] = self.final_cumu_portfolio
        self.participant.vars['final_cumu_fix_portfolio'] = self.final_cumu_fix_portfolio
        self.participant.vars['final_cumu_con'] = self.final_cumu_con
        self.participant.vars['final_cumu_sus'] = self.final_cumu_sus


class Attention2(Page):
    form_model = 'player'
    form_fields = ['attention_2']

    def is_displayed(self):
        return self.participant.vars.get('treatment') in ['T2', 'T6', 'T7']

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
        return player.participant.vars.get('attention_failed', False) and player.participant.vars.get('treatment') in ['T2', 'T6', 'T7']


page_sequence = [Stage1, Instruction,
                 Decision_P0, Decision_P1, Decision_P2, Decision_P3, Decision_P4, Decision_P5,
                 Attention2, Thank_You]
