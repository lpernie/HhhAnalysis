def hist1D(tree, todraw, xbins, cut, B):

    xBins = int(x_bins[1:-1].split(',')[0])
    xminBin = float(x_bins[1:-1].split(',')[1])
    xmaxBin = float(x_bins[1:-1].split(',')[2])
    b1 = ROOT.TH1F("%s"%B,"%s"%B,xBins,xminBin,xmaxBin)
    tree.Draw("%s>>%s"%(todraw,B),cut)
    ROOT.SetOwnership(b1, False)
    #b1.Print()
    return b1

#___________________________________________
def draw1D_v2(filelist,x_bins,x_title,cut,benchmarks, pic_name):
    

    xBins = int(x_bins[1:-1].split(',')[0])
    xminBin = float(x_bins[1:-1].split(',')[1])
    xmaxBin = float(x_bins[1:-1].split(',')[2])
    b1 = ROOT.TH1F("b1","b1",xBins,xminBin,xmaxBin)
    b1.SetTitle("h2#rightarrow hh#rightarrow WWWW"+" "*24 + "14TeV")
    b1.GetYaxis().SetTitle("Events")
    b1.GetXaxis().SetTitle("%s"%x_title)
    #b1.GetYaxis().SetRangeUser(0.0,10000)
    b1.SetStats(0)
     


    color = [ROOT.kRed, ROOT.kBlue, ROOT.kMagenta+2, ROOT.kGreen+2, ROOT.kCyan]
    maker = [20,21,22,23,34]
    legend = ROOT.TLegend(0.75,0.6,0.86,0.94)
    legend.SetFillColor(ROOT.kWhite)
#    legend.SetFillStyle(0)
    legend.SetTextSize(0.05)
    legend.SetTextFont(62)
    hs1 = ROOT.THStack("hs1","%s distribution"%x_title)
    hs2 = ROOT.THStack("hs2","%s distribution"%x_title)
    hs3 = ROOT.THStack("hs3","%s distribution"%x_title)
    hs4 = ROOT.THStack("hs4","%s distribution"%x_title)
    hists_1 = []
    hists_2 = []
    hists_3 = []
    hists_4 = []
    for nfile in range(len(filelist)):
	hists_1.append(ROOT.TH1F("hist1_%d"%nfile,"hist1_%d"%nfile, 190, 200, 4000))
	hists_2.append(ROOT.TH1F("hist2_%d"%nfile,"hist2_%d"%nfile, 190, 200, 4000))
	hists_3.append(ROOT.TH1F("hist3_%d"%nfile,"hist3_%d"%nfile,30,0,300))
	hists_4.append(ROOT.TH1F("hist4_%d"%nfile,"hist4_%d"%nfile,30,0,900))
	
    for nfile in range(len(filelist)):
	
	rootfile = filelist[nfile]
	B = benchmarks[nfile]
    	f = ROOT.TFile(rootfile)
	lists = f.GetListOfKeys()
	for x in range(len(lists)):
		subkey = lists.At(x)
		obj = subkey.ReadObj()
		if obj.GetName()=="evtree":
			continue
		print " title ",obj.GetTitle()," Name ",obj.GetName()
		maxbin = obj.GetMaximumBin()
		
		hists_1[nfile].Fill(obj.GetXaxis().GetBinCenter(maxbin))
		hists_3[nfile].Fill(obj.GetBinContent(maxbin))
		hists_4[nfile].Fill(obj.Integral())
		obj.Scale(1.0/obj.Integral())
		hists_2[nfile].Add(obj.Rebin(20))
	hists_1[nfile].SetLineColor(color[nfile])
	hists_1[nfile].SetMarkerColor(color[nfile])
	hists_1[nfile].SetMarkerStyle(maker[nfile])
	
	hists_2[nfile].SetLineColor(color[nfile])
	hists_2[nfile].SetMarkerColor(color[nfile])
	hists_2[nfile].SetMarkerStyle(maker[nfile])

	hists_3[nfile].SetLineColor(color[nfile])
	hists_3[nfile].SetMarkerColor(color[nfile])
	hists_3[nfile].SetMarkerStyle(maker[nfile])

	hists_4[nfile].SetLineColor(color[nfile])
	hists_4[nfile].SetMarkerColor(color[nfile])
	hists_4[nfile].SetMarkerStyle(maker[nfile])
	
	if (nfile==len(filelist)-1):
		hists_1[nfile].Scale(1.0/5.0)
		hists_2[nfile].Scale(1.0/5.0)
	hists_3[nfile].Scale(1.0/hists_3[nfile].Integral())
	hists_4[nfile].Scale(1.0/hists_4[nfile].Integral())

	hs1.Add(hists_1[nfile])
	hs2.Add(hists_2[nfile])
	hs3.Add(hists_3[nfile])
	hs4.Add(hists_4[nfile])
	legend.AddEntry(hists_1[nfile], "%s"%B, "pl")
    
    c1 = ROOT.TCanvas()
    c1.SetGridx()
    c1.SetGridy()
    c1.SetTickx()
    c1.SetTicky()
  
    c1.Divide(2,2)
    c1.cd(1)
    hs1.Draw("nostack+p")
    hs1.GetHistogram().GetXaxis().SetTitle("%s"%x_title)
    hs1.GetHistogram().GetXaxis().SetRangeUser(xminBin, xmaxBin)
    legend.Draw("same")
    tex1 = ROOT.TLatex(0.25,.50,"Most probable mass")
    tex1.SetTextSize(0.05)
    tex1.SetTextFont(62)
    tex1.SetNDC()
    tex1.Draw("same")

    c1.cd(2)
    hs2.Draw("nostack+p")
    hs2.GetHistogram().GetXaxis().SetTitle("%s"%x_title)
    hs2.GetHistogram().GetXaxis().SetRangeUser(xminBin, xmaxBin)
    legend.Draw("same")
    tex2 = ROOT.TLatex(0.25,.50,"add all survival solution(normalized in each event)")
    tex2.SetTextSize(0.05)
    tex2.SetTextFont(62)
    tex2.SetNDC()
    tex2.Draw("same")

    c1.cd(3)
    hs3.Draw("nostack+p")
    hs3.SetTitle("bincontent of maximum bin, normalized  distribution")
    hs3.GetHistogram().GetXaxis().SetTitle("maximum bincontent")
    legend.Draw("same")
    tex3 = ROOT.TLatex(0.25,.50,"maximum  bin content from MMC")
    tex3.SetTextSize(0.05)
    tex3.SetTextFont(62)
    tex3.SetNDC()
    tex3.Draw("same")

    c1.cd(4)
    hs4.SetTitle("total number of survival solutions, normalized distribution")
    hs4.Draw("nostack+p")
    hs4.GetHistogram().GetXaxis().SetTitle("total number of survival solutions")
    legend.Draw("same")
    tex4 = ROOT.TLatex(0.25,.50,"total number of survival solutions")
    tex4.SetTextSize(0.05)
    tex4.SetTextFont(62)
    tex4.SetNDC()
    tex4.Draw("same")

    c1.cd()

    c1.SaveAs("Hhh_PDFvalidation_%s_combined.png"%pic_name)
    
	
		
#___________________________________________
def draw1D(filelist,dir,todraw,x_bins,x_title,cut,benchmarks, pic_name):
    
    c1 = ROOT.TCanvas()
    c1.SetGridx()
    c1.SetGridy()
    c1.SetTickx()
    c1.SetTicky()

    xBins = int(x_bins[1:-1].split(',')[0])
    xminBin = float(x_bins[1:-1].split(',')[1])
    xmaxBin = float(x_bins[1:-1].split(',')[2])
    
    b1 = ROOT.TH1F("b1","b1",xBins,xminBin,xmaxBin)
    b1.SetTitle("h2#rightarrow hh#rightarrow WWWW"+" "*24 + "14TeV")
    b1.GetYaxis().SetTitle("Events")
    b1.GetXaxis().SetTitle("%s"%x_title)
    b1.GetYaxis().SetRangeUser(0.0,10000)
    b1.SetStats(0)
    #b1.SetLogx()
    b1.Draw()
    #c1.SetLogx()
 
    color = [ROOT.kRed, ROOT.kBlue, ROOT.kMagenta+2, ROOT.kGreen+2, ROOT.kCyan]
    maker = [20,21,22,23,34]
    legend = ROOT.TLegend(0.65,0.65,0.8,0.94)
    legend.SetFillColor(ROOT.kWhite)
#    legend.SetFillStyle(0)
    legend.SetTextSize(0.05)
    legend.SetTextFont(62)
    #hs = ROOT.THStack("hs","%s distribution"%x_title)
    hs = ROOT.THStack("hs"," ")
    hists = []
    for nfile in range(len(filelist)):
        chain = ROOT.TChain(dir)	
	filedir = filelist[nfile]
	B = benchmarks[nfile]
    	if os.path.isdir(filedir):
          ls = os.listdir(filedir)
          for x in ls:
                x = filedir[:]+x
                if os.path.isdir(x):
                        continue
                chain.Add(x)
    	elif os.path.isfile(filedir):
          chain.Add(filedir)
    	else:
          print " it is not file or dir ", filedir

	#chain.Draw("%s>>%s(%d,%f,%f)"%(todraw,B, xBins, xminBin, xmaxBin ), cut)
	hist = hist1D(chain, todraw, x_bins, cut, B)
	#hs.Add(ROOT.TH1F(ROOT.gDirectory.Get(B)))
        #legend.AddEntry(ROOT.TH1F(ROOT.gDirectory.Get(B)),"%s"%B,"pl") 
	#hists.append(ROOT.TH1F(ROOT.gDirectory.Get(B)).Clone(B))
	hist.SetLineColor(color[nfile])
	hist.SetLineWidth(3)
	hist.SetMarkerColor(color[nfile])
	hist.SetMarkerStyle(maker[nfile])
	hist.Scale(1.0/hist.GetEntries())
        hs.Add(hist)
        
	legend.AddEntry(hist, "%s"%B, "l")

	#htmp = hist1D(t, todraw, x_bins, cut, B)
	#htmp.Print("ALL")
	hists.append(hist)
	print "nfile ",nfile," B ",B
    print "hists ",hists	
 
    hs.Draw("nostack")
    hs.GetHistogram().GetXaxis().SetTitle("%s"%x_title)
    hs.GetHistogram().GetYaxis().SetTitle("Normalized to unity")
    legend.Draw("same")
    c1.SaveAs("paper_test/Hhh_PDFvalidation_hasdRljet_%s.pdf"%pic_name)
    c1.SaveAs("paper_test/Hhh_PDFvalidation_hasdRljet_%s.png"%pic_name)
    c1.SaveAs("paper_test/Hhh_PDFvalidation_hasdRljet_%s.C"%pic_name)

