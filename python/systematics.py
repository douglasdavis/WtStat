from collections import OrderedDict

SYS_WEIGHTS = OrderedDict()
SYS_WEIGHTS['JVT'          ] =  ['weight_sys_jvt_UP'                                        , 'weight_sys_jvt_DOWN'                                        , 'Weights'      , '40' , 'JVT' ]
SYS_WEIGHTS['Pileup'       ] =  ['weight_sys_pileup_UP'                                     , 'weight_sys_pileup_DOWN'                                     , 'Weights'      , '40' , 'Pileup' ]
SYS_WEIGHTS['EL_Trig'      ] =  ['weight_sys_leptonSF_EL_SF_Trigger_UP'                     , 'weight_sys_leptonSF_EL_SF_Trigger_DOWN'                     , 'WeightLepSFs' , '40' , 'Electron Trig']
SYS_WEIGHTS['EL_Reco'      ] =  ['weight_sys_leptonSF_EL_SF_Reco_UP'                        , 'weight_sys_leptonSF_EL_SF_Reco_DOWN'                        , 'WeightLepSFs' , '40' , 'Electron Reco']
SYS_WEIGHTS['EL_ID'        ] =  ['weight_sys_leptonSF_EL_SF_ID_UP'                          , 'weight_sys_leptonSF_EL_SF_ID_DOWN'                          , 'WeightLepSFs' , '40' , 'Electron ID']
SYS_WEIGHTS['EL_Isol'      ] =  ['weight_sys_leptonSF_EL_SF_Isol_UP'                        , 'weight_sys_leptonSF_EL_SF_Isol_DOWN'                        , 'WeightLepSFs' , '40' , 'Electron Isol']
SYS_WEIGHTS['MU_TrigStat'  ] =  ['weight_sys_leptonSF_MU_SF_Trigger_STAT_UP'                , 'weight_sys_leptonSF_MU_SF_Trigger_STAT_DOWN'                , 'WeightLepSFs' , '40' , 'Muon TrigStat']
SYS_WEIGHTS['MU_TrigSyst'  ] =  ['weight_sys_leptonSF_MU_SF_Trigger_SYST_UP'                , 'weight_sys_leptonSF_MU_SF_Trigger_SYST_DOWN'                , 'WeightLepSFs' , '40' , 'Muon TrigSyst']
SYS_WEIGHTS['MU_IDStat'    ] =  ['weight_sys_leptonSF_MU_SF_ID_STAT_UP'                     , 'weight_sys_leptonSF_MU_SF_ID_STAT_DOWN'                     , 'WeightLepSFs' , '40' , 'Muon IDStat']
SYS_WEIGHTS['MU_IDSyst'    ] =  ['weight_sys_leptonSF_MU_SF_ID_SYST_UP'                     , 'weight_sys_leptonSF_MU_SF_ID_SYST_DOWN'                     , 'WeightLepSFs' , '40' , 'Muon IDSyst']
SYS_WEIGHTS['MU_IDStatLPT' ] =  ['weight_sys_leptonSF_MU_SF_ID_STAT_LOWPT_UP'               , 'weight_sys_leptonSF_MU_SF_ID_STAT_LOWPT_DOWN'               , 'WeightLepSFs' , '40' , 'Muon IDStatLPT' ]
SYS_WEIGHTS['MU_IDSystLPT' ] =  ['weight_sys_leptonSF_MU_SF_ID_SYST_LOWPT_UP'               , 'weight_sys_leptonSF_MU_SF_ID_SYST_LOWPT_DOWN'               , 'WeightLepSFs' , '40' , 'Muon IDSystLPT' ]
SYS_WEIGHTS['MU_IsolStat'  ] =  ['weight_sys_leptonSF_MU_SF_Isol_STAT_UP'                   , 'weight_sys_leptonSF_MU_SF_Isol_STAT_DOWN'                   , 'WeightLepSFs' , '40' , 'Muon IsolStat'  ]
SYS_WEIGHTS['MU_IsolSyst'  ] =  ['weight_sys_leptonSF_MU_SF_Isol_SYST_UP'                   , 'weight_sys_leptonSF_MU_SF_Isol_SYST_DOWN'                   , 'WeightLepSFs' , '40' , 'Muon IsolSyst'  ]
SYS_WEIGHTS['MU_TTVAStat'  ] =  ['weight_sys_leptonSF_MU_SF_TTVA_STAT_UP'                   , 'weight_sys_leptonSF_MU_SF_TTVA_STAT_DOWN'                   , 'WeightLepSFs' , '40' , 'Muon TTVAStat'  ]
SYS_WEIGHTS['MU_TTVASyst'  ] =  ['weight_sys_leptonSF_MU_SF_TTVA_SYST_UP'                   , 'weight_sys_leptonSF_MU_SF_TTVA_SYST_DOWN'                   , 'WeightLepSFs' , '40' , 'Muon TTVASyst'  ]

SYS_WEIGHTS['B_ev_B_0'     ] =  ['weight_sys_bTagSF_MV2c10_Continuous_eigenvars_B_0_up'     , 'weight_sys_bTagSF_MV2c10_Continuous_eigenvars_B_0_down'     , 'WeightBTag'   , '40' , 'b-tag eigenv B0'     ]
SYS_WEIGHTS['B_ev_B_1'     ] =  ['weight_sys_bTagSF_MV2c10_Continuous_eigenvars_B_1_up'     , 'weight_sys_bTagSF_MV2c10_Continuous_eigenvars_B_1_down'     , 'WeightBTag'   , '40' , 'b-tag eigenv B1'     ]
SYS_WEIGHTS['B_ev_B_2'     ] =  ['weight_sys_bTagSF_MV2c10_Continuous_eigenvars_B_2_up'     , 'weight_sys_bTagSF_MV2c10_Continuous_eigenvars_B_2_down'     , 'WeightBTag'   , '40' , 'b-tag eigenv B2'     ]
SYS_WEIGHTS['B_ev_B_3'     ] =  ['weight_sys_bTagSF_MV2c10_Continuous_eigenvars_B_3_up'     , 'weight_sys_bTagSF_MV2c10_Continuous_eigenvars_B_3_down'     , 'WeightBTag'   , '40' , 'b-tag eigenv B3'     ]
SYS_WEIGHTS['B_ev_B_4'     ] =  ['weight_sys_bTagSF_MV2c10_Continuous_eigenvars_B_4_up'     , 'weight_sys_bTagSF_MV2c10_Continuous_eigenvars_B_4_down'     , 'WeightBTag'   , '40' , 'b-tag eigenv B4'     ]
SYS_WEIGHTS['B_ev_B_5'     ] =  ['weight_sys_bTagSF_MV2c10_Continuous_eigenvars_B_5_up'     , 'weight_sys_bTagSF_MV2c10_Continuous_eigenvars_B_5_down'     , 'WeightBTag'   , '40' , 'b-tag eigenv B5'     ]
SYS_WEIGHTS['B_ev_B_6'     ] =  ['weight_sys_bTagSF_MV2c10_Continuous_eigenvars_B_6_up'     , 'weight_sys_bTagSF_MV2c10_Continuous_eigenvars_B_6_down'     , 'WeightBTag'   , '40' , 'b-tag eigenv B6'     ]
SYS_WEIGHTS['B_ev_B_7'     ] =  ['weight_sys_bTagSF_MV2c10_Continuous_eigenvars_B_7_up'     , 'weight_sys_bTagSF_MV2c10_Continuous_eigenvars_B_7_down'     , 'WeightBTag'   , '40' , 'b-tag eigenv B7'     ]
SYS_WEIGHTS['B_ev_B_8'     ] =  ['weight_sys_bTagSF_MV2c10_Continuous_eigenvars_B_8_up'     , 'weight_sys_bTagSF_MV2c10_Continuous_eigenvars_B_8_down'     , 'WeightBTag'   , '40' , 'b-tag eigenv B8'     ]
SYS_WEIGHTS['B_ev_B_9'     ] =  ['weight_sys_bTagSF_MV2c10_Continuous_eigenvars_B_9_up'     , 'weight_sys_bTagSF_MV2c10_Continuous_eigenvars_B_9_down'     , 'WeightBTag'   , '40' , 'b-tag eigenv B9'     ]
SYS_WEIGHTS['B_ev_B_10'     ] =  ['weight_sys_bTagSF_MV2c10_Continuous_eigenvars_B_10_up'     , 'weight_sys_bTagSF_MV2c10_Continuous_eigenvars_B_10_down'     , 'WeightBTag'   , '40' , 'b-tag eigenv B10'     ]
SYS_WEIGHTS['B_ev_B_11'     ] =  ['weight_sys_bTagSF_MV2c10_Continuous_eigenvars_B_11_up'     , 'weight_sys_bTagSF_MV2c10_Continuous_eigenvars_B_11_down'     , 'WeightBTag'   , '40' , 'b-tag eigenv B11'     ]
SYS_WEIGHTS['B_ev_B_12'     ] =  ['weight_sys_bTagSF_MV2c10_Continuous_eigenvars_B_12_up'     , 'weight_sys_bTagSF_MV2c10_Continuous_eigenvars_B_12_down'     , 'WeightBTag'   , '40' , 'b-tag eigenv B12'     ]
SYS_WEIGHTS['B_ev_B_13'     ] =  ['weight_sys_bTagSF_MV2c10_Continuous_eigenvars_B_13_up'     , 'weight_sys_bTagSF_MV2c10_Continuous_eigenvars_B_13_down'     , 'WeightBTag'   , '40' , 'b-tag eigenv B13'     ]
SYS_WEIGHTS['B_ev_B_14'     ] =  ['weight_sys_bTagSF_MV2c10_Continuous_eigenvars_B_14_up'     , 'weight_sys_bTagSF_MV2c10_Continuous_eigenvars_B_14_down'     , 'WeightBTag'   , '40' , 'b-tag eigenv B14'     ]
SYS_WEIGHTS['B_ev_B_15'     ] =  ['weight_sys_bTagSF_MV2c10_Continuous_eigenvars_B_15_up'     , 'weight_sys_bTagSF_MV2c10_Continuous_eigenvars_B_15_down'     , 'WeightBTag'   , '40' , 'b-tag eigenv B15'     ]
SYS_WEIGHTS['B_ev_B_16'     ] =  ['weight_sys_bTagSF_MV2c10_Continuous_eigenvars_B_16_up'     , 'weight_sys_bTagSF_MV2c10_Continuous_eigenvars_B_16_down'     , 'WeightBTag'   , '40' , 'b-tag eigenv B16'     ]
SYS_WEIGHTS['B_ev_B_17'     ] =  ['weight_sys_bTagSF_MV2c10_Continuous_eigenvars_B_17_up'     , 'weight_sys_bTagSF_MV2c10_Continuous_eigenvars_B_17_down'     , 'WeightBTag'   , '40' , 'b-tag eigenv B17'     ]
SYS_WEIGHTS['B_ev_B_18'     ] =  ['weight_sys_bTagSF_MV2c10_Continuous_eigenvars_B_18_up'     , 'weight_sys_bTagSF_MV2c10_Continuous_eigenvars_B_18_down'     , 'WeightBTag'   , '40' , 'b-tag eigenv B18'     ]
SYS_WEIGHTS['B_ev_B_19'     ] =  ['weight_sys_bTagSF_MV2c10_Continuous_eigenvars_B_19_up'     , 'weight_sys_bTagSF_MV2c10_Continuous_eigenvars_B_19_down'     , 'WeightBTag'   , '40' , 'b-tag eigenv B19'     ]
SYS_WEIGHTS['B_ev_B_20'     ] =  ['weight_sys_bTagSF_MV2c10_Continuous_eigenvars_B_20_up'     , 'weight_sys_bTagSF_MV2c10_Continuous_eigenvars_B_20_down'     , 'WeightBTag'   , '40' , 'b-tag eigenv B20'     ]
SYS_WEIGHTS['B_ev_B_21'     ] =  ['weight_sys_bTagSF_MV2c10_Continuous_eigenvars_B_21_up'     , 'weight_sys_bTagSF_MV2c10_Continuous_eigenvars_B_21_down'     , 'WeightBTag'   , '40' , 'b-tag eigenv B21'     ]
SYS_WEIGHTS['B_ev_B_22'     ] =  ['weight_sys_bTagSF_MV2c10_Continuous_eigenvars_B_22_up'     , 'weight_sys_bTagSF_MV2c10_Continuous_eigenvars_B_22_down'     , 'WeightBTag'   , '40' , 'b-tag eigenv B22'     ]
SYS_WEIGHTS['B_ev_B_23'     ] =  ['weight_sys_bTagSF_MV2c10_Continuous_eigenvars_B_23_up'     , 'weight_sys_bTagSF_MV2c10_Continuous_eigenvars_B_23_down'     , 'WeightBTag'   , '40' , 'b-tag eigenv B23'     ]
SYS_WEIGHTS['B_ev_B_24'     ] =  ['weight_sys_bTagSF_MV2c10_Continuous_eigenvars_B_24_up'     , 'weight_sys_bTagSF_MV2c10_Continuous_eigenvars_B_24_down'     , 'WeightBTag'   , '40' , 'b-tag eigenv B24'     ]
SYS_WEIGHTS['B_ev_B_25'     ] =  ['weight_sys_bTagSF_MV2c10_Continuous_eigenvars_B_25_up'     , 'weight_sys_bTagSF_MV2c10_Continuous_eigenvars_B_25_down'     , 'WeightBTag'   , '40' , 'b-tag eigenv B25'     ]
SYS_WEIGHTS['B_ev_B_26'     ] =  ['weight_sys_bTagSF_MV2c10_Continuous_eigenvars_B_26_up'     , 'weight_sys_bTagSF_MV2c10_Continuous_eigenvars_B_26_down'     , 'WeightBTag'   , '40' , 'b-tag eigenv B26'     ]
SYS_WEIGHTS['B_ev_B_27'     ] =  ['weight_sys_bTagSF_MV2c10_Continuous_eigenvars_B_27_up'     , 'weight_sys_bTagSF_MV2c10_Continuous_eigenvars_B_27_down'     , 'WeightBTag'   , '40' , 'b-tag eigenv B27'     ]
SYS_WEIGHTS['B_ev_B_28'     ] =  ['weight_sys_bTagSF_MV2c10_Continuous_eigenvars_B_28_up'     , 'weight_sys_bTagSF_MV2c10_Continuous_eigenvars_B_28_down'     , 'WeightBTag'   , '40' , 'b-tag eigenv B28'     ]
SYS_WEIGHTS['B_ev_B_29'     ] =  ['weight_sys_bTagSF_MV2c10_Continuous_eigenvars_B_29_up'     , 'weight_sys_bTagSF_MV2c10_Continuous_eigenvars_B_29_down'     , 'WeightBTag'   , '40' , 'b-tag eigenv B29'     ]
SYS_WEIGHTS['B_ev_B_30'     ] =  ['weight_sys_bTagSF_MV2c10_Continuous_eigenvars_B_30_up'     , 'weight_sys_bTagSF_MV2c10_Continuous_eigenvars_B_30_down'     , 'WeightBTag'   , '40' , 'b-tag eigenv B30'     ]
SYS_WEIGHTS['B_ev_B_31'     ] =  ['weight_sys_bTagSF_MV2c10_Continuous_eigenvars_B_31_up'     , 'weight_sys_bTagSF_MV2c10_Continuous_eigenvars_B_31_down'     , 'WeightBTag'   , '40' , 'b-tag eigenv B31'     ]
SYS_WEIGHTS['B_ev_B_32'     ] =  ['weight_sys_bTagSF_MV2c10_Continuous_eigenvars_B_32_up'     , 'weight_sys_bTagSF_MV2c10_Continuous_eigenvars_B_32_down'     , 'WeightBTag'   , '40' , 'b-tag eigenv B32'     ]
SYS_WEIGHTS['B_ev_B_33'     ] =  ['weight_sys_bTagSF_MV2c10_Continuous_eigenvars_B_33_up'     , 'weight_sys_bTagSF_MV2c10_Continuous_eigenvars_B_33_down'     , 'WeightBTag'   , '40' , 'b-tag eigenv B33'     ]
SYS_WEIGHTS['B_ev_B_34'     ] =  ['weight_sys_bTagSF_MV2c10_Continuous_eigenvars_B_34_up'     , 'weight_sys_bTagSF_MV2c10_Continuous_eigenvars_B_34_down'     , 'WeightBTag'   , '40' , 'b-tag eigenv B34'     ]
SYS_WEIGHTS['B_ev_B_35'     ] =  ['weight_sys_bTagSF_MV2c10_Continuous_eigenvars_B_35_up'     , 'weight_sys_bTagSF_MV2c10_Continuous_eigenvars_B_35_down'     , 'WeightBTag'   , '40' , 'b-tag eigenv B35'     ]
SYS_WEIGHTS['B_ev_B_36'     ] =  ['weight_sys_bTagSF_MV2c10_Continuous_eigenvars_B_36_up'     , 'weight_sys_bTagSF_MV2c10_Continuous_eigenvars_B_36_down'     , 'WeightBTag'   , '40' , 'b-tag eigenv B36'     ]
SYS_WEIGHTS['B_ev_B_37'     ] =  ['weight_sys_bTagSF_MV2c10_Continuous_eigenvars_B_37_up'     , 'weight_sys_bTagSF_MV2c10_Continuous_eigenvars_B_37_down'     , 'WeightBTag'   , '40' , 'b-tag eigenv B37'     ]
SYS_WEIGHTS['B_ev_B_38'     ] =  ['weight_sys_bTagSF_MV2c10_Continuous_eigenvars_B_38_up'     , 'weight_sys_bTagSF_MV2c10_Continuous_eigenvars_B_38_down'     , 'WeightBTag'   , '40' , 'b-tag eigenv B38'     ]
SYS_WEIGHTS['B_ev_B_39'     ] =  ['weight_sys_bTagSF_MV2c10_Continuous_eigenvars_B_39_up'     , 'weight_sys_bTagSF_MV2c10_Continuous_eigenvars_B_39_down'     , 'WeightBTag'   , '40' , 'b-tag eigenv B39'     ]
SYS_WEIGHTS['B_ev_B_40'     ] =  ['weight_sys_bTagSF_MV2c10_Continuous_eigenvars_B_40_up'     , 'weight_sys_bTagSF_MV2c10_Continuous_eigenvars_B_40_down'     , 'WeightBTag'   , '40' , 'b-tag eigenv B40'     ]
SYS_WEIGHTS['B_ev_B_41'     ] =  ['weight_sys_bTagSF_MV2c10_Continuous_eigenvars_B_41_up'     , 'weight_sys_bTagSF_MV2c10_Continuous_eigenvars_B_41_down'     , 'WeightBTag'   , '40' , 'b-tag eigenv B41'     ]
SYS_WEIGHTS['B_ev_B_42'     ] =  ['weight_sys_bTagSF_MV2c10_Continuous_eigenvars_B_42_up'     , 'weight_sys_bTagSF_MV2c10_Continuous_eigenvars_B_42_down'     , 'WeightBTag'   , '40' , 'b-tag eigenv B42'     ]
SYS_WEIGHTS['B_ev_B_43'     ] =  ['weight_sys_bTagSF_MV2c10_Continuous_eigenvars_B_43_up'     , 'weight_sys_bTagSF_MV2c10_Continuous_eigenvars_B_43_down'     , 'WeightBTag'   , '40' , 'b-tag eigenv B43'     ]
SYS_WEIGHTS['B_ev_B_44'     ] =  ['weight_sys_bTagSF_MV2c10_Continuous_eigenvars_B_44_up'     , 'weight_sys_bTagSF_MV2c10_Continuous_eigenvars_B_44_down'     , 'WeightBTag'   , '40' , 'b-tag eigenv B44'     ]

SYS_WEIGHTS['B_ev_C_0'     ] =  ['weight_sys_bTagSF_MV2c10_Continuous_eigenvars_C_0_up'     , 'weight_sys_bTagSF_MV2c10_Continuous_eigenvars_C_0_down'     , 'WeightBTag'   , '40' , 'b-tag eigenv C0'     ]
SYS_WEIGHTS['B_ev_C_1'     ] =  ['weight_sys_bTagSF_MV2c10_Continuous_eigenvars_C_1_up'     , 'weight_sys_bTagSF_MV2c10_Continuous_eigenvars_C_1_down'     , 'WeightBTag'   , '40' , 'b-tag eigenv C1'     ]
SYS_WEIGHTS['B_ev_C_2'     ] =  ['weight_sys_bTagSF_MV2c10_Continuous_eigenvars_C_2_up'     , 'weight_sys_bTagSF_MV2c10_Continuous_eigenvars_C_2_down'     , 'WeightBTag'   , '40' , 'b-tag eigenv C2'     ]
SYS_WEIGHTS['B_ev_C_3'     ] =  ['weight_sys_bTagSF_MV2c10_Continuous_eigenvars_C_3_up'     , 'weight_sys_bTagSF_MV2c10_Continuous_eigenvars_C_3_down'     , 'WeightBTag'   , '40' , 'b-tag eigenv C3'     ]
SYS_WEIGHTS['B_ev_C_4'     ] =  ['weight_sys_bTagSF_MV2c10_Continuous_eigenvars_C_4_up'     , 'weight_sys_bTagSF_MV2c10_Continuous_eigenvars_C_4_down'     , 'WeightBTag'   , '40' , 'b-tag eigenv C4'     ]
SYS_WEIGHTS['B_ev_C_5'     ] =  ['weight_sys_bTagSF_MV2c10_Continuous_eigenvars_C_5_up'     , 'weight_sys_bTagSF_MV2c10_Continuous_eigenvars_C_5_down'     , 'WeightBTag'   , '40' , 'b-tag eigenv C5'     ]
SYS_WEIGHTS['B_ev_C_6'     ] =  ['weight_sys_bTagSF_MV2c10_Continuous_eigenvars_C_6_up'     , 'weight_sys_bTagSF_MV2c10_Continuous_eigenvars_C_6_down'     , 'WeightBTag'   , '40' , 'b-tag eigenv C6'     ]
SYS_WEIGHTS['B_ev_C_7'     ] =  ['weight_sys_bTagSF_MV2c10_Continuous_eigenvars_C_7_up'     , 'weight_sys_bTagSF_MV2c10_Continuous_eigenvars_C_7_down'     , 'WeightBTag'   , '40' , 'b-tag eigenv C7'     ]
SYS_WEIGHTS['B_ev_C_8'     ] =  ['weight_sys_bTagSF_MV2c10_Continuous_eigenvars_C_8_up'     , 'weight_sys_bTagSF_MV2c10_Continuous_eigenvars_C_8_down'     , 'WeightBTag'   , '40' , 'b-tag eigenv C8'     ]
SYS_WEIGHTS['B_ev_C_9'     ] =  ['weight_sys_bTagSF_MV2c10_Continuous_eigenvars_C_9_up'     , 'weight_sys_bTagSF_MV2c10_Continuous_eigenvars_C_9_down'     , 'WeightBTag'   , '40' , 'b-tag eigenv C9'     ]
SYS_WEIGHTS['B_ev_C_10'     ] =  ['weight_sys_bTagSF_MV2c10_Continuous_eigenvars_C_10_up'     , 'weight_sys_bTagSF_MV2c10_Continuous_eigenvars_C_10_down'     , 'WeightBTag'   , '40' , 'b-tag eigenv C10'     ]
SYS_WEIGHTS['B_ev_C_11'     ] =  ['weight_sys_bTagSF_MV2c10_Continuous_eigenvars_C_11_up'     , 'weight_sys_bTagSF_MV2c10_Continuous_eigenvars_C_11_down'     , 'WeightBTag'   , '40' , 'b-tag eigenv C11'     ]
SYS_WEIGHTS['B_ev_C_12'     ] =  ['weight_sys_bTagSF_MV2c10_Continuous_eigenvars_C_12_up'     , 'weight_sys_bTagSF_MV2c10_Continuous_eigenvars_C_12_down'     , 'WeightBTag'   , '40' , 'b-tag eigenv C12'     ]
SYS_WEIGHTS['B_ev_C_13'     ] =  ['weight_sys_bTagSF_MV2c10_Continuous_eigenvars_C_13_up'     , 'weight_sys_bTagSF_MV2c10_Continuous_eigenvars_C_13_down'     , 'WeightBTag'   , '40' , 'b-tag eigenv C13'     ]
SYS_WEIGHTS['B_ev_C_14'     ] =  ['weight_sys_bTagSF_MV2c10_Continuous_eigenvars_C_14_up'     , 'weight_sys_bTagSF_MV2c10_Continuous_eigenvars_C_14_down'     , 'WeightBTag'   , '40' , 'b-tag eigenv C14'     ]
SYS_WEIGHTS['B_ev_C_15'     ] =  ['weight_sys_bTagSF_MV2c10_Continuous_eigenvars_C_15_up'     , 'weight_sys_bTagSF_MV2c10_Continuous_eigenvars_C_15_down'     , 'WeightBTag'   , '40' , 'b-tag eigenv C15'     ]
SYS_WEIGHTS['B_ev_C_16'     ] =  ['weight_sys_bTagSF_MV2c10_Continuous_eigenvars_C_16_up'     , 'weight_sys_bTagSF_MV2c10_Continuous_eigenvars_C_16_down'     , 'WeightBTag'   , '40' , 'b-tag eigenv C16'     ]
SYS_WEIGHTS['B_ev_C_17'     ] =  ['weight_sys_bTagSF_MV2c10_Continuous_eigenvars_C_17_up'     , 'weight_sys_bTagSF_MV2c10_Continuous_eigenvars_C_17_down'     , 'WeightBTag'   , '40' , 'b-tag eigenv C17'     ]
SYS_WEIGHTS['B_ev_C_18'     ] =  ['weight_sys_bTagSF_MV2c10_Continuous_eigenvars_C_18_up'     , 'weight_sys_bTagSF_MV2c10_Continuous_eigenvars_C_18_down'     , 'WeightBTag'   , '40' , 'b-tag eigenv C18'     ]
SYS_WEIGHTS['B_ev_C_19'     ] =  ['weight_sys_bTagSF_MV2c10_Continuous_eigenvars_C_19_up'     , 'weight_sys_bTagSF_MV2c10_Continuous_eigenvars_C_19_down'     , 'WeightBTag'   , '40' , 'b-tag eigenv C19'     ]

SYS_WEIGHTS['B_ev_L_0'     ] =  ['weight_sys_bTagSF_MV2c10_Continuous_eigenvars_Light_0_up'     , 'weight_sys_bTagSF_MV2c10_Continuous_eigenvars_Light_0_down'     , 'WeightBTag'   , '40' , 'b-tag eigenv L0'     ]
SYS_WEIGHTS['B_ev_L_1'     ] =  ['weight_sys_bTagSF_MV2c10_Continuous_eigenvars_Light_1_up'     , 'weight_sys_bTagSF_MV2c10_Continuous_eigenvars_Light_1_down'     , 'WeightBTag'   , '40' , 'b-tag eigenv L1'     ]
SYS_WEIGHTS['B_ev_L_2'     ] =  ['weight_sys_bTagSF_MV2c10_Continuous_eigenvars_Light_2_up'     , 'weight_sys_bTagSF_MV2c10_Continuous_eigenvars_Light_2_down'     , 'WeightBTag'   , '40' , 'b-tag eigenv L2'     ]
SYS_WEIGHTS['B_ev_L_3'     ] =  ['weight_sys_bTagSF_MV2c10_Continuous_eigenvars_Light_3_up'     , 'weight_sys_bTagSF_MV2c10_Continuous_eigenvars_Light_3_down'     , 'WeightBTag'   , '40' , 'b-tag eigenv L3'     ]
SYS_WEIGHTS['B_ev_L_4'     ] =  ['weight_sys_bTagSF_MV2c10_Continuous_eigenvars_Light_4_up'     , 'weight_sys_bTagSF_MV2c10_Continuous_eigenvars_Light_4_down'     , 'WeightBTag'   , '40' , 'b-tag eigenv L4'     ]
SYS_WEIGHTS['B_ev_L_5'     ] =  ['weight_sys_bTagSF_MV2c10_Continuous_eigenvars_Light_5_up'     , 'weight_sys_bTagSF_MV2c10_Continuous_eigenvars_Light_5_down'     , 'WeightBTag'   , '40' , 'b-tag eigenv L5'     ]
SYS_WEIGHTS['B_ev_L_6'     ] =  ['weight_sys_bTagSF_MV2c10_Continuous_eigenvars_Light_6_up'     , 'weight_sys_bTagSF_MV2c10_Continuous_eigenvars_Light_6_down'     , 'WeightBTag'   , '40' , 'b-tag eigenv L6'     ]
SYS_WEIGHTS['B_ev_L_7'     ] =  ['weight_sys_bTagSF_MV2c10_Continuous_eigenvars_Light_7_up'     , 'weight_sys_bTagSF_MV2c10_Continuous_eigenvars_Light_7_down'     , 'WeightBTag'   , '40' , 'b-tag eigenv L7'     ]
SYS_WEIGHTS['B_ev_L_8'     ] =  ['weight_sys_bTagSF_MV2c10_Continuous_eigenvars_Light_8_up'     , 'weight_sys_bTagSF_MV2c10_Continuous_eigenvars_Light_8_down'     , 'WeightBTag'   , '40' , 'b-tag eigenv L8'     ]
SYS_WEIGHTS['B_ev_L_9'     ] =  ['weight_sys_bTagSF_MV2c10_Continuous_eigenvars_Light_9_up'     , 'weight_sys_bTagSF_MV2c10_Continuous_eigenvars_Light_9_down'     , 'WeightBTag'   , '40' , 'b-tag eigenv L9'     ]
SYS_WEIGHTS['B_ev_L_10'     ] =  ['weight_sys_bTagSF_MV2c10_Continuous_eigenvars_Light_10_up'     , 'weight_sys_bTagSF_MV2c10_Continuous_eigenvars_Light_10_down'     , 'WeightBTag'   , '40' , 'b-tag eigenv L10'     ]
SYS_WEIGHTS['B_ev_L_11'     ] =  ['weight_sys_bTagSF_MV2c10_Continuous_eigenvars_Light_11_up'     , 'weight_sys_bTagSF_MV2c10_Continuous_eigenvars_Light_11_down'     , 'WeightBTag'   , '40' , 'b-tag eigenv L11'     ]
SYS_WEIGHTS['B_ev_L_12'     ] =  ['weight_sys_bTagSF_MV2c10_Continuous_eigenvars_Light_12_up'     , 'weight_sys_bTagSF_MV2c10_Continuous_eigenvars_Light_12_down'     , 'WeightBTag'   , '40' , 'b-tag eigenv L12'     ]
SYS_WEIGHTS['B_ev_L_13'     ] =  ['weight_sys_bTagSF_MV2c10_Continuous_eigenvars_Light_13_up'     , 'weight_sys_bTagSF_MV2c10_Continuous_eigenvars_Light_13_down'     , 'WeightBTag'   , '40' , 'b-tag eigenv L13'     ]
SYS_WEIGHTS['B_ev_L_14'     ] =  ['weight_sys_bTagSF_MV2c10_Continuous_eigenvars_Light_14_up'     , 'weight_sys_bTagSF_MV2c10_Continuous_eigenvars_Light_14_down'     , 'WeightBTag'   , '40' , 'b-tag eigenv L14'     ]
SYS_WEIGHTS['B_ev_L_15'     ] =  ['weight_sys_bTagSF_MV2c10_Continuous_eigenvars_Light_15_up'     , 'weight_sys_bTagSF_MV2c10_Continuous_eigenvars_Light_15_down'     , 'WeightBTag'   , '40' , 'b-tag eigenv L15'     ]
SYS_WEIGHTS['B_ev_L_16'     ] =  ['weight_sys_bTagSF_MV2c10_Continuous_eigenvars_Light_16_up'     , 'weight_sys_bTagSF_MV2c10_Continuous_eigenvars_Light_16_down'     , 'WeightBTag'   , '40' , 'b-tag eigenv L16'     ]
SYS_WEIGHTS['B_ev_L_17'     ] =  ['weight_sys_bTagSF_MV2c10_Continuous_eigenvars_Light_17_up'     , 'weight_sys_bTagSF_MV2c10_Continuous_eigenvars_Light_17_down'     , 'WeightBTag'   , '40' , 'b-tag eigenv L17'     ]
SYS_WEIGHTS['B_ev_L_18'     ] =  ['weight_sys_bTagSF_MV2c10_Continuous_eigenvars_Light_18_up'     , 'weight_sys_bTagSF_MV2c10_Continuous_eigenvars_Light_18_down'     , 'WeightBTag'   , '40' , 'b-tag eigenv L18'     ]
SYS_WEIGHTS['B_ev_L_19'     ] =  ['weight_sys_bTagSF_MV2c10_Continuous_eigenvars_Light_19_up'     , 'weight_sys_bTagSF_MV2c10_Continuous_eigenvars_Light_19_down'     , 'WeightBTag'   , '40' , 'b-tag eigenv L19'     ]


PDF_WEIGHTS = OrderedDict()
PDF_WEIGHTS['PDFset90900'] = ['weight_sys_PDFset=90900', 'PDF', '40' ]
PDF_WEIGHTS['PDFset90901'] = ['weight_sys_PDFset=90901', 'PDF', '40' ]
PDF_WEIGHTS['PDFset90902'] = ['weight_sys_PDFset=90902', 'PDF', '40' ]
PDF_WEIGHTS['PDFset90903'] = ['weight_sys_PDFset=90903', 'PDF', '40' ]
PDF_WEIGHTS['PDFset90904'] = ['weight_sys_PDFset=90904', 'PDF', '40' ]
PDF_WEIGHTS['PDFset90905'] = ['weight_sys_PDFset=90905', 'PDF', '40' ]
PDF_WEIGHTS['PDFset90906'] = ['weight_sys_PDFset=90906', 'PDF', '40' ]
PDF_WEIGHTS['PDFset90907'] = ['weight_sys_PDFset=90907', 'PDF', '40' ]
PDF_WEIGHTS['PDFset90908'] = ['weight_sys_PDFset=90908', 'PDF', '40' ]
PDF_WEIGHTS['PDFset90909'] = ['weight_sys_PDFset=90909', 'PDF', '40' ]
PDF_WEIGHTS['PDFset90910'] = ['weight_sys_PDFset=90910', 'PDF', '40' ]
PDF_WEIGHTS['PDFset90911'] = ['weight_sys_PDFset=90911', 'PDF', '40' ]
PDF_WEIGHTS['PDFset90912'] = ['weight_sys_PDFset=90912', 'PDF', '40' ]
PDF_WEIGHTS['PDFset90913'] = ['weight_sys_PDFset=90913', 'PDF', '40' ]
PDF_WEIGHTS['PDFset90914'] = ['weight_sys_PDFset=90914', 'PDF', '40' ]
PDF_WEIGHTS['PDFset90915'] = ['weight_sys_PDFset=90915', 'PDF', '40' ]
PDF_WEIGHTS['PDFset90916'] = ['weight_sys_PDFset=90916', 'PDF', '40' ]
PDF_WEIGHTS['PDFset90917'] = ['weight_sys_PDFset=90917', 'PDF', '40' ]
PDF_WEIGHTS['PDFset90918'] = ['weight_sys_PDFset=90918', 'PDF', '40' ]
PDF_WEIGHTS['PDFset90919'] = ['weight_sys_PDFset=90919', 'PDF', '40' ]
PDF_WEIGHTS['PDFset90920'] = ['weight_sys_PDFset=90920', 'PDF', '40' ]
PDF_WEIGHTS['PDFset90921'] = ['weight_sys_PDFset=90921', 'PDF', '40' ]
PDF_WEIGHTS['PDFset90922'] = ['weight_sys_PDFset=90922', 'PDF', '40' ]
PDF_WEIGHTS['PDFset90923'] = ['weight_sys_PDFset=90923', 'PDF', '40' ]
PDF_WEIGHTS['PDFset90924'] = ['weight_sys_PDFset=90924', 'PDF', '40' ]
PDF_WEIGHTS['PDFset90925'] = ['weight_sys_PDFset=90925', 'PDF', '40' ]
PDF_WEIGHTS['PDFset90926'] = ['weight_sys_PDFset=90926', 'PDF', '40' ]
PDF_WEIGHTS['PDFset90927'] = ['weight_sys_PDFset=90927', 'PDF', '40' ]
PDF_WEIGHTS['PDFset90928'] = ['weight_sys_PDFset=90928', 'PDF', '40' ]
PDF_WEIGHTS['PDFset90929'] = ['weight_sys_PDFset=90929', 'PDF', '40' ]
PDF_WEIGHTS['PDFset90930'] = ['weight_sys_PDFset=90930', 'PDF', '40' ]

SYS_TREES_TWOSIDED = OrderedDict()
SYS_TREES_TWOSIDED['EG_RES_ALL'                        ] = ['EG_RESOLUTION_ALL__1up'                                               , 'EG_RESOLUTION_ALL__1down'                                               , 'Egamma' , '40' ]
SYS_TREES_TWOSIDED['EG_SCALE_ALL'                      ] = ['EG_SCALE_ALL__1up'                                                    , 'EG_SCALE_ALL__1down'                                                    , 'Egamma' , '40' ]
SYS_TREES_TWOSIDED['Jet_BJES_Response'                 ] = ['JET_CategoryReduction_JET_BJES_Response__1up'                         , 'JET_CategoryReduction_JET_BJES_Response__1down'                         , 'Jets'   , '40' ]
SYS_TREES_TWOSIDED['Jet_EffectiveNP_Detector1'         ] = ['JET_CategoryReduction_JET_EffectiveNP_Detector1__1up'                 , 'JET_CategoryReduction_JET_EffectiveNP_Detector1__1down'                 , 'Jets'   , '40' ]
SYS_TREES_TWOSIDED['Jet_EffectiveNP_Detector2'         ] = ['JET_CategoryReduction_JET_EffectiveNP_Detector2__1up'                 , 'JET_CategoryReduction_JET_EffectiveNP_Detector2__1down'                 , 'Jets'   , '40' ]
SYS_TREES_TWOSIDED['Jet_EffNP_Mixed1'                  ] = ['JET_CategoryReduction_JET_EffectiveNP_Mixed1__1up'                    , 'JET_CategoryReduction_JET_EffectiveNP_Mixed1__1down'                    , 'Jets'   , '40' ]
SYS_TREES_TWOSIDED['Jet_EffNP_Mixed2'                  ] = ['JET_CategoryReduction_JET_EffectiveNP_Mixed2__1up'                    , 'JET_CategoryReduction_JET_EffectiveNP_Mixed2__1down'                    , 'Jets'   , '40' ]
SYS_TREES_TWOSIDED['Jet_EffNP_Mixed3'                  ] = ['JET_CategoryReduction_JET_EffectiveNP_Mixed3__1up'                    , 'JET_CategoryReduction_JET_EffectiveNP_Mixed3__1down'                    , 'Jets'   , '40' ]
SYS_TREES_TWOSIDED['Jet_EffNP_Modelling1'              ] = ['JET_CategoryReduction_JET_EffectiveNP_Modelling1__1up'                , 'JET_CategoryReduction_JET_EffectiveNP_Modelling1__1down'                , 'Jets'   , '40' ]
SYS_TREES_TWOSIDED['Jet_EffNP_Modelling2'              ] = ['JET_CategoryReduction_JET_EffectiveNP_Modelling2__1up'                , 'JET_CategoryReduction_JET_EffectiveNP_Modelling2__1down'                , 'Jets'   , '40' ]
SYS_TREES_TWOSIDED['Jet_EffNP_Modelling3'              ] = ['JET_CategoryReduction_JET_EffectiveNP_Modelling3__1up'                , 'JET_CategoryReduction_JET_EffectiveNP_Modelling3__1down'                , 'Jets'   , '40' ]
SYS_TREES_TWOSIDED['Jet_EffNP_Modelling4'              ] = ['JET_CategoryReduction_JET_EffectiveNP_Modelling4__1up'                , 'JET_CategoryReduction_JET_EffectiveNP_Modelling4__1down'                , 'Jets'   , '40' ]
SYS_TREES_TWOSIDED['Jet_EffNP_Statistical1'            ] = ['JET_CategoryReduction_JET_EffectiveNP_Statistical1__1up'              , 'JET_CategoryReduction_JET_EffectiveNP_Statistical1__1down'              , 'Jets'   , '40' ]
SYS_TREES_TWOSIDED['Jet_EffNP_Statistical2'            ] = ['JET_CategoryReduction_JET_EffectiveNP_Statistical2__1up'              , 'JET_CategoryReduction_JET_EffectiveNP_Statistical2__1down'              , 'Jets'   , '40' ]
SYS_TREES_TWOSIDED['Jet_EffNP_Statistical3'            ] = ['JET_CategoryReduction_JET_EffectiveNP_Statistical3__1up'              , 'JET_CategoryReduction_JET_EffectiveNP_Statistical3__1down'              , 'Jets'   , '40' ]
SYS_TREES_TWOSIDED['Jet_EffNP_Statistical4'            ] = ['JET_CategoryReduction_JET_EffectiveNP_Statistical4__1up'              , 'JET_CategoryReduction_JET_EffectiveNP_Statistical4__1down'              , 'Jets'   , '40' ]
SYS_TREES_TWOSIDED['Jet_EffNP_Statistical5'            ] = ['JET_CategoryReduction_JET_EffectiveNP_Statistical5__1up'              , 'JET_CategoryReduction_JET_EffectiveNP_Statistical5__1down'              , 'Jets'   , '40' ]
SYS_TREES_TWOSIDED['Jet_EffNP_Statistical6'            ] = ['JET_CategoryReduction_JET_EffectiveNP_Statistical6__1up'              , 'JET_CategoryReduction_JET_EffectiveNP_Statistical6__1down'              , 'Jets'   , '40' ]
SYS_TREES_TWOSIDED['Jet_EtaIntercal_Modelling'         ] = ['JET_CategoryReduction_JET_EtaIntercalibration_Modelling__1up'         , 'JET_CategoryReduction_JET_EtaIntercalibration_Modelling__1down'         , 'Jets'   , '40' ]
SYS_TREES_TWOSIDED['Jet_EtaIntercal_NonClosure_highE'  ] = ['JET_CategoryReduction_JET_EtaIntercalibration_NonClosure_highE__1up'  , 'JET_CategoryReduction_JET_EtaIntercalibration_NonClosure_highE__1down'  , 'Jets'   , '40' ]
SYS_TREES_TWOSIDED['Jet_EtaIntercal_NonClosure_negEta' ] = ['JET_CategoryReduction_JET_EtaIntercalibration_NonClosure_negEta__1up' , 'JET_CategoryReduction_JET_EtaIntercalibration_NonClosure_negEta__1down' , 'Jets'   , '40' ]
SYS_TREES_TWOSIDED['Jet_EtaIntercal_NonClosure_posEta' ] = ['JET_CategoryReduction_JET_EtaIntercalibration_NonClosure_posEta__1up' , 'JET_CategoryReduction_JET_EtaIntercalibration_NonClosure_posEta__1down' , 'Jets'   , '40' ]
SYS_TREES_TWOSIDED['Jet_EtaIntercal_TotalStat'         ] = ['JET_CategoryReduction_JET_EtaIntercalibration_TotalStat__1up'         , 'JET_CategoryReduction_JET_EtaIntercalibration_TotalStat__1down'         , 'Jets'   , '40' ]
SYS_TREES_TWOSIDED['Jet_Flavor_Composition'            ] = ['JET_CategoryReduction_JET_Flavor_Composition__1up'                    , 'JET_CategoryReduction_JET_Flavor_Composition__1down'                    , 'Jets'   , '40' ]
SYS_TREES_TWOSIDED['Jet_Flavor_Response'               ] = ['JET_CategoryReduction_JET_Flavor_Response__1up'                       , 'JET_CategoryReduction_JET_Flavor_Response__1down'                       , 'Jets'   , '40' ]
SYS_TREES_TWOSIDED['Jet_Pileup_OffsetMu'               ] = ['JET_CategoryReduction_JET_Pileup_OffsetMu__1up'                       , 'JET_CategoryReduction_JET_Pileup_OffsetMu__1down'                       , 'Jets'   , '40' ]
SYS_TREES_TWOSIDED['Jet_Pileup_OffsetNPV'              ] = ['JET_CategoryReduction_JET_Pileup_OffsetNPV__1up'                      , 'JET_CategoryReduction_JET_Pileup_OffsetNPV__1down'                      , 'Jets'   , '40' ]
SYS_TREES_TWOSIDED['Jet_Pileup_PtTerm'                 ] = ['JET_CategoryReduction_JET_Pileup_PtTerm__1up'                         , 'JET_CategoryReduction_JET_Pileup_PtTerm__1down'                         , 'Jets'   , '40' ]
SYS_TREES_TWOSIDED['Jet_Pileup_RhoTopology'            ] = ['JET_CategoryReduction_JET_Pileup_RhoTopology__1up'                    , 'JET_CategoryReduction_JET_Pileup_RhoTopology__1down'                    , 'Jets'   , '40' ]
SYS_TREES_TWOSIDED['Jet_PunchThrough_MC16'             ] = ['JET_CategoryReduction_JET_PunchThrough_MC16__1up'                     , 'JET_CategoryReduction_JET_PunchThrough_MC16__1down'                     , 'Jets'   , '40' ]
SYS_TREES_TWOSIDED['Jet_SingleParticle_HighPt'         ] = ['JET_CategoryReduction_JET_SingleParticle_HighPt__1up'                 , 'JET_CategoryReduction_JET_SingleParticle_HighPt__1down'                 , 'Jets'   , '40' ]
SYS_TREES_TWOSIDED['MET_SoftTrk_Scale'                 ] = ['MET_SoftTrk_ScaleUp'                                                  , 'MET_SoftTrk_ScaleDown'                                                  , 'MET'    , '40' ]
SYS_TREES_TWOSIDED['MUON_ID'                           ] = ['MUON_ID__1up'                                                         , 'MUON_ID__1down'                                                         , 'Muon'   , '40' ]
SYS_TREES_TWOSIDED['MUON_MS'                           ] = ['MUON_MS__1up'                                                         , 'MUON_MS__1down'                                                         , 'Muon'   , '40' ]
SYS_TREES_TWOSIDED['MUON_SAGITTA_RESBIAS'              ] = ['MUON_SAGITTA_RESBIAS__1up'                                            , 'MUON_SAGITTA_RESBIAS__1down'                                            , 'Muon'   , '40' ]
SYS_TREES_TWOSIDED['MUON_SAGITTA_RHO'                  ] = ['MUON_SAGITTA_RHO__1up'                                                , 'MUON_SAGITTA_RHO__1down'                                                , 'Muon'   , '40' ]
SYS_TREES_TWOSIDED['MUON_SCALE'                        ] = ['MUON_SCALE__1up'                                                      , 'MUON_SCALE__1down'                                                      , 'Muon'   , '40' ]


SYS_TREES_ONESIDED = OrderedDict()
SYS_TREES_ONESIDED['MET_SoftTrk_ResoPara'          ] = ['MET_SoftTrk_ResoPara'                                        , 'MET'   , '40' ]
SYS_TREES_ONESIDED['MET_SoftTrk_ResoPerp'          ] = ['MET_SoftTrk_ResoPerp'                                        , 'MET'   , '40' ]
SYS_TREES_ONESIDED['Jet_JER_DataVsMC'              ] = ['JET_CategoryReduction_JET_JER_DataVsMC__1up'                 , 'JER'   , '40' ]
SYS_TREES_ONESIDED['Jet_JER_EffNP_1'               ] = ['JET_CategoryReduction_JET_JER_EffectiveNP_1__1up'            , 'JER'   , '40' ]
SYS_TREES_ONESIDED['Jet_JER_EffNP_2'               ] = ['JET_CategoryReduction_JET_JER_EffectiveNP_2__1up'            , 'JER'   , '40' ]
SYS_TREES_ONESIDED['Jet_JER_EffNP_3'               ] = ['JET_CategoryReduction_JET_JER_EffectiveNP_3__1up'            , 'JER'   , '40' ]
SYS_TREES_ONESIDED['Jet_JER_EffNP_4'               ] = ['JET_CategoryReduction_JET_JER_EffectiveNP_4__1up'            , 'JER'   , '40' ]
SYS_TREES_ONESIDED['Jet_JER_EffNP_5'               ] = ['JET_CategoryReduction_JET_JER_EffectiveNP_5__1up'            , 'JER'   , '40' ]
SYS_TREES_ONESIDED['Jet_JER_EffNP_6'               ] = ['JET_CategoryReduction_JET_JER_EffectiveNP_6__1up'            , 'JER'   , '40' ]
SYS_TREES_ONESIDED['Jet_JER_EffectiveNP_7restTerm' ] = ['JET_CategoryReduction_JET_JER_EffectiveNP_7restTerm__1up'    , 'JER'   , '40' ]


def to_json():
    import json

    entries = {
        'SYS_WEIGHTS' : {},
        'SYS_TREES_TWOSIDED': {},
        'SYS_TREES_ONESIDED': {},
        'PDF_WEIGHTS' : {},
    }

    for k, v in SYS_WEIGHTS.items():
        name = k
        up = v[0]
        down = v[1]
        cat = v[2]
        smooth = v[3]
        entries['SYS_WEIGHTS'][name] = {
            'name': name,
            'up': up,
            'down': down,
            'cat': cat,
            'smoothing': smooth
        }

    for k, v in SYS_TREES_TWOSIDED.items():
        name = k
        up = v[0]
        down = v[1]
        cat = v[2]
        smooth = v[3]
        entries['SYS_TREES_TWOSIDED'][name] = {
            'name': name,
            'up': up,
            'down': down,
            'cat': cat,
            'smoothing': smooth
        }

    for k, v in SYS_TREES_ONESIDED.items():
        name = k
        up = v[0]
        cat = v[1]
        smooth = v[2]
        entries['SYS_TREES_ONESIDED'][name] = {
            'name': name,
            'up': up,
            'cat': cat,
            'smoothing': smooth
        }

    for k, v in PDF_WEIGHTS.items():
        name = k
        up = v[0]
        var = v[1],
        smooth = v[2]
        entries['PDF_WEIGHTS'][name] = {
            'name': name,
            'up': up,
            'cat': cat,
            'smoothing': smooth
        }

    print(json.dumps(entries, indent=2))

if __name__ == '__main__':
    to_json()
