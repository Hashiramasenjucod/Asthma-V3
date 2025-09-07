
Asthma MB Basket Checker (V2 Form Edition)
-----------------------------------------
This is a form version of the Asthma MB checker.

- When `trigger_creation` condition is met, a new form appears.
- You can enter two medicines with codes and max quantities to create your own basket.
- The created basket is displayed back to you (not saved).

Files:
- valid_icd10_asthma.json : valid ICD-10 codes for Asthma
- asthma_mb.json          : original basket medicines and max qty
- app_streamlit_asthma_fun.py : Streamlit fun app

Run locally:
    pip install streamlit
    streamlit run app_streamlit_asthma_fun.py

Deploy to Streamlit Cloud:
1. Upload these files to a public GitHub repo.
2. Go to https://share.streamlit.io and create a new app.
3. Set the main file path to `app_streamlit_asthma_fun.py`.
4. Deploy — you'll get a public URL.
