# machine learning model that will recommend music to user based off of the time of the day, 
# day of the week, and/ or activity that they are performing. This prediction is based off of
# past logs that they put in (what time, what activities, and what mood that activity matches)

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier