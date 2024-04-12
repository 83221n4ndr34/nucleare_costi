# spoiler allert

# hey, dico a te, con il ditino, so che sei più bravo di noi a programmare, quindi perchè non fai un bel fork e ci aiuti?


import pandas as pd
import streamlit as st
import plotly.graph_objs as go
import os
import yaml

# Funzione per caricare gli scenari dal file YAML
def carica_scenari_da_yaml(percorso_file):
    with open(percorso_file, 'r') as file:
        dati = yaml.safe_load(file)
    return dati['scenari']


# determinazione del percorso del file YAML rispetto al percorso di questo script
percorso_file_yaml = os.path.join(os.path.dirname(__file__), 'scenari.yml')

# import degli scenari
scenari = carica_scenari_da_yaml(percorso_file_yaml)
# st.write("Scenari caricati:", scenari)  # li carica correttamente fin qui

st.title('Il modello più semplicistico di analisi dei costi del nucleare')
st.header('Nuclear is :blue[cool] :sunglasses:', divider='rainbow')
st.write(
    "Questa app è stata creata da [Umberto Bertonelli](https://umbertobertonelli.it) con il gentilissimo supporto di [Comitato Nucleare e Ragione](https://www.instagram.com/nucleareeragione/).")
st.write("La documentazione completa è disponibile [qui](https://github.com/DrElegantia/nucleare_costi/tree/main).")
st.divider()

st.subheader('Nucleare: ma quanto ci costi?')

st.subheader(
    'In Italia da qualche anno ormai si è tornati a parlare di nucleare, e spesso una delle domande (*lecite*) che viene posta al centro del dibattito è: :blue[***MA QUANTO CI COSTA?***]')

st.markdown("A questa domanda, vengono poste diverse risposte:")

st.markdown(
    "- **Il costo iniziale di costruzione di una centrale nucleare è elevato, ma nel lungo periodo potrebbe risultare vantaggioso in termini di riduzione dei costi energetici.**")
st.markdown(
    "- **Le tecnologie nucleari stanno evolvendo, e ci sono progetti per centrali più sicure e economicamente convenienti nel futuro.**")
st.markdown(
    " - **Il costo dell'energia nucleare dipende da vari fattori, tra cui il prezzo del combustibile nucleare e le misure di sicurezza implementate.**")
st.markdown(" - **Costerebbe di più uno scenario 100% rinnovabile.**")
st.markdown(" - **Costa troppo.**")

st.markdown("Chiaramente queste non sono le uniche risposte!")

st.markdown(
    "Essendo che il costo del nucleare, ma in generale di qualsiasi opera pubblica, dipende da molti fattori, abbiamo provato a rispondere diversamente, con qualche dato alla mano!")

st.markdown("Abbiamo individuato i principali fattori che influenzano il costo del nucleare:")

st.markdown("- **Il tasso di interesse per prendere a prestito le risorse necessarie**")
st.markdown("- **Il tempo di costruzione**")
st.markdown(" - **Il Costo Overnight, ovvero il costo complessivo al netto del finanziamento**")
st.markdown(" - **Il tasso di apprendimento**")

st.write("Assumiamo per semplicità che ogni reattore abbia una produzione di 1000MW")

st.write("Nel modello, ipotiziamo che lo stato voglia realizzare un certo numero di reattori (decisi dall'utente).")

st.write(
    'Date le ipotesi riferite al FOAK (First-Of-A-Kind), ovvero il primo progetto di reattore, calcoliamo gli interessi attraverso il tasso composto, sulla base del costo al netto dei costi di finanziamento,')
st.write('In base al tasso di apprendimento andiamo a stimare tempi e costi dei successivi reattori.')
st.write(
    "Una volta definite tutte queste condizioni, ipotiziamo di far partire la costruzione di un reattore all'anno.")

st.markdown(
    "Per stimare gli impatti macroeconomici, abbiamo considerato lo scenario base de [***LE TENDENZE DI MEDIO-LUNGO PERIODO DEL SISTEMA PENSIONISTICO E SOCIO-SANITARIO – AGGIORNAMENTO 2023***](https://www.rgs.mef.gov.it/_Documenti/VERSIONE-I/Attivit--i/Spesa-soci/Attivita_di_previsione_RGS/2023/Rapporto-2023.pdf#page=473) realizzato dalla Ragioneria Generale dello Stato.")
st.markdown(
    "Per la stima del PIL, abbiamo adottato la metodologia illustrata dall'Ufficio Parlamentare di Bilancio in occasione del report [***Cambiamenti nelle proiezioni di medio-lungo periodo della spesa pensionistica in Italia***](https://www.upbilancio.it/wp-content/uploads/2020/10/Flash-2_2020.pdf).")
st.markdown(
    "Per la stima della finanza pubblica, abbiamo usato i dati realtivi alla voci di entrata e alla voci di uscita in rapporto al pil presentati in [NADEF 2023](https://www.dt.mef.gov.it/export/sites/sitodt/modules/documenti_it/analisi_progammazione/documenti_programmatici/nadef_2023/NADEF-2023.pdf#page=75), adottando alcuni accorgimento al fine di ricalcare quanto previsto dal [FMI](https://www.imf.org/en/Publications/CR/Issues/2022/07/28/Italy-2022-Article-IV-Consultation-Press-Release-Staff-Report-and-Statement-by-the-521484).")

st.markdown(
    "Il PIL aggiuntivo realizzato con il nucleare, in accordo con il modello fornito da UPB, si basa sul prodotto fra occupati, dati dalla somma degli occupati nelle varie fasi di vita del reattore (costruzione e operatività) e dell'occupazione indotta e indiretta, e relativo valore aggiunto. Inoltre, abbiamo previsto la possibilità di determinare un aumento in termini percentuali della produttività del settore dell'industria. Per la stima dell'occupazione abbiamo preso a riferimento [***Measuring Employment Generated by the Nuclear Power Sector***](https://www.oecd-nea.org/jcms/pl_14912) prodotto da NEA")

st.write("Siamo consci che il nostro modello soffra di molte limitazioni, ad esempio:")

st.markdown("- **La mancanza di considerazione di fattori come la variabilità dei costi di capitale e operativi**")
st.markdown("- **Gli eventualli periodi recessivi futuri**")
st.markdown(" - **La stima degli impatti di integrazione fra nucleare e altre fonti rinnovabili**")
st.markdown(" - **Il tasso di apprendimento lineare e costante**")
st.markdown(" - **I possibili ritardi accumulati dai progetti per impedimenti burocratici, sociali o di altra natura**")
st.markdown(" - **Eventuali altri impatti di finanza pubblica che compromettano le casse dello stato**")
st.markdown(" - **Non viene considerata l'energia prodotta**")

st.markdown(
    "Tuttavia, il modello è utile per fornire una stima grossolana iniziale dei costi e del tempo di realizzazione di un progetto di energia nucleare, oltre che del suo impatto sulla finanza pubblica e le variabili macroeconomiche italiane.")

st.write(
    "Se si vuole approfondire il tema attraverso documenti e opinione di esperti, qui trovate un'intervista al prof. Jacopo Buongiorno, Direttore del Centro per i sistemi avanzati di energia nucleare al MIT. Inoltre, in descrizione al video abbiamo lasciato ulteriori documenti, paper ed analisi utili a contestualizzare il tema.")
# URL del video su YouTube
video_url = "https://youtu.be/FOqnCk1Uv7I"

# Incorpora il video nella tua app Streamlit
st.video(video_url)

st.divider()
pluto = False


# controllo dei consensi

consenso1 = st.checkbox('Sono consapevole dei limiti del modello e ho compreso la natura del modello.')
consenso2 = st.checkbox('Sono consapevole che, come ogni modello, anche questo è errato.')
consenso3 = st.checkbox('Sono consapevole che le risposte del modello dipendono dalle ipotesi che io andrò a selezionare, oltre che dalla struttura dello stesso.')




if consenso1 and consenso2 and consenso3:
    modello = st.radio(
        "Che profilo vuoi impostare al tuo modello?",
        ["BEST CASE SCENARIO", "SCENARIO MEDIANO", "TASSI BASSI", "SUPER APPRENDIMENTO", "WORST CASE SCENARIO",
            'SMR', "PERSONALIZZA MODELLO"],
        help="Selezionando un modello verranno valorizzati in modo automatico i vari parametri, questi saranno riportati nei singoli grafici. Se si preferisce valorizzare autonomamente i parametri è sufficiente selezionare l'opzione personalizza modello")
    #st.write(f"{modello}")
    # convertire gli spazi in underscore per corrispondere alle chiavi nel dizionario
    
    modello = modello.replace(" ", "_").upper()

    if modello is not None and modello in scenari:
        i = 0
        t = 0
        progetti = 0
        partenza = 0
        apprendimento = 0
        costo_base = 0
        occupati_operativita = 0
        occupati_indiretti = 0
        occupati_costruzione = 0
        occupati_indotto = 0
        pil_diretti = 0
        pil_indiretti = 0
        pil_costruzione = 0
        pil_indotto = 0
        pil_eco = 0
        taglio = 0
        
        scenario = scenari[modello]

        # assegnazione dinamica di variabili
        for chiave, valore in scenario.items():
            # assegnazione di una variabile globale per ogni chiave del dizionario 
            globals()[chiave] = valore  
        # st.write(f"Variabili per lo scenario '{modello}':", scenario)
        
        
        # assegnazione diretta delle variabili dai valori del dizionario
       # i = scenario['i']
       # t = scenario['t']
       # progetti = scenario['progetti']
       # partenza = scenario['partenza']
       # apprendimento = scenario['apprendimento']
       # costo_base = scenario['costo_base']
       # occupati_operativita = scenario['occupati_operativita']
       # occupati_indiretti = scenario['occupati_indiretti']
       # occupati_costruzione = scenario['occupati_costruzione']
       # occupati_indotto = scenario['occupati_indotto']
       # pil_diretti = scenario['pil_diretti']
       # pil_indiretti = scenario['pil_indiretti']
       # pil_costruzione = scenario['pil_costruzione']
       # pil_indotto = scenario['pil_indotto']
       # pil_eco = scenario['pil_eco']
       # taglio = scenario['taglio']

    elif modello == "PERSONALIZZA MODELLO":

        
        i = st.slider(
            'Che tasso di  interesse prevedi per il costo del finanziamento? Dato espresso in termini percentuali',
            4, 20, 4, help="Il tasso di interesse influenza il costo complessivo dell'operazione")
        
        t = st.slider(
            'In quanto tempo stimi venga realizzato il FOAK? Dato espresso in anni.',
            4, 30, 12,
            help="Il tempo dei successivi reattori è dato dal tempo del FOAK e dal tasso di apprendimento.")

        costo_base = st.slider(
            'A quanto stimi possa ammontare il costo overnight del FOAK? Dato espresso in miliardi di €.',
            0.5, 20.0, 10.0,
            help="Il costo overnight rappresenta il costo complessivo per realizzare il reattore, al netto del costo di finanziamento.")

        apprendimento = st.slider(
            'A quanto stimi il tasso di apprendimento? Dato espresso in termini percentuali.',
            -10, 10, 3,
            help="Il tasso di apprendimento stima la curva di apprendimento che si prevede avrà il progetto. Il tasso per il modello avrà effetto sia sul tempo di realizzazione che sul costo con pari entità. Se negativo, il tasso va ad aumentare tempi e costi di realizzazione.")
        
        progetti = st.slider(
            'Su quanti reattori vuoi basare il modello?',
            1, 35, 26,
            help="Il modello si basa sull'ipotesi che tutti i reattori appartengano allo stesso tipo.")
        
        partenza = 2026

        occupati_costruzione = st.slider(
            f'A quanto ammonta la stima di occupati/anno per la costruzione del reattore? Dato in FTE.',
            1000, 2500, 2200,
            help="L'occupazione complessiva per la fase di costruzione è influenzata dai tempi di realizzazione del singolo reattore")
        
        occupati_operativita = st.slider(
            f"A quanto ammonta la stima di occupati/anno durante l'operativià del reattore? Dato in FTE.",
            300, 900, 600,
            help="L'occupazione complessiva durante l'operativià è influenzata dall'entrata in funzione del singolo reattore")

        occupati_indiretti = st.slider(
            f'A quanto ammonta la stima di occupati/anno indiretti rispetto agli occupati/anno diretti (costruzione + operatività)? Dato in termini percentuali',
            0, 100, 33,
            help="L'occupazione complessiva indiretta si riferisce alla catena del valore, pertanto è influenzata sia dagli occupati diretti.")

        occupati_indotto = st.slider(
            f'A quanto ammonta la stima di occupati/anno indotti rispetto agli occupati/anno diretti e indiretti? Dato in termini percentuali.',
            0, 100, 66,
            help="L'occupazione complessiva indiretta si riferisce ai posti di lavoro indotti dall'industria dell'energia nucleare darivanti dal flusso circolare di reddito nell'economia nazionale, pertanto è influenzata sia dagli occupati diretti che dagli occupati indiretti.")

        pil_costruzione = st.slider(
            f"A quanto ammonta la stima di valore aggiunto prodotto per ogni singolo occupato nella fase di costruzione del reattore rispetto alla media nazionale? Dato in termini percentuali.",
            -100, 100, 10)

        pil_diretti = st.slider(
            f"A quanto ammonta la stima di valore aggiunto prodotto per ogni singolo occupato coinvolto nell'operatività del singolo reattore rispetto alla media nazionale? Dato in termini percentuali.",
            0, 150, 100)

        pil_indiretti = st.slider(
            f"A quanto ammonta la stima di valore aggiunto prodotto per ogni singolo occupato indiretto nel settore dell'energia nucleare rispetto alla media nazionale? Dato in termini percentuali.",
            -100, 100, 10)
        
        pil_indotto = st.slider(
            f"A quanto ammonta la stima di valore aggiunto prodotto per ogni singolo occupato indotto dall'industria dell'energia nucleare rispetto alla media nazionale? Dato in termini percentuali.",
            -100, 100, -10)
        
        pil_eco = st.slider(
            f"Alla fine del progetto, a quanto ammonta la variazione della produttività nel settore dell'industria ed energia grazie all'adozione dell'energia nucleare? Dato in termini percentuali.",
            0, 100, 10,
            help="Il PIL oltre ad aumentare per effetto dell'occupazione diretta e indiretta aggiuntiva, può aumentare a seguito della migliorata produttività dell'economia grazie al cambiamento tecnologico. Qui è possibile valorizzare un coefficiente che andrà a moltiplicare il valore aggiunto per occupato del settore dell'Industria, che pesa circa il 25% del PIL.")

        genre = st.radio(
            "Vuoi che il modello preveda un taglio della spesa pensionistica?",
            ["No", "dell'1% di pil", "del 2% del pil"],
            help='Sulla base delle stime RGS il modello calcola la spesa epnsionistica, è possibile ridurre il suo impatto sui conti pubblici di alcuni punti di pil attraverso la selezione.')

        if genre == "No":
            taglio = 0
        elif genre == "dell'1% di pil":
            taglio = 1
        elif genre == "del 2% del pil":
            taglio = 2


    def costo_opera(i, t, co):
        costo_opera_list = []
        for k in range(1, t + 1):
            costo_opera = (co / t) * (1 + i) ** (k)
            costo_opera_list.append(costo_opera)
        costo_opera = sum(costo_opera_list)
        return costo_opera


    a_results = []
    t_results = []
    c_results = []

    costo_base = costo_base * 1000000000
    i = i / 100

    apprendimento = apprendimento / 100

    for p in range(0, progetti + 0):
        tempo = round(t * max((1 - apprendimento) ** p, 0.3))
        costo = costo_base * max((1 - apprendimento) ** p, 0.3)
        a = costo_opera(i, tempo, costo)
        a_results.append(a)
        t_results.append(tempo)
        c_results.append(costo)

    df = pd.DataFrame({'progetti': a_results, 'Tempo': t_results, 'costo_netto': c_results})
    df['Interessi'] = df.progetti - df.costo_netto

    # Assumendo che df sia il tuo DataFrame e che contenga le colonne necessarie

    # Creare le tracce per il grafico a barre
    trace1 = go.Bar(x=df.index, y=df.costo_netto, name='Costo Overnight', marker=dict(color='#1A76FF'))
    trace2 = go.Bar(x=df.index, y=df.Interessi, name='Costo di Finanziamento', marker=dict(color='#84C9FF'))

    # Creare il layout del grafico
    layout = go.Layout(
        title=f'Costo dell\'n-esimo reattore scomposto in <span style="color:#1A76FF;">OVERNIGHT</span> e <span style="color:#84C9FF;"> DI FINANZIAMENTO</span> <br> Costo medio di 1 reattore: {sum(df.progetti) / 1000000000 / progetti:.2f} mld €<br> Ipotesi: i={i * 100:.2f}%, apprendimento={apprendimento * 100:.2f}%, Tempo FOAK={t} anni, costo overnight FOAK={costo_base / 1000000000:.2f} mld €',
        xaxis=dict(title='Progetto Realizzato'),
        yaxis=dict(title='Costo in €'),
        barmode='stack',  # Impostare 'stack' per impilare le barre
        showlegend=False
    )

    # Creare la figura
    fig = go.Figure(data=[trace1, trace2], layout=layout)

    # Mostrare il grafico
    st.plotly_chart(fig)

    df['Quote'] = df.progetti / df.Tempo
    df['start'] = 1
    df['Partenza'] = partenza + df.start.shift(1).cumsum()
    if pluto == True:
        df['Partenza'] = round(partenza + df.start.shift(1).cumsum() / 3)
    df.loc[0, 'Partenza'] = partenza

    df['Conclusione'] = df['Partenza'] + df.Tempo

    df['Partenza'] = df['Partenza'].fillna(0)
    new_dfs = []
    for _, row in df.iterrows():
        start_year = int(row['Partenza'])
        end_year = int(row['Conclusione'])
        year_range = range(start_year, end_year)  # Aggiungo 1 per includere anche l'anno di conclusione
        project_df = pd.DataFrame({
            'Anno': year_range,
            'progetti': row['progetti'] / row['Tempo'],
            'Interessi': row['Interessi'] / row['Tempo'],
            'Costo_netto': row['costo_netto'] / row['Tempo'],
            'Quote': row['Quote'],
            'Avanzamento': 1 / row['Tempo'],
            'start': row['start']
        })
        new_dfs.append(project_df)

    # Concatenare tutti i nuovi dataframe in uno solo
    result_df = pd.concat(new_dfs, ignore_index=True)

    df_def = result_df.groupby('Anno').agg({
        'Quote': sum,
        'progetti': sum,
        'Interessi': sum,
        'Costo_netto': sum,
        'Avanzamento': sum,
        'start': sum

    })
    df_def.Avanzamento = df_def.Avanzamento.cumsum()

    # Creare le tracce per il grafico a barre
    trace1 = go.Bar(x=df_def.index, y=df_def.Costo_netto, name='Costo overnight', marker=dict(color='#1A76FF'))
    trace2 = go.Bar(x=df_def.index, y=df_def.Interessi, name='Costo di finanziamento',
                    marker=dict(color='#84C9FF'))

    # Creare il layout del grafico
    layout = go.Layout(
        title=f'Andamento delle spese annuali, scomposte in <span style="color:#1A76FF;">OVERNIGHT</span> e <span style="color:#84C9FF;">DI FINANZIAMENTO</span> <br> Spesa media annuale: {(df_def.Costo_netto.mean() + df_def.Interessi.mean()) / 1000000000:.2f} mld € <br> Ipotesi: i={i * 100:.2f}%, apprendimento={apprendimento * 100:.2f}%, Tempo FOAK = {t} anni, costo overnight FOAK={costo_base / 1000000000:.2f} mld €',
        xaxis=dict(title='Anno'),
        yaxis=dict(title='Costo in €'),
        barmode='stack',
        showlegend=False
    )

    # Creare la figura
    fig = go.Figure(data=[trace1, trace2], layout=layout)

    # Mostrare il grafico
    st.plotly_chart(fig)

    # Creare le tracce per il grafico a barre
    trace1 = go.Bar(x=df_def.index, y=df_def.Costo_netto.cumsum(), name='Costo overnight',
                    marker=dict(color='#1A76FF'))
    trace2 = go.Bar(x=df_def.index, y=df_def.Interessi.cumsum(), name='Costo di finanziamento',
                    marker=dict(color='#84C9FF'))

    # Creare il layout del grafico
    layout = go.Layout(
        title=f'Andamento della spesa cumulata, scomposta in <span style="color:#1A76FF;">OVERNIGHT</span> e <span style="color:#84C9FF;">DI FINANZIAMENTO</span> <br> Spesa complessiva: {(df_def.Costo_netto.sum() + df_def.Interessi.sum()) / 1000000000:.2f} mld € <br> Ipotesi: i={i * 100:.2f}%, apprendimento={apprendimento * 100:.2f}%, Tempo FOAK={t} anni, costo overnight FOAK={costo_base / 1000000000:.2f} mld €',
        xaxis=dict(title='Anno'),
        yaxis=dict(title='Costo in €'),
        barmode='stack',
        showlegend=False
    )

    # Creare la figura
    fig = go.Figure(data=[trace1, trace2], layout=layout)

    # Mostrare il grafico
    st.plotly_chart(fig)

    # Dati originali
    data = {
        'Anno': [2015, 2020, 2025, 2030, 2035, 2040, 2045, 2050, 2055, 2060, 2065, 2070],
        'Popolazione [20-54]': [28.337, 26.753, 24.942, 23.533, 22.474, 21.683, 20.876, 20.167, 19.518, 18.862,
                                18.161, 17.547],
        'Popolazione [55-64]': [7.604, 8.431, 9.200, 9.373, 8.730, 7.647, 6.857, 6.563, 6.476, 6.491, 6.554,
                                6.393],
        'Popolazione totale': [60.295, 59.641, 58.560, 57.906, 57.185, 56.370, 55.395, 54.165, 52.630, 50.906,
                                49.213, 47.722],
        'PIL reale (mld di € 2015)': [1.655, 1.574, 1.809, 1.882, 1.939, 2.005, 2.076, 2.170, 2.279, 2.395,
                                        2.508, 2.614],
        'Spesa pensionistica/PIL': [15.6, 16.9, 16.1, 16.4, 16.8, 17, 16.8, 16.1, 15.1, 14.4, 14.1, 14.1],
        'Numero di occupati': [22.121, 22.385, 23.737, 23.972, 23.597, 22.828, 21.891, 21.315, 20.951, 20.639,
                                20.269, 19.847]
    }

    popolazione = pd.DataFrame(data)
    popolazione['Popolazione [20-64]'] = popolazione['Popolazione [20-54]'] + popolazione['Popolazione [55-64]']

    # Creazione del DataFrame con tutti gli anni desiderati
    anni_desiderati = pd.DataFrame({'Anno': range(2015, 2071)})

    # Merge dei DataFrame per avere tutti gli anni con i relativi dati
    popolazione_anni_completi = pd.merge(anni_desiderati, popolazione, on='Anno', how='left')

    # Riempimento dei vuoti interpolando i dati
    popolazione_anni_completi_interpolati = popolazione_anni_completi.interpolate(method='linear', axis=0)

    pop = popolazione_anni_completi_interpolati
    pop['Numero occupati di 15−64 anni'] = pop['Numero di occupati'] * 1000000
    pop['PIL per occupato di 15−64 anni'] = (pop['PIL reale (mld di € 2015)'] * 1000000000000) / (
    pop['Numero occupati di 15−64 anni'])

    df_def = result_df.groupby('Anno').agg({
        'Quote': sum,
        'progetti': sum,
        'Interessi': sum,
        'Costo_netto': sum,
        'Avanzamento': sum,
        'start': sum

    })
    df_def.Avanzamento = df_def.Avanzamento.cumsum()
    df_def['end'] = df_def.index.map(lambda x: (df['Conclusione'] < x).sum())
    # Unione dei DataFrame 'df_def' e 'pop' sulla colonna 'Anno'
    df_def = df_def.merge(pop, on='Anno', how='left')

    df_def['Avanzamento_app'] = df_def['Avanzamento'].astype(int)
    df_def.at[df_def.index[-1], 'Avanzamento_app'] = progetti
    # Dati in lavoratori annui per reattore

    df_def['Stima pil RGS'] = df_def['PIL per occupato di 15−64 anni'] * df_def['Numero occupati di 15−64 anni']
    df_def['Numero costruttori nucleare'] = df_def['start'] * occupati_costruzione
    df_def['Numero addetti ope nucleare'] = occupati_operativita * df_def['end']
    df_def['Numero addetti indiretti nucleare'] = df_def[
                                                        'Numero addetti ope nucleare'] * occupati_indiretti / 100 + \
                                                    df_def[
                                                        'Numero costruttori nucleare'] * occupati_indiretti / 100
    df_def['Numero addetti indotti nucleare'] = df_def['Numero addetti ope nucleare'] * occupati_indotto / 100 + \
                                                df_def['Numero costruttori nucleare'] * occupati_indotto / 100 + \
                                                df_def[
                                                    'Numero addetti indiretti nucleare'] * occupati_indotto / 100

    df_def['Numero occupati di 15−64 anni nucleare'] = df_def['Numero addetti ope nucleare'] + df_def[
        'Numero addetti indiretti nucleare'] + df_def['Numero occupati di 15−64 anni'] + df_def[
                                                            'Numero costruttori nucleare'] + df_def[
                                                            'Numero addetti indotti nucleare']

    df_def['PIL per costruttori nucleare'] = df_def['Numero costruttori nucleare'] * (
                1 + pil_costruzione / 100) * df_def['PIL per occupato di 15−64 anni']

    df_def['PIL per addetto ope nucleare'] = df_def['Numero addetti ope nucleare'] * (1 + pil_diretti / 100) * \
                                                df_def['PIL per occupato di 15−64 anni']

    df_def['PIL per addetto indiretto nucleare'] = df_def['Numero addetti indiretti nucleare'] * (
                1 + pil_indiretti / 100) * df_def['PIL per occupato di 15−64 anni']
    df_def['PIL per addetto indotto nucleare'] = df_def['Numero addetti indiretti nucleare'] * (
                1 + pil_indotto / 100) * df_def['PIL per occupato di 15−64 anni']

    df_def['PIL aggiuntivo nucleare'] = df_def['PIL per addetto ope nucleare'] + df_def[
        'PIL per addetto indiretto nucleare'] + df_def['PIL per costruttori nucleare'] + df_def[
                                            'PIL per addetto indotto nucleare']
    df_def['PIL modello nucleare'] = df_def['PIL aggiuntivo nucleare'] + df_def['Stima pil RGS'] * (
                1 + pil_eco * df_def['end'] / progetti * 0.20 / 100)
    df_def['Stima crescita pil RGS'] = (df_def['Stima pil RGS'] / df_def['Stima pil RGS'].shift(1) - 1) * 100
    df_def['Stima crescita pil Nucleare'] = (df_def['PIL modello nucleare'] / df_def[
        'PIL modello nucleare'].shift(1) - 1) * 100

    # Creare le tracce per il grafico a linee
    trace1 = go.Scatter(x=df_def['Anno'], y=df_def['PIL modello nucleare'], mode='lines',
                        name='PIL - Stima modello Nucleare', marker=dict(color='#1A76FF'))
    trace2 = go.Scatter(x=df_def['Anno'], y=df_def['Stima pil RGS'], mode='lines',
                        name='PIL - Stima RGS - Scenario nazionale base', marker=dict(color='#FF0000'))

    # Creare il layout del grafico
    layout = go.Layout(
        title='Andamento del PIL confronto fra <br> <span style="color:#FF0000;">RGS - SCENARIO NAZIONALE BASE</span> e <span style="color:#1A76FF;">STIMA MODELLO NUCLEARE</span>',
        xaxis=dict(title='Anno'),
        yaxis=dict(title='Stima PIL'),
        showlegend=False
    )

    # Creare la figura
    fig = go.Figure(data=[trace2, trace1], layout=layout)

    # Mostrare il grafico
    st.plotly_chart(fig)

    finanza = st.radio( "Vuoi modificare i dati di finanza pubblica?",["No", "Sì"], help="Esprimi i valori in rapporto al PIL")

    if finanza=='No':
        debpil = 139
        redditi=8
        Consumi_intermedi=5
        prest_social=5
        spes_corr=3
        int_pass=4
        spes_cc=3.5
        ent_dir=15
        ent_indir=15
        ent_incc=0.1
        contr=15
        ae=4
        aent=1



    if finanza=='Sì':

        debpil = st.number_input('Rapporto debito PIL - in %', min_value=0, max_value=300, value=139, label_visibility="visible")
        redditi = st.number_input('SPESE - Redditi da lavoro dipendente - in % PIL', min_value=0, max_value=100, value=8, label_visibility="visible")
        Consumi_intermedi = st.number_input('SPESE - Consumi Intermedi - in % PIL', min_value=0, max_value=100, value=5, label_visibility="visible")
        prest_social = st.number_input('SPESE - Altre prestazioni sociali - in % PIL', min_value=0, max_value=100, value=5, label_visibility="visible")
        spes_corr = st.number_input('SPESE - Altre spese correnti - in % PIL', min_value=0, max_value=100, value=3, label_visibility="visible")
        int_pass=st.number_input('SPESE - Interessi Passivi - in % PIL', min_value=0, max_value=100, value=4, label_visibility="visible")
        spes_cc=st.number_input('SPESE - Totale spese in conto capitale - in % PIL', min_value=0, max_value=100, value=3, label_visibility="visible")
        ent_dir=st.number_input('ENTRATE - Entrate dirette - in % PIL', min_value=0, max_value=100, value=15, label_visibility="visible")
        ent_indir=st.number_input('ENTRATE - Entrate indirette - in % PIL', min_value=0, max_value=100, value=15, label_visibility="visible")
        ent_incc=st.number_input('ENTRATE - Entrate in conto capitale - in % PIL', min_value=0, max_value=100, value=0, label_visibility="visible")
        contr=st.number_input('ENTRATE - Contributi - in % PIL', min_value=0, max_value=100, value=15, label_visibility="visible")
        ae=st.number_input('ENTRATE - Altre Entrate - in % PIL', min_value=0, max_value=100, value=4, label_visibility="visible")
        aent=st.number_input('ENTRATE - Altre Entrate Non Tributarie - in % PIL', min_value=0, max_value=100, value=1, label_visibility="visible")


    df_def['Redditi da lavoro dipendente'] = df_def['Stima pil RGS'] * redditi/100
    df_def['Consumi_intermedi'] = df_def['Stima pil RGS'] * Consumi_intermedi/100
    df_def['Altre prestazioni sociali'] = df_def['Stima pil RGS'] * prest_social/100
    df_def['Spesa pensionistica'] = (df_def['Spesa pensionistica/PIL'] - taglio) * df_def['Stima pil RGS'] / 100
    df_def['Altre spese correnti'] = df_def['Stima pil RGS'] * spes_corr/100
    df_def['Interessi passivi'] = df_def['Stima pil RGS'] * int_pass/100
    df_def['Totale spese in conto capitale'] = df_def['Stima pil RGS'] * spes_cc/100

    df_def['Spese'] = df_def['Spesa pensionistica'] + df_def['Totale spese in conto capitale'] + df_def[
        'Altre spese correnti'] + df_def['Interessi passivi'] + df_def['Redditi da lavoro dipendente'] + df_def[
                            'Redditi da lavoro dipendente'] + df_def['Altre prestazioni sociali'] + df_def[
                            'Consumi_intermedi']

    df_def['Entrate dirette'] = df_def['Stima pil RGS'] * ent_dir/100
    df_def['Entrate indirette'] = df_def['Stima pil RGS'] * ent_indir/100
    df_def['Entrate in conto capitale'] = df_def['Stima pil RGS'] * ent_incc/100
    df_def['Entrate contributi'] = df_def['Stima pil RGS'] * contr/100
    df_def['Entrate altre'] = df_def['Stima pil RGS'] * ae/100
    df_def['Entrate altre non tributarie'] = df_def['Stima pil RGS'] * aent/100
    df_def['Entrate'] = df_def['Entrate dirette'] + df_def['Entrate indirette'] + df_def[
        'Entrate in conto capitale'] + df_def['Entrate contributi'] + df_def['Entrate altre'] + df_def[
                            'Entrate altre non tributarie']

    df_def['Indebitamento netto'] = df_def['Entrate'] - df_def['Spese']
    df_def['Debito'] = - df_def['Indebitamento netto'].cumsum() + df_def.loc[0, 'Stima pil RGS'] * debpil / 100
    df_def['Spese con nucleare'] = df_def['Spese'] + df_def['Quote']
    df_def['Entrate con nucleare'] = df_def['Entrate'] + df_def['PIL aggiuntivo nucleare'] * (ent_dir+ent_indir+ent_incc+contr)/100
    df_def['Indebitamento netto con nucleare'] = df_def['Entrate con nucleare'] - df_def['Spese con nucleare']

    df_def['Debito con nucleare'] = - df_def['Indebitamento netto con nucleare'].cumsum() + df_def.loc[
        0, 'Stima pil RGS'] * debpil / 100

    # Calcola il rapporto debito/PIL e debito nucleare/PIL per ogni anno
    rapporto_debito_pil = df_def['Debito'] / df_def['Stima pil RGS']
    rapporto_debito_nucleare_pil = df_def['Debito con nucleare'] / df_def['PIL modello nucleare']

    # Creare le tracce per il grafico a linee
    trace1 = go.Scatter(x=df_def['Anno'], y=rapporto_debito_pil, mode='lines',
                        name='RGS - SCENARIO NAZIONALE BASE', marker=dict(color='#FF0000'))
    trace2 = go.Scatter(x=df_def['Anno'], y=rapporto_debito_nucleare_pil, mode='lines',
                        name='STIMA MODELLO NUCLEARE', marker=dict(color='#1A76FF'))

    # Creare il layout del grafico
    layout = go.Layout(
        title='Andamento del rapporto Debito / PIL, confronto fra <br> <span style="color:#FF0000;">RGS - SCENARIO NAZIONALE BASE</span> e <span style="color:#1A76FF;">STIMA MODELLO NUCLEARE</span>',
        xaxis=dict(title='Anno'),
        yaxis=dict(title='Rapporto Debito/PIL'),
        showlegend=False
    )

    # Creare la figura
    fig = go.Figure(data=[trace1, trace2], layout=layout)

    # Mostrare il grafico
    st.plotly_chart(fig)

    # Creare le tracce per il grafico a linee
    trace1 = go.Scatter(x=df_def['Anno'], y=df_def['Stima crescita pil RGS'], mode='lines',
                        name='RGS - SCENARIO NAZIONALE BASE', marker=dict(color='#FF0000'))
    trace2 = go.Scatter(x=df_def['Anno'], y=df_def['Stima crescita pil Nucleare'], mode='lines',
                        name='STIMA MODELLO NUCLEARE', marker=dict(color='#1A76FF'))

    # Creare il layout del grafico
    layout = go.Layout(
        title='Andamento crescita del PIL, confronto fra <br> <span style="color:#FF0000;">RGS - SCENARIO NAZIONALE BASE</span> e <span style="color:#1A76FF;">STIMA MODELLO NUCLEARE</span>',
        xaxis=dict(title='Anno'),
        yaxis=dict(title='Stima Crescita PIL'),
        showlegend=False
    )

    # Creare la figura
    fig = go.Figure(data=[trace1, trace2], layout=layout)

    # Mostrare il grafico
    st.plotly_chart(fig)

    # Creare le tracce per il grafico a linee
    trace1 = go.Scatter(x=df_def['Anno'], y=df_def['Indebitamento netto'] / df_def['Stima pil RGS'] * 100,
                        mode='lines', name='RGS - SCENARIO NAZIONALE BASE', marker=dict(color='#FF0000'))
    trace2 = go.Scatter(x=df_def['Anno'],
                        y=df_def['Indebitamento netto con nucleare'] / df_def['PIL modello nucleare'] * 100,
                        mode='lines', name='STIMA MODELLO NUCLEARE', marker=dict(color='#1A76FF'))

    # Creare il layout del grafico
    layout = go.Layout(
        title='Andamento Indebitamento Netto in rapporto al PIL, confronto fra <br> <span style="color:#FF0000;">RGS - SCENARIO NAZIONALE BASE</span> e <span style="color:#1A76FF;">STIMA MODELLO NUCLEARE</span>',
        xaxis=dict(title='Anno'),
        yaxis=dict(title='Indebitamento Netto'),
        showlegend=False
    )

    # Creare la figura
    fig = go.Figure(data=[trace1, trace2], layout=layout)
    # Mostrare il grafico
    st.plotly_chart(fig)

    a=st.toggle('Grafici Cumulati',value=False)

    if a==False:



        trace1 = go.Scatter(x=df_def['Anno'], y=df_def['Numero costruttori nucleare'], mode='lines',
                            name='Numero costruttori nucleare', line=dict(color="#cc6100"))
        trace2 = go.Scatter(x=df_def['Anno'], y=df_def['Numero addetti indiretti nucleare'], mode='lines',
                            name='Numero addetti indiretti nucleare', line=dict(color="#a34372"))
        trace3 = go.Scatter(x=df_def['Anno'], y=df_def['Numero addetti ope nucleare'], mode='lines',
                            name='Numero addetti operatività nucleare', line=dict(color="#74ba45"))
        trace4 = go.Scatter(x=df_def['Anno'], y=df_def['Numero addetti indotti nucleare'], mode='lines',
                            name='Numero addetti indotti nucleare',
                            line=dict(color="#9d9d34"))  # Nuova traccia per gli indotti

        # Creare il layout del grafico, includendo il titolo personalizzato e rimuovendo la legenda
        layout = go.Layout(
            title=f'Occupazione nucleare scomposta in <br> <span style="color:#cc6100;">costruttori nucleare</span>, <span style="color:#a34372;">addetti indiretti nucleare</span>, <span style="color:#74ba45;">addetti diretti nucleare</span>, e <span style="color:#9d9d34;">addetti indotti nucleare</span>',
            xaxis=dict(title='Anno'),
            yaxis=dict(title='N° Occupati'),
            showlegend=False  # Rimuove la legenda
        )

        # Creare la figura aggiungendo tutte le tracce
        fig = go.Figure(data=[trace1, trace2, trace3, trace4], layout=layout)
        st.plotly_chart(fig)

        # Creare le tracce per il grafico a linee
        trace1 = go.Scatter(x=df_def['Anno'], y=df_def['PIL aggiuntivo nucleare'],
                            mode='lines', name='PIL aggiuntivo nucleare', marker=dict(color='#1A76FF'))
        trace2 = go.Scatter(x=df_def['Anno'],
                            y=df_def['Quote'],
                            mode='lines', name='Costo annuale', marker=dict(color='#FF0000'))

        # Creare il layout del grafico
        layout = go.Layout(
            title='Confronto fra <br> <span style="color:#FF0000;">Uscite cumulate</span> e <span style="color:#1A76FF;">PIL aggiuntivo modello nucleare</span>',
            xaxis=dict(title='Anno'),
            yaxis=dict(title='Dati in €'),
            showlegend=False
        )

        # Creare la figura
        fig = go.Figure(data=[trace1, trace2], layout=layout)

        # Mostrare il grafico
        st.plotly_chart(fig)

    if a==True:
        trace1 = go.Scatter(x=df_def['Anno'], y=df_def['Numero costruttori nucleare'].cumsum(), mode='lines',
                            name='Numero costruttori nucleare', line=dict(color="#cc6100"))
        trace2 = go.Scatter(x=df_def['Anno'], y=df_def['Numero addetti indiretti nucleare'].cumsum(), mode='lines',
                            name='Numero addetti indiretti nucleare', line=dict(color="#a34372"))
        trace3 = go.Scatter(x=df_def['Anno'], y=df_def['Numero addetti ope nucleare'].cumsum(), mode='lines',
                            name='Numero addetti operatività nucleare', line=dict(color="#74ba45"))
        trace4 = go.Scatter(x=df_def['Anno'], y=df_def['Numero addetti indotti nucleare'].cumsum(), mode='lines',
                            name='Numero addetti indotti nucleare',
                            line=dict(color="#9d9d34"))  # Nuova traccia per gli indotti

        # Creare il layout del grafico, includendo il titolo personalizzato e rimuovendo la legenda
        layout = go.Layout(
            title=f'Occupazione nucleare scomposta in <br> <span style="color:#cc6100;">costruttori nucleare</span>, <span style="color:#a34372;">addetti indiretti nucleare</span>, <span style="color:#74ba45;">addetti diretti nucleare</span>, e <span style="color:#9d9d34;">addetti indotti nucleare</span>',
            xaxis=dict(title='Anno'),
            yaxis=dict(title='N° Occupati'),
            showlegend=False  # Rimuove la legenda
        )

        # Creare la figura aggiungendo tutte le tracce
        fig = go.Figure(data=[trace1, trace2, trace3, trace4], layout=layout)
        st.plotly_chart(fig)

        # Creare le tracce per il grafico a linee
        trace1 = go.Scatter(x=df_def['Anno'], y=df_def['PIL aggiuntivo nucleare'].cumsum(),
                            mode='lines', name='PIL aggiuntivo nucleare', marker=dict(color='#1A76FF'))
        trace2 = go.Scatter(x=df_def['Anno'],
                            y=df_def['Quote'].cumsum(),
                            mode='lines', name='Costo annuale', marker=dict(color='#FF0000'))

        # Creare il layout del grafico
        layout = go.Layout(
            title='Confronto fra <br> <span style="color:#FF0000;">Costi Totali</span> e <span style="color:#1A76FF;">PIL aggiuntivo modello nucleare</span>',
            xaxis=dict(title='Anno'),
            yaxis=dict(title='Dati in €'),
            showlegend=False
        )

        # Creare la figura
        fig = go.Figure(data=[trace1, trace2], layout=layout)

        # Mostrare il grafico
        st.plotly_chart(fig)

    # Definizione del testo con le formule LaTeX
    latex_text = r"""
    La formula per calcolare il costo dell'operazione in base al tasso di interesse e al tempo di realizzazione è:

    $$
    costo\_opera = co \times (1 + i)^t
    $$

    dove:
    - $costo\_opera$ è il costo dell'operazione,
    - $co$ è il costo overnight,
    - $i$ è il tasso di interesse,
    - $t$ è il tempo di realizzazione.

    La formula per calcolare il tempo di realizzazione di un progetto in base al tasso di apprendimento è:

    $$
    tempo = t \times (1 - apprendimento)^p
    $$

    dove:
    - $tempo$ è il tempo di realizzazione del progetto,
    - $t$ è il tempo di realizzazione del FOAK (First-of-A-Kind),
    - $apprendimento$ è il tasso di apprendimento,
    - $p$ è il numero di progetti realizzati.

    La formula per calcolare il costo overnight di un progetto in base al tasso di apprendimento è:

    $$
    costo overnight = co FOAK \times (1 - apprendimento)^p
    $$

    dove:
    - $co FOAK$ è il costo overnight del FOAK (First-of-A-Kind),
    - $apprendimento$ è il tasso di apprendimento,
    - $p$ è il numero di progetti realizzati.



    La formula per calcolare il valore aggiunto per occupato è:

    $$
    valore\_aggiunto = occupati \times valore\_aggiunto\_per\_occupato
    $$

    dove:
    - $valore\_aggiunto$ è il valore aggiunto,
    - $occupati$ è il numero di occupati,
    - $valore\_aggiunto\_per\_occupato$ è il valore aggiunto per occupato.

    La formula per calcolare il PIL in base al valore aggiunto e al numero di occupati è:

    $$
    PIL = valore\_aggiunto \times occupati
    $$

    dove:
    - $PIL$ è il Prodotto Interno Lordo,
    - $valore\_aggiunto$ è il valore aggiunto,
    - $occupati$ è il numero di occupati.

    La formula per calcolare il PIL aggiuntivo del progetto nucleare è:

    $$
    PILn = VAnd \times Ond + VAni \times Oni+ VAnc \times Onc
    $$

    dove:
    - $PILn$ è il Prodotto Interno Lordo generato dal nucleare,
    - $VAnd$ è il valore aggiunto del singolo occupato diretto nel progetto nucleare,
    - $VAni$ è il valore aggiunto del singolo occupato indiretto nel progetto nucleare,
    - $VAnc$ è il valore aggiunto del singolo occupato nella fase di costruzione del progetto nucleare,
    - $Ond$ è il numero di occupati diretti nel progetto nucleare,
    - $Oni$ è il numero di occupati indiretti nel progetto nucleare,
    - $Onc$ è il numero di occupati nella fase di costuzione del progetto nucleare,
    """

    # Utilizzo di st.markdown() per renderizzare il testo formattato in Markdown

    with st.expander("Come abbiamo fatto i conti"):
        st.markdown(latex_text, unsafe_allow_html=True)
