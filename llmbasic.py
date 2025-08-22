from llama_cpp import Llama
import re

# Load model
model_path = "./Phi-3.5-mini-instruct-Q4_K_M.gguf"
llm = Llama(model_path=model_path, n_ctx=2048)

def extract_sql_query(output_text):
    match = re.search(r"```sql\s*(.*?)\s*```", output_text, re.DOTALL)
    if match:
        return match.group(1).strip()
    return None

def get_sql_query(user_question):
    schema = """
Database Schema (with primary keys and HMDA code definitions by column):

-- Lookup Tables
Ethnicity_Lookup(ethnicity_code PK, ethnicity_name)
  • ethnicity_code: 1=Hispanic or Latino, 2=Not Hispanic, 3=Info not provided (mail/phone), 4=Not applicable, 5=No co-applicant

Sex_Type(sex_code PK, sex_name)
  • sex_code: 1=Male, 2=Female, 3=Info not provided (mail/phone), 4=Not applicable, 5=No co-applicant

Race_Lookup(race_code PK, race_name)
  • race_code: 1=American Indian/Alaska Native, 2=Asian, 3=Black/African American, 4=Native Hawaiian/Other Pacific Islander, 5=White, 6=Info not provided, 7=Not applicable, 8=No co-applicant

Loan_Type(loan_type PK, loan_type_name)
  • loan_type: 1=Conventional, 2=FHA-insured, 3=VA-guaranteed, 4=FSA/RHS

Loan_Purpose(loan_purpose PK, loan_purpose_name)
  • loan_purpose: 1=Home purchase, 2=Home improvement, 3=Refinancing

Property(property_type PK, property_type_name)
  • property_type: 1=1-4 family, 2=Manufactured housing, 3=Multifamily

Preapproval(preapproval PK, preapproval_name)
  • preapproval: 1=Requested, 2=Not requested, 3=Not applicable

Owner_Occupancy(owner_occupancy PK, owner_occupancy_name)
  • owner_occupancy: 1=Owner-occupied, 2=Not owner-occupied, 3=Not applicable

Purchaser(purchaser_type PK, purchaser_type_name)
  • purchaser_type: 0=Not sold, 1=Fannie Mae, ..., 9=Other purchaser

HOEPA(hoepa_status PK, hoepa_status_name)
  • hoepa_status: 1=HOEPA loan, 2=Not a HOEPA loan

Lien(lien_status PK, lien_status_name)
  • lien_status: 1=First lien, 2=Subordinate lien, 3=No lien, 4=Not applicable

Action_Taken(action_taken PK, action_taken_name)
  • action_taken: 1=Originated, 2=Approved not accepted, 3=Denied, 4=Withdrawn, 5=Incomplete, 6=Purchased, 7=Preapproval denied, 8=Preapproval approved not accepted

Agency(agency_code PK, agency_name, agency_abbr)
  • agency_code: 1=OCC, 2=FRS, 3=FDIC, 5=NCUA, 7=HUD, 9=CFPB

Respondent(respondent_code PK, respondent_id TEXT)
  • respondent_id: 10-character HMDA respondent identifier

Denial_Codes(denial_code PK, denial_reason_name)
  • denial_reason: 1=Debt-to-income, 2=Employment history, 3=Credit history, 4=Collateral, 5=Insufficient cash, 6=Unverifiable info, 7=Incomplete app, 8=Mortgage insurance denied, 9=Other

Denial(denial_id PK)

Denial_Reasons(denial_id FK, denial_reason FK, reason_order PK)

State(state_code PK, state_name, state_abbr)
County(state_code FK, county_code PK, county_name)
MSA(msamd PK, msamd_name)

-- Applicant / Co-Applicant Tables
Applicant_Main(applicant_id PK, applicant_income_000s, applicant_sex FK, applicant_ethnicity FK)

Applicant_Race(applicant_id FK, race_code FK, race_order PK)

Co_Applicant_Main(co_applicant_id PK, co_applicant_sex FK, co_applicant_ethnicity FK)

Co_Applicant_Race(co_applicant_id FK, race_code FK, race_order PK)

-- Loan Info
Loan(loan_id PK, loan_type FK, loan_amount_000s, loan_purpose FK)

-- Property Location
Location(location_id PK, msamd FK, state_code FK, county_code FK,
         census_tract_number, population, minority_population, hud_median_family_income,
         tract_to_msamd_income, number_of_owner_occupied_units, number_of_1_to_4_family_units)

-- Metadata
AllNullColumns(null_id PK, edit_status, edit_status_name, sequence_number, application_date_indicator)
  • edit_status: 5=Validity edit failure, 6=Quality edit failure, 7=Both
  • application_date_indicator: 0=On/after 01-01-2004, 1=Before 01-01-2004, 2=Not available
  • sequence_number: unique number per respondent

-- Loan Applications
LoanApplication(application_id PK,
    applicant_id FK, co_applicant_id FK,
    loan_id FK, location_id FK,
    purchaser_type FK, denial_id FK,
    respondent_code FK, agency_code FK,
    as_of_year, preapproval FK, rate_spread,
    action_taken FK, hoepa_status FK, lien_status FK,
    owner_occupancy FK, property_type FK
)
"""

    prompt = f"""Write a SQL query in response to the following detailed schema and user question.

Schema:
{schema}

Question:
{user_question}

Respond only with the SQL query enclosed in ```sql ... ```"""

    try:
        response = llm(prompt, max_tokens=256)
        output_text = response["choices"][0]["text"]
        return extract_sql_query(output_text)
    except (KeyError, IndexError, TypeError) as e:
        print(f"Error extracting SQL from LLM response: {e}")
        return None
