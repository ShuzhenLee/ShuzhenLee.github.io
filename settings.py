from os import environ

SESSION_CONFIGS = [
    # dict(
    #     name='General_Instructions_Before_Each_Treatment',
    #     app_sequence=['General_Instructions'],
    #     num_demo_participants=3,
    # ),
    dict(
        name='Session_1_2x2study_display_and_green_label',
        app_sequence=['General_Instructions',
                      'Short_History', 'No_Label_Short_History',
                      'Descriptive_Information', 'Demo_Account',
                      'No_Label_Descriptive_Information', 'No_Label_Demo_Account',
                      'FLEX_Real_Investment', 'No_Label_FLEX_Real_Investment',
                      'Second_Chance', 'No_Label_Second_Chance',
                      'Survey'],
        num_demo_participants=10,
        max_per_treatment=150,  # Default, adjustable on the session page
    ),
    dict(
        name='Session_2_3Treatments_flexibility_and_choice',
        app_sequence=['General_Instructions_session2', 'Short_History',
                      'Descriptive_Information', 'Demo_Account',
                      'Choice',
                      'FIX_Real_Investment', 'FLEX_Real_Investment',
                      'Second_Chance', 'Survey'],
        num_demo_participants=10,
        max_per_treatment=150,  # Default, adjustable on the session page
    ),
    dict(
        name='Treatment_1_Baseline_Descriptive_FLEX_Sustainable',
        app_sequence=['General_Instructions', 'Short_History', 'Descriptive_Information', 'FLEX_Real_Investment',
                      'Second_Chance', 'Survey'],
        num_demo_participants=3,
    ),
    dict(
        name='Treatment_2_Demo_Account_FLEX_Sustainable',
        app_sequence=['General_Instructions', 'Short_History', 'Demo_Account', 'FLEX_Real_Investment',
                      'Second_Chance', 'Survey'],
        num_demo_participants=3,
    ),
    dict(
        name='Treatment_3_Descriptive_FLEX_Normal_Labelling',
        app_sequence=['General_Instructions', 'No_Label_Short_History',
                      'No_Label_Descriptive_Information', 'No_Label_FLEX_Real_Investment',
                      'No_Label_Second_Chance', 'Survey'],
        num_demo_participants=3,
    ),
    dict(
        name='Treatment_4_Demo_Account_FLEX_Normal_Labelling',
        app_sequence=['General_Instructions', 'No_Label_Short_History',
                      'No_Label_Demo_Account', 'No_Label_FLEX_Real_Investment',
                      'No_Label_Second_Chance', 'Survey'],
        num_demo_participants=4,
    ),
    dict(
        name='Treatment_5_Descriptive_FIX_Sustainable',
        app_sequence=['General_Instructions_session2', 'Short_History', 'Descriptive_Information', 'FIX_Real_Investment',
                      'Second_Chance', 'Survey'],
        num_demo_participants=5,
    ),
    dict(
        name='Treatment_6_Demo_Account_FIX_Sustainable',
        app_sequence=['General_Instructions_session2', 'Short_History', 'Demo_Account', 'FIX_Real_Investment',
                      'Second_Chance', 'Survey'],
        num_demo_participants=6,
    ),
    dict(
        name='Treatment_7_Demo_Account_CHOICE_Sustainable',
        app_sequence=['General_Instructions_session2', 'Short_History', 'Demo_Account', 'Choice',
                      'FLEX_Real_Investment', 'FIX_Real_Investment',
                      'Second_Chance', 'Survey'],
        num_demo_participants=7,
    ),


]

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=1.00, participation_fee=0.00, doc=""
)

PARTICIPANT_FIELDS = []
SESSION_FIELDS = []
DEBUG = False

# rooms
ROOMS = [
    dict(
        name='Session1',
        display_name='Study Room 1',
    ),
    dict(
        name='Session2',
        display_name='Study Room 2',
    ),
]

# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'en'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'USD'
USE_POINTS = True


ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
# ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')
ADMIN_PASSWORD = 'password'

DEMO_PAGE_INTRO_HTML = """ """

SECRET_KEY = '6400448567047'
