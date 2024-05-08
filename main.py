# hey, dico a te, con il ditino, so che sei più bravo di noi a programmare, quindi perchè non fai un bel fork e ci aiuti?
# (vale anche per chi ha obiezoni o consigli per migliorare la parte puramente modellistica)

# https://c.xkcd.com/random/comic/


import pandas as pd
import streamlit as st
import streamlit.components.v1 as components
import plotly.graph_objs as go
import os
import yaml


# funzione per caricare gli scenari dal file YAML
def carica_scenari_da_yaml(percorso_file):
    with open(percorso_file, 'r') as file:
        dati = yaml.safe_load(file)
    return dati['scenari']


# determinazione del percorso del file YAML rispetto al percorso di questo script
percorso_file_yaml = os.path.join(os.path.dirname(__file__), 'scenari.yml')

# import degli scenari
scenari = carica_scenari_da_yaml(percorso_file_yaml)

st.title("Il modello più semplicistico per un'analisi dell'impatto economico-finanziario di un programma energetico nucleare")

st.header('Nuclear is :blue[cool] :sunglasses:', divider='rainbow')

st.write("Questa app è stata creata da [Umberto Bertonelli](https://umbertobertonelli.it) con il gentilissimo supporto di [Comitato Nucleare e Ragione](https://www.instagram.com/nucleareeragione/).")

st.write("La documentazione completa è disponibile [qui](https://github.com/DrElegantia/nucleare_costi/tree/main).")
st.divider()

st.subheader('Nucleare: ma quanto ci costi?')

st.subheader('In Italia da qualche anno ormai si è tornati a parlare di energia nucleare, e spesso una delle domande (*lecite*) che viene posta al centro del dibattito è: :blue[***MA QUANTO CI COSTA?***]')

st.markdown("**A questa domanda, vengono poste diverse risposte:**")

st.markdown(" - Costa troppo.")
st.markdown(" - Se l'energia nucleare fosse incentivata come le rinnovabili costerebbe di meno")
st.markdown(" - Costa comunque di meno di un mix energetico 100% rinnovabile.")
st.markdown( "- Il costo iniziale per un reattore nucleare sarebbe elevato, ma nel lungo periodo risultarebbe vantaggioso in termini di riduzione dei costi energetici.")
st.markdown( "- Le tecnologie nucleari stanno evolvendo, e ci sono progetti per reattori più sicuri ed economicamente sostenibili.")
st.markdown(" - Essendo l'energia nucleare una fonte energetica programmabile a basse emissioni di gas serra non ha senso confrontare i suoi costi con quelli di altre fonti non programmabili oppure con quelle fossili.")
st.markdown(" - Il costo per i rifiuti ed il rischio di incidente è troppo alto.")

st.markdown("Chiaramente queste non sono le uniche risposte!")

st.markdown("Essendo che il costo del nucleare, come ogni fonte energetica ed opera pubblica, dipende da molti fattori, abbiamo provato a rispondere diversamente, con qualche dato alla mano!")

st.markdown("**In particolare questo applicativo ha lo scopo di stimare l'impatto sui conti pubblici e sulle variabili macroeconomiche italiane di un programma energetico nucleare finanziato interamente con soldi pubblici, anche se i risultati possono essere interpretati in modo più generale.**")
st.markdown("Fare una stima diretta del costo dell'energia (elettricità) prodotta o di un certo mix energetico non è, quindi, lo scopo di questo applicativo. Per fare questo sarebbe necessario eseguire un altro tipo di [Modellazione e simulazione di scenari](https://en.wikipedia.org/wiki/Energy_modeling). Per maggiori informazioni si veda la [Nota 1]", unsafe_allow_html=True)

st.write("La potenza di ogni reattore non influisce direttamente sui risultati del modello")
st.write("È possibile cambiare il numero totale di reattori costruiti nel programma nel suo complesso.")

st.write("""Tuttavia, non sono modificabili né l'anno di partenza (2026) né il numero di reattori costruiti all'anno, che rimane 1 a prescindere dal numero di reattori totali (eccetto nello **"scenario SMR"** in cui sono 3 reattori all'anno).""")

# testo formattato con Markdown e LaTeX
latex_parametri = r"""
**I parametri che, invece, determinano il costo di costruzione per il reattore k-esimo sono:**

- **k:** il numero del reattore, ossia quanti reattori del programma sono già stati completati oppure sono in costruzione.
- **Costo Overnight FOAK (First-Of-A-Kind):** Il costo per la costruzione del primo di reattore. Con "costo overnight" si intende il costo di costruzione escludendo gli effetti finanziari (come ad esempio il costo degli interessi per il debito o il prestito). Le componenti principali sono: i costi diretti per la costruzione (materiali, componenti, attrezzature, manodopera), i costi di pre-costruzione (preparazione del sito, sviluppo e licenza del reattore) ed altri costi indiretti (costi amministrativi vari).
- **Tempo di Costruzione FOAK:** La durata necessaria per completare la costruzione del primo reattore.
- **Tasso di Interesse:** Il costo del capitale impiegato nella costruzione del reattore, che influisce sui costi finanziari totali.
- **Tasso di Apprendimento:** La riduzione dei costi e dei tempi dovuta all'esperienza acquisita nella costruzione dei reattori precedenti.

Per non complicare eccessivamente il modello si assume che per ogni reattore la **distribuzione del Costo Overnight** sui T Anni di Costruzione sia uniforme su tutto il periodo:

$$costo\_annuale_k = \frac{costo\_overnight_k}{T_k}$$

Il costo overnight ed il tempo di costruzione per il **reattore k-esimo** sono calcolati in funzione del corrispondente valore per il primo reattore (FOAK) opportunamente ridotto in base ad un **parametro di apprendimento** e a *k*. In modo più formale questa relazione può essere scritta come:

$$y_k = f(y_{FOAK}, k; \theta)$$

Infine per trovare il costo capitale totale (CAPEX) per il reattore k-esimo al costo overnight trovato viene aggiunto il **costo per il finanziamento**. Il debito fatto per il costo overnight inizia ad essere ripagato una volta finito di costruire il reattore quindi gli interessi sul debito all'anno *t* saranno pagati per tutto il costo del reattore sostenuto fino a quel momento:

$$\text{interessi\_overnight}_{t,k} = costo\_annuale_k \times t$$

Per quanto riguarda il **pagamento degli interessi** sono considerate due differenti modalità: Lineare o Composta. In questo modello queste due modalità possono essere interpretate facendo riferimento al saldo complessivo dello stato:

- se è in avanzo può ripagare gli interessi di anno in anno e questi non generano altro debito (**calcolo lineare**);
- se è in deficit allora gli interessi dovuti genereranno altro debito, su cui andranno pagati altri interessi (**calcolo composto**).

I costi operativi e di mantenimento (OPEX) e per il decommissioning non sono stati considerati, anche perché influiscono in modo marginale il costo totale di un reattore.

Per maggiori dettagli e spiegazioni sulla **metodologia di calcolo** si veda la [Nota 2]
"""

st.markdown(latex_parametri, unsafe_allow_html=True)

## descrizione per impatti economici
st.markdown("Per stimare gli impatti macroeconomici, abbiamo considerato lo scenario base de [***LE TENDENZE DI MEDIO-LUNGO PERIODO DEL SISTEMA PENSIONISTICO E SOCIO-SANITARIO – AGGIORNAMENTO 2023***](https://www.rgs.mef.gov.it/_Documenti/VERSIONE-I/Attivit--i/Spesa-soci/Attivita_di_previsione_RGS/2023/Rapporto-2023.pdf#page=473) realizzato dalla Ragioneria Generale dello Stato.")

st.markdown("Per la stima del PIL, abbiamo adottato la metodologia illustrata dall'Ufficio Parlamentare di Bilancio in occasione del report [***Cambiamenti nelle proiezioni di medio-lungo periodo della spesa pensionistica in Italia***](https://www.upbilancio.it/wp-content/uploads/2020/10/Flash-2_2020.pdf).")

st.markdown("Per la stima della finanza pubblica, abbiamo usato i dati realtivi alla voci di entrata e alla voci di uscita in rapporto al pil presentati in [NADEF 2023](https://www.dt.mef.gov.it/export/sites/sitodt/modules/documenti_it/analisi_progammazione/documenti_programmatici/nadef_2023/NADEF-2023.pdf#page=75), adottando alcuni accorgimento al fine di ricalcare quanto previsto dal [FMI](https://www.imf.org/en/Publications/CR/Issues/2022/07/28/Italy-2022-Article-IV-Consultation-Press-Release-Staff-Report-and-Statement-by-the-521484).")

st.markdown("Il PIL aggiuntivo realizzato con il nucleare, in accordo con il modello fornito da UPB, si basa sul prodotto fra occupati, dati dalla somma degli occupati nelle varie fasi di vita del reattore (costruzione e operatività) e dell'occupazione indotta e indiretta, e relativo valore aggiunto. Inoltre, abbiamo previsto la possibilità di determinare un aumento in termini percentuali della produttività del settore dell'industria. Per la stima dell'occupazione abbiamo preso a riferimento [***Measuring Employment Generated by the Nuclear Power Sector***](https://www.oecd-nea.org/jcms/pl_14912) prodotto da NEA")

st.write("**Siamo consci che il nostro modello, nonostante le possibilità di personalizzazione, soffra di molte limitazioni e semplificazioni, ad esempio:**")

st.markdown(" - La costruzione fissa di 1 reattore all'anno (3 per gli SMR)")
st.markdown(" - La mancanza di modellazione per le differenze fra reattori costruiti nella stessa centrale rispetto a quelli in siti diversi")
st.markdown("- La mancanza di considerazione per la variabilità dei costi e dei tempi che non sempre decrescono seguendo una funzione precisa di reattore in reattore")
st.markdown("- La stessa cosa vale per i tassi di interesse che non è detto rimangano fissi nel tempo e di progetto in progetto")
st.markdown(" - Come già detto [Nota 1] la mancata modellizzazione dell'intero mix elettrico e quindi del costo dell'elettricità (ed energia considerando anche potenziale calore per industrie e riscaldamenti)")
st.markdown(" - Più in generale la non considerazione del resto dell'infrastruttura energetica (reti, accumuli, altre infrastrutture di servizio ecc)")
st.markdown(" - I possibili ritardi accumulati dai progetti per impedimenti burocratici, sociali o di altra natura")
st.markdown("- Gli eventualli periodi recessivi futuri")
st.markdown(" - Eventuali altri impatti di finanza pubblica che compromettano le casse dello stato")
st.markdown("- In generale data la complessità dell'argomento manca la componente probabilistica degli scenari, non ci sono intervalli di confidenza ed ogni scenario è deterministico")

st.markdown("Tuttavia, il modello è utile per fornire una stima grossolana iniziale dei costi e del tempo di realizzazione di un progetto di energia nucleare, oltre che del suo impatto sulla finanza pubblica e le variabili macroeconomiche italiane.")

st.write("Se si vuole **approfondire il tema dell'energia nucleare** ed in particolare dei suoi costi e dello stato dei programmi nei vari paesi attraverso documenti e opinione di esperti, qui trovate un'intervista al prof. Jacopo Buongiorno, Direttore del Centro per i sistemi avanzati di energia nucleare al MIT. Inoltre, in descrizione al video abbiamo lasciato ulteriori documenti, paper ed analisi utili a contestualizzare il tema.")

# URL del video su YouTube con l'intervista a Buongiorno
video_url = "https://youtu.be/FOqnCk1Uv7I"

# inclusione del video nella pagina rispettando le proporzioni della copertina originale
video_embed_code = f"""
<div style="position:relative;padding-bottom:56.25%;height:0;">
    <iframe src="https://www.youtube.com/embed/{video_url.split('/')[-1]}" 
            style="position:absolute;top:0;left:0;width:100%;height:100%;" 
            frameborder="0" allowfullscreen></iframe>
</div>
"""
components.html(video_embed_code, height=315)

st.divider()

# controllo dei consensi
consenso1 = st.checkbox('Sono consapevole dei limiti del modello e ho compreso la natura del modello.')
consenso2 = st.checkbox('Sono consapevole che, come ogni modello, anche questo è errato.')
consenso3 = st.checkbox('Sono consapevole che le risposte del modello dipendono dalle ipotesi che io andrò a selezionare, oltre che dalla struttura dello stesso.')

if consenso1 and consenso2 and consenso3:
    modello = st.radio(
        "Che profilo vuoi impostare al tuo modello?",
        ["BEST CASE SCENARIO", "SCENARIO MEDIANO", "TASSI BASSI", "SUPER APPRENDIMENTO", "WORST CASE SCENARIO",'SMR', "PERSONALIZZA MODELLO"],
        help = "Selezionando un modello verranno valorizzati in modo automatico i vari parametri, questi saranno riportati nei singoli grafici. Se si preferisce valorizzare autonomamente i parametri è sufficiente selezionare l'opzione personalizza modello"
    )
    
    boolean_smr = modello == "SMR"

    # convertire gli spazi in underscore per corrispondere alle chiavi nel dizionario
    modello = modello.replace(" ", "_").upper()

    if modello is not None and modello in scenari:

        scenario = scenari[modello]

        # assegnazione dinamica di variabili
        for chiave, valore in scenario.items():
            # assegnazione di una variabile globale per ogni chiave del dizionario
            globals()[chiave] = valore
            # st.write(f"Variabili per lo scenario '{modello}':", scenario)

        # assegnazione diretta delle variabili dai valori del dizionario

    elif modello == "PERSONALIZZA_MODELLO":

        progetti = st.number_input(
            'Su quanti reattori vuoi basare il modello?',
            min_value = 1, max_value = 35, value = 26,
            help = "Il modello si basa sull'ipotesi che tutti i reattori appartengano allo stesso tipo."
        )

        costo_base = st.number_input(
            'A quanto stimi possa ammontare il costo overnight del FOAK? Dato espresso in miliardi di €.',
            min_value = 0.5, max_value = 20.0, value = 10.0,
            help = "Il costo overnight rappresenta il costo complessivo per realizzare il reattore, al netto del costo di finanziamento."
        )

        t = st.number_input(
            'In quanto tempo stimi venga realizzato il FOAK? Dato espresso in anni.',
            min_value = 4, max_value = 30, value = 12,
            help = "Il tempo dei successivi reattori è dato dal tempo del FOAK e dal tasso di apprendimento."
        )
        
        i = st.number_input(
            'Che tasso di  interesse prevedi per il costo del finanziamento? Dato espresso in termini percentuali',
            min_value = 4.0, max_value = 20.0, value = 4.0,
            help = "Il tasso di interesse influenza il costo complessivo dell'operazione"
        )
        
        metodo_interessi = st.radio(
            'Vuoi che si utilizzi il metodo lineare o quello composto per il calcolo degli interessi?',
            ('Lineare', 'Composto'), index = 0,  # default Lineare
            help = "Lineare è più conservativo, si veda sopra o la [Nota 2] per i dettagli"
        )
        
        apprendimento = st.number_input(
            'A quanto stimi il tasso di apprendimento? Dato espresso in termini percentuali.',
            min_value = -10.0, max_value = 10.0, value = 3.0,
            help = "Il tasso di apprendimento stima la curva di apprendimento che si prevede avrà il progetto. Il tasso per il modello avrà effetto sia sul tempo di realizzazione che sul costo con pari entità. Se negativo, il tasso va ad aumentare tempi e costi di realizzazione."
        )

        partenza = 2026

        occupati_costruzione = st.number_input(
            f'A quanto ammonta la stima di occupati/anno per la costruzione del reattore? Dato in FTE.',
            min_value = 1000, max_value = 2500, value = 2200,
            help = "L'occupazione complessiva per la fase di costruzione è influenzata dai tempi di realizzazione del singolo reattore"
        )

        occupati_operativita = st.number_input(
            f"A quanto ammonta la stima di occupati/anno durante l'operativià del reattore? Dato in FTE.",
            min_value = 300, max_value = 900, value = 600,
            help = "L'occupazione complessiva durante l'operativià è influenzata dall'entrata in funzione del singolo reattore"
        )

        occupati_indiretti = st.number_input(
            f'A quanto ammonta la stima di occupati/anno indiretti rispetto agli occupati/anno diretti (costruzione + operatività)? Dato in termini percentuali',
            min_value = 0.0, max_value = 100.0, value = 33.0,
            help = "L'occupazione complessiva indiretta si riferisce alla catena del valore, pertanto è influenzata sia dagli occupati diretti."
        )

        occupati_indotto = st.number_input(
            f'A quanto ammonta la stima di occupati/anno indotti rispetto agli occupati/anno diretti e indiretti? Dato in termini percentuali.',
            min_value = 0.0, max_value = 100.0, value = 66.0,
            help = "L'occupazione complessiva indiretta si riferisce ai posti di lavoro indotti dall'industria dell'energia nucleare darivanti dal flusso circolare di reddito nell'economia nazionale, pertanto è influenzata sia dagli occupati diretti che dagli occupati indiretti."
        )

        pil_costruzione = st.number_input(
            f"A quanto ammonta la stima di valore aggiunto prodotto per ogni singolo occupato nella fase di costruzione del reattore rispetto alla media nazionale? Dato in termini percentuali.",
            min_value = -100.0, max_value = 100.0, value = 10.0
        )

        pil_diretti = st.number_input(
            f"A quanto ammonta la stima di valore aggiunto prodotto per ogni singolo occupato coinvolto nell'operatività del singolo reattore rispetto alla media nazionale? Dato in termini percentuali.",
            min_value = 0.0, max_value = 150.0, value = 100.0
        )

        pil_indiretti = st.number_input(
            f"A quanto ammonta la stima di valore aggiunto prodotto per ogni singolo occupato indiretto nel settore dell'energia nucleare rispetto alla media nazionale? Dato in termini percentuali.",
            min_value = -100.0, max_value = 100.0, value = 10.0
        )

        pil_indotto = st.number_input(
            f"A quanto ammonta la stima di valore aggiunto prodotto per ogni singolo occupato indotto dall'industria dell'energia nucleare rispetto alla media nazionale? Dato in termini percentuali.",
            min_value = -100.0, max_value = 100.0, value = -10.0
        )

        pil_eco = st.number_input(
            f"Alla fine del progetto, a quanto ammonta la variazione della produttività nel settore dell'industria ed energia grazie all'adozione dell'energia nucleare? Dato in termini percentuali.",
            min_value = 0.0, max_value = 100.0, value = 10.0,
            help = "Il PIL oltre ad aumentare per effetto dell'occupazione diretta e indiretta aggiuntiva, può aumentare a seguito della migliorata produttività dell'economia grazie al cambiamento tecnologico. Qui è possibile valorizzare un coefficiente che andrà a moltiplicare il valore aggiunto per occupato del settore dell'Industria, che pesa circa il 25% del PIL."
        )



    # Funzione per calcolare gli esborsi annuali per la costruzione di un reattore con opzione per interesse composto
    # @input i (float): Tasso di interesse annuo.
    # @input t (int): Durata totale della costruzione, espressa in anni.
    # @input overnight (float): Costo totale overnight del reattore.
    # @input anno_start (int): Anno di inizio della costruzione.
    # @input i_composto (bool): Se True, calcola l'interesse come composto, altrimenti come semplice.
    # @output df (pandas.DataFrame): DataFrame contenente colonne con l'anno,
    #                                il costo overnight, gli interessi ed il costo totale per ogni anno.

    def costo_opera(i, t, overnight, anno_start, i_composto=True):
        dati = {
            'anno': [],
            'costo_overnight_anno': [],
            'costo_interessi_anno': [],
            'costo_totale_anno': []
        }

        costo_annuale = overnight / t
        # capitale accumulato a t=0 per il calcolo con interesse composto
        capitale_precedente = 0
        # lista per accumulare interessi se non composti
        interessi_cumulativi = [0] * t 

        for anno in range(1, t + 1): # anno indica il tempo trascorso dall'inizio della costruzione
            if i_composto: # calcolo con interesse composto
                capitale_accumulato = capitale_precedente + costo_annuale
                interessi = capitale_accumulato * i 
                # aggiornamento del capitale
                capitale_precedente = capitale_accumulato + interessi 
            else: # calcolo con interesse lineare
                # gli interessi sono pagati per ogni costo overnight sostenuto negli anni precedenti
                interessi = anno * costo_annuale * i

            # anno di riferimento
            dati['anno'].append(anno_start + anno - 1)
            dati['costo_overnight_anno'].append(costo_annuale)
            dati['costo_interessi_anno'].append(interessi)
            dati['costo_totale_anno'].append(costo_annuale + interessi)  
        
        df = pd.DataFrame(dati)
        return df


    # conversione in miliardi
    # costo_base = costo_base * 1000000000
    
    ## tutti i costi saranno espressi in miliardi
    
    # conversione in %
    apprendimento = apprendimento / 100
    i = i / 100
    
    # true se è stato selezionato il metodo per gli interessi composti
    boolean_i = (metodo_interessi == "composto")
    # testo per i titoli nei crafici
    metodo_interessi_titolo = "composti" if boolean_i else "lineari"
    
    # anno di partenza
    anno_start = partenza

    # numero di reattori da costruire all'anno
    reattori_per_anno = 3 if boolean_smr else 1
    
    # lista per i dataframe ottenuti da costo_opera con i costi annuali per ogni reattore
    df_list = []
    
    # riempimento lista con gli n progetti
    for p in range(progetti // reattori_per_anno):

        # ciclo per costruire i reattori necessari per l'anno corrente
        for k in range(reattori_per_anno):
            # calcolo del tempo e del costo per il progetto corrente aggiornando per l'apprendimento
            # viene impostata una riduzione massima del 70% rispetto al FOAK
            # per gli SMR c'è apprendimento anche fra i 3 reattori dello stesso anno
            tempo = round(t * max((1 - apprendimento) ** (p * reattori_per_anno + k), 0.3))
            costo = costo_base * max((1 - apprendimento) ** (p * reattori_per_anno + k), 0.3)

            # calcolo dei costi per il progetto corrente utilizzando costo_opera
            df_progetto = costo_opera(i, tempo, costo, anno_start, boolean_i)

            df_list.append(df_progetto)

        # aggiornamento dell'anno di partenza per il prossimo progetto
        anno_start += 1


    # funzione per aggregare i costi dei progetti con due modalità: "reattore" e "anno".
    # @input df_list (list): lista di dataframe (da output funzione costo_opera) contenenti i costi annuali per ogni reattore.
    # @input group_by (str): modalità di aggregazione, "reattore" o "anno".
    # @output df_reattori o df_anni (pandas.DataFrame):
    #          - df_reattori: dataframe con colonne tempo, costo_totale, costo_overnight, costo_interessi.
    #          - df_anni: dataframe con colonne anno, costo_totale, costo_overnight, costo_interessi, reattori_finiti e reattori_in_costruzione.
    
    def costo_progetto(df_list, group_by):
        if group_by == "reattore":
            # inizializzazione del dataframe con le colonne specifiche
            df_reattori = pd.DataFrame(columns=['tempo', 'costo_totale', 'costo_overnight', 'costo_interessi'])

            # iterazione attraverso i dataframe per ogni reattore e calcolo dei valori aggregati
            for idx, df in enumerate(df_list, start=1):
                # calcolo del tempo di costruzione come lunghezza del dataframe
                tempo = len(df)
                costo_totale = df['costo_totale_anno'].sum()
                costo_overnight = df['costo_overnight_anno'].sum()
                costo_interessi = df['costo_interessi_anno'].sum()
                # aggiunta al dataframe della nuova riga creata
                df_reattori.loc[idx] = [tempo, costo_totale, costo_overnight, costo_interessi]

            return df_reattori

        elif group_by == "anno":
            # concatenazione dei dataframe in uno unico
            df_concatenato = pd.concat(df_list, ignore_index = True)

            # calcolo dell'anno di completamento di ciascun reattore
            reattori_finiti = [df['anno'].max() for df in df_list]

            # aggregazione per anno dei costi totali, per overnight e per interessi
            df_anni = df_concatenato.groupby('anno').agg({
                'costo_totale_anno': 'sum',
                'costo_overnight_anno': 'sum',
                'costo_interessi_anno': 'sum'
            }).reset_index()

            # nuovi nomi delle colonne
            df_anni.columns = ['anno', 'costo_totale', 'costo_overnight', 'costo_interessi']

            # aggiunta delle colonne reattori_finiti e reattori_in_costruzione
            df_anni['reattori_finiti'] = df_anni['anno'].apply(lambda anno: sum([1 for fine in reattori_finiti if fine <= anno]))
            df_anni['reattori_in_costruzione'] = df_concatenato.groupby('anno').size().values

            return df_anni


    df_reattori = costo_progetto(group_by = "reattore", df_list= df_list)
    df_anni = costo_progetto(group_by = "anno", df_list= df_list)

    ## grafico con barre per reattore

    # incrementare l'indice di 1 per farlo partire da 1
    x_values_reattori = df_reattori.index + 1
    # aggiunta del costo totale come popup
    custom_data_reattori = df_reattori[['costo_totale']].values  
    
    # tracce per il grafico a barre
    trace1_reattori = go.Bar(
        x = x_values_reattori,
        y = df_reattori['costo_overnight'],
        name = 'Costi overnight: ',
        marker = dict(color = '#1A76FF'),
        customdata = custom_data_reattori,
        hoverinfo = 'skip'
    )

    trace2_reattori = go.Bar(
        x = x_values_reattori,
        y = df_reattori['costo_interessi'],
        name = 'Costi di finanziamento: ',
        marker = dict(color = '#84C9FF'),
        customdata = custom_data_reattori,
        hoverinfo = 'skip'
    )

    # creazione del grafico
    layout_reattori = go.Layout(
        title = "Costo dell'n-esimo reattore scomposto in <span style = 'color:#1A76FF;'>OVERNIGHT</span> e <span style = 'color:#84C9FF;'>DI FINANZIAMENTO</span>",
        xaxis = dict(title = 'Progetto realizzato'),
        yaxis = dict(title = 'Miliardi di €'),
        barmode = 'stack',
        showlegend = False,
        annotations = [
            dict(
                text = (
                    f"Costo medio di 1 reattore: {df_reattori['costo_totale'].mean():.3f} mld €<br>"
                    f"<span style = 'font-size:10px;'>Ipotesi: interessi = {i * 100:.2f}% ({metodo_interessi_titolo}), apprendimento = {apprendimento * 100:.2f}%, tempo FOAK = {t} anni, overnight FOAK = {costo_base:.3f} mld €</span>"
                ),
                xref = 'paper', yref = 'paper', x = 0, y = 1.05, # posizione rispetto al grafico
                align = 'left', xanchor = 'left', yanchor = 'bottom',  # allineamento
                showarrow = False, font = dict(size = 12)
            )
        ]
    )

    fig_reattori = go.Figure(data = [trace1_reattori, trace2_reattori], layout = layout_reattori)

    # personalizzare le informazioni visualizzate al passaggio del mouse
    fig_reattori.update_traces(
        hovertemplate = (
            "<b>Reattore numero %{x}:</b><br>"
            "<span style = 'color:%{marker.color};'>%{fullData.name}</span>: %{y:.3f} mld €<br>"
            "Costo totale: %{customdata[0]:.3f} mld €"
        )
    )
    
    # per la visualizzazione del grafico
    st.plotly_chart(fig_reattori)


    ## grafico con barre per anno

    x_values_anni = df_anni['anno']
    # dati aggiuntivi come popup
    custom_data_anni = list(list(row) for row in zip(df_anni['costo_totale'], df_anni['reattori_finiti'], df_anni['reattori_in_costruzione']))

    trace1_anni = go.Bar(
        x = x_values_anni,
        y = df_anni['costo_overnight'],
        name = 'Costo overnight',
        marker = dict(color = '#1A76FF'),
        customdata = custom_data_anni,
        hoverinfo = 'skip'
    )
    trace2_anni = go.Bar(
        x = x_values_anni,
        y = df_anni['costo_interessi'],
        name = 'Costo di finanziamento',
        marker = dict(color = '#84C9FF'),
        customdata = custom_data_anni,
        hoverinfo = 'skip'
    )

    layout_anni = go.Layout(
        title = "Andamento delle spese annuali, scomposte in <span style = 'color:#1A76FF;'>OVERNIGHT</span> e <span style = 'color:#84C9FF;'>DI FINANZIAMENTO</span>",
        xaxis = dict(title = 'Anno'),
        yaxis = dict(title = 'Miliardi di €'),
        barmode = 'stack',
        showlegend = False,
        annotations = [
            dict(
                text = (
                    f"Spesa media annuale: {(df_anni['costo_totale'].mean()):.3f} mld €<br>"
                    f"<span style = 'font-size:10px;'>Ipotesi: interessi = {i * 100:.2f}% ({metodo_interessi_titolo}), apprendimento = {apprendimento * 100:.2f}%, tempo FOAK = {t} anni, overnight FOAK = {costo_base:.2f} mld €</span>"
                ),
                xref = 'paper', yref = 'paper', x = 0, y = 1.05,
                align = 'left', xanchor = 'left', yanchor = 'bottom',
                showarrow = False, font = dict(size = 10)
            )
        ]
    )

    fig_anni = go.Figure(data = [trace1_anni, trace2_anni], layout = layout_anni)

    fig_anni.update_traces(
        hovertemplate = (
            "<b>Anno %{x}:</b><br>"
            "<span style = 'color:%{marker.color};'>%{fullData.name}</span>: %{y:.3f} mld €<br>"
            "Costo totale: %{customdata[0]:.3f} mld €<br>"
            "Reattori finiti: %{customdata[1]}<br>"
            "Reattori in costruzione: %{customdata[2]}"
        )
    )

    st.plotly_chart(fig_anni)



    ## grafico con barre per anno, cumulativo

    x_values_anni_cum = df_anni['anno']
    custom_data_anni_cum = list(list(row) for row in zip(df_anni['costo_totale'].cumsum(), df_anni['reattori_finiti'], df_anni['reattori_in_costruzione']))

    trace1_anni_cum = go.Bar(
        x = x_values_anni_cum,
        y = df_anni['costo_overnight'].cumsum(),
        name = 'Costo overnight cumulato',
        marker = dict(color = '#1A76FF'),
        customdata = custom_data_anni_cum,
        hoverinfo = 'skip'
    )
    trace2_anni_cum = go.Bar(
        x = x_values_anni_cum,
        y = df_anni['costo_interessi'].cumsum(),
        name = 'Costo di finanziamento cumulato',
        marker = dict(color = '#84C9FF'),
        customdata = custom_data_anni_cum,
        hoverinfo = 'skip'
    )

    layout_anni_cum = go.Layout(
        title = "Andamento della spesa cumulata, scomposta in <span style = 'color:#1A76FF;'>OVERNIGHT</span> e <span style = 'color:#84C9FF;'>DI FINANZIAMENTO</span>",
        xaxis = dict(title = 'Anno'),
        yaxis = dict(title = 'Miliardi di €'),
        barmode = 'stack',
        showlegend = False,
        annotations = [
            dict(
                text = (
                    f"Spesa complessiva: {(df_anni['costo_totale'].sum()):.3f} mld €<br>"
                    f"<span style = 'font-size:10px;'>Ipotesi: interessi = {i * 100:.2f}% ({metodo_interessi_titolo}), apprendimento = {apprendimento * 100:.2f}%, tempo FOAK = {t} anni, overnight FOAK = {costo_base:.2f} mld €</span>"
                ),
                xref = 'paper', yref = 'paper', x = 0, y = 1.05,
                align = 'left', xanchor = 'left', yanchor = 'bottom',
                showarrow = False, font = dict(size = 10)
            )
        ]
    )

    fig_anni_cum = go.Figure(data = [trace1_anni_cum, trace2_anni_cum], layout = layout_anni_cum)

    fig_anni_cum.update_traces(
        hovertemplate = (
            "<b>Fino all'anno %{x}:</b><br>"
            "<span style = 'color:%{marker.color};'>%{fullData.name}</span>: %{y:.3f} mld €<br>"
            "Costo totale cumulato: %{customdata[0]:.3f} mld €<br>"
            "Reattori finiti: %{customdata[1]}<br>"
            "Reattori in costruzione: %{customdata[2]}"
        )
    )

    st.plotly_chart(fig_anni_cum)



    ### parte economica

    # dati originali
    data_pop = {
        'Anno': [2015, 2020, 2025, 2030, 2035, 2040, 2045, 2050, 2055, 2060, 2065, 2070],
        'Popolazione [20-54]': [28.337, 26.753, 24.942, 23.533, 22.474, 21.683, 20.876, 20.167, 19.518, 18.862, 18.161, 17.547],
        'Popolazione [55-64]': [7.604, 8.431, 9.200, 9.373, 8.730, 7.647, 6.857, 6.563, 6.476, 6.491, 6.554, 6.393],
        'Popolazione totale': [60.295, 59.641, 58.560, 57.906, 57.185, 56.370, 55.395, 54.165, 52.630, 50.906, 49.213, 47.722],
        'PIL reale (mld di € 2015)': [1.655, 1.574, 1.809, 1.882, 1.939, 2.005, 2.076, 2.170, 2.279, 2.395, 2.508, 2.614],
        'Spesa pensionistica/PIL': [15.6, 16.9, 16.1, 16.4, 16.8, 17, 16.8, 16.1, 15.1, 14.4, 14.1, 14.1],
        'Numero di occupati': [22.121, 22.385, 23.737, 23.972, 23.597, 22.828, 21.891, 21.315, 20.951, 20.639, 20.269, 19.847],
        'tasso': [4.1, 3.5, 4.2, 5.5, 6.4, 6.9, 7.1, 7.2, 7.0, 6.8, 6.6, 6.4],
        'entrate': [47.8, 47.3, 47.6, 50, 50.5, 51, 51, 51, 51, 51, 50, 50]
    }

    popolazione = pd.DataFrame(data_pop)

    # calcolo della popolazione totale [20-64]
    popolazione['popolazione_20_64'] = popolazione['Popolazione [20-54]'] + popolazione['Popolazione [55-64]']

    # df con tutti gli anni desiderati
    anni_desiderati = pd.DataFrame({'Anno': range(2015, 2071)})

    # merge dei df per avere tutti gli anni con i relativi dati
    popolazione_anni_completi = pd.merge(anni_desiderati, popolazione, on='Anno', how='left')

    # riempimento dei vuoti interpolando i dati in modo lineare
    popolazione_anni_completi_interpolati = popolazione_anni_completi.interpolate(method='linear', axis=0)

    # preparazione del df finale per la popolazione
    pop = popolazione_anni_completi_interpolati
    pop['occupati_15-64'] = pop['Numero di occupati'] * 1e6
    pop['pil_per_occupato_15-64'] = (pop['PIL reale (mld di € 2015)'] * 1e12) / pop['occupati_15-64']

    # unione di df_anni con il df della popolazione
    df_anni = df_anni.merge(pop, left_on='anno', right_on='Anno', how='left')

    ## colonne aggiuntive al df_anni necessarie per gli impatti economici
    df_anni['Stima_pil_rgs'] = df_anni['pil_per_occupato_15-64'] * df_anni['occupati_15-64']
    
    # calcolo lavoratori aggiuntivi nello scenario nucleari
    df_anni['costruttori_nucleare'] = df_anni['reattori_in_costruzione'] * occupati_costruzione
    
    df_anni['operatori_nucleare'] = df_anni['reattori_finiti'] * occupati_operativita
   
    df_anni['addetti_indiretti_nucleare'] = (
        df_anni['costruttori_nucleare'] * occupati_indiretti / 100
        + df_anni['operatori_nucleare'] * occupati_indiretti / 100
    )
    
    df_anni['addetti_indotti_nucleare'] = (
        df_anni['costruttori_nucleare'] * occupati_indotto / 100
        + df_anni['operatori_nucleare'] * occupati_indotto / 100
        + df_anni['addetti_indiretti_nucleare'] * occupati_indotto / 100
    )

    # calcolo PIL per addetto aggiuntivo nello scenario nucleare
    df_anni['pil_per_costruttore_nucleare'] = (df_anni['costruttori_nucleare'] * (1 + pil_costruzione / 100) * df_anni['pil_per_occupato_15-64'])

    df_anni['pil_per_operatore_nucleare'] = (df_anni['operatori_nucleare'] * (1 + pil_diretti / 100) * df_anni['pil_per_occupato_15-64'])

    df_anni['pil_per_addetto_indiretto_nucleare'] = (df_anni['addetti_indiretti_nucleare'] * (1 + pil_indiretti / 100) * df_anni['pil_per_occupato_15-64'])

    df_anni['pil_per_addetto_indotto_nucleare'] = (df_anni['addetti_indotti_nucleare'] * (1 + pil_indotto / 100) * df_anni['pil_per_occupato_15-64'])

    # calcolo PIL aggiuntivo nello scenario nucleare
    df_anni['pil_aggiuntivo_nucleare'] = (
        df_anni['pil_per_costruttore_nucleare']
        + df_anni['pil_per_operatore_nucleare']
        + df_anni['pil_per_addetto_indiretto_nucleare']
        + df_anni['pil_per_addetto_indotto_nucleare']
    )

    df_anni['pil_modello_nucleare'] = (
        # PIL aggiuntivo dallo scenario nucleare fra lavoratori diretti, indiretti ed indotti
        df_anni['pil_aggiuntivo_nucleare']
        # PIL aggiuntivo per maggior produttività nel settore dell'industria ed energia grazie all'adozione dell'energia nucleare
        + df_anni['Stima_pil_rgs'] * (1 + pil_eco * df_anni['reattori_finiti'] / progetti * 0.20 / 100)
    )

    # crescita del PIL
    df_anni['stima_crescita_pil_RGS'] = (df_anni['Stima_pil_rgs'] / df_anni['Stima_pil_rgs'].shift(1) - 1) * 100
    df_anni['stima_crescita_pil_nucleare'] = (df_anni['pil_modello_nucleare'] / df_anni['pil_modello_nucleare'].shift(1) - 1) * 100


    ## grafico andamento PIL (confronto scenario nucleare vs senza)

    x_values_econ_pil = df_anni['anno']

    custom_data_econ_pil = list(zip(df_anni['reattori_finiti'], df_anni['reattori_in_costruzione']))

    trace1_econ_pil = go.Scatter(
        x = x_values_econ_pil,
        y = df_anni['pil_modello_nucleare'],
        mode = 'lines',
        name = 'PIL - Stima scenario Nucleare',
        marker = dict(color = '#1A76FF'),
        customdata = custom_data_econ_pil
    )

    trace2_econ_pil = go.Scatter(
        x = x_values_econ_pil,
        y = df_anni['Stima_pil_rgs'],
        mode = 'lines',
        name = 'PIL - Stima RGS - Scenario nazionale base',
        marker = dict(color = '#FF0000'),
        customdata = custom_data_econ_pil
    )

    layout_econ_pil = go.Layout(
        title = 'Andamento del PIL italiano, confronto fra <br> <span style="color:#FF0000;">RGS - SCENARIO NAZIONALE BASE</span> e <span style="color:#1A76FF;">STIMA SCENARIO NUCLEARE</span>',
        xaxis = dict(title = 'Anno'),
        yaxis = dict(title = 'Miliardi di €'),
        showlegend = False
    )

    fig_econ_pil = go.Figure(data = [trace2_econ_pil, trace1_econ_pil], layout = layout_econ_pil)

    fig_econ_pil.update_traces(hovertemplate = '%{x}: %{y:.2f} mld €<br>Reattori completati: %{customdata[0]}<br>Reattori in costruzione: %{customdata[1]}')

    st.plotly_chart(fig_econ_pil)
    

    ## domanda per modificare i dati dello scenario di base
    finanza = st.radio(
        "Vuoi modificare i dati di finanza pubblica?", ["No", "Sì"],
        help = "Esprimi i valori in rapporto al PIL"
    )

    if finanza == 'No':
        debpil = 139
        redditi = 8
        consumi_intermedi = 4
        prest_social = 4
        spes_corr = 3
        spes_cc = 3
        ent_dir = 15
        ent_indir = 15
        ent_incc = 0.1
        contr = 15
        rdp = 0.6
        ae = 4
        aent = 1
        taglio = 0

    if finanza == 'Sì':

        debpil = st.number_input('Rapporto debito PIL - in %', min_value = 0.0, max_value = 300.0, value = 139.0, label_visibility = "visible")
        redditi = st.number_input('SPESE - Redditi da lavoro dipendente - in % PIL', min_value = 0.0, max_value = 100.0, value = 8.0, label_visibility = "visible")
        consumi_intermedi = st.number_input('SPESE - Consumi Intermedi - in % PIL', min_value = 0.0, max_value = 100.0, value = 5.0, label_visibility = "visible")
        prest_social = st.number_input('SPESE - Altre prestazioni sociali - in % PIL', min_value = 0.0, max_value = 100.0, value = 5.0, label_visibility = "visible")
        spes_corr = st.number_input('SPESE - Altre spese correnti - in % PIL', min_value = 0.0, max_value = 100.0, value = 3.0, label_visibility = "visible")

        spes_cc = st.number_input('SPESE - Totale spese in conto capitale - in % PIL', min_value = 0.0, max_value = 100.0, value = 3.0, label_visibility = "visible")
        ent_dir = st.number_input('ENTRATE - Entrate dirette - in % PIL', min_value = 0.0, max_value = 100.0, value = 15.0, label_visibility = "visible")
        ent_indir = st.number_input('ENTRATE - Entrate indirette - in % PIL', min_value = 0.0, max_value = 100.0, value = 15.0, label_visibility = "visible")
        ent_incc = st.number_input('ENTRATE - Entrate in conto capitale - in % PIL', min_value = 0.0, max_value = 100.0, value = 0.0, label_visibility = "visible")
        contr = st.number_input('ENTRATE - Contributi - in % PIL', min_value = 0.0, max_value = 100.0, value = 15.0, label_visibility = "visible")
        rdp = st.number_input('ENTRATE - Redditi da proprietà - in % PIL', min_value = 0.0, max_value = 100.0, value = 0.6, label_visibility = "visible")
        ae = st.number_input('ENTRATE - Altre Entrate - in % PIL', min_value = 0.0, max_value = 100.0, value = 4.0, label_visibility = "visible")
        aent = st.number_input('ENTRATE - Altre Entrate Non Tributarie - in % PIL', min_value = 0.0, max_value = 100.0, value = 1.0, label_visibility = "visible")
        genre = st.radio(
            "Vuoi che il modello preveda un taglio della spesa pensionistica?",
            ["No", "dell'1% di pil", "del 2% del pil"],
            help='Sulla base delle stime RGS il modello calcola la spesa epnsionistica, è possibile ridurre il suo impatto sui conti pubblici di alcuni punti di pil attraverso la selezione.'
        )

        if genre == "No":
            taglio = 0
        elif genre == "dell'1% di pil":
            taglio = 1
        elif genre == "del 2% del pil":
            taglio = 2

    ## altre colonne aggiuntive al df_anni necessarie per gli impatti economici
    
    # calcolo delle spese
    df_anni['redditi_da_lavoro_dipendente'] = df_anni['Stima_pil_rgs'] * redditi / 100
    df_anni['consumi_intermedi'] = df_anni['Stima_pil_rgs'] * consumi_intermedi / 100
    df_anni['altre_prestazioni_sociali'] = df_anni['Stima_pil_rgs'] * prest_social / 100
    df_anni['spesa_pensionistica'] = (df_anni['Spesa_pensionistica/PIL'] - taglio) * df_anni['Stima_pil_rgs'] / 100
    df_anni['altre_spese_correnti'] = df_anni['Stima_pil_rgs'] * spes_corr / 100
    df_anni['interessi_passivi'] = df_anni['Stima_pil_rgs'] * df_anni['tasso'] / 100
    df_anni['spese_in_conto_capitale'] = df_anni['Stima_pil_rgs'] * spes_cc / 100

    df_anni['spese'] = (
        df_anni['spesa_pensionistica']
        + df_anni['spese_in_conto_capitale']
        + df_anni['altre_spese_correnti']
        + df_anni['interessi_passivi']
        + df_anni['redditi_da_lavoro_dipendente']
        + df_anni['consumi_intermedi']
        + df_anni['altre_prestazioni_sociali']
    )
    
    # calcolo delle entrate
    df_anni['entrate_dirette'] = df_anni['Stima_pil_rgs'] * ent_dir / 100
    df_anni['entrate_indirette'] = df_anni['Stima_pil_rgs'] * ent_indir / 100
    df_anni['entrate_in_conto_capitale'] = df_anni['Stima_pil_rgs'] * ent_incc / 100
    df_anni['entrate_contributi'] = df_anni['Stima_pil_rgs'] * contr / 100
    df_anni['entrate_altre'] = df_anni['Stima_pil_rgs'] * ae / 100
    df_anni['entrate_altre_non_tributarie'] = df_anni['Stima_pil_rgs'] * aent / 100
    df_anni['redditi_da_proprieta'] = df_anni['Stima_pil_rgs'] * rdp / 100

    df_anni['entrate'] = (
        df_anni['entrate_dirette']
        + df_anni['entrate_indirette']
        + df_anni['entrate_in_conto_capitale']
        + df_anni['entrate_contributi']
        + df_anni['entrate_altre']
        + df_anni['entrate_altre_non_tributarie']
        + df_anni['redditi_da_proprieta']
    )

    # ricalcolo delle entrate sulla base del valore aggiunto
    df_anni['entrate'] = df_anni['Stima_pil_rgs'] * df_anni['entrate'] / 100

    df_anni['indebitamento_netto'] = df_anni['entrate'] - df_anni['spese']
    df_anni['debito'] = - df_anni['indebitamento_netto'].cumsum() + df_anni.loc[0, 'Stima_pil_rgs'] * debpil / 100

    df_anni['spese_con_nucleare'] = df_anni['spese'] + df_anni['costo_totale']
    df_anni['entrate_con_nucleare'] = df_anni['entrate'] + df_anni['pil_aggiuntivo_nucleare'] * (ent_dir + ent_indir + ent_incc + contr) / 100
    df_anni['indebitamento_netto_con_nucleare'] = df_anni['entrate_con_nucleare'] - df_anni['spese_con_nucleare']

    df_anni['debito_con_nucleare'] = -df_anni['indebitamento_netto_con_nucleare'].cumsum() + df_anni.loc[0, 'Stima_pil_rgs'] * debpil / 100

    # calcolare il rapporto debito/PIL e debito nucleare/PIL per ogni anno
    rapporto_debito_pil = df_anni['debito'] / df_anni['Stima_pil_rgs']
    rapporto_debito_nucleare_pil = df_anni['debito_con_nucleare'] / df_anni['pil_modello_nucleare']


    ## grafico andamento debito/PIL (confronto scenario nucleare vs senza)

    x_values_econ_deb_pil = df_anni['anno']

    custom_data_econ_deb_pil = list(
        list(row) for row in zip(
            df_anni['debito'],
            df_anni['Stima_pil_rgs'],
            df_anni['reattori_finiti'],
            df_anni['reattori_in_costruzione']
        )
    )

    trace1_econ_deb_pil = go.Scatter(
        x = x_values_econ_deb_pil,
        y = rapporto_debito_pil,
        mode = 'lines',
        name = 'RGS - SCENARIO NAZIONALE BASE',
        marker = dict(color = '#FF0000'),
        customdata = custom_data_econ_deb_pil
    )
    trace2_econ_deb_pil = go.Scatter(
        x = x_values_econ_deb_pil,
        y = rapporto_debito_nucleare_pil,
        mode = 'lines',
        name = 'STIMA MODELLO NUCLEARE',
        marker = dict(color = '#1A76FF'),
        customdata = custom_data_econ_deb_pil
    )

    layout_econ_deb_pil = go.Layout(
        title = 'Andamento del rapporto Debito / PIL, confronto fra <br> <span style="color:#FF0000;">RGS - SCENARIO NAZIONALE BASE</span> e <span style="color:#1A76FF;">STIMA MODELLO NUCLEARE</span>',
        xaxis = dict(title = 'Anno'),
        yaxis = dict(title = 'Rapporto Debito/PIL'),
        showlegend = False
    )

    fig_econ_deb_pil = go.Figure(data = [trace1_econ_deb_pil, trace2_econ_deb_pil], layout = layout_econ_deb_pil)

    fig_econ_deb_pil.update_traces(hovertemplate = '%{x}: %{y:.2%}<br>Debito: %{customdata[0]:,.2f} mld €<br>PIL: %{customdata[1]:,.2f} mld €<br>Reattori completati: %{customdata[2]}<br>Reattori in costruzione: %{customdata[3]}')

    st.plotly_chart(fig_econ_deb_pil)


    ## grafico andamento crescita PIL YoY (confronto scenario nucleare vs senza)

    x_values_econ_cresc_pil = df_anni['anno']

    custom_data_econ_cresc_pil = list(
        list(row) for row in zip(
            df_anni['Stima_pil_rgs'],
            df_anni['reattori_finiti'],
            df_anni['reattori_in_costruzione']
        )
    )

    trace1_econ_cresc_pil = go.Scatter(
        x = x_values_econ_cresc_pil,
        y = df_anni['stima_crescita_pil_RGS'],
        mode = 'lines',
        name = 'RGS - SCENARIO NAZIONALE BASE',
        marker = dict(color = '#FF0000'),
        customdata = custom_data_econ_cresc_pil
    )
    trace2_econ_cresc_pil = go.Scatter(
        x = x_values_econ_cresc_pil,
        y = df_anni['stima_crescita_pil_nucleare'],
        mode = 'lines',
        name = 'STIMA MODELLO NUCLEARE',
        marker = dict(color = '#1A76FF'),
        customdata = custom_data_econ_cresc_pil
    )

    layout_econ_cresc_pil = go.Layout(
        title = 'Andamento crescita del PIL anno su anno, confronto fra <br> <span style="color:#FF0000;">RGS - SCENARIO NAZIONALE BASE</span> e <span style="color:#1A76FF;">STIMA MODELLO NUCLEARE</span>',
        xaxis = dict(title = 'Anno'),
        yaxis = dict(title = 'Stima Crescita PIL'),
        showlegend = False
    )

    fig_econ_cresc_pil = go.Figure(data = [trace1_econ_cresc_pil, trace2_econ_cresc_pil], layout = layout_econ_cresc_pil)
    
    fig_econ_cresc_pil.update_traces(hovertemplate = '%{x}: %{y:.2f}%<br>PIL: %{customdata[0]:,.2f} mld €<br>Reattori completati: %{customdata[1]}<br>Reattori in costruzione: %{customdata[2]}')

    st.plotly_chart(fig_econ_cresc_pil)

    
    ## grafico andamento indebitamento netto in % sul PIL (confronto scenario nucleare vs senza)

    x_values_econ_deb = df_anni['anno']

    custom_data_econ_deb = list(
        list(row) for row in zip(
            df_anni['debito'],
            df_anni['Stima_pil_rgs'],
            df_anni['reattori_finiti'],
            df_anni['reattori_in_costruzione']
        )
    )

    trace1_econ_deb = go.Scatter(
        x = x_values_econ_deb,
        y = df_anni['indebitamento_netto'] / df_anni['Stima_pil_rgs'] * 100,
        mode = 'lines',
        name = 'RGS - SCENARIO NAZIONALE BASE',
        marker = dict(color = '#FF0000'),
        customdata = custom_data_econ_deb
    )
    trace2_econ_deb = go.Scatter(
        x = x_values_econ_deb,
        y = df_anni['indebitamento_netto_con_nucleare'] / df_anni['pil_modello_nucleare'] * 100,
        mode = 'lines',
        name = 'STIMA MODELLO NUCLEARE',
        marker = dict(color = '#1A76FF'),
        customdata = custom_data_econ_deb
    )

    layout_econ_deb = go.Layout(
        title = 'Andamento Indebitamento Netto in rapporto al PIL, confronto fra <br> <span style="color:#FF0000;">RGS - SCENARIO NAZIONALE BASE</span> e <span style="color:#1A76FF;">STIMA MODELLO NUCLEARE</span>',
        xaxis = dict(title = 'Anno'),
        yaxis = dict(title = 'Indebitamento Netto (%)'),
        showlegend = False
    )

    fig_econ_deb = go.Figure(data = [trace1_econ_deb, trace2_econ_deb], layout = layout_econ_deb)

    fig_econ_deb.update_traces(hovertemplate = '%{x}: %{y:.2f}%<br>Debito: %{customdata[0]:,.2f} mld €<br>PIL: %{customdata[1]:,.2f} mld €<br>Reattori completati: %{customdata[2]}<br>Reattori in costruzione: %{customdata[3]}')

    st.plotly_chart(fig_econ_deb)

    
    ## grafici occupazione nucleare
    lav_cum_boolean = True
    
    if lav_cum_boolean == False:
        x_values_lav = df_anni['anno']

        custom_data_lav = list(
            list(row) for row in zip(
                df_anni['costo_totale'],
                df_anni['reattori_finiti'],
                df_anni['reattori_in_costruzione']
            )
        )

        trace1_lav = go.Scatter(
            x = x_values_lav,
            y = df_anni['costruttori_nucleare'],
            mode = 'lines',
            name = 'Costruzione',
            line = dict(color = "#cc6100"),
            customdata = custom_data_lav
        )
        trace2_lav = go.Scatter(
            x = x_values_lav,
            y = df_anni['addetti_indiretti_nucleare'],
            mode = 'lines',
            name = 'Indiretti',
            line = dict(color = "#a34372"),
            customdata = custom_data_lav
        )
        trace3_lav = go.Scatter(
            x = x_values_lav,
            y = df_anni['operatori_nucleare'],
            mode = 'lines',
            name = 'Operatori',
            line = dict(color = "#74ba45"),
            customdata = custom_data_lav
        )
        trace4_lav = go.Scatter(
            x = x_values_lav,
            y = df_anni['addetti_indotti_nucleare'],
            mode = 'lines',
            name = 'Indotti',
            line = dict(color = "#9d9d34"),
            customdata = custom_data_lav
        )

        layout_lav = go.Layout(
            title = f'Occupazione nucleare scomposta in <br> <span style="color:#cc6100;">costruttori nucleare</span>, <span style="color:#a34372;">addetti indiretti nucleare</span>, <span style="color:#74ba45;">operatori nucleare</span>, e <span style="color:#9d9d34;">addetti indotti nucleare</span>',
            xaxis = dict(title = 'Anno'),
            yaxis = dict(title = 'N° Occupati'),
            showlegend = False
        )

        fig_lav = go.Figure(data = [trace1_lav, trace2_lav, trace3_lav, trace4_lav], layout = layout_lav)

        fig_lav.update_traces(hovertemplate = '%{x}: %{y:,.0f}<br>Costo totale: %{customdata[0]:,.2f} mld €<br>Reattori completati: %{customdata[1]}<br>Reattori in costruzione: %{customdata[2]}')

        st.plotly_chart(fig_lav)

    else:
        ## cumulati
        x_values_lav_cum = df_anni['anno']
        
        custom_data_lav_cum = list(
            list(row) for row in zip(
                df_anni['costo_totale'].cumsum(),
                df_anni['reattori_finiti'],
                df_anni['reattori_in_costruzione']
            )
        )

        trace1_lav_cum = go.Scatter(
            x = x_values_lav_cum,
            y = df_anni['costruttori_nucleare'].cumsum(),
            mode = 'lines',
            name = 'Costruzione',
            line = dict(color = "#cc6100"),
            customdata = custom_data_lav_cum
        )
        trace2_lav_cum = go.Scatter(
            x = x_values_lav_cum,
            y = df_anni['addetti_indiretti_nucleare'].cumsum(),
            mode = 'lines',
            name = 'Indiretti',
            line = dict(color = "#a34372"),
            customdata = custom_data_lav_cum
        )
        trace3_lav_cum = go.Scatter(
            x = x_values_lav_cum,
            y = df_anni['operatori_nucleare'].cumsum(),
            mode = 'lines',
            name = 'Operatori',
            line = dict(color = "#74ba45"),
            customdata = custom_data_lav_cum
        )
        trace4_lav_cum = go.Scatter(
            x = x_values_lav_cum,
            y = df_anni['addetti_indotti_nucleare'].cumsum(),
            mode = 'lines',
            name = 'Indotti',
            line = dict(color = "#9d9d34"),
            customdata = custom_data_lav_cum
        )

        layout_lav_cum = go.Layout(
            title = f'Occupazione nucleare scomposta in <br> <span style="color:#cc6100;">costruttori nucleare</span>, <span style="color:#a34372;">addetti indiretti nucleare</span>, <span style="color:#74ba45;">operatori nucleare</span>, e <span style="color:#9d9d34;">addetti indotti nucleare</span>',
            xaxis = dict(title = 'Anno'),
            yaxis = dict(title = 'N° Occupati'),
            showlegend = False
        )

        fig_lav_cum = go.Figure(data = [trace1_lav_cum, trace2_lav_cum, trace3_lav_cum, trace4_lav_cum], layout = layout_lav_cum)

        fig_lav_cum.update_traces(hovertemplate = '%{x}: %{y:,.0f}<br>Costo totale cumulato: %{customdata[0]:,.2f} mld €<br>Reattori completati: %{customdata[1]}<br>Reattori in costruzione: %{customdata[2]}')

        st.plotly_chart(fig_lav_cum)
    
    # per impostare il grafico sopra come cumulato o meno
    lav_cum_boolean = st.toggle('Visualizza il grafico sopra come valori cumulati', value = False)
    
    
    ## grafici per il confronto fra uscite nucleare e PIL aggiuntivo
    econ_cum_boolean = False

    if econ_cum_boolean == False:

        x_values_econ_confronto = df_anni['anno']
        
        trace1_econ_confronto = go.Scatter(
            x = x_values_econ_confronto,
            y = df_anni['PIL aggiuntivo'],
            mode = 'lines',
            name = 'PIL aggiuntivo nucleare',
            marker = dict(color = '#1A76FF'),
            customdata = list(
                list(row) for row in zip(
                    df_anni['costo_overnight'],
                    df_anni['costo_interessi'],
                    df_anni['reattori_finiti'],
                    df_anni['reattori_in_costruzione']
                )
            ),
            hovertemplate = '%{x}:<br>Trace 1:<br>Costi overnight: €%{customdata[0]:,.2f}<br>Costi tassi: €%{customdata[1]:,.2f}<br>Reattori completati: %{customdata[2]}<br>Reattori in costruzione: %{customdata[3]}<extra></extra>'
        )
        trace2_econ_confronto = go.Scatter(
            x = x_values_econ_confronto,
            y = df_anni['costo_totale'],
            mode = 'lines',
            name = 'Costo annuale',
            marker = dict(color = '#FF0000'),
            customdata = list(
                list(row) for row in zip(
                    df_anni['PIL'],
                    (df_anni['debito'] / df_anni['PIL']) * 100,
                    (df_anni['indebitamento_netto'] / df_anni['PIL']) * 100
                )
            ),
            hovertemplate = '%{x}:<br>Trace 2:<br>PIL: €%{customdata[0]:,.2f}<br>Debito/PIL: %{customdata[1]:.2f}%<br>Indebitamento netto/PIL: %{customdata[2]:.2f}%<extra></extra>'
        )

        layout_econ_confronto = go.Layout(
            title = 'Confronto fra <br> <span style = "color:#FF0000;">Uscite cumulate</span> e <span style = "color:#1A76FF;">PIL aggiuntivo modello nucleare</span>',
            xaxis = dict(title = 'Anno'),
            yaxis = dict(title = 'Dati in €'),
            showlegend = False
        )

        fig_econ_confronto = go.Figure(data = [trace1_econ_confronto, trace2_econ_confronto], layout = layout_econ_confronto)

        st.plotly_chart(fig_econ_confronto)

    else:
        ## cumulati
        x_values_econ_confronto_cum = df_anni['anno']

        trace1_econ_confronto_cum = go.Scatter(
            x = x_values_econ_confronto_cum,
            y = df_anni['PIL aggiuntivo nucleare'].cumsum(),
            mode = 'lines',
            name = 'PIL aggiuntivo nucleare',
            marker = dict(color = '#1A76FF'),
            customdata = list(
                list(row) for row in zip(
                    df_anni['costo_overnight'].cumsum(),
                    df_anni['costo_tassi'].cumsum(),
                    df_anni['reattori_finiti'],
                    df_anni['reattori_in_costruzione']
                )
            ),
            hovertemplate = '%{x}:<br>Trace 1:<br>Costi overnight cumulati: €%{customdata[0]:,.2f}<br>Costi tassi cumulati: €%{customdata[1]:,.2f}<br>Reattori completati: %{customdata[2]}<br>Reattori in costruzione: %{customdata[3]}<extra></extra>'
        )
        trace2_econ_confronto_cum = go.Scatter(
            x = x_values_econ_confronto_cum,
            y = df_anni['costo_totale'].cumsum(),
            mode = 'lines',
            name = 'Costo annuale',
            marker = dict(color = '#FF0000'),
            customdata = list(
                list(row) for row in zip(
                    df_anni['PIL'],
                    (df_anni['debito'] / df_anni['PIL']) * 100,
                    (df_anni['indebitamento_netto'] / df_anni['PIL']) * 100
                )
            ),
            hovertemplate = '%{x}:<br>Trace 2:<br>PIL: €%{customdata[0]:,.2f}<br>Debito/PIL: %{customdata[1]:.2f}%<br>Indebitamento netto/PIL: %{customdata[2]:.2f}%<extra></extra>'
        )

        layout_econ_confronto_cum = go.Layout(
            title = 'Confronto fra <br> <span style = "color:#FF0000;">Costi Totali</span> e <span style = "color:#1A76FF;">PIL aggiuntivo modello nucleare</span>',
            xaxis = dict(title = 'Anno'),
            yaxis = dict(title = 'Dati in €'),
            showlegend = False
        )

        fig_econ_confronto_cum = go.Figure(data = [trace1_econ_confronto_cum, trace2_econ_confronto_cum], layout = layout_econ_confronto_cum)

        st.plotly_chart(fig_econ_confronto_cum)

    
    # per impostare il grafico sopra come cumulato o meno
    econ_cum_boolean = st.toggle('Visualizza il grafico sopra come valori cumulati', value = False)



### testo per le spiegazioni (le note)
# quelli che sembrano commenti all'interno di r""" """ sono titoli usando la sintassi markdown

latex_text_applicativo = r"""
    # A cosa NON serve questo applicativo
    
    Di seguito sono elencati vari aspetti della [modellazione e simulazione di scenari energetici](https://en.wikipedia.org/wiki/Energy_modeling) che questo applicativo non analizza né prende in considerazione con alcuni esempi di letteratura per ciascuno di essi.

    Come detto, questo applicativo non è fatto per stimare direttamente il **costo dell'energia** (elettricità) prodotta né per fare **analisi di sensibilità** sulle diverse fonti.

    - Neumann, Fabian, e Tom Brown. *Broad ranges of investment configurations for renewable power systems, robust to cost uncertainty and near-optimality*. iScience 26, fasc. 5 (19 maggio 2023): 106702. [https://doi.org/10.1016/j.isci.2023.106702](https://doi.org/10.1016/j.isci.2023.106702)
    - Duan, Lei, e Ken Caldeira. *Implications of uncertainty in technology cost projections for least-cost decarbonized electricity systems*. iScience 27, fasc. 1 (19 gennaio 2024): 108685. [https://doi.org/10.1016/j.isci.2023.108685](https://doi.org/10.1016/j.isci.2023.108685)
    - *Carbon neutrality - Energy pathways to 2050 | RTE*. Consultato 3 maggio 2024. [https://analysesetdonnees.rte-france.com/en/publications/energy-pathways-2050](https://analysesetdonnees.rte-france.com/en/publications/energy-pathways-2050)

    Non ha la volontà di esplorare e confrontare diversi **scenari energetici** e mix elettrici.

    - America, Net-Zero. *Net-Zero America*. Net-Zero America Consultato 3 maggio 2024. [https://netzeroamerica.princeton.edu](https://netzeroamerica.princeton.edu)
    - *100\% Clean Electricity by 2035 Study*. Consultato 3 maggio 2024. [https://www.nrel.gov/analysis/100-percent-clean-electricity-by-2035-study.html](https://www.nrel.gov/analysis/100-percent-clean-electricity-by-2035-study.html)
    - Redazione. *Qual è il mix elettrico più economico per un’Italia CO2-free?* Energia (blog), 29 giugno 2022. [https://www.rivistaenergia.it/2022/06/qual-e-il-mix-elettrico-piu-economico-per-unitalia-co2-free](https://www.rivistaenergia.it/2022/06/qual-e-il-mix-elettrico-piu-economico-per-unitalia-co2-free/)
    - *PyPSA server*. Consultato 3 maggio 2024. [https://model.energy/scenarios/results/12a2e82c-f8dd-43ab-b2d7-c89018f789a9](https://model.energy/scenarios/results/12a2e82c-f8dd-43ab-b2d7-c89018f789a9)
    - entsog, entsoe. *TYNDP 2022 Scenario Report – Introduction and Executive Summary*. Consultato 3 maggio 2024. [https://2022.entsos-tyndp-scenarios.eu](https://2022.entsos-tyndp-scenarios.eu/)

    Non ha la volontà di **studiare e valutare uno specifico scenario dal punto di vista energetico** (simulazioni orarie, infrastrutture necessarie, vincoli macroregionali).

    - Brown, Patrick R., e Audun Botterud. *The Value of Inter-Regional Coordination and Transmission in Decarbonizing the US Electricity System*. Joule 5, fasc. 1 (20 gennaio 2021): 115–34. [https://doi.org/10.1016/j.joule.2020.11.013](https://doi.org/10.1016/j.joule.2020.11.013)
    - Bustreo, C., U. Giuliani, D. Maggio, e G. Zollino. *How fusion power can contribute to a fully decarbonized European power mix after 2050*. Fusion Engineering and Design, SI:SOFT-30, 146 (1 settembre 2019): 2189–93. [https://doi.org/10.1016/j.fusengdes.2019.03.150](https://doi.org/10.1016/j.fusengdes.2019.03.150)
"""

latex_text_conti = r"""
    # Formule per il calcolo del costo del reattore

    ## Calcolo degli interessi

    ### Interessi Lineari
    In questa modalità, solo il debito fatto per la spesa overnight genera interessi mentre non si cumulano interessi sugli interessi.

    - **Interessi per l'anno \( t \):**
    $$\text{interessi}_t = t \times \text{costo\_annuale} \times i$$

    - **Spesa totale per l'anno \( t \):**
    $$\text{spesa\_totale}_t = \text{costo\_annuale} + \text{interessi}_t$$

    - **Totale interessi pagati fino all'anno \( t \):**
    $$\text{interessi\_cumulati}_t = \sum_{k=1}^{t} (k \times \text{costo\_annuale} \times i)$$

    - **Totale spesa fino all'anno \( t \):**
    $$\text{spesa\_cumulata}_t = \text{costo\_annuale} \times t + \text{interessi\_cumulati}_t$$

    ### Interessi Composti
    In questa modalità, gli interessi non vengono subito ripagati ma generano altro debito, quindi gli interessi per l'anno \( t \) sono calcolati sul capitale cumulato all'anno precedente incrementato dagli interessi per l'anno precedente.

    - **Capitale accumulato all'inizio dell'anno \( t \):**
    $$\text{capitale\_cumulato}_t = \text{capitale\_cumulato}_{t-1} + \text{costo\_annuale}$$

    - **Interessi per l'anno \( t \):**
    $$\text{interessi}_t = \text{capitale\_cumulato}_t \times i$$

    - **Spesa totale per l'anno \( t \):**
    $$\text{spesa\_totale}_t = \text{costo\_annuale} + \text{interessi}_t$$

    - **Totale interessi pagati fino all'anno \( t \):**
    $$\text{interessi\_cumulati}_t = \sum_{k=1}^{t} ((\text{capitale\_cumulato}_{k-1} + \text{costo\_annuale}) \times i)$$

    - **Aggiornamento del capitale accumulato (totale spesa fino all'anno \( t \)):**
    $$\text{capitale\_cumulato}_t = \text{capitale\_cumulato}_t + \text{interessi}_t$$

    ### Esempio di Applicazione

    Supponiamo che:
    - Il periodo di costruzione \( T \) sia di 7 anni.
    - Il costo totale del reattore \( X \) sia 7000 unità monetarie (costo annuale = 1000).
    - Il tasso di interesse annuo \( i \) sia del 7\% (0.07).

    #### Calcolo con Interessi Non Composti
    **Anno 1:**
    $$\text{interessi}_1 = 1000 \times 0.07 = 70$$
    $$\text{spesa\_totale}_1 = 1000 + 70 = 1070$$

    **Anno 2:**
    $$\text{interessi}_2 = 2000 \times 0.07 = 140$$
    $$\text{spesa\_totale}_2 = 1000 + 140 = 1140$$

    **Spesa totale accumulata dopo 2 anni:**
    $$\text{totale\_cumulativo\_2} = 1070 + 1140 = 2210$$

    #### Calcolo con Interessi Composti
    **Anno 1:**
    $$\text{capitale\_accumulato}_1 = 1000$$
    $$\text{interessi}_1 = 1000 \times 0.07 = 70$$
    $$\text{spesa\_totale}_1 = 1000 + 70 = 1070$$

    **Anno 2:**
    $$\text{capitale\_accumulato}_2 = 1070 + 1000 = 2070$$
    $$\text{interessi}_2 = 2070 \times 0.07 = 144.9$$
    $$\text{spesa\_totale}_2 = 1000 + 144.9 = 1144.9$$

    **Spesa totale accumulata dopo 2 anni:**
    $$\text{totale\_cumulativo\_2} = 1070 + 1144.9 = 2214.9$$

    #### Confronto
    La differenza \(2214.9 - 2210 = 4.9\) unità monetarie corrisponde alla spesa per gli interessi sugli interessi \(0.07 \times 70 = 4.9\). Dopo soli due anni gli unici interessi accumulati sono quelli del primo anno ma alla fine della costruzione la differenza diventa più significativa:
    - **Spesa complessiva con l'interesse lineare:** 8960 unità monetarie.
    - **Spesa complessiva con l'interesse composto:** 9259.80 unità monetarie.
    - **Differenza complessiva:** 299.80 unità monetarie, ossia il 4.28\% rispetto al costo totale overnight.

    # Metodologia per la stima degli impatti macroeconomici

    **La formula per calcolare il valore aggiunto per occupato è:**

    $$valore\_aggiunto = occupati \times valore\_aggiunto\_per\_occupato$$

    dove:
    - $valore\_aggiunto$ è il valore aggiunto,
    - $occupati$ è il numero di occupati,
    - $valore\_aggiunto\_per\_occupato$ è il valore aggiunto per occupato.

    **La formula per calcolare il PIL in base al valore aggiunto e al numero di occupati è:**

    $$PIL = valore\_aggiunto \times occupati$$

    dove:
    - $PIL$ è il Prodotto Interno Lordo,
    - $valore\_aggiunto$ è il valore aggiunto,
    - $occupati$ è il numero di occupati.

    **La formula per calcolare il PIL aggiuntivo del progetto nucleare è:**

    $$PILn = VAnd \times Ond + VAni \times Oni + VAnc \times Onc$$

    dove:
    - $PILn$ è il Prodotto Interno Lordo generato dal nucleare,
    - $VAnd$ è il valore aggiunto del singolo occupato diretto nel progetto nucleare,
    - $VAni$ è il valore aggiunto del singolo occupato indiretto nel progetto nucleare,
    - $VAnc$ è il valore aggiunto del singolo occupato nella fase di costruzione del progetto nucleare,
    - $Ond$ è il numero di occupati diretti nel progetto nucleare,
    - $Oni$ è il numero di occupati indiretti nel progetto nucleare,
    - $Onc$ è il numero di occupati nella fase di costruzione del progetto nucleare.
"""

# Utilizzo di st.markdown() per renderizzare il testo formattato in Markdown

with st.expander("[Nota 1] A cosa NON serve questo applicativo"):
    st.markdown(latex_text_applicativo, unsafe_allow_html=True)

with st.expander("[Nota 2] Come abbiamo fatto i conti"):
    st.markdown(latex_text_conti, unsafe_allow_html=True)
