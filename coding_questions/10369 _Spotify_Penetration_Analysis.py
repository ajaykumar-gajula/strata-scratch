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
