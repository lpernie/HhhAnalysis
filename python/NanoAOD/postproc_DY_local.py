#!/usr/bin/env python
import os, sys
import ROOT
ROOT.PyConfig.IgnoreCommandLineOptions = True

from PhysicsTools.NanoAODTools.postprocessing.framework.postprocessor import PostProcessor

from HHbbWWProducer import *
from PhysicsTools.NanoAODTools.postprocessing.modules.btv.btagSFProducer import *
from PhysicsTools.NanoAODTools.postprocessing.modules.jme.jecUncertainties import *
from PhysicsTools.NanoAODTools.postprocessing.modules.jme.jetmetUncertainties import *
from PhysicsTools.NanoAODTools.postprocessing.modules.common.lepSFProducer import *
from PhysicsTools.NanoAODTools.postprocessing.modules.jme.mht import *
from PhysicsTools.NanoAODTools.postprocessing.modules.common.puWeightProducer import *
#from  PhysicsTools.NanoAODTools.postprocessing.examples.puWeightProducer import *


files = ["root://cms-xrd-global.cern.ch//store/mc/RunIISummer16NanoAOD/GluGluToBulkGravitonToHHTo2B2VTo2L2Nu_M-400_narrow_13TeV-madgraph-v2/NANOAODSIM/PUMoriond17_05Feb2018_94X_mcRun2_asymptotic_v2-v1/00000/82738046-5711-E811-ADAF-0CC47A4D75F0.root"]
filesTTbar= [
'root://cms-xrd-global.cern.ch//store/group/cmst3/group/nanoAOD/NanoTestProd006/TTJets_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/RunIISummer17MiniAOD-92X-NanoCrabProd006/171006_155430/0000/nanolzma_1.root',
]
filesTTbar = ["/fdata/hepx/store/user/taohuang/HH_NanoAOD/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8_RunIIFall17_NanoAOD.root"]
filesSignal = ["/fdata/hepx/store/user/taohuang/HH_NanoAOD/GravitonToHHTo2B2VTo2L2Nu_M-400_narrow_13TeV_NanoAOD_2.root"]
filesdata_MuMu = ["/fdata/hepx/store/user/taohuang/HH_NanoAOD/Run2016B_DoubleMuon_EC6E35C0-630C-E811-AB01-00215A450982.root"]
filesdata_ElEl = ["/fdata/hepx/store/user/taohuang/HH_NanoAOD/Run2016B_DoubleEG_E8EE52A1-4D0C-E811-BFE1-90E2BACC5EEC.root"]
filesdata_MuEl = ["/fdata/hepx/store/user/taohuang/HH_NanoAOD/Run2016B_MuonEG_E480DF59-890C-E811-995A-0242AC130002.root"]
filesDY0j = ["/fdata/hepx/store/user/taohuang/NANOAOD/DYToLL_0J_13TeV-amcatnloFXFX-pythia8/84C5AEED-8E19-E811-9948-F04DA2757237.root"]


#selection='''(Sum$(Electron_pt > 20 && Electron_mvaSpring16GP_WP90) >= 2  ||
# Sum$(Muon_pt > 20) >= 2 ||
# Sum$(Electron_pt > 20 && Electron_mvaSpring16GP_WP80) >= 1   ||
# Sum$(Muon_pt > 20 && Muon_tightId) >= 1 ||
# (Sum$(Muon_pt > 20) == 0 && Sum$(Electron_pt > 20 && Electron_mvaSpring16GP_WP90) == 0 && MET_pt > 150 ) ) 
# &&  Sum$((abs(Jet_eta)<2.5 && Jet_pt > 20 && Jet_jetId)) >= 2 && Entry$ < 1000 
#'''
#
#selectionALL='''Sum$(Electron_pt > 20 && Electron_mvaSpring16GP_WP90) >= 2  ||
# Sum$(Electron_pt > 20 && Electron_mvaSpring16GP_WP80) >= 1   ||
# Sum$(Jet_pt > 40 && Jet_jetId) >= 4   || 
#Sum$(Jet_pt *(abs(Jet_eta)<2.5 && Jet_pt > 20 && Jet_jetId)) > 160  || 
#MET_pt > 100  || Sum$(Muon_pt > 20 && Muon_tightId) >= 1
#'''
###mhtProducer(jetSelection, muonSelection, electronSelection), adding the selected obj and filling MHT_pt and MHT_phi
mht_hh = lambda : mhtProducer( lambda j : j.pt > 20 and abs(j.eta) < 2.4,
                            lambda mu : mu.pt > 10 and abs(mu.eta) < 2.4,
                            lambda el : el.pt > 10 and abs(el.eta) < 2.5 )

#p=PostProcessor(".",files,selection.replace('\n',' '),"keep_and_drop.txt",[puAutoWeight(),jetmetUncertainties2016All(), btagSF2016, hhbbWW()],provenance=True)
#p=PostProcessor(".",files,selection.replace('\n',' '),"keep_and_drop.txt",[puAutoWeight(),jetmetUncertainties2016All(), btagSF2016(), hhbbWW()],provenance=True)
#p=PostProcessor(".",files,selection.replace('\n',' '),"keep_and_drop.txt",[puAutoWeight(), hhbbWW()],provenance=True)
#p=PostProcessor(".",filesSignal,"1","keep_and_drop.txt",[puAutoWeight(), lepSF(), btagSF2016(), mht_hh(), hhbbWW()],provenance=True)
##cp leptonSF/cMVAv2_Moriond17_B_H.csv   ../../../PhysicsTools/NanoAODTools/data/btagSF/
btagSF2016_cMVA = lambda : btagSFProducer("2016",  algo = 'cmva', sfFileName='cMVAv2_Moriond17_B_H.csv')
btagSF2017_cMVA = lambda : btagSFProducer("2017",  algo = 'cmva')
outputdir = "/fdata/hepx/store/user/taohuang/HH_NanoAOD"
#p=PostProcessor(outputdir, filesTTbar, cut = "1", branchsel = "keep_and_drop_pre.txt", modules = [ ], friend = False, provenance=True, outputbranchsel="keep_and_drop_out.txt")
p=PostProcessor(outputdir, filesTTbar, cut = "1", branchsel = "keep_and_drop_pre.txt", modules = [puAutoWeight(), btagSF2016_cMVA(), mht_hh(), HHbbWWProducer(True,  DYestimation = True,verbose = 1) ], friend = True, provenance=True)
#p=PostProcessor(".",filesdata_MuMu,"1","keep_and_drop.txt",[mht_hh(), hhbbWW_data("DoubleMuon")],provenance=True)
#p=PostProcessor(".",filesdata_MuEl,"1","keep_and_drop.txt",[mht_hh(), hhbbWW_data("MuonEG")],provenance=True)
#p=PostProcessor(".",filesdata_ElEl,"1","keep_and_drop.txt",[mht_hh(), hhbbWW_data("DoubleEG")],provenance=True)

p.run()

