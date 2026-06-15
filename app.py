import streamlit as st
import pandas as pd

# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------

st.set_page_config(
    page_title="Airline Retention Intelligence",
    page_icon="✈️",
    layout="wide"
)

# --------------------------------------------------
# LOAD DATA
# --------------------------------------------------

df = pd.read_csv("model_df.csv")

# --------------------------------------------------
# TITLE
# --------------------------------------------------

st.title("✈️ Airline Retention Intelligence Platform")
st.markdown(
    "Identify high-risk customers, understand customer value, and generate retention actions."
)

st.divider()

# --------------------------------------------------
# KPI CARDS
# --------------------------------------------------

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Total Customers",
        f"{len(df):,}"
    )

with col2:
    st.metric(
        "Average CLV",
        f"${df['CLV'].mean():,.0f}"
    )

with col3:
    st.metric(
        "High Risk Customers",
        len(df[df['Churn_Probability'] >= 0.70])
    )

with col4:
    st.metric(
        "Highest Value Segment",
        df.groupby('Segment')['CLV'].mean().idxmax()
    )

st.divider()

# --------------------------------------------------
# CUSTOMER LOOKUP
# --------------------------------------------------

st.header("🔍 Customer Lookup")

customer_id = st.selectbox(
    "Select Customer ID",
    sorted(df['Loyalty Number'].unique())
)

customer = df[df['Loyalty Number'] == customer_id].iloc[0]

c1, c2, c3 = st.columns(3)

with c1:
    st.metric(
        "Customer Lifetime Value",
        f"${customer['CLV']:,.0f}"
    )

with c2:
    st.metric(
        "Segment",
        customer['Segment']
    )

with c3:
    st.metric(
        "Churn Probability",
        f"{customer['Churn_Probability']:.1%}"
    )

# --------------------------------------------------
# ACTION RECOMMENDATIONS
# --------------------------------------------------

def get_action(segment):

    actions = {

        "Silent VIPs":
        "🎁 Premium retention package, exclusive rewards, concierge support.",

        "Road Warriors":
        "✈️ Maintain engagement through loyalty benefits and tier progression.",

        "Frequent Travelers":
        "📈 Encourage upgrades, premium routes and status acceleration.",

        "Reward Seekers":
        "🎯 Offer bonus redemption campaigns and personalized point offers.",

        "Dormant Members":
        "🚨 Immediate win-back campaign with bonus miles and discounts."
    }

    return actions.get(
        segment,
        "Monitor customer behavior."
    )

st.subheader("Recommended Action")

st.success(
    get_action(customer['Segment'])
)

st.divider()

# --------------------------------------------------
# CAMPAIGN GENERATOR
# --------------------------------------------------

st.header("📢 Retention Campaign Generator")

segment = st.selectbox(
    "Choose Segment",
    sorted(df['Segment'].unique())
)

campaigns = {

    "Silent VIPs":
    {
        "Campaign": "Premium Retention Program",
        "Offer": "Complimentary lounge access + bonus rewards",
        "Timing": "Immediately",
        "Goal": "Protect high-value customers"
    },

    "Road Warriors":
    {
        "Campaign": "Loyalty Appreciation Campaign",
        "Offer": "Bonus miles on frequent routes",
        "Timing": "Quarterly",
        "Goal": "Maintain engagement"
    },

    "Frequent Travelers":
    {
        "Campaign": "Tier Upgrade Campaign",
        "Offer": "Double status points",
        "Timing": "Monthly",
        "Goal": "Increase loyalty"
    },

    "Reward Seekers":
    {
        "Campaign": "Redemption Booster",
        "Offer": "20% extra value on point redemption",
        "Timing": "Before seasonal peaks",
        "Goal": "Increase reward engagement"
    },

    "Dormant Members":
    {
        "Campaign": "Win-Back Campaign",
        "Offer": "Double miles on next booking",
        "Timing": "Immediately",
        "Goal": "Reduce churn risk"
    }
}

campaign = campaigns[segment]

st.info(f"""
### Campaign Name
{campaign['Campaign']}

### Offer
{campaign['Offer']}

### Recommended Timing
{campaign['Timing']}

### Objective
{campaign['Goal']}
""")

st.divider()

# --------------------------------------------------
# HIGH-RISK CUSTOMERS
# --------------------------------------------------

st.header("🚨 High-Risk Customers")

high_risk = df[
    df['Churn_Probability'] >= 0.70
]

display_cols = [
    'Loyalty Number',
    'Segment',
    'CLV',
    'Churn_Probability'
]

available_cols = [
    col for col in display_cols
    if col in high_risk.columns
]

st.dataframe(
    high_risk[available_cols]
    .sort_values(
        by='Churn_Probability',
        ascending=False
    ),
    use_container_width=True
)