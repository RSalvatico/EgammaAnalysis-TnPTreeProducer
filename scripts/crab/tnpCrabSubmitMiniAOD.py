from CRABClient.UserUtilities import config, getUsernameFromSiteDB
import sys
config = config()

submitVersion = "Moriond17_GainSwitch_newTnP_v3"

mainOutputDir = '/store/user/rasharma/TriggerEfficiency/%s' % submitVersion

config.General.transferLogs = True

config.JobType.pluginName  = 'Analysis'

# Name of the CMSSW configuration file
config.JobType.psetName  = 'TnPTreeProducer_cfg.py'
config.Data.allowNonValidInputDataset = False
config.JobType.sendExternalFolder     = True

config.Data.inputDBS = 'global'
config.Data.publication = False

#config.Data.publishDataName = 

config.Site.storageSite = 'T3_US_FNALLPC'



if __name__ == '__main__':

    from CRABAPI.RawCommand import crabCommand
    from CRABClient.ClientExceptions import ClientException
    from httplib import HTTPException

    # We want to put all the CRAB project directories from the tasks we submit here into one common directory.
    # That's why we need to set this parameter (here or above in the configuration file, it does not matter, we will not overwrite it).
    config.General.workArea = 'crab_%s' % submitVersion

    def submit(config):
        try:
            crabCommand('submit', config = config)
        except HTTPException as hte:
            print "Failed submitting task: %s" % (hte.headers)
        except ClientException as cle:
            print "Failed submitting task: %s" % (cle)


    ##### submit MC
    #config.Data.outLFNDirBase = '%s/%s/' % (mainOutputDir,'mc')
    config.Data.outLFNDirBase = '/store/user/rasharma/TriggerEfficiency/Moriond17_GainSwitch_newTnP_v3/mc'
    config.Data.splitting     = 'FileBased'
    config.Data.unitsPerJob   = 8
    config.JobType.pyCfgParams  = ['isMC=True','GT=80X_mcRun2_asymptotic_2016_TrancheIV_v6']

    config.General.requestName  = 'DYToLL_mcAtNLO'
    config.Data.inputDataset    = '/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/MINIAODSIM'
    submit(config)


    config.General.requestName  = 'DYToLL_madgraph_Moriond17'
    config.Data.inputDataset    = '/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v2/MINIAODSIM'
    submit(config)


    ##### now submit DATA
    #config.Data.outLFNDirBase = '%s/%s/' % (mainOutputDir,'data')
    config.Data.outLFNDirBase = '/store/user/rasharma/TriggerEfficiency/Moriond17_GainSwitch_newTnP_v3/data'
    config.Data.splitting     = 'LumiBased'
    config.Data.lumiMask      = '/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions16/13TeV/ReReco/Final/Cert_271036-284044_13TeV_23Sep2016ReReco_Collisions16_JSON.txt'
    config.Data.unitsPerJob   = 100
    config.JobType.pyCfgParams  = ['isMC=False','GT=80X_dataRun2_2016SeptRepro_v7']
 
    config.General.requestName  = '2016rereco_RunB_v2'
    config.Data.inputDataset    = '/SingleElectron/Run2016B-23Sep2016-v2/MINIAOD'
    submit(config)
    config.General.requestName  = '2016rereco_RunB_v3'
    config.Data.inputDataset    = '/SingleElectron/Run2016B-23Sep2016-v3/MINIAOD'
    submit(config)
    config.General.requestName  = '2016rereco_RunC'
    config.Data.inputDataset    = '/SingleElectron/Run2016C-23Sep2016-v1/MINIAOD'
    submit(config)
    config.General.requestName  = '2016rereco_RunD'
    config.Data.inputDataset    = '/SingleElectron/Run2016D-23Sep2016-v1/MINIAOD'
    submit(config)
    config.General.requestName  = '2016rereco_RunE'
    config.Data.inputDataset    = '/SingleElectron/Run2016E-23Sep2016-v1/MINIAOD'
    submit(config)
    config.General.requestName  = '2016rereco_RunF'
    config.Data.inputDataset    = '/SingleElectron/Run2016F-23Sep2016-v1/MINIAOD'
    submit(config)

    config.JobType.pyCfgParams  = ['isMC=False',doEleTree,doPhoTree,doHLTTree,calibEn,'GT=80X_dataRun2_Prompt_v16']
    config.General.requestName  = '2016rereco_RunG'
    config.Data.inputDataset    = '/SingleElectron/Run2016G-23Sep2016-v1/MINIAOD'
    submit(config)
    config.General.requestName  = '2016prompt_RunHv2'
    config.Data.inputDataset    = '/SingleElectron/Run2016H-PromptReco-v2/MINIAOD'
    submit(config)
    config.General.requestName  = '2016prompt_RunHv3'
    config.Data.inputDataset    = '/SingleElectron/Run2016H-PromptReco-v3/MINIAOD'
    submit(config)


