from typing import Any, Text, Dict, List;
from rasa_sdk import Action, Tracker;
from rasa_sdk.executor import CollectingDispatcher;
import re; import sqlite3;
class ActionNIM(Action):
    def name(self) -> Text:
        return "NIM";
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        con = sqlite3.connect('/home/ade/Dokumen/Old/NLP/bin/kode');
        nim =   re.search("[0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]", 
                tracker.latest_message.get('text'))[0];
        
        dispatcher.utter_message(text = "Fakultas:\t" + str(con.execute("select nama from fakultas where kode = " + str(nim[0:2]) + ";").fetchall()[0][0]));
        #dispatcher.utter_message(text = "Prodi:\t" + str(con.execute("select nama from prodi where kode = " + str(nim[2:2]) + ";").fetchall()[0][0]));
        dispatcher.utter_message(text = "Tipe:\t\t" + str(con.execute("select nama from tipe where kode = " + str(nim[4:5]) + ";").fetchall()[0][0]));
        dispatcher.utter_message(text = "Jalur:\t\t" + str(con.execute("select nama from jalur where kode = " + str(nim[5:6]) + ";").fetchall()[0][0]));
        dispatcher.utter_message(text = "Bulan masuk:\t" + str(nim[6:7]));
        dispatcher.utter_message(text = "Tahun masuk:\t" + str(nim[7:9]));
        dispatcher.utter_message(text = "Tahun keluar:\t" + str(nim[9:11]));
        dispatcher.utter_message(text = "No. urut:\t" + str(nim[11:14]));
        
        return [];
