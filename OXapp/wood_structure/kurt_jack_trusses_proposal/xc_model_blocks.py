preprocessor= FEcase.getPreprocessor
nodes= preprocessor.getNodeHandler
elements= preprocessor.getElementHandler
points= preprocessor.getMultiBlockTopology.getPoints
lines= preprocessor.getMultiBlockTopology.getLines
surfaces= preprocessor.getMultiBlockTopology.getSurfaces
groups= preprocessor.getSets
pt0= points.newPntIDPos3d(0,geom.Pos3d(1.79314208719,0.0,0.0)); pt0.setProp("labels",[u'xc_regular_trusses', u'xc_supports'])
pt1= points.newPntIDPos3d(1,geom.Pos3d(1.79314208719,10.1969541374,0.0)); pt1.setProp("labels",[u'xc_regular_trusses', u'xc_supports'])
pt2= points.newPntIDPos3d(2,geom.Pos3d(1.79314208719,10.9246641374,0.0)); pt2.setProp("labels",[u'xc_regular_trusses', u'xc_lvl_blind_fascia', u'xc_east_facade_loads'])
pt3= points.newPntIDPos3d(3,geom.Pos3d(2.09794208719,0.0,0.0)); pt3.setProp("labels",[u'xc_regular_trusses', u'xc_supports'])
pt4= points.newPntIDPos3d(4,geom.Pos3d(2.09794208719,10.1969541374,0.0)); pt4.setProp("labels",[u'xc_regular_trusses', u'xc_supports'])
pt5= points.newPntIDPos3d(5,geom.Pos3d(2.09794208719,10.9246641374,0.0)); pt5.setProp("labels",[u'xc_regular_trusses', u'xc_lvl_blind_fascia', u'xc_east_facade_loads'])
pt6= points.newPntIDPos3d(6,geom.Pos3d(2.40274208719,0.0,0.0)); pt6.setProp("labels",[u'xc_regular_trusses', u'xc_supports'])
pt7= points.newPntIDPos3d(7,geom.Pos3d(2.40274208719,10.1969541374,0.0)); pt7.setProp("labels",[u'xc_regular_trusses', u'xc_supports'])
pt8= points.newPntIDPos3d(8,geom.Pos3d(2.40274208719,10.9246641374,0.0)); pt8.setProp("labels",[u'xc_regular_trusses', u'xc_lvl_blind_fascia', u'xc_east_facade_loads'])
pt9= points.newPntIDPos3d(9,geom.Pos3d(2.70754208719,0.0,0.0)); pt9.setProp("labels",[u'xc_regular_trusses', u'xc_supports'])
pt10= points.newPntIDPos3d(10,geom.Pos3d(2.70754208719,10.1969541374,0.0)); pt10.setProp("labels",[u'xc_regular_trusses', u'xc_supports'])
pt11= points.newPntIDPos3d(11,geom.Pos3d(2.70754208719,10.9246641374,0.0)); pt11.setProp("labels",[u'xc_regular_trusses', u'xc_lvl_blind_fascia', u'xc_east_facade_loads'])
pt12= points.newPntIDPos3d(12,geom.Pos3d(3.01234208719,0.0,0.0)); pt12.setProp("labels",[u'xc_regular_trusses', u'xc_supports'])
pt13= points.newPntIDPos3d(13,geom.Pos3d(3.01234208719,10.1969541374,0.0)); pt13.setProp("labels",[u'xc_regular_trusses', u'xc_supports'])
pt14= points.newPntIDPos3d(14,geom.Pos3d(3.01234208719,10.9246641374,0.0)); pt14.setProp("labels",[u'xc_regular_trusses', u'xc_lvl_blind_fascia', u'xc_east_facade_loads'])
pt15= points.newPntIDPos3d(15,geom.Pos3d(3.31714208719,0.0,0.0)); pt15.setProp("labels",[u'xc_regular_trusses', u'xc_supports'])
pt16= points.newPntIDPos3d(16,geom.Pos3d(3.31714208719,10.1969541374,0.0)); pt16.setProp("labels",[u'xc_regular_trusses', u'xc_supports'])
pt17= points.newPntIDPos3d(17,geom.Pos3d(3.31714208719,10.9246641374,0.0)); pt17.setProp("labels",[u'xc_regular_trusses', u'xc_lvl_blind_fascia', u'xc_east_facade_loads'])
pt18= points.newPntIDPos3d(18,geom.Pos3d(3.62194208719,0.0,0.0)); pt18.setProp("labels",[u'xc_regular_trusses', u'xc_supports'])
pt19= points.newPntIDPos3d(19,geom.Pos3d(3.62194208719,10.1969541374,0.0)); pt19.setProp("labels",[u'xc_regular_trusses', u'xc_supports'])
pt20= points.newPntIDPos3d(20,geom.Pos3d(3.62194208719,10.9246641374,0.0)); pt20.setProp("labels",[u'xc_regular_trusses', u'xc_lvl_blind_fascia', u'xc_east_facade_loads'])
pt21= points.newPntIDPos3d(21,geom.Pos3d(3.92674208719,0.0,0.0)); pt21.setProp("labels",[u'xc_regular_trusses', u'xc_supports'])
pt22= points.newPntIDPos3d(22,geom.Pos3d(3.92674208719,10.1969541374,0.0)); pt22.setProp("labels",[u'xc_regular_trusses', u'xc_supports'])
pt23= points.newPntIDPos3d(23,geom.Pos3d(3.92674208719,10.9246641374,0.0)); pt23.setProp("labels",[u'xc_regular_trusses', u'xc_lvl_blind_fascia', u'xc_east_facade_loads'])
pt24= points.newPntIDPos3d(24,geom.Pos3d(4.23154208719,0.0,0.0)); pt24.setProp("labels",[u'xc_regular_trusses', u'xc_supports'])
pt25= points.newPntIDPos3d(25,geom.Pos3d(4.23154208719,10.1969541374,0.0)); pt25.setProp("labels",[u'xc_regular_trusses', u'xc_supports'])
pt26= points.newPntIDPos3d(26,geom.Pos3d(4.23154208719,10.9246641374,0.0)); pt26.setProp("labels",[u'xc_regular_trusses', u'xc_lvl_blind_fascia', u'xc_east_facade_loads'])
pt27= points.newPntIDPos3d(27,geom.Pos3d(4.53634208719,0.0,0.0)); pt27.setProp("labels",[u'xc_regular_trusses', u'xc_supports'])
pt28= points.newPntIDPos3d(28,geom.Pos3d(4.53634208719,10.1969541374,0.0)); pt28.setProp("labels",[u'xc_regular_trusses', u'xc_supports'])
pt29= points.newPntIDPos3d(29,geom.Pos3d(4.53634208719,10.9246641374,0.0)); pt29.setProp("labels",[u'xc_regular_trusses', u'xc_lvl_blind_fascia', u'xc_east_facade_loads'])
pt30= points.newPntIDPos3d(30,geom.Pos3d(4.84114208719,0.0,0.0)); pt30.setProp("labels",[u'xc_blue_girder', u'xc_supports'])
pt31= points.newPntIDPos3d(31,geom.Pos3d(4.84114208719,0.6096,0.0)); pt31.setProp("labels",[u'xc_blue_girder', u'xc_jack_trusses'])
pt32= points.newPntIDPos3d(32,geom.Pos3d(4.84114208719,10.1969541374,0.0)); pt32.setProp("labels",[u'xc_blue_girder', u'xc_supports'])
pt33= points.newPntIDPos3d(33,geom.Pos3d(4.84114208719,10.9246641374,0.0)); pt33.setProp("labels",[u'xc_blue_girder', u'xc_lvl_blind_fascia', u'xc_east_facade_loads'])
pt34= points.newPntIDPos3d(34,geom.Pos3d(5.14594208719,8.4955551756,0.0)); pt34.setProp("labels",[u'xc_jack_trusses', u'xc_blue_girder'])
pt35= points.newPntIDPos3d(35,geom.Pos3d(5.14594208719,10.9246641374,0.0)); pt35.setProp("labels",[u'xc_jack_trusses', u'xc_lvl_blind_fascia', u'xc_east_facade_loads'])
pt36= points.newPntIDPos3d(36,geom.Pos3d(5.45074208719,8.4955551756,0.0)); pt36.setProp("labels",[u'xc_jack_trusses', u'xc_blue_girder'])
pt37= points.newPntIDPos3d(37,geom.Pos3d(5.45074208719,10.9246641374,0.0)); pt37.setProp("labels",[u'xc_jack_trusses', u'xc_lvl_blind_fascia', u'xc_east_facade_loads'])
pt38= points.newPntIDPos3d(38,geom.Pos3d(5.75554208719,8.4955551756,0.0)); pt38.setProp("labels",[u'xc_jack_trusses', u'xc_blue_girder'])
pt39= points.newPntIDPos3d(39,geom.Pos3d(5.75554208719,10.9246641374,0.0)); pt39.setProp("labels",[u'xc_jack_trusses', u'xc_lvl_blind_fascia', u'xc_east_facade_loads'])
pt40= points.newPntIDPos3d(40,geom.Pos3d(6.06034208719,8.4955551756,0.0)); pt40.setProp("labels",[u'xc_jack_trusses', u'xc_blue_girder'])
pt41= points.newPntIDPos3d(41,geom.Pos3d(6.06034208719,10.9246641374,0.0)); pt41.setProp("labels",[u'xc_jack_trusses', u'xc_lvl_blind_fascia', u'xc_east_facade_loads'])
pt42= points.newPntIDPos3d(42,geom.Pos3d(6.36514208719,8.4955551756,0.0)); pt42.setProp("labels",[u'xc_jack_trusses', u'xc_blue_girder'])
pt43= points.newPntIDPos3d(43,geom.Pos3d(6.36514208719,10.9246641374,0.0)); pt43.setProp("labels",[u'xc_jack_trusses', u'xc_lvl_blind_fascia', u'xc_east_facade_loads'])
pt44= points.newPntIDPos3d(44,geom.Pos3d(5.82189958719,10.1969541374,0.0)); pt44.setProp("labels",[u'xc_bearing_wall'])
pt45= points.newPntIDPos3d(45,geom.Pos3d(0.0,10.1969541374,0.0)); pt45.setProp("labels",[u'xc_bearing_wall'])
pt46= points.newPntIDPos3d(46,geom.Pos3d(6.54960958719,10.9246641374,0.0)); pt46.setProp("labels",[u'xc_south_facade', u'xc_lvl_blind_fascia'])
pt47= points.newPntIDPos3d(47,geom.Pos3d(6.54960958719,-1.93178885101,0.0)); pt47.setProp("labels",[u'xc_south_facade'])
pt48= points.newPntIDPos3d(48,geom.Pos3d(5.82189958719,-1.93178885101,0.0)); pt48.setProp("labels",[u'xc_bearing_wall'])
pt49= points.newPntIDPos3d(49,geom.Pos3d(0.0,0.0,0.0)); pt49.setProp("labels",[u'xc_bearing_wall'])
pt50= points.newPntIDPos3d(50,geom.Pos3d(8.4805657406,0.0,0.0)); pt50.setProp("labels",[u'xc_bearing_wall'])
pt51= points.newPntIDPos3d(51,geom.Pos3d(5.82189958719,0.6096,0.0)); pt51.setProp("labels",[u'xc_jack_trusses', u'xc_supports'])
pt52= points.newPntIDPos3d(52,geom.Pos3d(5.82189958719,1.2192,0.0)); pt52.setProp("labels",[u'xc_jack_trusses', u'xc_supports'])
pt53= points.newPntIDPos3d(53,geom.Pos3d(4.84114208719,1.2192,0.0)); pt53.setProp("labels",[u'xc_jack_trusses', u'xc_blue_girder'])
pt54= points.newPntIDPos3d(54,geom.Pos3d(5.82189958719,1.8223258626,0.0)); pt54.setProp("labels",[u'xc_jack_trusses', u'xc_supports'])
pt55= points.newPntIDPos3d(55,geom.Pos3d(4.84114208719,1.8223258626,0.0)); pt55.setProp("labels",[u'xc_jack_trusses', u'xc_blue_girder'])
pt56= points.newPntIDPos3d(56,geom.Pos3d(5.82189958719,2.4319258626,0.0)); pt56.setProp("labels",[u'xc_jack_trusses', u'xc_supports'])
pt57= points.newPntIDPos3d(57,geom.Pos3d(4.84114208719,2.4319258626,0.0)); pt57.setProp("labels",[u'xc_jack_trusses', u'xc_blue_girder'])
pt58= points.newPntIDPos3d(58,geom.Pos3d(5.82189958719,3.0350517252,0.0)); pt58.setProp("labels",[u'xc_jack_trusses', u'xc_supports'])
pt59= points.newPntIDPos3d(59,geom.Pos3d(4.8411420872,3.0350517252,0.0)); pt59.setProp("labels",[u'xc_jack_trusses', u'xc_blue_girder'])
pt60= points.newPntIDPos3d(60,geom.Pos3d(5.82189958719,3.6446517252,0.0)); pt60.setProp("labels",[u'xc_jack_trusses', u'xc_supports'])
pt61= points.newPntIDPos3d(61,geom.Pos3d(4.8411420872,3.6446517252,0.0)); pt61.setProp("labels",[u'xc_jack_trusses', u'xc_blue_girder'])
pt62= points.newPntIDPos3d(62,geom.Pos3d(5.82189958719,4.2477775878,0.0)); pt62.setProp("labels",[u'xc_jack_trusses', u'xc_supports'])
pt63= points.newPntIDPos3d(63,geom.Pos3d(4.8411420872,4.2477775878,0.0)); pt63.setProp("labels",[u'xc_jack_trusses', u'xc_blue_girder'])
pt64= points.newPntIDPos3d(64,geom.Pos3d(5.82189958719,4.8573775878,0.0)); pt64.setProp("labels",[u'xc_jack_trusses', u'xc_supports'])
pt65= points.newPntIDPos3d(65,geom.Pos3d(4.8411420872,4.8573775878,0.0)); pt65.setProp("labels",[u'xc_jack_trusses', u'xc_blue_girder'])
pt66= points.newPntIDPos3d(66,geom.Pos3d(5.82189958719,5.4605034504,0.0)); pt66.setProp("labels",[u'xc_jack_trusses', u'xc_supports'])
pt67= points.newPntIDPos3d(67,geom.Pos3d(4.8411420872,5.4605034504,0.0)); pt67.setProp("labels",[u'xc_jack_trusses', u'xc_blue_girder'])
pt68= points.newPntIDPos3d(68,geom.Pos3d(5.82189958719,6.0701034504,0.0)); pt68.setProp("labels",[u'xc_jack_trusses', u'xc_supports'])
pt69= points.newPntIDPos3d(69,geom.Pos3d(4.8411420872,6.0701034504,0.0)); pt69.setProp("labels",[u'xc_jack_trusses', u'xc_blue_girder'])
pt70= points.newPntIDPos3d(70,geom.Pos3d(5.82189958719,6.673229313,0.0)); pt70.setProp("labels",[u'xc_jack_trusses', u'xc_supports'])
pt71= points.newPntIDPos3d(71,geom.Pos3d(4.8411420872,6.673229313,0.0)); pt71.setProp("labels",[u'xc_jack_trusses', u'xc_blue_girder'])
pt72= points.newPntIDPos3d(72,geom.Pos3d(5.82189958719,7.282829313,0.0)); pt72.setProp("labels",[u'xc_jack_trusses', u'xc_supports'])
pt73= points.newPntIDPos3d(73,geom.Pos3d(4.8411420872,7.282829313,0.0)); pt73.setProp("labels",[u'xc_jack_trusses', u'xc_blue_girder'])
pt74= points.newPntIDPos3d(74,geom.Pos3d(5.82189958719,7.8859551756,0.0)); pt74.setProp("labels",[u'xc_jack_trusses', u'xc_supports'])
pt75= points.newPntIDPos3d(75,geom.Pos3d(4.8411420872,7.8859551756,0.0)); pt75.setProp("labels",[u'xc_jack_trusses', u'xc_blue_girder'])
pt76= points.newPntIDPos3d(76,geom.Pos3d(6.54960958719,0.6096,0.0)); pt76.setProp("labels",[u'xc_jack_trusses', u'xc_south_facade_loads'])
pt77= points.newPntIDPos3d(77,geom.Pos3d(6.54960958719,1.2192,0.0)); pt77.setProp("labels",[u'xc_jack_trusses', u'xc_south_facade_loads'])
pt78= points.newPntIDPos3d(78,geom.Pos3d(6.54960958719,1.8223258626,0.0)); pt78.setProp("labels",[u'xc_jack_trusses', u'xc_south_facade_loads'])
pt79= points.newPntIDPos3d(79,geom.Pos3d(6.54960958719,2.4319258626,0.0)); pt79.setProp("labels",[u'xc_jack_trusses', u'xc_south_facade_loads'])
pt80= points.newPntIDPos3d(80,geom.Pos3d(6.54960958719,3.0350517252,0.0)); pt80.setProp("labels",[u'xc_jack_trusses', u'xc_south_facade_loads'])
pt81= points.newPntIDPos3d(81,geom.Pos3d(6.54960958719,3.6446517252,0.0)); pt81.setProp("labels",[u'xc_jack_trusses', u'xc_south_facade_loads'])
pt82= points.newPntIDPos3d(82,geom.Pos3d(6.54960958719,4.2477775878,0.0)); pt82.setProp("labels",[u'xc_jack_trusses', u'xc_south_facade_loads'])
pt83= points.newPntIDPos3d(83,geom.Pos3d(6.54960958719,4.8573775878,0.0)); pt83.setProp("labels",[u'xc_jack_trusses', u'xc_south_facade_loads'])
pt84= points.newPntIDPos3d(84,geom.Pos3d(6.54960958719,5.4605034504,0.0)); pt84.setProp("labels",[u'xc_jack_trusses', u'xc_south_facade_loads'])
pt85= points.newPntIDPos3d(85,geom.Pos3d(6.54960958719,6.0701034504,0.0)); pt85.setProp("labels",[u'xc_jack_trusses', u'xc_south_facade_loads'])
pt86= points.newPntIDPos3d(86,geom.Pos3d(6.54960958719,6.673229313,0.0)); pt86.setProp("labels",[u'xc_jack_trusses', u'xc_south_facade_loads'])
pt87= points.newPntIDPos3d(87,geom.Pos3d(6.54960958719,7.282829313,0.0)); pt87.setProp("labels",[u'xc_jack_trusses', u'xc_south_facade_loads'])
pt88= points.newPntIDPos3d(88,geom.Pos3d(6.54960958719,7.8859551756,0.0)); pt88.setProp("labels",[u'xc_jack_trusses', u'xc_south_facade_loads'])
pt89= points.newPntIDPos3d(89,geom.Pos3d(4.8411420872,8.4955551756,0.0)); pt89.setProp("labels",[u'xc_blue_girder'])
pt90= points.newPntIDPos3d(90,geom.Pos3d(6.54960958719,8.4955551756,0.0)); pt90.setProp("labels",[u'xc_blue_girder', u'xc_south_facade_loads', u'xc_south_facade_loads2'])
pt91= points.newPntIDPos3d(91,geom.Pos3d(0.0,10.9246641374,0.0)); pt91.setProp("labels",[u'xc_lvl_blind_fascia', u'xc_supports'])
pt92= points.newPntIDPos3d(92,geom.Pos3d(5.82189958719,8.4955551756,0.0)); pt92.setProp("labels",[u'xc_blue_girder', u'xc_supports'])
l0= lines.newLine(10, 11); l0.setProp("labels",[u'xc_regular_trusses'])
l1= lines.newLine(9, 10); l1.setProp("labels",[u'xc_regular_trusses'])
l2= lines.newLine(12, 13); l2.setProp("labels",[u'xc_regular_trusses'])
l3= lines.newLine(4, 5); l3.setProp("labels",[u'xc_regular_trusses'])
l4= lines.newLine(7, 8); l4.setProp("labels",[u'xc_regular_trusses'])
l5= lines.newLine(6, 7); l5.setProp("labels",[u'xc_regular_trusses'])
l6= lines.newLine(3, 4); l6.setProp("labels",[u'xc_regular_trusses'])
l7= lines.newLine(1, 2); l7.setProp("labels",[u'xc_regular_trusses'])
l8= lines.newLine(65, 67); l8.setProp("labels",[u'xc_blue_girder'])
l9= lines.newLine(0, 1); l9.setProp("labels",[u'xc_regular_trusses'])
l10= lines.newLine(69, 71); l10.setProp("labels",[u'xc_blue_girder'])
l11= lines.newLine(18, 19); l11.setProp("labels",[u'xc_regular_trusses'])
l12= lines.newLine(31, 53); l12.setProp("labels",[u'xc_blue_girder'])
l13= lines.newLine(55, 57); l13.setProp("labels",[u'xc_blue_girder'])
l14= lines.newLine(59, 61); l14.setProp("labels",[u'xc_blue_girder'])
l15= lines.newLine(68, 69); l15.setProp("labels",[u'xc_jack_trusses'])
l16= lines.newLine(70, 71); l16.setProp("labels",[u'xc_jack_trusses'])
l17= lines.newLine(56, 57); l17.setProp("labels",[u'xc_jack_trusses'])
l18= lines.newLine(58, 59); l18.setProp("labels",[u'xc_jack_trusses'])
l19= lines.newLine(52, 53); l19.setProp("labels",[u'xc_jack_trusses'])
l20= lines.newLine(54, 55); l20.setProp("labels",[u'xc_jack_trusses'])
l21= lines.newLine(64, 65); l21.setProp("labels",[u'xc_jack_trusses'])
l22= lines.newLine(66, 67); l22.setProp("labels",[u'xc_jack_trusses'])
l23= lines.newLine(60, 61); l23.setProp("labels",[u'xc_jack_trusses'])
l24= lines.newLine(62, 63); l24.setProp("labels",[u'xc_jack_trusses'])
l25= lines.newLine(71, 73); l25.setProp("labels",[u'xc_blue_girder'])
l26= lines.newLine(75, 89); l26.setProp("labels",[u'xc_blue_girder'])
l27= lines.newLine(63, 65); l27.setProp("labels",[u'xc_blue_girder'])
l28= lines.newLine(67, 69); l28.setProp("labels",[u'xc_blue_girder'])
l29= lines.newLine(92, 40); l29.setProp("labels",[u'xc_blue_girder'])
l30= lines.newLine(34, 36); l30.setProp("labels",[u'xc_blue_girder'])
l31= lines.newLine(74, 75); l31.setProp("labels",[u'xc_jack_trusses'])
l32= lines.newLine(76, 51); l32.setProp("labels",[u'xc_jack_trusses'])
l33= lines.newLine(72, 73); l33.setProp("labels",[u'xc_jack_trusses'])
l34= lines.newLine(79, 56); l34.setProp("labels",[u'xc_jack_trusses'])
l35= lines.newLine(77, 52); l35.setProp("labels",[u'xc_jack_trusses'])
l36= lines.newLine(78, 54); l36.setProp("labels",[u'xc_jack_trusses'])
l37= lines.newLine(13, 14); l37.setProp("labels",[u'xc_regular_trusses'])
l38= lines.newLine(15, 16); l38.setProp("labels",[u'xc_regular_trusses'])
l39= lines.newLine(16, 17); l39.setProp("labels",[u'xc_regular_trusses'])
l40= lines.newLine(73, 75); l40.setProp("labels",[u'xc_blue_girder'])
l41= lines.newLine(19, 20); l41.setProp("labels",[u'xc_regular_trusses'])
l42= lines.newLine(21, 22); l42.setProp("labels",[u'xc_regular_trusses'])
l43= lines.newLine(22, 23); l43.setProp("labels",[u'xc_regular_trusses'])
l44= lines.newLine(24, 25); l44.setProp("labels",[u'xc_regular_trusses'])
l45= lines.newLine(25, 26); l45.setProp("labels",[u'xc_regular_trusses'])
l46= lines.newLine(27, 28); l46.setProp("labels",[u'xc_regular_trusses'])
l47= lines.newLine(89, 34); l47.setProp("labels",[u'xc_blue_girder'])
l48= lines.newLine(40, 42); l48.setProp("labels",[u'xc_blue_girder'])
l49= lines.newLine(36, 38); l49.setProp("labels",[u'xc_blue_girder'])
l50= lines.newLine(2, 91); l50.setProp("labels",[u'xc_lvl_blind_fascia'])
l51= lines.newLine(42, 90); l51.setProp("labels",[u'xc_blue_girder'])
l52= lines.newLine(11, 8); l52.setProp("labels",[u'xc_lvl_blind_fascia'])
l53= lines.newLine(89, 32); l53.setProp("labels",[u'xc_blue_girder'])
l54= lines.newLine(88, 74); l54.setProp("labels",[u'xc_jack_trusses'])
l55= lines.newLine(81, 60); l55.setProp("labels",[u'xc_jack_trusses'])
l56= lines.newLine(80, 58); l56.setProp("labels",[u'xc_jack_trusses'])
l57= lines.newLine(83, 64); l57.setProp("labels",[u'xc_jack_trusses'])
l58= lines.newLine(82, 62); l58.setProp("labels",[u'xc_jack_trusses'])
l59= lines.newLine(85, 68); l59.setProp("labels",[u'xc_jack_trusses'])
l60= lines.newLine(84, 66); l60.setProp("labels",[u'xc_jack_trusses'])
l61= lines.newLine(87, 72); l61.setProp("labels",[u'xc_jack_trusses'])
l62= lines.newLine(86, 70); l62.setProp("labels",[u'xc_jack_trusses'])
l63= lines.newLine(28, 29); l63.setProp("labels",[u'xc_regular_trusses'])
l64= lines.newLine(30, 31); l64.setProp("labels",[u'xc_blue_girder'])
l65= lines.newLine(32, 33); l65.setProp("labels",[u'xc_blue_girder'])
l66= lines.newLine(34, 35); l66.setProp("labels",[u'xc_jack_trusses'])
l67= lines.newLine(36, 37); l67.setProp("labels",[u'xc_jack_trusses'])
l68= lines.newLine(53, 55); l68.setProp("labels",[u'xc_blue_girder'])
l69= lines.newLine(57, 59); l69.setProp("labels",[u'xc_blue_girder'])
l70= lines.newLine(61, 63); l70.setProp("labels",[u'xc_blue_girder'])
l71= lines.newLine(51, 31); l71.setProp("labels",[u'xc_jack_trusses'])
l72= lines.newLine(49, 50); l72.setProp("labels",[u'xc_bearing_wall'])
l73= lines.newLine(44, 48); l73.setProp("labels",[u'xc_bearing_wall'])
l74= lines.newLine(46, 47); l74.setProp("labels",[u'xc_south_facade'])
l75= lines.newLine(2, 5); l75.setProp("labels",[u'xc_lvl_blind_fascia'])
l76= lines.newLine(17, 14); l76.setProp("labels",[u'xc_lvl_blind_fascia'])
l77= lines.newLine(33, 29); l77.setProp("labels",[u'xc_lvl_blind_fascia'])
l78= lines.newLine(39, 37); l78.setProp("labels",[u'xc_lvl_blind_fascia'])
l79= lines.newLine(5, 8); l79.setProp("labels",[u'xc_lvl_blind_fascia'])
l80= lines.newLine(26, 23); l80.setProp("labels",[u'xc_lvl_blind_fascia'])
l81= lines.newLine(17, 20); l81.setProp("labels",[u'xc_lvl_blind_fascia'])
l82= lines.newLine(11, 14); l82.setProp("labels",[u'xc_lvl_blind_fascia'])
l83= lines.newLine(26, 29); l83.setProp("labels",[u'xc_lvl_blind_fascia'])
l84= lines.newLine(20, 23); l84.setProp("labels",[u'xc_lvl_blind_fascia'])
l85= lines.newLine(33, 35); l85.setProp("labels",[u'xc_lvl_blind_fascia'])
l86= lines.newLine(39, 41); l86.setProp("labels",[u'xc_lvl_blind_fascia'])
l87= lines.newLine(35, 37); l87.setProp("labels",[u'xc_lvl_blind_fascia'])
l88= lines.newLine(38, 92); l88.setProp("labels",[u'xc_blue_girder'])
l89= lines.newLine(43, 46); l89.setProp("labels",[u'xc_lvl_blind_fascia'])
l90= lines.newLine(43, 41); l90.setProp("labels",[u'xc_lvl_blind_fascia'])
l91= lines.newLine(42, 43); l91.setProp("labels",[u'xc_jack_trusses'])
l92= lines.newLine(40, 41); l92.setProp("labels",[u'xc_jack_trusses'])
l93= lines.newLine(38, 39); l93.setProp("labels",[u'xc_jack_trusses'])
l94= lines.newLine(44, 45); l94.setProp("labels",[u'xc_bearing_wall'])
