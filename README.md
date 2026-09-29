# Python Security Automation — SSH Log Analyzer

## Descrizione

Questo progetto consiste nello sviluppo da zero di un **log analyzer in Python 3** per l'analisi automatizzata dei tentativi di autenticazione SSH falliti.

L'obiettivo è replicare, in forma semplificata, un'attività che un **SOC Analyst** potrebbe svolgere manualmente o tramite un sistema **SIEM**: analizzare un log di autenticazione, individuare i tentativi di login falliti, raggrupparli per indirizzo IP e identificare automaticamente gli IP che superano una determinata soglia di tentativi sospetti.

Il progetto è stato realizzato come laboratorio pratico di **Blue Team e Security Automation**.

## Obiettivo

Lo script è progettato per:

- leggere un file di log SSH in formato `auth.log`;
- individuare i tentativi di autenticazione falliti;
- estrarre gli indirizzi IP sorgente;
- raggruppare i tentativi per indirizzo IP;
- contare il numero di tentativi falliti provenienti da ciascun IP;
- confrontare il numero di tentativi con una soglia definita;
- segnalare automaticamente gli IP che superano tale soglia;
- distinguere, per quanto possibile, i tentativi sospetti dagli eventi di autenticazione riusciti.

Il superamento della soglia viene utilizzato come **indicatore di possibile attività di brute-force o credential stuffing**, senza considerarlo automaticamente una prova di attacco.

## Scenario del laboratorio

Il dataset utilizzato è un file di log SSH di esempio costruito utilizzando un formato realistico simile a quello dei normali `auth.log` Linux.

Il dataset contiene diversi scenari:

- un IP `203.0.113.45` che effettua numerosi tentativi di accesso utilizzando diversi username, tra cui `admin`, `root`, `test` e `postgres`;
- un IP `198.51.100.7` associato a un singolo tentativo fallito;
- alcuni login legittimi completati con successo.

Il comportamento del primo IP è intenzionalmente costruito per simulare un'attività automatizzata e ripetitiva, utile per testare la capacità dello script di identificare pattern sospetti.

> Gli indirizzi IP utilizzati nel dataset appartengono agli intervalli riservati alla documentazione e agli esempi e non rappresentano sistemi reali.

## Logica di analisi

L'analisi segue una pipeline semplificata simile a quella utilizzata nei processi di security monitoring:

1. **Log ingestion** — lettura del file di autenticazione;
2. **Parsing** — analisi delle singole righe del log;
3. **Detection** — individuazione dei tentativi di login falliti;
4. **Extraction** — estrazione degli indirizzi IP e degli username coinvolti;
5. **Aggregation** — raggruppamento degli eventi per indirizzo IP;
6. **Threshold analysis** — confronto del numero di tentativi con la soglia configurata;
7. **Alerting** — segnalazione degli IP che presentano un numero anomalo di tentativi.

## Contenuti

- Report completo del laboratorio in formato PDF
- Script contenente i comandi eseguiti
- Codice Python sviluppato del Log Analyzer

[Visualizza il laboratorio ->](./phyton-security-analyzer/)
