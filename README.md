# ISO 27001 Control Wheel Generator
Streamlit application that converts ISO 27001 security control status spreadsheets into interactive, downloadable HTML radial charts using Plotly.

## Link 
Deployed site can be found at: https://exceltoradialcontrolsgraph.streamlit.app/

## Template 
An example dataset format is required for the generator to work properly. The app expects an uploaded Excel (`.xlsx`, `.xls`) or CSV file where the first four columns contain:
1. **Control ID** (e.g., A.5.1)
2. **Control Name** (e.g., Policies for information security)
3. **Status** (e.g., Yes, No, Boundary)
4. **Score/5** (Numeric value)

The application will automatically drop header rows and filter the data to generate separate interactive wheels for distinct control families (e.g., A.5, A.6, A.7).

### Privacy Note: 
This application processes potentially sensitive compliance data entirely in-memory. Uploaded files are not stored, logged, or persisted on the server after the browser session is closed or the charts are generated.

### Created by Ethan Deysel
