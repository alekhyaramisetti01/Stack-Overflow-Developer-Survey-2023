import pandas as pd

# Load original dataset
df = pd.read_csv("survey_data_updated 5.csv")

# Helper function to process multi-select columns
def process_multivalue_column(column_name, output_filename):
    if column_name not in df.columns:
        print(f"❌ Column '{column_name}' not found.")
        return
    
    temp = df.dropna(subset=[column_name]).copy()
    temp[column_name] = temp[column_name].str.split(";")
    temp = temp.explode(column_name)
    temp[column_name] = temp[column_name].str.strip()
    top_10 = temp[column_name].value_counts().head(10).reset_index()
    top_10.columns = [column_name.replace("WantToWorkWith", "").replace("Webframe", "WebFramework").replace("Platform", "Platform"), "Count"]
    top_10.to_csv(output_filename, index=False)
    print(f"✅ Saved: {output_filename}")

# Process all multi-select columns for Tab 2
process_multivalue_column("LanguageWantToWorkWith", "top_10_language_want_to_work_with.csv")
process_multivalue_column("DatabaseWantToWorkWith", "top_10_database_want_to_work_with.csv")
process_multivalue_column("PlatformWantToWorkWith", "top_10_platform_want_to_work_with.csv")
process_multivalue_column("WebframeWantToWorkWith", "top_10_webframework_want_to_work_with.csv")

# ---------------------
# Demographics tab data
# ---------------------

# Age distribution (Pie Chart)
age_df = df["Age"].dropna().value_counts().reset_index()
age_df.columns = ["Age", "Count"]
age_df.to_csv("age_distribution.csv", index=False)
print("✅ Saved: age_distribution.csv")

# Country count (Map Chart)
country_df = df["Country"].dropna().value_counts().reset_index()
country_df.columns = ["Country", "Count"]
country_df.to_csv("country_distribution.csv", index=False)
print("✅ Saved: country_distribution.csv")

# Education level (Line Chart)
ed_df = df["EdLevel"].dropna().value_counts().reset_index()
ed_df.columns = ["EducationLevel", "Count"]
ed_df.to_csv("education_level_distribution.csv", index=False)
print("✅ Saved: education_level_distribution.csv")

# Age x Education (Stacked Bar Chart)
age_edu_df = df[["Age", "EdLevel"]].dropna()
age_edu_grouped = age_edu_df.groupby(["Age", "EdLevel"]).size().reset_index(name="Count")
age_edu_grouped.to_csv("age_by_education.csv", index=False)
print("✅ Saved: age_by_education.csv")
