
import numpy as np

from astropy.cosmology import FlatLambdaCDM
cosmo = FlatLambdaCDM(H0=70, Om0=0.3)

from import_catalogs import get_cat, get_cat_z
cat_small_ids, cat_z1_ids, cat_z3_ids = get_cat()
cat_small_z, cat_z1_z, cat_z3_z = get_cat_z()

vb = False


# new SpeedyMC results:

# Format:
#ID
#Ln(Age/yr)    sigma(Ln(Age/yr))
#Ln(StM/MSun)  sigma(Ln(StM/MSun))
#EBV    sigma(EBV)
#ln(tau)   sigma(ln(tau))
#SFR    sigma(SFR)    BF_Chi2     Quality(1=best)

speedy_cat = np.genfromtxt('code_outputs/SpeedyMC_CANDELS_GDSS_Cali_wSFR_Del.out')
if vb == True:
    print(speedy_cat.shape)

# SpeedyMC doesn't output SFRs, need to calculate it using the linexp SFH.

#ID     Ln(Age/yr)    sigma(Ln(Age/yr))  Ln(StM/MSun)  sigma(Ln(StM/MSun))
#EBV    sigma(EBV)    ln(tau)   sigma(ln(tau))    BF_Chi2     Quality(1=best)
speedy_id_small = speedy_cat[0:,0]
speedy_mass_small = np.log10(np.exp(speedy_cat[0:,3]))
speedy_mass_lo_small = np.log10(np.exp(speedy_cat[0:,3] - speedy_cat[0:,4]))
speedy_mass_hi_small = np.log10(np.exp(speedy_cat[0:,3] + speedy_cat[0:,4]))



# Should age be this quantity, or
speedy_age = cosmo.age(cat_small_z).value - np.exp(speedy_cat[0:,1])/1e9
# or
#speedy_age = np.exp(speedy_cat[0:,1])/1e9
speedy_tau = np.exp(speedy_cat[0:,7])

#timeax = np.arange(0.01,14,0.01)

#speedy_mass_calc = np.zeros((len(speedy_id_small),))
#speedy_sfr_calc =  np.zeros((len(speedy_id_small),))
#for t_id in range(len(speedy_id_small)):
#    speedy_sfh = ((timeax - speedy_age[t_id])/speedy_tau[t_id])*np.exp(-((timeax - speedy_age[t_id])/speedy_tau[t_id]))
#
#    mask = (speedy_sfh < 0)
#    speedy_sfh[mask] = 0
#
#    time_index = np.argmin(np.abs(timeax - cosmo.age(cat_small_z[t_id]).value))
#    small_timeax = timeax[0:time_index]
#    small_speedy_sfh = speedy_sfh[0:time_index]
#
#    tempmass = (np.trapz(x = small_timeax*1e9, y = small_speedy_sfh))

    # adding a factor of 0.6 to account for stellar vs galaxy mass.
    # need to ask Viviana how she does this.
#    small_speedy_sfh_massnorm = small_speedy_sfh * (10**speedy_mass_small[t_id]/(tempmass*0.6))

#    speedy_mass_calc[t_id] = np.log10(np.trapz(x = small_timeax*1e9, y = small_speedy_sfh_massnorm))
#    speedy_sfr_calc[t_id] = np.log10(small_speedy_sfh_massnorm[-1])

    #plt.plot(timeax,speedy_sfh)
    #plt.title('speedy mass: '+str(speedy_mass_calc[t_id]))
    #plt.show()

#print(speedy_mass_calc)
#plt.plot(speedy_mass_calc, speedy_mass_small,'.')
#plt.title('mass comparison')
#plt.show()

#print(speedy_sfr_calc)

if vb == True:
    print(speedy_cat[0:,9])


speedy_Av_small = (speedy_cat[0:,5])*4.05
speedy_Av_lo_small = (speedy_cat[0:,5] - speedy_cat[0:,6])*4.05
speedy_Av_hi_small = (speedy_cat[0:,5] + speedy_cat[0:,6])*4.05

#speedy_sfr_small = np.zeros_like(speedy_mass_small)
#speedy_sfr_small = speedy_sfr_calc

speedy_sfr_small = np.log10((speedy_cat[0:,9]))
speedy_sfr_lo_small = np.log10((speedy_cat[0:,9] - speedy_cat[0:,10]))
speedy_sfr_hi_small = np.log10((speedy_cat[0:,9] + speedy_cat[0:,10]))

if vb == True:
    plt.scatter(speedy_mass_small,speedy_sfr_small,c=speedy_Av_small)
    plt.colorbar()
    plt.ylim(-4,3)
    plt.xlim(8,12)
    plt.xlabel('log Stellar Mass')
    plt.ylabel('log SFR')
    plt.show()

    print(speedy_cat[0:,3],speedy_cat[0:,4])



speedy_cat = np.genfromtxt('code_outputs/SpeedyMC_CANDELS_GDSS_z1_Cali_wSFR_Del.out')
if vb == True:
    print(speedy_cat.shape)

#ID     Ln(Age/yr)    sigma(Ln(Age/yr))  Ln(StM/MSun)  sigma(Ln(StM/MSun))
#EBV    sigma(EBV)    ln(tau)   sigma(ln(tau))    BF_Chi2     Quality(1=best)

speedy_id_z1 = speedy_cat[0:,0]
speedy_mass_z1 = np.log10(np.exp(speedy_cat[0:,3]))
speedy_mass_lo_z1 = np.log10(np.exp(speedy_cat[0:,3] - speedy_cat[0:,4]))
speedy_mass_hi_z1 = np.log10(np.exp(speedy_cat[0:,3] + speedy_cat[0:,4]))
speedy_mass_z1_masked = speedy_mass_z1[~np.isnan(speedy_mass_z1)]

speedy_Av_z1 = (speedy_cat[0:,5])*4.05
speedy_Av_lo_z1 = (speedy_cat[0:,5] - speedy_cat[0:,6])*4.05
speedy_Av_hi_z1 = (speedy_cat[0:,5] + speedy_cat[0:,6])*4.05


speedy_sfr_z1 = np.log10((speedy_cat[0:,9]))
speedy_sfr_lo_z1 = np.log10((speedy_cat[0:,9] - speedy_cat[0:,10]))
speedy_sfr_hi_z1 = np.log10((speedy_cat[0:,9] + speedy_cat[0:,10]))

if vb == True:
    print(speedy_mass_hi_z1- speedy_mass_lo_z1)

# Should age be this quantity, or
#speedy_age = cosmo.age(cat_z1_z).value - np.exp(speedy_cat[0:,1])/1e9
# or
#speedy_age = np.exp(speedy_cat[0:,1])/1e9

#speedy_tau = np.exp(speedy_cat[0:,7])

#timeax = np.arange(0.01,14,0.01)

#speedy_mass_calc = np.zeros((len(speedy_id_z1),))
#speedy_sfr_calc =  np.zeros((len(speedy_id_z1),))
#for t_id in range(len(speedy_id_z1)):
#    speedy_sfh = ((timeax - speedy_age[t_id])/speedy_tau[t_id])*np.exp(-((timeax - speedy_age[t_id])/speedy_tau[t_id]))
#
#    mask = (speedy_sfh < 0)
#    speedy_sfh[mask] = 0
#
#    time_index = np.argmin(np.abs(timeax - cosmo.age(cat_z1_z[t_id]).value))
#    small_timeax = timeax[0:time_index]
#    small_speedy_sfh = speedy_sfh[0:time_index]
#
#    tempmass = (np.trapz(x = small_timeax*1e9, y = small_speedy_sfh))

    # adding a factor of 0.6 to account for stellar vs galaxy mass.
    # need to ask Viviana how she does this.
#    small_speedy_sfh_massnorm = small_speedy_sfh * (10**speedy_mass_z1[t_id]/(tempmass*0.6))
#
#    speedy_mass_calc[t_id] = np.log10(np.trapz(x = small_timeax*1e9, y = small_speedy_sfh_massnorm))
#    speedy_sfr_calc[t_id] = np.log10(small_speedy_sfh_massnorm[-1])


#speedy_sfr_z1 = np.zeros_like(speedy_mass_z1)
#speedy_mass_small = np.log10(np.exp(speedy_cat[0:,3]))
#speedy_mass_lo_small = np.log10(np.exp(speedy_cat[0:,3] - speedy_cat[0:,4]))
#speedy_mass_hi_small = np.log10(np.exp(speedy_cat[0:,3] + speedy_cat[0:,4]))


if vb == True:
    plt.scatter(speedy_mass_z1,speedy_sfr_z1,c=speedy_Av_z1)
    plt.colorbar()
    plt.ylim(-4,3)
    plt.xlim(8,12)
    plt.xlabel('log Stellar Mass')
    plt.ylabel('log SFR')
    plt.show()

# need to ask Viviana how to use uncertainties on tau, t0 to compute SFR uncertainties





speedy_cat = np.genfromtxt('code_outputs/SpeedyMC_CANDELS_GDSS_z3_Cali_wSFR_Del.out')
if vb == True:
    print(speedy_cat.shape)

#ID     Ln(Age/yr)    sigma(Ln(Age/yr))  Ln(StM/MSun)  sigma(Ln(StM/MSun))
#EBV    sigma(EBV)    ln(tau)   sigma(ln(tau))    BF_Chi2     Quality(1=best)

speedy_id_z3 = speedy_cat[0:,0]
speedy_mass_z3 = np.log10(np.exp(speedy_cat[0:,3]))
speedy_mass_lo_z3 = np.log10(np.exp(speedy_cat[0:,3]) - np.exp(speedy_cat[0:,4]))
speedy_mass_hi_z3 = np.log10(np.exp(speedy_cat[0:,3]) + np.exp(speedy_cat[0:,4]))
speedy_mass_z3_masked = speedy_mass_z3[~np.isnan(speedy_mass_z3)]

speedy_Av_z3 = (speedy_cat[0:,5])*4.05
speedy_Av_lo_z3 = (speedy_cat[0:,5] - speedy_cat[0:,6])*4.05
speedy_Av_hi_z3 = (speedy_cat[0:,5] + speedy_cat[0:,6])*4.05


speedy_sfr_z3 = np.log10((speedy_cat[0:,9]))
speedy_sfr_lo_z3 = np.log10((speedy_cat[0:,9] - speedy_cat[0:,10]))
speedy_sfr_hi_z3 = np.log10((speedy_cat[0:,9] + speedy_cat[0:,10]))


if vb == True:
    plt.scatter(speedy_mass_z3,speedy_sfr_z3,c=speedy_Av_z3)
    plt.colorbar()
    plt.ylim(-4,3)
    plt.xlim(8,12)
    plt.xlabel('log Stellar Mass')
    plt.ylabel('log SFR')
    plt.show()

print('imported SpeedyMC fits.')
