import streamlit as st

def berakna_ugl_roi(
    kurskostnad,
    boende_mat,
    resor,
    lon_bortfall,
    personalomsattning_forr,
    kostnad_per_omsattning,
    sjukfranvaro_dagar,
    antal_personer_sjuka,
    kostnad_per_dag,
    produktivitetstapp_procent,
    teamstorlek,
    arlig_lonekostnad_per_person,
    forbattringsgrad_procent
):
    total_kostnad = kurskostnad + boende_mat + resor + lon_bortfall
    kostnad_personalomsattning = personalomsattning_forr * kostnad_per_omsattning
    kostnad_sjukfranvaro = sjukfranvaro_dagar * antal_personer_sjuka * kostnad_per_dag
    produktivitetstapp = (produktivitetstapp_procent / 100) * teamstorlek * arlig_lonekostnad_per_person
    total_forrlust = kostnad_personalomsattning + kostnad_sjukfranvaro + produktivitetstapp
    besparing = total_forrlust * (forbattringsgrad_procent / 100)
    roi = besparing / total_kostnad if total_kostnad > 0 else 0

    return total_kostnad, total_forrlust, besparing, roi

st.title("UGL ROI-Kalkylator")

st.sidebar.header("Ange dina siffror")
kurskostnad = st.sidebar.number_input("Kurskostnad (SEK)", value=35000)
boende_mat = st.sidebar.number_input("Boende och mat (SEK)", value=9000)
resor = st.sidebar.number_input("Resor (SEK)", value=2000)
lon_bortfall = st.sidebar.number_input("Lönekostnad/bortfall (SEK)", value=25000)
personalomsattning_forr = st.sidebar.number_input("Antal medarbetare som slutar per år", value=2)
kostnad_per_omsattning = st.sidebar.number_input("Kostnad per ersättning (SEK)", value=250000)
sjukfranvaro_dagar = st.sidebar.number_input("Sjukdagar per person/år", value=10)
antal_personer_sjuka = st.sidebar.number_input("Antal personer med frånvaro", value=4)
kostnad_per_dag = st.sidebar.number_input("Kostnad per sjukdag (SEK)", value=3500)
produktivitetstapp_procent = st.sidebar.number_input("Produktivitetsbortfall (%)", value=5)
teamstorlek = st.sidebar.number_input("Storlek på teamet (personer)", value=10)
arlig_lonekostnad_per_person = st.sidebar.number_input("Årlig lön per person (SEK)", value=600000)
forbattringsgrad_procent = st.sidebar.number_input("Förbättring efter UGL (%)", value=30)

if st.button("Beräkna ROI"):
    total_kostnad, total_forrlust, besparing, roi = berakna_ugl_roi(
        kurskostnad,
        boende_mat,
        resor,
        lon_bortfall,
        personalomsattning_forr,
        kostnad_per_omsattning,
        sjukfranvaro_dagar,
        antal_personer_sjuka,
        kostnad_per_dag,
        produktivitetstapp_procent,
        teamstorlek,
        arlig_lonekostnad_per_person,
        forbattringsgrad_procent
    )

    st.subheader("Resultat")
    st.write(f"Total investering (UGL): {total_kostnad:,.0f} SEK")
    st.write(f"Årlig förlust innan åtgärd: {total_forrlust:,.0f} SEK")
    st.write(f"Uppskattad besparing efter UGL: {besparing:,.0f} SEK")
    st.write(f"Beräknad ROI: {roi:.2f}x investeringen")
