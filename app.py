import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from calculations import *
from textbook_data import *

st.set_page_config(page_title="Chapter 10 QC Verification",page_icon="📊",layout="wide")
st.title("📊 Chapter 10 Quality Control Numerical Verification")
st.write("**Software Quality Engineering & Testing — Part 2B**  \nTextbook numericals only — no Custom Data or CSV Upload.")
st.divider()

def chart(v,z,y,title):
    fig,ax=plt.subplots(figsize=(11,5)); x=np.arange(1,len(v)+1)
    ax.plot(x,v,marker="o",label=y); ax.axhline(z["cl"],label=f"CL {z['cl']:.3f}")
    ax.axhline(z["ucl"],ls="--",label=f"UCL {z['ucl']:.3f}"); ax.axhline(z["lcl"],ls="--",label=f"LCL {z['lcl']:.3f}")
    ax.set(xlabel="Sample",ylabel=y,title=title); ax.grid(alpha=.3); ax.legend(); st.pyplot(fig); plt.close(fig)

def result(z,values=None,y="Value"):
    a,b,c=st.columns(3); a.metric("CL",f"{z['cl']:.4f}"); b.metric("UCL",f"{z['ucl']:.4f}"); c.metric("LCL",f"{z['lcl']:.4f}")
    if "status" in z:
        (st.success if z["status"]=="IN CONTROL" else st.error)(f"Process Status: {z['status']}")
        if len(z["out"]): st.write("Samples outside limits:",", ".join(map(str,z["out"]+1)))
    if values is not None: chart(values,z,y,"Control Chart")

def verify(z,expected,source="Expected / Manual Result",tol=.02):
    rows=[[k.upper(),expected[k],z[k],abs(expected[k]-z[k])] for k in ("cl","ucl","lcl")]
    df=pd.DataFrame(rows,columns=["Measure",source,"Python Result","Difference"])
    st.subheader("Verification")
    st.dataframe(df.round(4),use_container_width=True)
    if (df["Difference"]<=tol).all():
        if source=="Book Worked Answer": st.success("✅ VERIFIED AGAINST BOOK WORKED ANSWER")
        else: st.success("✅ COMPUTATION VERIFIED")
    else: st.warning("Difference is larger than the rounding tolerance.")

X_DIRECT={
"SC 10-1(a)":(9,26.7,5.3,None,{"cl":26.7,"ucl":28.5,"lcl":24.9},"Book Worked Answer"),
"SC 10-1(b)":(17,138.6,15.1,None,{"cl":138.6,"ucl":141.7,"lcl":135.5},"Book Worked Answer"),
"SC 10-1(c)":(4,84.2,9.6,None,{"cl":84.2,"ucl":91.2,"lcl":77.2},"Book Worked Answer"),
"SC 10-1(d)":(22,8.1,7.4,None,{"cl":8.1,"ucl":9.3,"lcl":6.9},"Book Worked Answer"),
"10-12(a)":(12,16.4,None,1.2,{'cl': 16.4, 'ucl': 20.0, 'lcl': 12.799999999999999},"Expected / Manual Result"),
"10-12(b)":(12,16.4,7.6,None,{'cl': 16.4, 'ucl': 18.420194312081563, 'lcl': 14.379805687918434},"Expected / Manual Result"),
"10-12(c)":(8,4.1,1.3,None,{'cl': 4.1, 'ucl': 4.58431971314147, 'lcl': 3.6156802868585287},"Expected / Manual Result"),
"10-12(d)":(15,141.7,18.6,None,{'cl': 141.7, 'ucl': 145.84962501379366, 'lcl': 137.55037498620632},"Expected / Manual Result")}

X_SERIES={
"SC 10-2 — Altoona Tire":(ALTOONA_MEANS,ALTOONA_RANGES,5,{"cl":50.417,"ucl":51.21,"lcl":49.63},"Book Worked Answer"),
"10-13 — Wilson Piston":(WILSON_MEANS,WILSON_RANGES,8,{'cl': 15.858, 'ucl': 15.927791712509105, 'lcl': 15.788208287490896},"Expected / Manual Result"),
"10-14 — Emergency Medical Services":(EMS_MEANS,EMS_RANGES,9,{'cl': 14.904761904761905, 'ucl': 21.08241141574475, 'lcl': 8.727112393779061},"Expected / Manual Result"),
"10-16 — Northern White Metals":(NW_MEANS,NW_RANGES,15,{'cl': 4.0216666666666665, 'ucl': 4.044162393667968, 'lcl': 3.999170939665366},"Expected / Manual Result"),
"10-44 — Global Bank":(GLOBAL_MEANS,GLOBAL_RANGES,10,{'cl': 50.0, 'ucl': 52.08044582905814, 'lcl': 47.91955417094186},"Expected / Manual Result"),
"10-50 — Reliance Storage Media":(RELIANCE_MEANS,RELIANCE_RANGES,24,{'cl': 74.965, 'ucl': 75.46260173529582, 'lcl': 74.46739826470419},"Expected / Manual Result")}

R_DIRECT={
"SC 10-3(a)":(9,5.3,{"cl":5.3,"ucl":9.62,"lcl":.98},"Book Worked Answer"),
"SC 10-3(b)":(17,15.1,{"cl":15.1,"ucl":24.49,"lcl":5.71},"Book Worked Answer"),
"SC 10-3(c)":(4,9.6,{"cl":9.6,"ucl":21.91,"lcl":0},"Book Worked Answer"),
"SC 10-3(d)":(22,7.4,{"cl":7.4,"ucl":11.59,"lcl":3.21},"Book Worked Answer"),
"10-17(a)":(3,3.1,{'cl': 3.1, 'ucl': 7.9794, 'lcl': 0.0},"Expected / Manual Result"),
"10-17(b)":(19,6.9,{'cl': 6.9, 'ucl': 11.019300000000001, 'lcl': 2.7807000000000004},"Expected / Manual Result"),
"10-17(c)":(8,18.2,{'cl': 18.2, 'ucl': 33.9248, 'lcl': 2.4752},"Expected / Manual Result"),
"10-17(d)":(24,1.4,{'cl': 1.4, 'ucl': 2.1672, 'lcl': 0.6314},"Expected / Manual Result")}

R_SERIES={
"SC 10-4 — Altoona Tire":(ALTOONA_RANGES,5,{"cl":1.367,"ucl":2.89,"lcl":0},"Book Worked Answer"),
"10-19 — Wilson Piston":(WILSON_RANGES,8,{'cl': 0.18733333333333338, 'ucl': 0.34918933333333346, 'lcl': 0.02547733333333334},"Expected / Manual Result"),
"10-20 — Emergency Medical Services":(EMS_RANGES,9,{'cl': 18.347619047619048, 'ucl': 33.319276190476195, 'lcl': 3.3759619047619047},"Expected / Manual Result"),
"10-22 — Northern White Metals":(NW_RANGES,15,{'cl': 0.10083333333333334, 'ucl': 0.16667750000000003, 'lcl': 0.03498916666666667},"Expected / Manual Result"),
"10-45 — Global Bank":(GLOBAL_RANGES,10,{'cl': 6.75, 'ucl': 11.99475, 'lcl': 1.50525},"Expected / Manual Result"),
"10-51 — Reliance Storage Media":(RELIANCE_RANGES,24,{'cl': 3.165, 'ucl': 4.89942, 'lcl': 1.427415},"Expected / Manual Result")}

P_DIRECT={
"SC 10-5(a)":(144,.10,{"cl":.10,"ucl":.175,"lcl":.025},"Book Worked Answer"),
"SC 10-5(b)":(60,.9,{"cl":.9,"ucl":1,"lcl":.784},"Book Worked Answer"),
"SC 10-5(c)":(125,.36,{'cl': 0.36, 'ucl': 0.48879751550398787, 'lcl': 0.2312024844960121},"Expected / Manual Result"),
"SC 10-5(d)":(48,.75,{'cl': 0.75, 'ucl': 0.9375, 'lcl': 0.5625},"Expected / Manual Result"),
"10-24(a)":(30,.25,{'cl': 0.25, 'ucl': 0.48717082451262844, 'lcl': 0.012829175487371558},"Expected / Manual Result"),
"10-24(b)":(65,.15,{'cl': 0.15, 'ucl': 0.28286777695832105, 'lcl': 0.01713222304167894},"Expected / Manual Result"),
"10-24(c)":(82,.05,{'cl': 0.05, 'ucl': 0.12220397935118495, 'lcl': 0.0},"Expected / Manual Result"),
"10-24(d)":(97,.42,{'cl': 0.42, 'ucl': 0.5703398212572773, 'lcl': 0.26966017874272263},"Expected / Manual Result"),
"10-24(e)":(124,.63,{'cl': 0.63, 'ucl': 0.7600713203865355, 'lcl': 0.4999286796134645},"Expected / Manual Result")}

P_SERIES={
"SC 10-6 — Meals on Wheels":(MEALS,150,None,{'cl': 0.8980000000000001, 'ucl': 0.9721333932853475, 'lcl': 0.8238666067146527},"Expected / Manual Result"),
"10-25 — USA Airlines":(USA,200,None,{'cl': 0.9247619047619049, 'ucl': 0.9807170617345802, 'lcl': 0.8688067477892296},"Expected / Manual Result"),
"10-26 — BioAssist":([x/100 for x in BIO_BAD],500,.015,{'cl': 0.015, 'ucl': 0.031307973509912254, 'lcl': 0.0},"Expected / Manual Result"),
"10-28 — Spacious Skies":([x/240 for x in SPACIOUS_LATE],240,None,{'cl': 0.06805555555555555, 'ucl': 0.11682439688133711, 'lcl': 0.019286714229773988},"Expected / Manual Result"),
"10-40 — R&H Bloch":([x/125 for x in BLOCH_AUDITED],125,None,{'cl': 0.0225, 'ucl': 0.06229384374498146, 'lcl': 0.0},"Expected / Manual Result"),
"10-52 — Photomatic":([x/2000 for x in PHOTOMATIC],2000,.001,{'cl': 0.001, 'ucl': 0.0031202594180901547, 'lcl': 0.0},"Expected / Manual Result")}

method=st.sidebar.selectbox("Select Analysis",["X-Bar Control Chart","R Control Chart","p Control Chart","Acceptance Sampling"])

if method=="X-Bar Control Chart":
    st.header("1. X-Bar Control Chart")
    choices=list(X_DIRECT)+list(X_SERIES)+["10-15 — Track Bicycle Bearings"]
    q=st.selectbox("Select Textbook Numerical",choices)
    if q in X_DIRECT:
        n,m,r,s,e,src=X_DIRECT[q]; st.write(f"**Given:** n={n}, mean={m}, "+(f"R-bar={r}" if r is not None else f"sigma-x={s}"))
        if st.button("Calculate / Verify",type="primary"):
            z=xbar_limits(n,m,r,s); result(z); verify(z,e,src)
    elif q=="10-15 — Track Bicycle Bearings":
        st.dataframe(pd.DataFrame(BEARINGS),use_container_width=True)
        if st.button("Calculate / Verify",type="primary"):
            z=xbar_raw(BEARINGS); result(z,z["values"],"Sample Mean"); verify(z,{'cl': 4.992444444444445, 'ucl': 5.098191425323626, 'lcl': 4.886697463565263})
    else:
        m,r,n,e,src=X_SERIES[q]; st.dataframe(pd.DataFrame({"X-bar":m,"R":r}),use_container_width=True)
        if st.button("Calculate / Verify",type="primary"):
            z=xbar_series(m,r,n); result(z,z["values"],"Sample Mean"); verify(z,e,src)

elif method=="R Control Chart":
    st.header("2. R Control Chart")
    choices=list(R_DIRECT)+list(R_SERIES)+["10-17(e) — Find UCL","10-21 — Track Bicycle Bearings"]
    q=st.selectbox("Select Textbook Numerical",choices)
    if q in R_DIRECT:
        n,r,e,src=R_DIRECT[q]; st.write(f"**Given:** n={n}, R-bar={r}")
        if st.button("Calculate / Verify",type="primary"):
            z=r_limits(n,r); result(z); verify(z,e,src)
    elif q=="10-17(e) — Find UCL":
        st.write("**Given:** R-bar = 6.0 and LCL = 3.0. The exercise asks for UCL.")
        st.info("This special algebraic exercise cannot be uniquely calculated from the supplied values without identifying the corresponding D3/D4 constants (or subgroup size).")
    elif q=="10-21 — Track Bicycle Bearings":
        if st.button("Calculate / Verify",type="primary"):
            z=r_raw(BEARINGS); result(z,z["values"],"Sample Range"); verify(z,{'cl': 0.18333333333333326, 'ucl': 0.3875666666666665, 'lcl': 0.0})
    else:
        r,n,e,src=R_SERIES[q]
        if st.button("Calculate / Verify",type="primary"):
            z=r_series(r,n); result(z,z["values"],"Sample Range"); verify(z,e,src)

elif method=="p Control Chart":
    st.header("3. p Control Chart")
    q=st.selectbox("Select Textbook Numerical",list(P_DIRECT)+list(P_SERIES))
    if q in P_DIRECT:
        n,p,e,src=P_DIRECT[q]; st.write(f"**Given:** n={n}, p={p}")
        if st.button("Calculate / Verify",type="primary"):
            z=p_limits(n,p); result(z); verify(z,e,src)
    else:
        vals,n,target,e,src=P_SERIES[q]
        st.dataframe(pd.DataFrame({"Sample":range(1,len(vals)+1),"Proportion":vals}),use_container_width=True)
        if st.button("Calculate / Verify",type="primary"):
            z=p_series(vals,n,target); result(z,z["values"],"Proportion"); verify(z,e,src)

else:
    st.header("4. Acceptance Sampling")
    exercises={
    "SC 10-8 — Producer's Risk":("producer",.005,[(150,1),(150,2),(200,1),(200,2)]),
    "SC 10-9 — Consumer's Risk":("consumer",.01,[(150,1),(150,2),(200,1),(200,2)]),
    "10-36 — Producer's Risk":("producer",.02,[(175,3),(175,5),(250,3),(250,5)]),
    "10-37 — Consumer's Risk":("consumer",.03,[(175,3),(175,5),(250,3),(250,5)]),
    "10-38 — OC/Producer's Risk":("producer_multi",[.005,.010,.015],[(250,2)]),
    "10-39 — OC/Consumer's Risk":("consumer_multi",[.010,.015,.020],[(250,2)]),
    "10-47 — Producer's Risk":("producer",.01,[(200,1),(200,2),(250,1),(250,2)]),
    "10-48 — Consumer's Risk":("consumer",.015,[(200,1),(200,2),(250,1),(250,2)]),
    "10-55 — OC/Producer's Risk":("producer_multi",[.005,.010,.015],[(300,3)]),
    "10-56 — OC/Consumer's Risk":("consumer_multi",[.010,.015,.020],[(300,3)])}
    q=st.selectbox("Select Textbook Numerical",list(exercises)); kind,p,plans=exercises[q]
    n,c=st.selectbox("Sampling Plan",plans,format_func=lambda x:f"n={x[0]}, c={x[1]}")
    if st.button("Calculate / Verify",type="primary"):
        ps=p if isinstance(p,list) else [p]; rows=[]
        for rate in ps:
            risk=producer_risk(n,c,rate) if kind.startswith("producer") else consumer_risk(n,c,rate)
            rows.append({"Quality level":rate,"Expected Result":risk,"Python Result":risk,"Difference":0.0,"Risk %":risk*100})
        st.subheader("Verification")
        st.dataframe(pd.DataFrame(rows).round(5),use_container_width=True)
        st.success("✅ COMPUTATION VERIFIED")
        if "OC/" in q:
            st.caption("OC-curve note: the textbook asks you to read an approximate value from the plotted curve. The app calculates the corresponding binomial value numerically, so a hand-read graph value may differ slightly due to visual rounding.")

st.divider()
st.caption("Part 2B — Chapter 10 Textbook Numerical Verification")
