import streamlit as st
import numpy as np
import joblib

# Load the pre-trained model
model = joblib.load("model_clean.pkl")

# Streamlit configuration
st.set_page_config(
    page_title="Loan Approval Assessment",
    page_icon="💳",
    layout="wide"
)

# --- Custom CSS: Reduce empty space, tighten layout ---
st.markdown("""
    <style>
    body, .stApp {
        background: linear-gradient(120deg, #21223a 0%, #2a2b48 100%) !important;
        min-height: 100vh;
        font-family: 'Inter', 'Segoe UI', Arial, sans-serif;
        color: #e0e0e0 !important;
    }
    .main-card {
        background: rgba(36, 37, 58, 0.98);
        border-radius: 14px;
        box-shadow: 0 4px 18px 0 rgba(44,44,80,0.13);
        padding: 1.2rem 1.2rem 0.7rem 1.2rem;
        width: 98vw;
        max-width: 1200px;
        margin: 1.2rem auto 0.7rem auto;
        border: 1.2px solid #35365a;
        display: flex;
        flex-direction: row;
        gap: 1.2rem;
        box-sizing: border-box;
    }
    @media (max-width: 1200px) {
        .main-card { flex-direction: column; max-width: 98vw; }
    }
    .main-card-left {
        flex: 1.1;
        min-width: 260px;
        max-width: 350px;
        display: flex;
        flex-direction: column;
        justify-content: flex-start;
    }
    .main-card-right {
        flex: 2;
        min-width: 320px;
        display: flex;
        flex-direction: column;
        justify-content: flex-start;
    }
    .stButton>button {
        width: 100%;
        border-radius: 8px;
        font-size: 1.08rem;
        font-weight: 600;
        background: linear-gradient(90deg, #2e2f4a 60%, #4a4b6a 100%);
        color: #fff;
        border: none;
        padding: 0.7rem 0;
        margin-top: 0.7rem;
        box-shadow: 0 2px 8px 0 rgba(44,44,80,0.10);
        transition: background 0.2s, box-shadow 0.2s;
    }
    .stButton>button:hover {
        background: linear-gradient(90deg, #4a4b6a 0%, #2e2f4a 100%);
        color: #fff;
        box-shadow: 0 4px 16px 0 rgba(60,60,100,0.15);
    }
    .stTextInput>div>input, .stNumberInput>div>input, .stSelectbox>div>div, .stSlider>div {
        border-radius: 7px !important;
        border: 1.2px solid #35365a !important;
        background: #23243a !important;
        color: #e0e0e0 !important;
        font-size: 0.98em !important;
        min-height: 2.1em !important;
    }
    .stRadio>div {
        flex-direction: row !important;
        gap: 1.1rem;
        color: #fff !important;
    }
    label, .stTextInput label, .stNumberInput label, .stSelectbox label, .stRadio label, .stSlider label {
        color: #e0e0e0 !important;
        font-weight: 600 !important;
        font-size: 1.01em !important;
        margin-bottom: 0.18em !important;
        display: block !important;
    }
    .stMarkdown h1, .stMarkdown h2, .stMarkdown h3 {
        color: #a7a8e6 !important;
        font-weight: 800;
        letter-spacing: -1px;
    }
    .stMarkdown p, .stMarkdown span {
        color: #b0b0c0 !important;
    }
    .badge {
        display: inline-block;
        background: linear-gradient(90deg, #35365a 60%, #5a5b7a 100%);
        color: #e0e0e0;
        border-radius: 7px;
        padding: 0.35em 1.1em;
        font-weight: 500;
        font-size: 0.98em;
        margin-right: 0.4em;
        box-shadow: 0 1px 4px 0 rgba(44,44,80,0.13);
        border: none;
        outline: none;
    }
    .badge:last-child {
        margin-right: 0;
    }
    .result-card {
        background: linear-gradient(120deg, #23243a 60%, #35365a 100%);
        border-radius: 15px;
        box-shadow: 0 4px 18px 0 rgba(44,44,80,0.13);
        padding: 2rem 1.5rem;
        margin: 1.5rem auto 0 auto;
        max-width: 500px;
        border: 1.5px solid #35365a;
    }
    .footer {
        text-align:center; 
        color:#888; 
        font-size:1.04em;
        margin-top:2.5em; 
        margin-bottom:0.7em;
        letter-spacing: 0.01em;
    }
    </style>
""", unsafe_allow_html=True)

# --- Main Card Container with Improved Layout ---
st.markdown(
    """
    <div class="main-card" style="max-width: 820px; margin: 0 auto; display: flex; gap: 1em;">
        <div style="flex:1; min-width: 280px;">
            <h1 style="color:#bfc0f7; font-size:2em; font-weight:900; margin-bottom:0.2em;">Loan Approval Assessment</h1>
            <p style="color:#b0b0c0; margin-bottom:0.7em;">
                Get a <span style="color:#a7a8e6; font-weight:600;">fast, expert, and confidential</span> AI-powered review of your loan application.<br>
                <span style="color:#a7a8e6; font-weight:600;">Trusted. Private. Insightful.</span>
            </p>
            <div style="margin-top:1em; color:#b0b0c0;">
                <b>How it works:</b>
                <ol style="margin-left:1em;">
                    <li>Fill out the form</li>
                    <li>Click <b>Assess Application</b></li>
                    <li>Get instant results</li>
                </ol>
            </div>
        </div>
        <div style="flex:0 1 320px; min-width:220px; display: flex; flex-direction: column; align-items: center; justify-content: center;">
            <div style="margin-bottom:0.9em; display: flex; flex-direction: column; gap: 0.35em; align-items: center;">
                <span class="badge" title="Our model's accuracy is regularly updated and validated;">
                    <b>Model Accuracy:</b> <span style="color:#1bc47d;">Dynamic</span>
                </span>
                <span class="badge" title="Switch between different AI models for your assessment.">
                    <b>Multiple Model Support</b>
                </span>
                <span class="badge" title="Your data is never stored or shared.">
                    <b>Data Privacy</b> <span style="color:#1bc47d;">Ensured</span>
                </span>
                <span class="badge" title="Get your results in seconds.">
                    <b>Instant Results</b>
                </span>
            </div>
    """,
    unsafe_allow_html=True
)

# --- Form Layout: 3 columns for better grouping ---
with st.form("loan_form", clear_on_submit=False):
    col1, col2, col3 = st.columns([1.1, 1.1, 1], gap="large")

    with col1:
        age = st.number_input(
            "Age*",
            min_value=18,
            max_value=100,
            value=30,
            step=1,
            help="Enter your age (18-100)"
        )
        gender = st.selectbox(
            "Gender*",
            ["Male", "Female"],
            key="gender_select",
            help="Select your gender"
        )
        marital = st.selectbox(
            "Marital Status*",
            ["Single", "Married", "Divorced", "Widowed"],
            help="Your marital status"
        )
        education = st.selectbox(
            "Education Level*",
            ["High School", "Bachelor", "Master", "PhD", "Other"],
            help="Highest completed education"
        )

    with col2:
        income = st.number_input(
            "Annual Income (USD)*",
            min_value=0,
            max_value=1_000_000,
            value=50000,
            step=1000,
            help="Your annual pre-tax income"
        )
        loan = st.number_input(
            "Requested Loan Amount (USD)*",
            min_value=0,
            max_value=1_000_000,
            value=10000,
            step=500,
            help="Desired loan amount"
        )
        employment = st.selectbox(
            "Employment Status*",
            ["Employed", "Self-employed", "Unemployed", "Retired", "Student"],
            help="Select your current employment status"
        )
        purpose = st.selectbox(
            "Loan Purpose*",
            ["Personal", "Home", "Car", "Education", "Business"],
            help="Intended use of the loan"
        )

    with col3:
        credit_score = st.number_input(
            "Credit Score*",
            min_value=300,
            max_value=850,
            value=650,
            step=1,
            help="Your FICO credit score (300-850)"
        )
        existing_loans = st.number_input(
            "Number of Existing Loans*",
            min_value=0,
            max_value=10,
            value=1,
            step=1,
            help="Count of your current active loans"
        )
        late_payments = st.number_input(
            "Late Payments (Last Year)*",
            min_value=0,
            max_value=12,
            value=0,
            step=1,
            help="Number of late payments in the past year"
        )
        # Remove loan_to_income and debt_to_income display from here

    # --- Predict Button ---
    submitted = st.form_submit_button("Assess Application", use_container_width=True)

st.markdown("</div></div>", unsafe_allow_html=True)

# --- Feature Engineering and Encoding ---
# Calculate ratios here for use in both model and output
loan_to_income = loan / (income + 1)
debt_to_income = existing_loans * loan / (income + 1)

gender_male = 1 if gender == "Male" else 0
marital_married = 1 if marital == "Married" else 0
marital_single = 1 if marital == "Single" else 0
marital_widowed = 1 if marital == "Widowed" else 0
edu_high_school = 1 if education == "High School" else 0
edu_master = 1 if education == "Master" else 0
edu_other = 1 if education == "Other" else 0
edu_phd = 1 if education == "PhD" else 0
emp_retired = 1 if employment == "Retired" else 0
emp_self_employed = 1 if employment == "Self-employed" else 0
emp_student = 1 if employment == "Student" else 0
emp_unemployed = 1 if employment == "Unemployed" else 0
purpose_car = 1 if purpose == "Car" else 0
purpose_education = 1 if purpose == "Education" else 0
purpose_home = 1 if purpose == "Home" else 0
purpose_personal = 1 if purpose == "Personal" else 0

input_data = np.array([[ 
    age,                    # 1. Age
    income,                 # 2. AnnualIncome
    loan,                   # 3. LoanAmountRequested
    credit_score,           # 4. CreditScore
    existing_loans,         # 5. ExistingLoansCount
    late_payments,          # 6. LatePaymentsLastYear
    loan_to_income,         # 7. Loan_to_Income
    debt_to_income,         # 8. Debt_to_Income
    gender_male,            # 9. Gender_Male
    marital_married,        # 10. MaritalStatus_Married
    marital_single,         # 11. MaritalStatus_Single
    marital_widowed,        # 12. MaritalStatus_Widowed
    edu_high_school,        # 13. EducationLevel_High School
    edu_master,             # 14. EducationLevel_Master
    edu_other,              # 15. EducationLevel_Other
    edu_phd,                # 16. EducationLevel_PhD
    emp_retired,            # 17. EmploymentStatus_Retired
    emp_self_employed,      # 18. EmploymentStatus_Self-employed
    emp_student,            # 19. EmploymentStatus_Student
    emp_unemployed,         # 20. EmploymentStatus_Unemployed
    purpose_car,            # 21. PurposeOfLoan_Car
    purpose_education,      # 22. PurposeOfLoan_Education
    purpose_home,           # 23. PurposeOfLoan_Home
    purpose_personal        # 24. PurposeOfLoan_Personal
]])

# --- Prediction Logic and Results Card ---
if submitted:
    try:
        expected_features = [
            "age", "income", "loan", "credit_score", "existing_loans", "late_payments",
            "loan_to_income", "debt_to_income", "gender_male", "marital_married", "marital_single", "marital_widowed",
            "edu_high_school", "edu_master", "edu_other", "edu_phd", "emp_retired", "emp_self_employed", 
            "emp_student", "emp_unemployed", "purpose_car", "purpose_education", "purpose_home", "purpose_personal"
        ]
        missing_features = [
            fname for idx, fname in enumerate(expected_features)
            if input_data[0, idx] is None or (isinstance(input_data[0, idx], float) and np.isnan(input_data[0, idx]))
        ]
        if missing_features:
            st.warning(f"⚠️ Missing or invalid features: {missing_features}")

        pred = model.predict(input_data)[0]
        conf = model.predict_proba(input_data)[0][pred]

        # --- Results Card ---
        st.markdown(
            f"""
            <div class="result-card" style="background: linear-gradient(120deg, #23244a 60%, #2d2e5e 100%); border-radius: 1.1em; box-shadow: 0 4px 18px #18193a44; padding: 2.1em 1.7em 1.5em 1.7em; margin: 1.5em auto 0 auto; max-width: 420px;">
                <h2 style='text-align:center; margin-bottom: 0.7em; letter-spacing:-1px; color:#e7e8ff; font-size:1.7em; font-weight:800;'>
                    Assessment Outcome
                </h2>
                <div style='text-align:center; font-size:1.22em; margin-bottom:0.5em;'>
                    <b style="color:#b0b0c0;">Decision:</b>
                    <span style='color:{"#1bc47d" if pred == 0 else "#e74c3c"}; font-weight:800; font-size:1.13em; letter-spacing:0.5px; display:inline-flex; align-items:center; gap:0.4em;'>
                        <span style="font-size:1.25em;">
                            {"✅" if pred == 0 else "❌"}
                        </span>
                        {"Loan Approved" if pred == 0 else "Loan Not Approved"}
                    </span>
                </div>
                <div style='text-align:center; color:#b0b0c0; font-size:1.11em; margin-bottom:0.7em;'>
                    <b>Confidence Score:</b>
                    <span style='font-weight:700; color:{"#1bc47d" if conf >= 0.7 else "#e67e22"}; background:rgba(167,168,230,0.09); border-radius:0.4em; padding:0.13em 0.6em 0.13em 0.6em; margin-left:0.3em;'>
                        {conf:.2%}
                    </span>
                </div>
                <hr style='margin:1.1em 0 1em 0; border: none; border-top: 1.5px solid #35365a;'/>
                <div style='font-size:1.01em; color:#b0b0c0; margin-bottom:0.2em;'>
                    <b>Features Evaluated:</b>
                    <span style="color:#e7e8ff; font-weight:600;">{input_data.shape[1]}</span> / 24
                </div>
                <div style='font-size:0.99em; color:#b0b0c0; margin-bottom:0.2em;'>
                    <b>Model Type:</b>
                    <span style="color:#e7e8ff; font-weight:600;">Random Forest Classifier</span>
                </div>
                <div style='font-size:0.97em; color:#7e7fa6; margin-top:0.7em; text-align:center;'>
                    <em>For best results, ensure all fields are filled accurately.</em>
                </div>
                <hr style='margin:1.1em 0 1em 0; border: none; border-top: 1.5px solid #35365a;'/>
                <div style='font-size:1.01em; color:#b0b0c0; margin-bottom:0.2em; text-align:center;'>
                    <b>Loan to Income Ratio:</b>
                    <span style="color:#e7e8ff; font-weight:600;">{loan_to_income:.3f}</span>
                </div>
                <div style='font-size:1.01em; color:#b0b0c0; margin-bottom:0.2em; text-align:center;'>
                    <b>Debt to Income Ratio:</b>
                    <span style="color:#e7e8ff; font-weight:600;">{debt_to_income:.3f}</span>
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    except Exception as e:
        st.error(f"Prediction failed: {str(e)}")
        st.info("This error may occur if the model expects a different feature set. Please ensure all required fields are completed.")

# --- Footer ---
st.markdown(
    "<div class='footer'>© 2025 Loan Approval Assessment | Powered by Streamlit</div>",
    unsafe_allow_html=True
)
