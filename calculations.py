import numpy as np
from scipy.stats import binom, hypergeom

D2={2:1.128,3:1.693,4:2.059,5:2.326,6:2.534,7:2.704,8:2.847,9:2.970,10:3.078,11:3.173,12:3.258,13:3.336,14:3.407,15:3.472,16:3.532,17:3.588,18:3.640,19:3.689,20:3.735,21:3.778,22:3.819,23:3.858,24:3.895,25:3.931}
D3_D4={2:(0,3.267),3:(0,2.574),4:(0,2.282),5:(0,2.114),6:(0,2.004),7:(.076,1.924),8:(.136,1.864),9:(.184,1.816),10:(.223,1.777),11:(.256,1.744),12:(.283,1.717),13:(.307,1.693),14:(.328,1.672),15:(.347,1.653),16:(.363,1.637),17:(.378,1.622),18:(.391,1.608),19:(.403,1.597),20:(.415,1.585),21:(.425,1.575),22:(.434,1.566),23:(.443,1.557),24:(.451,1.548),25:(.459,1.541)}

def calculate_xbar_from_summary(n,grand_mean,average_range=None,sigma=None):
    if sigma is not None: margin=3*sigma/np.sqrt(n)
    elif average_range is not None:
        if n not in D2: raise ValueError("Supported sample sizes are 2-25.")
        margin=3*average_range/(D2[n]*np.sqrt(n))
    else: raise ValueError("Provide average_range or sigma.")
    return {"cl":float(grand_mean),"ucl":float(grand_mean+margin),"lcl":float(grand_mean-margin)}

def calculate_xbar_from_sample_summaries(sample_means,sample_ranges,n):
    m=np.asarray(sample_means,float); r=np.asarray(sample_ranges,float)
    gm=float(m.mean()); rb=float(r.mean()); z=calculate_xbar_from_summary(n,gm,rb)
    o=np.where((m>z["ucl"])|(m<z["lcl"]))[0]
    return {**z,"grand_mean":gm,"average_range":rb,"sample_means":m,"sample_ranges":r,"out_of_control":o,"status":"OUT OF CONTROL" if len(o) else "IN CONTROL"}

def calculate_r_from_summary(n,average_range):
    if n not in D3_D4: raise ValueError("Supported sample sizes are 2-25.")
    d3,d4=D3_D4[n]
    return {"cl":float(average_range),"ucl":float(d4*average_range),"lcl":float(d3*average_range),"D3":d3,"D4":d4}

def calculate_r_from_ranges(ranges,n):
    r=np.asarray(ranges,float); rb=float(r.mean()); z=calculate_r_from_summary(n,rb)
    o=np.where((r>z["ucl"])|(r<z["lcl"]))[0]
    return {**z,"average_range":rb,"ranges":r,"out_of_control":o,"status":"OUT OF CONTROL" if len(o) else "IN CONTROL"}

def calculate_p_chart(proportions,sample_size,center=None):
    p=np.asarray(proportions,float); pb=float(p.mean() if center is None else center)
    s=np.sqrt(pb*(1-pb)/sample_size); u=min(1,pb+3*s); l=max(0,pb-3*s)
    o=np.where((p>u)|(p<l))[0]
    return {"p_bar":pb,"cl":pb,"ucl":float(u),"lcl":float(l),"proportions":p,"out_of_control":o,"status":"OUT OF CONTROL" if len(o) else "IN CONTROL"}

def acceptance_probability(n,c,p): return float(binom.cdf(c,n,p))

def producer_risk(n,c,aql): return 1-acceptance_probability(n,c,aql)

def consumer_risk(n,c,ltpd): return acceptance_probability(n,c,ltpd)

def acceptance_sampling(lot_size,sample_size,defect_probability,acceptance_number,simulations=10000,seed=42):
    d=round(lot_size*defect_probability)
    exact=float(hypergeom.cdf(acceptance_number,lot_size,d,sample_size))
    approx=acceptance_probability(sample_size,acceptance_number,defect_probability)
    rng=np.random.default_rng(seed)
    draws=rng.hypergeometric(lot_size-d,d,sample_size,size=simulations)
    sim=float(np.mean(draws<=acceptance_number))
    return {"defective_items":d,"exact_probability":exact,"binomial_probability":approx,"simulated_probability":sim,"difference":abs(exact-sim),"simulated_defects":draws}
