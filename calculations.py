import numpy as np
from scipy.stats import binom

D2={2:1.128,3:1.693,4:2.059,5:2.326,6:2.534,7:2.704,8:2.847,9:2.970,10:3.078,11:3.173,12:3.258,13:3.336,14:3.407,15:3.472,16:3.532,17:3.588,18:3.640,19:3.689,20:3.735,21:3.778,22:3.819,23:3.858,24:3.895,25:3.931}
D3_D4={2:(0,3.267),3:(0,2.574),4:(0,2.282),5:(0,2.114),6:(0,2.004),7:(.076,1.924),8:(.136,1.864),9:(.184,1.816),10:(.223,1.777),11:(.256,1.744),12:(.283,1.717),13:(.307,1.693),14:(.328,1.672),15:(.347,1.653),16:(.363,1.637),17:(.378,1.622),18:(.391,1.608),19:(.403,1.597),20:(.415,1.585),21:(.425,1.575),22:(.434,1.566),23:(.443,1.557),24:(.451,1.548),25:(.459,1.541)}

def xbar_limits(n,mean,rbar=None,sigma_x=None):
    if sigma_x is not None: margin=3*sigma_x
    elif rbar is not None: margin=3*rbar/(D2[n]*np.sqrt(n))
    else: raise ValueError("Provide rbar or sigma_x")
    return {"cl":float(mean),"ucl":float(mean+margin),"lcl":float(mean-margin)}

def xbar_series(means,ranges,n):
    means=np.asarray(means,float); ranges=np.asarray(ranges,float)
    gm=float(means.mean()); rb=float(ranges.mean()); z=xbar_limits(n,gm,rb)
    out=np.where((means>z["ucl"])|(means<z["lcl"]))[0]
    return {**z,"values":means,"rbar":rb,"out":out,"status":"OUT OF CONTROL" if len(out) else "IN CONTROL"}

def xbar_raw(data):
    a=np.asarray(data,float)
    return xbar_series(a.mean(1),a.max(1)-a.min(1),a.shape[1])

def r_limits(n,rbar):
    d3,d4=D3_D4[n]
    return {"cl":float(rbar),"ucl":float(rbar*d4),"lcl":float(rbar*d3)}

def r_series(ranges,n):
    r=np.asarray(ranges,float); rb=float(r.mean()); z=r_limits(n,rb)
    out=np.where((r>z["ucl"])|(r<z["lcl"]))[0]
    return {**z,"values":r,"rbar":rb,"out":out,"status":"OUT OF CONTROL" if len(out) else "IN CONTROL"}

def r_raw(data):
    a=np.asarray(data,float)
    return r_series(a.max(1)-a.min(1),a.shape[1])

def p_limits(n,p):
    s=np.sqrt(p*(1-p)/n)
    return {"cl":float(p),"ucl":float(min(1,p+3*s)),"lcl":float(max(0,p-3*s))}

def p_series(values,n,target=None):
    v=np.asarray(values,float); center=float(v.mean() if target is None else target); z=p_limits(n,center)
    out=np.where((v>z["ucl"])|(v<z["lcl"]))[0]
    return {**z,"values":v,"out":out,"status":"OUT OF CONTROL" if len(out) else "IN CONTROL"}

def p_from_counts(counts,n,target=None):
    return p_series(np.asarray(counts,float)/n,n,target)

def p_accept(n,c,p): return float(binom.cdf(c,n,p))
def producer_risk(n,c,aql): return 1-p_accept(n,c,aql)
def consumer_risk(n,c,ltpd): return p_accept(n,c,ltpd)
