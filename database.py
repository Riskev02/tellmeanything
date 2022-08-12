from deta import Deta
from streamlit import secrets

deta = Deta(secrets["deta_key"])
db = deta.Base('individu_db')

def post_message(message):
    color_card = ['bg-primary','bg-secondary','bg-success','bg-danger','bg-warning','bg-info','bg-dark']
    item = db.fetch()
    item_res = item.items
    item_c = max([i["count"] for i in item_res],default = 0)
    m_bgc = db.fetch({'count':item_c}).items
    if m_bgc == []:
        m_bgc = 0
    elif m_bgc[0]["count-bg"] == 6 or (m_bgc is None):
        m_bgc[0]["count-bg"] = 0
        m_bgc = m_bgc[0]["count-bg"] 
    else:
        m_bgc[0]["count-bg"] += 1
        m_bgc = m_bgc[0]["count-bg"]
    item_c += 1
    payload = {
        'message':message,
        'count':item_c,
        'count-bg':m_bgc,
        'bg-color':color_card[m_bgc]
    }
    return db.put(payload)

