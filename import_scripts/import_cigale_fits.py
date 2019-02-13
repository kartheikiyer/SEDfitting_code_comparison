
import numpy as np
from astropy.io import fits
from import_catalogs import get_cat
cat_small_ids, cat_z1_ids, cat_z3_ids = get_cat()

vb = False


cigale_cat = np.genfromtxt('code_outputs/cigale_results_noAGN.txt')
if vb == True:
    print(cigale_cat.shape)

# what parameter should I use to best compare to the Calzetti Av that other codes produce?

#header: id
#bayes.attenuation.E_BVs.stellar.young  bayes.attenuation.E_BVs.stellar.young_err
#bayes.attenuation.FUV  bayes.attenuation.FUV_err
#bayes.param.IRX  bayes.param.IRX_err  bayes.param.beta_calz94  bayes.param.beta_calz94_err
#bayes.sfh.age  bayes.sfh.age_err  bayes.sfh.burst_age  bayes.sfh.burst_age_err
#bayes.sfh.f_burst  bayes.sfh.f_burst_err  bayes.sfh.tau_main  bayes.sfh.tau_main_err
#bayes.stellar.metallicity  bayes.stellar.metallicity_err
#bayes.dust.luminosity  bayes.dust.luminosity_err
#bayes.param.restframe_Lnu(FUV)  bayes.param.restframe_Lnu(FUV)_err
#bayes.sfh.sfr10Myrs  bayes.sfh.sfr10Myrs_err
#bayes.stellar.m_star  bayes.stellar.m_star_err
#best.chi_square  best.reduced_chi_square
#best.attenuation.B_B90  best.attenuation.E_BVs.nebular.continuum_old
#best.attenuation.E_BVs.nebular.continuum_young
#best.attenuation.E_BVs.nebular.lines_old  best.attenuation.E_BVs.nebular.lines_young
#best.attenuation.E_BVs.stellar.old  best.attenuation.E_BVs.stellar.young
#best.attenuation.FUV  best.attenuation.V_B90  best.attenuation.ebvs_old_factor
#best.attenuation.powerlaw_slope  best.attenuation.uv_bump_amplitude  best.attenuation.uv_bump_wavelength
#best.attenuation.uv_bump_width  best.dust.alpha  best.dust.gamma  best.dust.qpah  best.dust.umin
#best.nebular.f_dust  best.nebular.f_esc  best.nebular.lines_width  best.nebular.logU
#best.param.EW(500.7/1.0)  best.param.EW(656.3/1.0)    best.param.IRX  best.param.beta_calz94
#best.param.restframe_FUV-NUV  best.param.restframe_NUV-r_prime  best.sfh.age  best.sfh.burst_age
#best.sfh.f_burst  best.sfh.tau_burst  best.sfh.tau_main  best.stellar.age_m_star  best.stellar.imf
#best.stellar.metallicity  best.stellar.old_young_separation_age  best.universe.age
#best.universe.luminosity_distance  best.universe.redshift  best.attenuation.nebular.continuum_old
#best.attenuation.nebular.continuum_young  best.attenuation.nebular.lines_old  best.attenuation.nebular.lines_young
#best.attenuation.stellar.old  best.attenuation.stellar.young  best.dust.luminosity     best.dust.mass
#best.param.restframe_Lnu(FUV)  best.param.restframe_Lnu(V_B90)  best.sfh.integrated
#best.sfh.sfr  best.sfh.sfr100Myrs  best.sfh.sfr10Myrs   best.stellar.lum  best.stellar.lum_ly
#best.stellar.lum_ly_old  best.stellar.lum_ly_young  best.stellar.lum_old  best.stellar.lum_young
#best.stellar.m_gas  best.stellar.m_gas_old  best.stellar.m_gas_young  best.stellar.m_star  best.stellar.m_star_old
#best.stellar.m_star_young  best.stellar.n_ly  best.stellar.n_ly_old  best.stellar.n_ly_young
#best.CTIO_U       best.VIMOS_U     best.ACS_F435W     best.ACS_F606W     best.ACS_F775W     best.ACS_F814W
#best.ACS_F850LP    best.WFC3_F098M    best.WFC3_F105W    best.WFC3_F125W    best.WFC3_F160W      best.ISAAC_KS
#best.HAWKI_KS      best.IRAC_CH1      best.IRAC_CH2      best.IRAC_CH3      best.IRAC_CH4


cigale_id = cigale_cat[0:,0]

# the Cigale output is a single file for both the small and z=1 catalogs.
# I'm splitting this into two catalogs

cigale_mask_small = np.zeros_like(cigale_id)
for i in range(len(cat_small_ids)):
    cigale_mask_small[cigale_id == cat_small_ids[i]+1] = 1

cigale_mask_z1 = np.zeros_like(cigale_id)
for i in range(len(cat_z1_ids)):
    cigale_mask_z1[cigale_id == cat_z1_ids[i]+1] = 1

if vb == True:
    print(np.sum(cigale_mask_small))
    print(np.sum(cigale_mask_z1))

#----------------------------------

cigale_id_small = cigale_id[cigale_mask_small.astype(bool)]



cigale_mass_small_noagn = np.log10(cigale_cat[cigale_mask_small.astype(bool),25])
cigale_mass_err_noagn = np.log10(cigale_cat[cigale_mask_small.astype(bool),26])
cigale_mass_lo_small_noagn = np.log10(10**cigale_mass_small_noagn - 10**cigale_mass_err_noagn)
cigale_mass_hi_small_noagn = np.log10(10**cigale_mass_small_noagn + 10**cigale_mass_err_noagn)

cigale_id_z1 = cigale_id[cigale_mask_z1.astype(bool)]

cigale_sfr_small_noagn = np.log10(cigale_cat[cigale_mask_small.astype(bool),23])
cigale_sfr_err_noagn = np.log10(cigale_cat[cigale_mask_small.astype(bool),24])
cigale_sfr_lo_small_noagn = np.log10(10**cigale_sfr_small_noagn - 10**cigale_sfr_err_noagn)
cigale_sfr_hi_small_noagn = np.log10(10**cigale_sfr_small_noagn + 10**cigale_sfr_err_noagn)


cigale_mass_z1_noagn = np.log10(cigale_cat[cigale_mask_z1.astype(bool),25])
cigale_mass_err_z1_noagn = np.log10(cigale_cat[cigale_mask_z1.astype(bool),26])
cigale_mass_lo_z1_noagn = np.log10(10**cigale_mass_z1_noagn - 10**cigale_mass_err_z1_noagn)
cigale_mass_hi_z1_noagn = np.log10(10**cigale_mass_z1_noagn + 10**cigale_mass_err_z1_noagn)
if vb == True:
    plt.hist(cigale_mass_z1_noagn)
    plt.show()

cigale_sfr_z1_noagn = np.log10(cigale_cat[cigale_mask_z1.astype(bool),23])
cigale_sfr_err_z1_noagn = np.log10(cigale_cat[cigale_mask_z1.astype(bool),24])
cigale_sfr_lo_z1_noagn = np.log10(10**cigale_sfr_z1_noagn - 10**cigale_sfr_z1_noagn)
cigale_sfr_hi_z1_noagn = np.log10(10**cigale_sfr_z1_noagn + 10**cigale_sfr_z1_noagn)
if vb == True:
    plt.hist(cigale_sfr_z1_noagn)
    plt.show()

if vb == True:
    plt.plot(cigale_mass_small_noagn,cigale_sfr_small_noagn,'o')
    plt.ylim(-4,3)
    plt.xlim(8,12)
    plt.xlabel('log Stellar Mass')
    plt.ylabel('log SFR')
    plt.show()

    plt.plot(cigale_mass_z1_noagn,cigale_sfr_z1_noagn,'o')
    plt.ylim(-4,3)
    plt.xlim(8,12)
    plt.xlabel('log Stellar Mass')
    plt.ylabel('log SFR')
    plt.show()


#------------------------------------------------------------------
# with AGN

#id
#bayes.agn.fracAGN  bayes.agn.fracAGN_err     bayes.agn.psy  bayes.agn.psy_err
#bayes.agn.tau  bayes.agn.tau_err
#bayes.attenuation.E_BVs.stellar.young  bayes.attenuation.E_BVs.stellar.young_err
#bayes.attenuation.FUV  bayes.attenuation.FUV_err
#bayes.param.IRX  bayes.param.IRX_err  bayes.param.beta_calz94  bayes.param.beta_calz94_err
#bayes.sfh.age  bayes.sfh.age_err  bayes.sfh.burst_age  bayes.sfh.burst_age_err
#bayes.sfh.f_burst  bayes.sfh.f_burst_err  bayes.sfh.tau_main  bayes.sfh.tau_main_err
#bayes.stellar.metallicity  bayes.stellar.metallicity_err  bayes.dust.luminosity  bayes.dust.luminosity_err
#bayes.param.restframe_Lnu(FUV)  bayes.param.restframe_Lnu(FUV)_err
#bayes.sfh.sfr10Myrs  bayes.sfh.sfr10Myrs_err
#bayes.stellar.m_star  bayes.stellar.m_star_err  best.chi_square  best.reduced_chi_square  best.agn.beta  best.agn.fracAGN  best.agn.gamma  best.agn.opening_angle  best.agn.psy  best.agn.r_ratio  best.agn.tau  best.attenuation.B_B90  best.attenuation.E_BVs.nebular.continuum_old  best.attenuation.E_BVs.nebular.continuum_young  best.attenuation.E_BVs.nebular.lines_old  best.attenuation.E_BVs.nebular.lines_young  best.attenuation.E_BVs.stellar.old  best.attenuation.E_BVs.stellar.young  best.attenuation.FUV  best.attenuation.V_B90  best.attenuation.ebvs_old_factor  best.attenuation.powerlaw_slope  best.attenuation.uv_bump_amplitude  best.attenuation.uv_bump_wavelength  best.attenuation.uv_bump_width  best.dust.alpha  best.dust.gamma  best.dust.qpah  best.dust.umin  best.nebular.f_dust  best.nebular.f_esc  best.nebular.lines_width  best.nebular.logU  best.param.EW(500.7/1.0)  best.param.EW(656.3/1.0)    best.param.IRX  best.param.beta_calz94  best.param.restframe_FUV-NUV  best.param.restframe_NUV-r_prime  best.sfh.age  best.sfh.burst_age  best.sfh.f_burst  best.sfh.tau_burst  best.sfh.tau_main  best.stellar.age_m_star  best.stellar.imf  best.stellar.metallicity  best.stellar.old_young_separation_age  best.universe.age  best.universe.luminosity_distance  best.universe.redshift  best.agn.agn_luminosity  best.agn.luminosity  best.agn.scatt_luminosity  best.agn.therm_luminosity  best.attenuation.nebular.continuum_old  best.attenuation.nebular.continuum_young  best.attenuation.nebular.lines_old  best.attenuation.nebular.lines_young  best.attenuation.stellar.old  best.attenuation.stellar.young  best.dust.luminosity     best.dust.mass  best.param.restframe_Lnu(FUV)  best.param.restframe_Lnu(V_B90)  best.sfh.integrated       best.sfh.sfr  best.sfh.sfr100Myrs  best.sfh.sfr10Myrs   best.stellar.lum  best.stellar.lum_ly  best.stellar.lum_ly_old  best.stellar.lum_ly_young  best.stellar.lum_old  best.stellar.lum_young  best.stellar.m_gas  best.stellar.m_gas_old  best.stellar.m_gas_young  best.stellar.m_star  best.stellar.m_star_old  best.stellar.m_star_young  best.stellar.n_ly  best.stellar.n_ly_old  best.stellar.n_ly_young        best.CTIO_U       best.VIMOS_U     best.ACS_F435W     best.ACS_F606W     best.ACS_F775W     best.ACS_F814W    best.ACS_F850LP    best.WFC3_F098M    best.WFC3_F105W    best.WFC3_F125W    best.WFC3_F160W      best.ISAAC_KS      best.HAWKI_KS      best.IRAC_CH1      best.IRAC_CH2      best.IRAC_CH3      best.IRAC_CH4

if vb == True:
    print('doing things with AGN now')

cigale_cat = np.genfromtxt('code_outputs/cigale_results_wAGN.txt')
if vb == True:
    print(cigale_cat.shape)

cigale_id = cigale_cat[0:,0]

cigale_mask_small = np.zeros_like(cigale_id)
for i in range(len(cat_small_ids)):
    cigale_mask_small[cigale_id == cat_small_ids[i]+1] = 1

cigale_mask_z1 = np.zeros_like(cigale_id)
for i in range(len(cat_z1_ids)):
    cigale_mask_z1[cigale_id == cat_z1_ids[i]+1] = 1

if vb == True:
    print(np.sum(cigale_mask_small))
    print(np.sum(cigale_mask_z1))

cigale_id_small = cigale_id[cigale_mask_small.astype(bool)]
cigale_mass_small_wagn = np.log10(cigale_cat[cigale_mask_small.astype(bool),31])
cigale_mass_err_wagn = np.log10(cigale_cat[cigale_mask_small.astype(bool),32])
cigale_mass_lo_small_wagn = np.log10(10**cigale_mass_small_wagn - 10**cigale_mass_err_wagn)
cigale_mass_hi_small_wagn = np.log10(10**cigale_mass_small_wagn + 10**cigale_mass_err_wagn)
if vb == True:
    plt.hist(cigale_mass_small_wagn)
    plt.show()

cigale_id_z1 = cigale_id[cigale_mask_z1.astype(bool)]
cigale_sfr_small_wagn = np.log10(cigale_cat[cigale_mask_small.astype(bool),29])
cigale_sfr_err_wagn = np.log10(cigale_cat[cigale_mask_small.astype(bool),30])
cigale_sfr_lo_small_wagn = np.log10(10**cigale_sfr_small_wagn - 10**cigale_sfr_err_wagn)
cigale_sfr_hi_small_wagn = np.log10(10**cigale_sfr_small_wagn + 10**cigale_sfr_err_wagn)
if vb == True:
    plt.hist(cigale_sfr_small_wagn)
    plt.show()

cigale_mass_z1_wagn = np.log10(cigale_cat[cigale_mask_z1.astype(bool),31])
cigale_mass_err_z1_wagn = np.log10(cigale_cat[cigale_mask_z1.astype(bool),32])
cigale_mass_lo_z1_wagn = np.log10(10**cigale_mass_z1_wagn - 10**cigale_mass_err_z1_wagn)
cigale_mass_hi_z1_wagn = np.log10(10**cigale_mass_z1_wagn + 10**cigale_mass_err_z1_wagn)
if vb == True:
    plt.hist(cigale_mass_z1_wagn)
    plt.show()

cigale_sfr_z1_wagn = np.log10(cigale_cat[cigale_mask_z1.astype(bool),29])
cigale_sfr_err_z1_wagn = np.log10(cigale_cat[cigale_mask_z1.astype(bool),30])
cigale_sfr_lo_z1_wagn = np.log10(10**cigale_sfr_z1_wagn - 10**cigale_sfr_z1_wagn)
cigale_sfr_hi_z1_wagn = np.log10(10**cigale_sfr_z1_wagn + 10**cigale_sfr_z1_wagn)
if vb == True:
    plt.hist(cigale_sfr_z1_wagn)
    plt.show()

if vb == True:
    plt.plot(cigale_mass_small_wagn,cigale_sfr_small_wagn,'o')
    plt.ylim(-4,3)
    plt.xlim(8,12)
    plt.xlabel('log Stellar Mass')
    plt.ylabel('log SFR')
    plt.show()

    plt.plot(cigale_mass_z1_wagn,cigale_sfr_z1_wagn,'o')
    plt.ylim(-4,3)
    plt.xlim(8,12)
    plt.xlabel('log Stellar Mass')
    plt.ylabel('log SFR')
    plt.show()


#header: id
#bayes.attenuation.E_BVs.stellar.young  bayes.attenuation.E_BVs.stellar.young_err
#bayes.attenuation.FUV  bayes.attenuation.FUV_err
#bayes.param.IRX  bayes.param.IRX_err  bayes.param.beta_calz94  bayes.param.beta_calz94_err
#bayes.sfh.age  bayes.sfh.age_err  bayes.sfh.burst_age  bayes.sfh.burst_age_err
#bayes.sfh.f_burst  bayes.sfh.f_burst_err  bayes.sfh.tau_main  bayes.sfh.tau_main_err
#bayes.stellar.metallicity  bayes.stellar.metallicity_err
#bayes.dust.luminosity  bayes.dust.luminosity_err
#bayes.param.restframe_Lnu(FUV)  bayes.param.restframe_Lnu(FUV)_err
#bayes.sfh.sfr10Myrs  bayes.sfh.sfr10Myrs_err
#bayes.stellar.m_star  bayes.stellar.m_star_err
#best.chi_square  best.reduced_chi_square  best.attenuation.B_B90  best.attenuation.E_BVs.nebular.continuum_old  best.attenuation.E_BVs.nebular.continuum_young  best.attenuation.E_BVs.nebular.lines_old  best.attenuation.E_BVs.nebular.lines_young  best.attenuation.E_BVs.stellar.old  best.attenuation.E_BVs.stellar.young  best.attenuation.FUV  best.attenuation.V_B90  best.attenuation.ebvs_old_factor  best.attenuation.powerlaw_slope  best.attenuation.uv_bump_amplitude  best.attenuation.uv_bump_wavelength  best.attenuation.uv_bump_width  best.dust.alpha  best.dust.gamma  best.dust.qpah  best.dust.umin  best.nebular.f_dust  best.nebular.f_esc  best.nebular.lines_width  best.nebular.logU  best.param.EW(500.7/1.0)  best.param.EW(656.3/1.0)    best.param.IRX  best.param.beta_calz94  best.param.restframe_FUV-NUV  best.param.restframe_NUV-r_prime  best.sfh.age  best.sfh.burst_age  best.sfh.f_burst  best.sfh.tau_burst  best.sfh.tau_main  best.stellar.age_m_star  best.stellar.imf  best.stellar.metallicity  best.stellar.old_young_separation_age  best.universe.age  best.universe.luminosity_distance  best.universe.redshift  best.attenuation.nebular.continuum_old  best.attenuation.nebular.continuum_young  best.attenuation.nebular.lines_old  best.attenuation.nebular.lines_young  best.attenuation.stellar.old  best.attenuation.stellar.young  best.dust.luminosity     best.dust.mass  best.param.restframe_Lnu(FUV)  best.param.restframe_Lnu(V_B90)  best.sfh.integrated       best.sfh.sfr  best.sfh.sfr100Myrs  best.sfh.sfr10Myrs   best.stellar.lum  best.stellar.lum_ly  best.stellar.lum_ly_old  best.stellar.lum_ly_young  best.stellar.lum_old  best.stellar.lum_young  best.stellar.m_gas  best.stellar.m_gas_old  best.stellar.m_gas_young  best.stellar.m_star  best.stellar.m_star_old  best.stellar.m_star_young  best.stellar.n_ly  best.stellar.n_ly_old  best.stellar.n_ly_young        best.CTIO_U       best.VIMOS_U     best.ACS_F435W     best.ACS_F606W     best.ACS_F775W     best.ACS_F814W    best.ACS_F850LP    best.WFC3_F098M    best.WFC3_F105W    best.WFC3_F125W    best.WFC3_F160W      best.ISAAC_KS      best.HAWKI_KS      best.IRAC_CH1      best.IRAC_CH2      best.IRAC_CH3      best.IRAC_CH4

#-------------------------------------------------------------------------------

cigale_full = fits.open('code_outputs/CIGALE_results_candels_goods-south_v0.fits')
# cigale_full.info()
# cigale_full[1].header

# what parameter should I use to best compare to the Calzetti Av that other codes produce?

#header: id
#bayes.attenuation.E_BVs.stellar.young  bayes.attenuation.E_BVs.stellar.young_err
#bayes.attenuation.FUV  bayes.attenuation.FUV_err
#bayes.param.IRX  bayes.param.IRX_err  bayes.param.beta_calz94  bayes.param.beta_calz94_err
#bayes.sfh.age  bayes.sfh.age_err  bayes.sfh.burst_age  bayes.sfh.burst_age_err
#bayes.sfh.f_burst  bayes.sfh.f_burst_err  bayes.sfh.tau_main  bayes.sfh.tau_main_err
#bayes.stellar.metallicity  bayes.stellar.metallicity_err
#bayes.dust.luminosity  bayes.dust.luminosity_err
#bayes.param.restframe_Lnu(FUV)  bayes.param.restframe_Lnu(FUV)_err
#bayes.sfh.sfr10Myrs  bayes.sfh.sfr10Myrs_err
#bayes.stellar.m_star  bayes.stellar.m_star_err
#best.chi_square  best.reduced_chi_square
#best.attenuation.B_B90  best.attenuation.E_BVs.nebular.continuum_old
#best.attenuation.E_BVs.nebular.continuum_young
#best.attenuation.E_BVs.nebular.lines_old  best.attenuation.E_BVs.nebular.lines_young
#best.attenuation.E_BVs.stellar.old  best.attenuation.E_BVs.stellar.young
#best.attenuation.FUV  best.attenuation.V_B90  best.attenuation.ebvs_old_factor
#best.attenuation.powerlaw_slope  best.attenuation.uv_bump_amplitude  best.attenuation.uv_bump_wavelength
#best.attenuation.uv_bump_width  best.dust.alpha  best.dust.gamma  best.dust.qpah  best.dust.umin
#best.nebular.f_dust  best.nebular.f_esc  best.nebular.lines_width  best.nebular.logU
#best.param.EW(500.7/1.0)  best.param.EW(656.3/1.0)    best.param.IRX  best.param.beta_calz94
#best.param.restframe_FUV-NUV  best.param.restframe_NUV-r_prime  best.sfh.age  best.sfh.burst_age
#best.sfh.f_burst  best.sfh.tau_burst  best.sfh.tau_main  best.stellar.age_m_star  best.stellar.imf
#best.stellar.metallicity  best.stellar.old_young_separation_age  best.universe.age
#best.universe.luminosity_distance  best.universe.redshift  best.attenuation.nebular.continuum_old
#best.attenuation.nebular.continuum_young  best.attenuation.nebular.lines_old  best.attenuation.nebular.lines_young
#best.attenuation.stellar.old  best.attenuation.stellar.young  best.dust.luminosity     best.dust.mass
#best.param.restframe_Lnu(FUV)  best.param.restframe_Lnu(V_B90)  best.sfh.integrated
#best.sfh.sfr  best.sfh.sfr100Myrs  best.sfh.sfr10Myrs   best.stellar.lum  best.stellar.lum_ly
#best.stellar.lum_ly_old  best.stellar.lum_ly_young  best.stellar.lum_old  best.stellar.lum_young
#best.stellar.m_gas  best.stellar.m_gas_old  best.stellar.m_gas_young  best.stellar.m_star  best.stellar.m_star_old
#best.stellar.m_star_young  best.stellar.n_ly  best.stellar.n_ly_old  best.stellar.n_ly_young
#best.CTIO_U       best.VIMOS_U     best.ACS_F435W     best.ACS_F606W     best.ACS_F775W     best.ACS_F814W
#best.ACS_F850LP    best.WFC3_F098M    best.WFC3_F105W    best.WFC3_F125W    best.WFC3_F160W      best.ISAAC_KS
#best.HAWKI_KS      best.IRAC_CH1      best.IRAC_CH2      best.IRAC_CH3      best.IRAC_CH4

cigale_full_cat = cigale_full[1].data

cigale_mass_z3 = np.zeros((len(cat_z3_ids)))
cigale_mass_err_z3 = np.zeros((len(cat_z3_ids)))
cigale_mass_z3_lo = np.zeros((len(cat_z3_ids)))
cigale_mass_z3_hi = np.zeros((len(cat_z3_ids)))

cigale_sfr_z3 = np.zeros((len(cat_z3_ids)))
cigale_sfr_err_z3 = np.zeros((len(cat_z3_ids)))
cigale_sfr_z3_lo = np.zeros((len(cat_z3_ids)))
cigale_sfr_z3_hi = np.zeros((len(cat_z3_ids)))

for i in range(len(cigale_mass_z3)):
    cigale_mass_z3[i] = np.log10(cigale_full_cat[cat_z3_ids[i].astype(int)][25])
    cigale_mass_err_z3[i] = np.log10(cigale_full_cat[cat_z3_ids[i].astype(int)][26])
    cigale_mass_z3_lo[i] = np.log10(10**cigale_mass_z3[i] - 10**cigale_mass_err_z3[i])
    cigale_mass_z3_hi[i] = np.log10(10**cigale_mass_z3[i] + 10**cigale_mass_err_z3[i])

    cigale_sfr_z3[i] = np.log10(cigale_full_cat[cat_z3_ids[i].astype(int)][23])
    cigale_sfr_err_z3[i] = np.log10(cigale_full_cat[cat_z3_ids[i].astype(int)][24])
    cigale_sfr_z3_lo[i] = np.log10(10**cigale_sfr_z3[i] - 10**cigale_sfr_err_z3[i])
    cigale_sfr_z3_hi[i] = np.log10(10**cigale_sfr_z3[i] + 10**cigale_sfr_err_z3[i])

    # print(cigale_full_cat[cat_z3_ids[i].astype(int)][0], cat_z3_ids[i])

if vb == True:
    plt.plot(cigale_mass_z3, cigale_sfr_z3,'o')
    plt.ylim(-4,3)
    plt.xlim(8,12)
    plt.xlabel('log Stellar Mass')
    plt.ylabel('log SFR')
    plt.show()

cigale_full.close()

#-------------------------------------------------------------------------------
#--------------NEW CIGALE FITS (from Kasia?)------------------------------------
#-------------------------------------------------------------------------------

#c1 = fits.open('code_outputs_IR/cigale_without_IR_without_AGNs_results.fits')
c1 = fits.open('code_outputs_IR/cigale_noIR_noAGN_results.fits')
if vb == True:
    print(c1.info())
#print(c1[1].header)

cigale_ids = np.zeros((len(cat_z1_ids),))

cigale_mass = np.zeros((len(cat_z1_ids),))
cigale_sfr = np.zeros((len(cat_z1_ids),))
cigale_Av = np.zeros((len(cat_z1_ids),))
cigale_Av_err = np.zeros((len(cat_z1_ids),))

for i in range(len(cat_z1_ids)):
    temp = c1[1].data[i][0]

    cigale_ids[i] = temp
    cigale_mass[i] = c1[1].data[i][1]
    cigale_sfr[i] = c1[1].data[i][3]
    cigale_Av[i] = c1[1].data[i][5]
    cigale_Av_err[i] = c1[1].data[i][6]

c1.close()

#c3 = fits.open('code_outputs_IR/cigale_wit_IR_with_AGNs_results.fits')
c3 = fits.open('code_outputs_IR/cigale_withIR_withAGN_results.fits')
if vb == True:
    print(c3.info())

cigale_ir_agn_ids = np.zeros((len(cat_z1_ids),))

cigale_ir_agn_mass = np.zeros((len(cat_z1_ids),))
cigale_ir_agn_sfr = np.zeros((len(cat_z1_ids),))
cigale_ir_agn_Av = np.zeros((len(cat_z1_ids),))

for i in range(len(cat_z1_ids)):
    temp = c3[1].data[i][0]

    cigale_ir_agn_ids[i] = temp
    cigale_ir_agn_mass[i] = c3[1].data[i][1]
    cigale_ir_agn_sfr[i] = c3[1].data[i][3]
    cigale_ir_agn_Av[i] = c3[1].data[i][5]


# c3[1].header
c3.close()

print('imported cigale fits.')
