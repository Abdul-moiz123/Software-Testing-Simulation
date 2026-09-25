import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from calculations import calculate_xbar_from_summary,calculate_xbar_from_sample_summaries,calculate_r_from_summary,calculate_r_from_ranges,calculate_p_chart,producer_risk,consumer_risk

st.set_page_config(page_title="Chapter 10 Quality Control Verification",page_icon="📊",layout="wide")
st.title("📊 Chapter 10 Quality Control Numerical Verification")
st.write("**Software Quality Engineering & Testing — Part 2B**\n\nThis application verifies textbook numericals from Chapter 10 of *Statistics for Management, 8th Edition*.")
st.divider()

BANK=[[63,55,56,53,61,64],[60,63,60,65,61,66],[57,60,61,65,66,62],[58,64,60,61,57,65],[79,68,65,61,74,71],[55,66,62,63,56,52],[57,61,58,64,55,63],[58,51,61,57,66,59],[65,66,62,68,61,67],[73,66,61,70,72,78],[57,63,56,64,62,59],[66,63,65,59,70,61],[63,53,69,60,61,58],[68,67,59,58,65,59],[70,62,66,80,71,76],[65,59,60,61,62,65],[63,69,58,56,66,61],[61,56,62,59,57,55],[65,57,69,62,58,72],[70,60,67,79,75,68]]
P=[.89,.91,.93,.95,.94,.96,.92,.91,.93,.90,.88,.94,.97,.94,.95,.92,.93,.92,.91,.93,.89]

def verify(book,result,tol=.02):
    if book is None:
        st.info("Compare this software-computed result with your Part 2A handwritten solution.")
        return
    rows=[]
    for k,n in [("cl","Center Line"),("ucl","UCL"),("lcl","LCL")]:
        rows.append([n,book[k],result[k],abs(book[k]-result[k])])
    df=pd.DataFrame(rows,columns=["Measure","Book Answer","Python Result","Difference"])
    st.dataframe(df.round(4),use_container_width=True)
    if (df["Difference"] <= tol).all():
        st.success("✅ VERIFIED")
    else:
        st.warning("Check textbook rounding/constants.")

def chart(values,cl,ucl,lcl,y,title):
    fig,ax=plt.subplots(figsize=(11,5)); x=np.arange(1,len(values)+1)
    ax.plot(x,values,marker="o",label=y); ax.axhline(cl,label=f"CL ({cl:.3f})")
    ax.axhline(ucl,linestyle="--",label=f"UCL ({ucl:.3f})"); ax.axhline(lcl,linestyle="--",label=f"LCL ({lcl:.3f})")
    ax.set(xlabel="Sample Number",ylabel=y,title=title); ax.grid(True,alpha=.3); ax.legend(); st.pyplot(fig); plt.close(fig)

method=st.sidebar.selectbox("Select Analysis",["X-Bar Control Chart","R Control Chart","p Control Chart","Acceptance Sampling"])

if method=="X-Bar Control Chart":
    st.header("1. X-Bar Control Chart")
    q=st.selectbox("Select Textbook Numerical",["SC 10-1(a) — Control Limit Calculation","TransCarolina Bank — Worked Example"])
    if q.startswith("SC"):
        st.write("**Given:** n = 9, grand mean = 26.7, average range = 5.3")
        if st.button("Verify X-Bar Numerical",type="primary"):
            z=calculate_xbar_from_summary(9,26.7,5.3)
            a,b,c=st.columns(3); a.metric("CL",f"{z['cl']:.3f}"); b.metric("UCL",f"{z['ucl']:.3f}"); c.metric("LCL",f"{z['lcl']:.3f}")
            verify({"cl":26.7,"ucl":28.5,"lcl":24.9},z)
    else:
        d=np.asarray(BANK,float); m=d.mean(1); r=d.max(1)-d.min(1)
        st.dataframe(pd.DataFrame(d,index=np.arange(1,21)),use_container_width=True)
        if st.button("Run X-Bar Analysis",type="primary"):
            z=calculate_xbar_from_sample_summaries(m,r,6)
            st.write(f"Grand Mean **{z['grand_mean']:.3f}** | R-bar **{z['average_range']:.3f}** | Status **{z['status']}**")
            chart(z["sample_means"],z["cl"],z["ucl"],z["lcl"],"Sample Mean","X-Bar Control Chart"); verify(None,z)

elif method=="R Control Chart":
    st.header("2. R Control Chart")
    q=st.selectbox("Select Textbook Numerical",["SC 10-3(a) — R-Chart Control Limits","TransCarolina Bank — Worked Example"])
    if q.startswith("SC"):
        st.write("**Given:** n = 17, R-bar = 15.1")
        if st.button("Verify R-Chart Numerical",type="primary"):
            z=calculate_r_from_summary(17,15.1)
            a,b,c=st.columns(3); a.metric("CL",f"{z['cl']:.3f}"); b.metric("UCL",f"{z['ucl']:.3f}"); c.metric("LCL",f"{z['lcl']:.3f}")
            verify({"cl":15.1,"ucl":24.49,"lcl":5.71},z)
    else:
        d=np.asarray(BANK,float); r=d.max(1)-d.min(1)
        if st.button("Run R-Chart Analysis",type="primary"):
            z=calculate_r_from_ranges(r,6)
            st.write(f"R-bar **{z['average_range']:.3f}** | Status **{z['status']}**")
            chart(z["ranges"],z["cl"],z["ucl"],z["lcl"],"Sample Range","R Control Chart"); verify(None,z)

elif method=="p Control Chart":
    st.header("3. p Control Chart")
    st.selectbox("Select Textbook Numerical",["Exercise 10-25 — USA Airlines Luggage Delivery"])
    st.dataframe(pd.DataFrame({"Sample":range(1,22),"Proportion":P}),use_container_width=True)
    if st.button("Verify p-Chart Numerical",type="primary"):
        z=calculate_p_chart(P,200)
        a,b,c=st.columns(3); a.metric("CL",f"{z['cl']:.4f}"); b.metric("UCL",f"{z['ucl']:.4f}"); c.metric("LCL",f"{z['lcl']:.4f}")
        st.write(f"Status: **{z['status']}**"); chart(z["proportions"],z["cl"],z["ucl"],z["lcl"],"Proportion","p Control Chart"); verify(None,z)

else:
    st.header("4. Acceptance Sampling")
    q=st.selectbox("Select Textbook Numerical",["SC 10-8 — Producer's Risk","SC 10-9 — Consumer's Risk"])
    plan=st.selectbox("Select Sampling Plan",["n=100, c=1","n=200, c=2"])
    n,c=(100,1) if plan.startswith("n=100") else (200,2)
    if q.startswith("SC 10-8"):
        st.write("**Lot size:** 2,000 | **AQL:** 0.5%")
        if st.button("Calculate Producer's Risk",type="primary"):
            st.metric("Producer's Risk (alpha)",f"{producer_risk(n,c,.005):.4%}")
    else:
        st.write("**LTPD:** 1%")
        if st.button("Calculate Consumer's Risk",type="primary"):
            st.metric("Consumer's Risk (beta)",f"{consumer_risk(n,c,.01):.4%}")

st.divider()
st.caption("Software Quality Engineering & Testing | Part 2B — Chapter 10 Textbook Numerical Verification")
