token = '628590242:AAEVn6EKF3LAYGVoq9Kcxmzuxx75CzGHv-0'
tokenClassbot ='661654546:AAFTfOatozTfqVOmb_y4UHsnumMLe7e7EE0'
URL='https://api.telegram.org/bot'+token+'/'
appid = "4d60ad5e0e64c13b446c424d8388d867"
count=False
Id = None
Command = False
God=["""Наш розум - космос \nТа не всяк ракету має...\nТому далеко не літає""",
     """Вульгарний танець... Тьху!\nДля імпотентів!\nАле яких він вартий компліментів!""",
     """Не питаю я у Неба:\n Що тобі від мене треба?\n вгору дурно не кричу:\n Лиш страждаю I мовчу !\n Все сприймаю так , як є:\n Що дають - те і моє""",
     """Депресія... Невесело...\n Сьогодні злий на все село !\n Учора був навеселі- ходив веселий по землі\n Тепер мов після зілля-\n Тяжке мені похмілля!\n Нема в`язкішої ріллі,\n Як жить у нашому селі :\n Увечері тут весело,\n А вранці - лип депресія...\n Життя живем бездумно,\n Та не завжди в нас сумно!\n Не страшно , що депресія:\n Вона - лише до вечера!\n Оте лихе , як праці,\n Буває тільки вранці!!\n Доходить , що повісився б!\n Та хто уранці Вішався!\n З бідою не страждаємо:\n До вечера розраемо!\n Щасливі в нашому селі,\n Лише коли навеселі!\n Даю на сотню двісті,\n що так воно і в місті""",
     """Йой , брати - українці!\n Щo ж - то деться з нами?\n Всі один - поодинці:\n Нам не стати панами!\n Всяк своєї сопе,\n Все зробилося шуте:\n Пустодзвонне, тупе,\n завидноше і люте...\n Мов який кочівник\n Те руйнуєм угурті,\n що стоїть - для усіх\n і не влізе до юрти .. \n14.02.2006""",
     """Наче жаби в лузі\n Лежимо на пузі..\n Час прийшов нам грати\n Непогані й карти:\n Кожному під пузо Бог підсунув туза..\n I козирна масть!\n Але хто ж віддасть?\n Певно, будем й далі\n Кум кати про жалі\n 19.09.2006р .""",
     """Світе світлий!\n                Не світи\n В темряву нас...\n                Відпусти!\n В темряві ми якось...\n                Звикли\n Нам життя деталі..\n                Зникли!\n Виглядаєм як скоти:\n Без деталей... З темноти!\n Hанизалось нам на мітли\n Без ідей !!! - \n Все , що робиться на світлі\n У людей\n 27.08.2005p."""]

httpCat=['https://image.ibb.co/cYpCqo/01.jpg',
'https://image.ibb.co/hKfSqo/ZKml_Pb_mtw_I.jpg',
'https://image.ibb.co/dvhU38/Zagy_BPpmdck.jpg',
'https://image.ibb.co/i2oQbT/yt_Zf_QFf_Q90c.jpg',
'https://image.ibb.co/c4nwi8/x_S5_W3ba4t_Y.jpg',
'https://image.ibb.co/eNuywT/ybug_DWSx_MB4.jpg',
'https://image.ibb.co/b8Ebi8/x_R1n_Tpsn8_JQ.jpg',
'https://image.ibb.co/kESkbT/XNhxo_Ywn_AQ0.jpg',
'https://image.ibb.co/cjebi8/x_N3_KAe2_q_J4.jpg',
'https://image.ibb.co/hb5tVo/x_ER3b_E6_OIp_Q.jpg',
'https://image.ibb.co/gJL5bT/X44q_Oh_BUa2_I.jpg',
'https://image.ibb.co/kPUbi8/WYABu_Yc_Z_Mg.jpg',
'https://image.ibb.co/c2AhO8/v_Ys_Sz_Ij_Fczg.jpg',
'https://image.ibb.co/ex8rGT/vo_XEWOXO0kc.jpg',
'https://image.ibb.co/jSJ2O8/Vkhz_U7_FVcws.jpg',
'https://image.ibb.co/d1jbi8/vlzb_Cw_PCl_QI.jpg',
'https://image.ibb.co/bwVtVo/v5xhr8_JJ_N0.jpg',
'https://image.ibb.co/ebDDVo/v_Amr_Nz_Qi0_Pw.jpg',
'https://image.ibb.co/gHU938/uw_QNX6_Qo94g.jpg',
'https://image.ibb.co/cHkhO8/Uwkq_Iq_MKY8.jpg',
'https://image.ibb.co/enxkbT/uud6qs_Fr_B0_M.jpg',
'https://image.ibb.co/cii2O8/u_Svq_Wt_Ot_Nt_A.jpg',
'https://image.ibb.co/diu938/u_Ibv4wi_Zf_G8.jpg',
'https://image.ibb.co/gJBp38/ud_Fc42i26j_E.jpg',
'https://image.ibb.co/jbJrGT/UDfax1zq_QF8.jpg',
'https://image.ibb.co/jNpLAo/Tv_Mg_Ojnzrn_U.jpg',
'https://image.ibb.co/m1MYVo/t_RES_m_Eg_Cw_E.jpg',
'https://image.ibb.co/jq66i8/t_Qwy3_KL0s_KM.jpg',
'https://image.ibb.co/duOVAo/t_Q3_Utxx_UAUU.jpg',
'https://image.ibb.co/khZFbT/Tg_BIHLe_LHLk.jpg',
'https://image.ibb.co/d7VXO8/sogp_GMqi_Hso.jpg',
'https://image.ibb.co/dESCO8/T9wue_Axjm_Zc.jpg',
'https://image.ibb.co/nEoK38/s_Nxgu_I7b0_V0.jpg',
'https://image.ibb.co/gAOmi8/SJxhko_QCIt4.jpg',
'https://image.ibb.co/jbDmi8/SDHj_UQb_Rgu_E.jpg',
'https://image.ibb.co/ctMTwT/s10_RT8_BP4_Bw.jpg',
'https://image.ibb.co/jKMiVo/S0_V0y_Alci78.jpg',
'https://image.ibb.co/foWiVo/RYnj_Ian_URFo.jpg',
'https://image.ibb.co/hrCqAo/r_Liv8_Igpo0c.jpg',
'https://image.ibb.co/kougGT/RJ6_Lwlm_Hpyw.jpg',
'https://image.ibb.co/ft8VAo/RIPji_Dnw8_Z8.jpg',
'https://image.ibb.co/ctHqAo/r_D0_CP_A_5_Ts.jpg',
'https://image.ibb.co/jpAXO8/q_PYqt_UNJAo.jpg',
'https://image.ibb.co/gNoxqo/q_RPk_Qqu7_TWQ.jpg',
'https://image.ibb.co/kTwTwT/Qpya_CZ8_Co1g.jpg',
'https://image.ibb.co/c6dabT/qpk_Qhilp_2k.jpg',
'https://image.ibb.co/m5zgGT/q_HYm_ORYsm2_Q.jpg',
'https://image.ibb.co/fHz3Vo/Qf_BJxh_IOJvc.jpg',
'https://image.ibb.co/kuzRi8/qaxozjcs_H0.jpg',
'https://image.ibb.co/cYPFbT/Q93l_Tb_Ho_LB8.jpg',
'https://image.ibb.co/mYkMGT/q7_Kyhky_HAGQ.jpg',
'https://image.ibb.co/io8VAo/PZCN9_Vds3s_I.jpg',
'https://image.ibb.co/nQ9sO8/PXl0_IG2_I0_OY.jpg',
'https://image.ibb.co/bMomi8/pv_UKMh_LUrd_I.jpg',
'https://image.ibb.co/koWiVo/Pu_Nc99_WB49_Y.jpg',
'https://image.ibb.co/cpMiVo/Pr4tn_Rw4e_CI.jpg',
'https://image.ibb.co/fcYK38/p_PU4_Dmw_EX8.jpg',
'https://image.ibb.co/h3OK38/p_MDJW8_Lr_Vw_Y.jpg',
'https://image.ibb.co/k05AAo/P_0_UKBGr_OHs.jpg',
'https://image.ibb.co/c04FbT/Oto_Zwq_ITIa_I.jpg',
'https://image.ibb.co/d12e38/on104p_V4gu4.jpg',
'https://image.ibb.co/eQ8xqo/o_T0wggyyk5_M.jpg',
'https://image.ibb.co/gpEFbT/OABNr_Lw_Q_I.jpg',
'https://image.ibb.co/e0fAAo/OJQ4ftj3b_UQ.jpg',
'https://image.ibb.co/mf8xqo/O84_Hwd_BQdhc.jpg',
'https://image.ibb.co/exMHqo/o83_Iyvfb4_MM.jpg',
'https://image.ibb.co/kFaXO8/NZz_KLSORXZs.jpg',
'https://image.ibb.co/gFcOVo/nw1_RETt_Cwzw.jpg',
'https://image.ibb.co/fK43Vo/n_Uy_Wig_Jc_BHU.jpg',
'https://image.ibb.co/fnRvbT/NSRS0_Ajq5y_U.jpg',
'https://image.ibb.co/daUFbT/n_OWYAn_GJe_BA.jpg',
'https://image.ibb.co/mCgTwT/n_OPzd_EWi12_Q.jpg',
'https://image.ibb.co/dhfcqo/nl_HFAckj9_Dk.jpg',
'https://image.ibb.co/k8QAAo/NCOPWo_ZCk_MM.jpg',
'https://image.ibb.co/iwTVAo/n_C1_X3_Ylz_FVM.jpg',
'https://image.ibb.co/n2XOVo/MJkxy_Cb_Mkc_Q.jpg',
'https://image.ibb.co/dmDmi8/Mh_G279lu_Kcw.jpg',
'https://image.ibb.co/kh6TwT/m_GZUYb_Jh_Y30.jpg',
'https://image.ibb.co/n8wTwT/Mfgc74_H_1z_E.jpg',
'https://image.ibb.co/e9mTwT/Mc_Ya0_P3_Eo_Q.jpg',
'https://image.ibb.co/jmnqAo/MAmb6p_BHFQ4.jpg',
'https://image.ibb.co/moTxqo/MAg_Uy5_Vq_NQg.jpg',
'https://image.ibb.co/gQacqo/MA6_KYMFl_Ds.jpg',
'https://image.ibb.co/kO0AAo/M9_g_FAoh3pk.jpg',
'https://image.ibb.co/nvkowT/l_NGb_IOXkg_Us.jpg',
'https://image.ibb.co/ht3xqo/l_nb_C_b_DGy_I.jpg',
'https://image.ibb.co/iQsCO8/lewp_L5_G_s_WI.jpg',
'https://image.ibb.co/eYc1GT/Lio_co_Tw54_U.jpg',
'https://image.ibb.co/hNbvbT/KUQgc_Ga_Zulo.jpg',
'https://image.ibb.co/cK8mi8/k_Su3_Mh_FPWco.jpg',
'https://image.ibb.co/dTo8wT/k_QVDVMGz_KTg.jpg',
'https://image.ibb.co/gHn1GT/k_MW8_QWTY02_Q.jpg',
'https://image.ibb.co/kFDabT/k_KUNVUJLAQY.jpg',
'https://image.ibb.co/cs3mi8/k_JL5p_HMy_BWs.jpg',
'https://image.ibb.co/fLbTwT/K233d_RTk_ZTY.jpg',
'https://image.ibb.co/kgBvbT/KHK_WUmok_Mk.jpg',
'https://image.ibb.co/eP38wT/j_ZMHe_PD_YA0.jpg',
'https://image.ibb.co/esQz38/K6d_Q7_Ecmb_KQ.jpg',
'https://image.ibb.co/f9oK38/Jtqs_xz_Le_Oo.jpg',
'https://image.ibb.co/kd6iVo/Jrk6yv_POJYc.jpg',
'https://image.ibb.co/dgeRi8/JQmlb9_PS_Gk.jpg',
'https://image.ibb.co/hXFowT/Jg_RUIea_PTqo.jpg',
'https://image.ibb.co/fT16i8/JFNa_Uj_M43_JI.jpg',
'https://image.ibb.co/bLLz38/J3v_81tp_CME.jpg',
'https://image.ibb.co/fougGT/j3_Jkevy_JU2_E.jpg',
'https://image.ibb.co/mh4gGT/j1m_El2i4_ZGI.jpg',
'https://image.ibb.co/ii3xqo/J_n_Nqlr_N4m_Y.jpg',
'https://image.ibb.co/igeywT/Iw_Ecyy6x_KBg.jpg',
'https://image.ibb.co/i31YVo/i_Sof_Eac_R06w.jpg',
'https://image.ibb.co/n9A5bT/Iqmhck_SNlt_U.jpg',
'https://image.ibb.co/hWc7qo/imrau_Tq5t54.jpg',
'https://image.ibb.co/nO3QbT/hi_vhd_K8u_Oo.jpg',
'https://image.ibb.co/djatVo/HIE0_Qu18g90.jpg',
'https://image.ibb.co/bQtfAo/HHz_Wx8b_NMv0.jpg',
'https://image.ibb.co/hJGNO8/g_Wxyzd_QGZXg.jpg',
'https://image.ibb.co/bzLGi8/hc5_Xp_Vh6av4.jpg',
'https://image.ibb.co/nueWGT/gr_KMl_N9zvgw.jpg',
'https://image.ibb.co/kDahO8/Gi_Eznyaxk_8.jpg',
'https://image.ibb.co/njPywT/Fu_Hh_Ewiex_Y4.jpg',
'https://image.ibb.co/chmYVo/fkm03sxm_TS4.jpg',
'https://image.ibb.co/hxNkbT/ff_Id7_Xw_Kq_Yo.jpg',
'https://image.ibb.co/kmMdwT/ey_OGxcz04_Sg.jpg',
'https://image.ibb.co/btAtVo/fe2_Sq5zck_SM.jpg',
'https://image.ibb.co/igMdwT/EWu_Rqhp_I9_D8.jpg',
'https://image.ibb.co/nAn7qo/Ev_OZJz_Mp4jc.jpg',
'https://image.ibb.co/nHjnqo/Ev_BUr_Jd_Yigo.jpg',
'https://image.ibb.co/iPUbi8/Etdmx_SFG54.jpg',
'https://image.ibb.co/cakGi8/ENzdoc5_Xa_OQ.jpg',
'https://image.ibb.co/h6mNO8/Env93_Fq_OBDg.jpg',
'https://image.ibb.co/bYDfAo/e_MUUs_Ck1_OGI.jpg',
'https://image.ibb.co/hLfhO8/eidzi_FDsyjk.jpg',
'https://image.ibb.co/cRgp38/EHOpm_S6_RJw.jpg',
'https://image.ibb.co/hu7JwT/Eeo_R_hyh_YME.jpg',
'https://image.ibb.co/kyX7qo/ECiuz_UPa_Zwo.jpg',
'https://image.ibb.co/d9pnqo/Eccm3_Q0pi_VI.jpg',
'https://image.ibb.co/n8AtVo/Eb_Jr0bpt_PQ8.jpg',
'https://image.ibb.co/jdHJwT/DYm_PXiz_Xo_R8.jpg',
'https://image.ibb.co/kYFSqo/Dp_Uc_Fp_BSW8_Y.jpg',
'https://image.ibb.co/gYHJwT/Dnp_MBo_HQDhg.jpg',
'https://image.ibb.co/dCuywT/dl_IKHeg_Tg_Eg.jpg',
'https://image.ibb.co/no6BGT/Di_T84_WNjdko.jpg',
'https://image.ibb.co/cGG0Ao/DFw_TEve14.jpg',
'https://image.ibb.co/csMp38/d7_Bcti_Yaujc.jpg',
'https://image.ibb.co/mjzywT/De_Lzg_QGPV7_M.jpg',
'https://image.ibb.co/eti2O8/D4_XIUm_BKXU0.jpg',
'https://image.ibb.co/cKMBGT/csgxd_VRDm_DI.jpg',
'https://image.ibb.co/hpebi8/Crj2jzb_EVMA.jpg',
'https://image.ibb.co/mReywT/c_R4_BDft_O1rk.jpg',
'https://image.ibb.co/j6zLAo/Cp_Tu_Gume_KDg.jpg',
'https://image.ibb.co/h9dfAo/cm_X2_P4u_Pil_I.jpg',
'https://image.ibb.co/nGVtVo/c_GVg2by8_CRI.jpg',
'https://image.ibb.co/mrr0Ao/cl_YLQ1_UHEn4.jpg',
'https://image.ibb.co/i0KWGT/byo2r_SVYf_Zg.jpg',
'https://image.ibb.co/gw6p38/b_Ueb_ZPBP3_Uc.jpg',
'https://image.ibb.co/eF10Ao/Bu8_FAYVM8_T4.jpg',
'https://image.ibb.co/kXLtVo/b_Td_I0_R2_D75_Q.jpg',
'https://image.ibb.co/ehqGi8/Bt1_HB5_Fjnl_I.jpg',
'https://image.ibb.co/ctyrGT/Bros_Ge1b_XEY.jpg',
'https://image.ibb.co/grOQbT/BN1_DUCD2h_D8.jpg',
'https://image.ibb.co/cNH7qo/b_GJz81_Ffb_AA.jpg',
'https://image.ibb.co/edu938/bd0_HCg_Dyu_O8.jpg',
'https://image.ibb.co/dyY2O8/b_Fg_QYn29xjg.jpg',
'https://image.ibb.co/nLHkbT/a_XQVDQjzq_M4.jpg',
'https://image.ibb.co/nAAGi8/atp_Jqs_U1_SKA.jpg',
'https://image.ibb.co/k5AGi8/a_GG2p651_CZk.jpg',
'https://image.ibb.co/dFSwi8/aonbg_Rh_Q97_Y.jpg',
'https://image.ibb.co/njwBGT/Af_Hm_Qc_Iy3_Fo.jpg',
'https://image.ibb.co/ibF5bT/a_DR5w_VDd_NWA.jpg',
'https://image.ibb.co/jcCU38/Ae6y_Lq_F8i4.jpg',
'https://image.ibb.co/jVSwi8/abl_G5_Km4_Tqc.jpg',
'https://image.ibb.co/nwHwi8/A8_Arq0_VOYY0.jpg',
'https://image.ibb.co/g7RNO8/a1_U4_X_YQe_D4.jpg',
'https://image.ibb.co/mjSkbT/A5ia_QJSa2_Mw.jpg',
'https://image.ibb.co/jRWp38/a0_THar_K87_ZM.jpg',
'https://image.ibb.co/ca4nqo/a_2jv_BZBSy0.jpg',
'https://image.ibb.co/db1BGT/83_Cr_Msx_XO0.jpg',
'https://image.ibb.co/fehJwT/64ah_JNal8_SA.jpg',
'https://image.ibb.co/kX60Ao/55_XTVD9_Bsik.jpg',
'https://image.ibb.co/noi2O8/9_Wa3_m848_ZY.jpg',
'https://image.ibb.co/eBr0Ao/9_Btwp_C2_Fh4_Q.jpg',
'https://image.ibb.co/idQhO8/9i_V_GNOKkb_M.jpg',
'https://image.ibb.co/cMHwi8/9_Cf_Wdhg9f4.jpg',
'https://image.ibb.co/ekODVo/8v_Igl_RM_r7o.jpg',
'https://image.ibb.co/ejrdwT/8_l_Cr_Wm_YDl_E.jpg',
'https://image.ibb.co/kmjbi8/7_X9bra5o91_Y.jpg',
'https://image.ibb.co/b0Gp38/7_K9cz9goiv_U.jpg',
'https://image.ibb.co/f6PLAo/6q7m_OI66_Ga_Y.jpg',
'https://image.ibb.co/gku3Vo/6mjbtclvz_A.jpg',
'https://image.ibb.co/hk5AAo/6k_Onr3q8_To_Y.jpg',
'https://image.ibb.co/kxDxqo/5_Lhunvu_D_g_U.jpg',
'https://image.ibb.co/eunOVo/5j_Yimn_PDd_g.jpg',
'https://image.ibb.co/hxRvbT/5_F56_BMb_RE3_U.jpg']
