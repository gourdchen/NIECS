from neuroCombat import neuroCombat
import pandas as pd
import numpy as np
def combat(data,infoTable):
    
    covars = pd.DataFrame()
    covars['gender'] = infoTable.Gender
    covars['age'] = infoTable.Age
    covars['batch'] = infoTable.center
    covars['group'] = infoTable.Group
    data_for_combat = data.T
    print('Nan:',np.sum(np.isnan(data_for_combat)))
    print('Nan:',np.sum(np.isinf(data_for_combat)))
    data_combat = neuroCombat(dat=data_for_combat,
        covars=covars,
        batch_col=['batch'],continuous_cols=['age'],
        categorical_cols=['gender','group'])["data"]
    data_combat = data_combat.T
    return data_combat