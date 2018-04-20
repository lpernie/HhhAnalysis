#!/bin/bash
cd $CMSSW_BASE/src/HhhAnalysis/python/DYEstimation/
	    
sbatch Btaggingeff/Send_btaggingeff_TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8.slrm
 
sbatch Btaggingeff/Send_btaggingeff_DYJetsToLL_M-10to50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8.slrm
 
sbatch Btaggingeff/Send_btaggingeff_DYToLL_0J_13TeV-amcatnloFXFX-pythia8.slrm
 
sbatch Btaggingeff/Send_btaggingeff_DYToLL_1J_13TeV-amcatnloFXFX-pythia8.slrm
 
sbatch Btaggingeff/Send_btaggingeff_DYToLL_2J_13TeV-amcatnloFXFX-pythia8.slrm
 
sbatch Btaggingeff/Send_btaggingeff_ST_t-channel_top_4f_inclusiveDecays_13TeV-powhegV2-madspin-pythia8_TuneCUETP8M1.slrm
 
sbatch Btaggingeff/Send_btaggingeff_ST_t-channel_antitop_4f_inclusiveDecays_13TeV-powhegV2-madspin-pythia8_TuneCUETP8M1.slrm
 
sbatch Btaggingeff/Send_btaggingeff_ST_s-channel_4f_leptonDecays_13TeV-amcatnlo-pythia8_TuneCUETP8M1.slrm
 
sbatch Btaggingeff/Send_btaggingeff_ST_tW_antitop_5f_NoFullyHadronicDecays_13TeV-powheg_TuneCUETP8M1.slrm
 
sbatch Btaggingeff/Send_btaggingeff_ST_tW_top_5f_NoFullyHadronicDecays_13TeV-powheg_TuneCUETP8M1.slrm
 