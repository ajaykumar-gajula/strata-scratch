"""
## Query

Market penetration is an important metric for understanding Spotify's performance and growth potential in different regions.
You are part of the analytics team at Spotify and are tasked with calculating the active user penetration rate in specific markets.

For this task, 'active_users' are defined based on the  following criterias:

- last_active_date: The user must have interacted with Spotify within the last 30 days.
•	monthly_active_sessions: The user must have engaged with Spotify for at least 5 sessions in the past month.
•	listening_hours: The user must have spent at least 10 hours listening on Spotify in the past month.

Based on the condition above, calculate the active 'user_penetration_rate' by using the following formula.

- Active User Penetration Rate = (Number of Active Spotify Users in the Market / Total Population of the Market)

Total Population of the market is based on both active and passive users.

The output should contain 'country' and 'active_user_penetration_rate'. Make sure that all countries that appear in the dataset are also present in the output of your solution. Ensure there are 10 decimal places in your solution.

Let's assume the current_day is 2024-01-31.

- **DataFrame: penetration_analysis**
    
    **penetration_analysis**
    
    **country:**varchar
    
    **last_active_date:**datetime
    
    **monthly_active_sessions:**int
    
    **listening_hours:**int
    
    **total_population:**int
    
    **is_active:**bool

    """


# Import your libraries
import pandas as pd
from datetime import datetime
import numpy as np

penetration_analysis['act'] =np.where(((datetime.today().date() - penetration_analysis['last_active_date'].dt.date).dt.days)>30,np.where(penetration_analysis['monthly_active_sessions']>=5,np.where(penetration_analysis['listening_hours']>=10,1,0),0),0)
active_users = penetration_analysis[penetration_analysis['act'] == 1]
active_users_count = active_users.groupby('country').size()

# Group by country and extract the total population
total_population = penetration_analysis.groupby('country')['total_population'].first()
penetration_rate = (active_users_count / total_population).map(lambda x: '0.0000000000' if pd.isnull(x) else format(x, '.10f'))

penetration_rate_df = penetration_rate.reset_index().rename(columns={0: 'active_user_penetration_rate'})


penetration_rate_df
