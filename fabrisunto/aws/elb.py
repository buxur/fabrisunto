# -*- coding: UTF-8 -*-
import os, requests, json, time

class ELB:
    '''Common Class for aws elb objects'''

    def __init__(self,region,environmentname):
        self.region = region
        self.envname = environmentname
        self.client = boto3.client('elasticbeanstalk', region_name=self.region)

    def getStatus(botoclient, envid):
        try:
            eid = [envid]
            response = botoclient.describe_environments(EnvironmentIds=eid)
            for e in response['Environments']:
                if e['Health']:
                    return e['Health']
                else:
                    return ""
        except ClientError as e:
            print "[error] "+e.response['Error']['Message']

    def getAppVersion(envid):
        response = self.client.describe_environments(EnvironmentIds=[envid])
        version = ''
        for e in response['Environments']:
            version = e['VersionLabel']
        return version

    def getEnvironmentInfo():
        response = self.client.describe_environments()
        # Parse the environments
        for e in response['Environments']:
            if e['EnvironmentName'] == self.envname:
                appName = e['ApplicationName']
                envID = e['EnvironmentId']


