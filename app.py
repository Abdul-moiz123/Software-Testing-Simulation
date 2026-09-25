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

def verify(z,expected,tol=.02):
    if expected is None:
        st.info("Compare the software result with your Part 2A handwritten answer.")
        return
    rows=[[k.upper(),expected[k],z[k],abs(expected[k]-z[k])] for k in ("cl","ucl","lcl")]
    df=pd.DataFrame(rows,columns=["Measure","Book Answer","Python Result","Difference"])
    st.dataframe(df.round(4),use_container_width=True)
    if (df["Difference"]<=tol).all(): st.success("✅ VERIFIED")
    else: st.warning("Difference is larger than the rounding tolerance.")

X_DIRECT={
"SC 10-1(a)":(9,26.7,5.3,None,{"cl":26.7,"ucl":28.5,"lcl":24.9}),
"SC 10-1(b)":(17,138.6,15.1,None,{"cl":138.6,"ucl":141.7,"lcl":135.5}),
"SC 10-1(c)":(4,84.2,9.6,None,{"cl":84.2,"ucl":91.2,"lcl":77.2}),
"SC 10-1(d)":(22,8.1,7.4,None,{"cl":8.1,"ucl":9.3,"lcl":6.9}),
"10-12(a)":(12,16.4,None,1.2,None),
"10-12(b)":(12,16.4,7.6,None,None),"10-12(c)":(8,4.1,1.3,None,None),"10-12(d)":(15,141.7,18.6,None,None)}
X_SERIES={
"SC 10-2 — Altoona Tire":(ALTOONA_MEANS,ALTOONA_RANGES,5,{"cl":50.417,"ucl":51.21,"lcl":49.63}),
"10-13 — Wilson Piston":(WILSON_MEANS,WILSON_RANGES,8,None),
"10-14 — Emergency Medical Services":(EMS_MEANS,EMS_RANGES,9,None),
"10-16 — Northern White Metals":(NW_MEANS,NW_RANGES,15,None),
"10-44 — Global Bank":(GLOBAL_MEANS,GLOBAL_RANGES,10,None),
"10-50 — Reliance Storage Media":(RELIANCE_MEANS,RELIANCE_RANGES,24,None)}
R_DIRECT={
"SC 10-3(a)":(9,5.3,{"cl":5.3,"ucl":9.62,"lcl":.98}),"SC 10-3(b)":(17,15.1,{"cl":15.1,"ucl":24.49,"lcl":5.71}),
"SC 10-3(c)":(4,9.6,{"cl":9.6,"ucl":21.91,"lcl":0}),"SC 10-3(d)":(22,7.4,{"cl":7.4,"ucl":11.59,"lcl":3.21}),
"10-17(a)":(3,3.1,None),"10-17(b)":(19,6.9,None),"10-17(c)":(8,18.2,None),"10-17(d)":(24,1.4,None)}
R_SERIES={
"SC 10-4 — Altoona Tire":(ALTOONA_RANGES,5,{"cl":1.367,"ucl":2.89,"lcl":0}),
"10-19 — Wilson Piston":(WILSON_RANGES,8,None),"10-20 — Emergency Medical Services":(EMS_RANGES,9,None),
"10-22 — Northern White Metals":(NW_RANGES,15,None),"10-45 — Global Bank":(GLOBAL_RANGES,10,None),
"10-51 — Reliance Storage Media":(RELIANCE_RANGES,24,None)}
P_DIRECT={"SC 10-5(a)":(144,.10,{"cl":.10,"ucl":.175,"lcl":.025}),"SC 10-5(b)":(60,.9,{"cl":.9,"ucl":1,"lcl":.784}),
"SC 10-5(c)":(125,.36,None),"SC 10-5(d)":(48,.75,None),"10-24(a)":(30,.25,None),"10-24(b)":(65,.15,None),
"10-24(c)":(82,.05,None),"10-24(d)":(97,.42,None),"10-24(e)":(124,.63,None)}
P_SERIES={"SC 10-6 — Meals on Wheels":(MEALS,150,None,None),"10-25 — USA Airlines":(USA,200,None,None),
"10-26 — BioAssist":([x/100 for x in BIO_BAD],500,.015,None),"10-28 — Spacious Skies":([x/240 for x in SPACIOUS_LATE],240,None,None),
"10-40 — R&H Bloch":([x/125 for x in BLOCH_AUDITED],125,None,None),"10-52 — Photomatic":([x/2000 for x in PHOTOMATIC],2000,.001,None)}

method=st.sidebar.selectbox("Select Analysis",["X-Bar Control Chart","R Control Chart","p Control Chart","Acceptance Sampling"])

if method=="X-Bar Control Chart":
    st.header("1. X-Bar Control Chart")
    choices=list(X_DIRECT)+list(X_SERIES)+["10-15 — Track Bicycle Bearings"]
    q=st.selectbox("Select Textbook Numerical",choices)
    if q in X_DIRECT:
        n,m,r,s,e=X_DIRECT[q]; st.write(f"**Given:** n={n}, mean={m}, "+(f"R-bar={r}" if r is not None else f"sigma-x={s}"))
        if st.button("Calculate / Verify",type="primary"):
            z=xbar_limits(n,m,r,s); result(z); verify(z,e)
    elif q=="10-15 — Track Bicycle Bearings":
        st.dataframe(pd.DataFrame(BEARINGS),use_container_width=True)
        if st.button("Calculate / Verify",type="primary"):
            z=xbar_raw(BEARINGS); result(z,z["values"],"Sample Mean"); verify(z,None)
    else:
        m,r,n,e=X_SERIES[q]; st.dataframe(pd.DataFrame({"X-bar":m,"R":r}),use_container_width=True)
        if st.button("Calculate / Verify",type="primary"):
            z=xbar_series(m,r,n); result(z,z["values"],"Sample Mean"); verify(z,e)

elif method=="R Control Chart":
    st.header("2. R Control Chart")
    choices=list(R_DIRECT)+list(R_SERIES)+["10-17(e) — Find UCL","10-21 — Track Bicycle Bearings"]
    q=st.selectbox("Select Textbook Numerical",choices)
    if q in R_DIRECT:
        n,r,e=R_DIRECT[q]; st.write(f"**Given:** n={n}, R-bar={r}")
        if st.button("Calculate / Verify",type="primary"):
            z=r_limits(n,r); result(z); verify(z,e)
    elif q=="10-17(e) — Find UCL":
        st.write("**Given:** R-bar = 6.0 and LCL = 3.0. The exercise asks for UCL.")
        st.info("This special algebraic exercise is shown separately because n is not supplied directly.")
    elif q=="10-21 — Track Bicycle Bearings":
        if st.button("Calculate / Verify",type="primary"):
            z=r_raw(BEARINGS); result(z,z["values"],"Sample Range"); verify(z,None)
    else:
        r,n,e=R_SERIES[q]
        if st.button("Calculate / Verify",type="primary"):
            z=r_series(r,n); result(z,z["values"],"Sample Range"); verify(z,e)

elif method=="p Control Chart":
    st.header("3. p Control Chart")
    q=st.selectbox("Select Textbook Numerical",list(P_DIRECT)+list(P_SERIES))
    if q in P_DIRECT:
        n,p,e=P_DIRECT[q]; st.write(f"**Given:** n={n}, p={p}")
        if st.button("Calculate / Verify",type="primary"):
            z=p_limits(n,p); result(z); verify(z,e)
    else:
        vals,n,target,e=P_SERIES[q]
        st.dataframe(pd.DataFrame({"Sample":range(1,len(vals)+1),"Proportion":vals}),use_container_width=True)
        if st.button("Calculate / Verify",type="primary"):
            z=p_series(vals,n,target); result(z,z["values"],"Proportion"); verify(z,e)

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
        ps=p if isinstance(p,list) else [p]
        rows=[]
        for rate in ps:
            risk=producer_risk(n,c,rate) if kind.startswith("producer") else consumer_risk(n,c,rate)
            rows.append({"Quality level":rate,"Risk":risk,"Risk %":risk*100})
        st.dataframe(pd.DataFrame(rows).round(5),use_container_width=True)
        st.info("For OC-curve exercises, this computes the binomial probability represented by the curve; a graph-read answer may differ slightly because of visual rounding.")

st.divider()
st.caption("Part 2B — Chapter 10 Textbook Numerical Verification")
