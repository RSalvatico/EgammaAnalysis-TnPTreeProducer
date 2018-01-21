# EgammaAnalysis-TnPTreeProducer
TnP package for EGM: Twiki link: [here](https://twiki.cern.ch/twiki/bin/view/CMSPublic/ElectronTagAndProbe#Workflow_Description_in_80X)

## How to setup

	cmsrel CMSSW_8_0_27
	cd CMSSW_8_0_27/src
	cmsenv
	git cms-init
	git cms-merge-topic cms-egamma:EGM_gain_v1
	cd EgammaAnalysis/ElectronTools/data
	git clone -b Moriond17_gainSwitch_unc https://github.com/ECALELFS/ScalesSmearings.git
	cd $CMSSW_BASE/src
	git clone -b v2017.05.23_legacy80X_prelim https://github.com/cms-analysis/EgammaAnalysis-TnPTreeProducer EgammaAnalysis/TnPTreeProducer
	scram b -j8
	cd EgammaAnalysis/TnPTreeProducer/
	cmsenv
	cmsRun python/TnPTreeProducer_cfg.py doEleID=True isMC=False maxEvents=5000

### To submit crab jobs

	python ../scripts/crab/tnpCrabSubmitMiniAOD.py

