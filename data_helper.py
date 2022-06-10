#!/usr/bin/env python
# coding: utf-8

# In[34]:


import os
import dateutil.parser as dp


# In[5]:


def get_dataset_name(filepath):
    return os.path.basename(filepath)
    
def iso8601_to_epoch_ms(time):
    parsed_time = dp.parse(time)
    return int(parsed_time.timestamp()*1000)
    
def map_to_app_insight_entry(time, experiment_id, experiment_name,env):
    st_time = dp.parse(time['startTimeUtc'])
    st_time1 = int(st_time.timestamp()*1000)
    en_time = dp.parse(time['endTimeUtc'])
    en_time1 = int(en_time.timestamp()*1000)
    return {"resourceGroup": os.environ['RESOURCE_GROUP'],
                "amlWorkSpace": os.environ['WORKSPACE_NAME'],
                "subscriptions": os.environ['SUBSCRIPTION_ID'],
                "run_id": aml_run_details['runId'],
                "experimentName": experiment_name,
                "experimentId": experiment_id,
                "execution_time_ms": en_time1 - st_time1,
                "start_time_utc_ms": st_time1,
                "end_time_utc_ms": en_time1,
                "status": aml_run_details['status'],
                "app_profile": os.environ['APP_PROFILE'],
                "run_type": aml_run_details['properties']['azureml.runsource']
                }


# In[ ]:




