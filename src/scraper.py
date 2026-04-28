import requests
import sqlite3
import os
import json
import time

def fetch_data(page_index):
    base_url = "https://www.nemoapp.kr/api/store/search-list"
    params = {
        "Subway": 414,
        "Radius": 1000,
        "CompletedOnly": "false",
        "NELat": 37.685005099879895,
        "NELng": 127.09654581165293,
        "SWLat": 37.56971753173125,
        "SWLng": 126.98628077242054,
        "Zoom": 13,
        "SortBy": 29,
        "PageIndex": page_index
    }
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36",
        "Referer": "https://www.nemoapp.kr/store"
    }
    
    try:
        response = requests.get(base_url, params=params, headers=headers, timeout=10)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error: HTTP {response.status_code}")
            return None
    except Exception as e:
        print(f"Request Exception: {e}")
        return None

def get_sqlite_type(value):
    if isinstance(value, int):
        return "INTEGER"
    elif isinstance(value, float):
        return "REAL"
    else:
        return "TEXT"

def initialize_db(sample_item):
    if not sample_item:
        return None, None
        
    db_path = os.path.join("data", "nemo_stores.db")
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    keys = sorted(list(sample_item.keys()))
    cursor.execute("DROP TABLE IF EXISTS stores")
    
    columns = []
    for key in keys:
        sql_type = get_sqlite_type(sample_item.get(key))
        if key == 'id':
            columns.append(f"{key} {sql_type} PRIMARY KEY")
        else:
            columns.append(f"{key} {sql_type}")
    
    create_table_sql = f"CREATE TABLE stores ({', '.join(columns)})"
    cursor.execute(create_table_sql)
    conn.commit()
    
    return conn, keys

def save_items(conn, keys, items):
    if not items:
        return 0
        
    cursor = conn.cursor()
    placeholders = ", ".join(["?"] * len(keys))
    insert_sql = f"INSERT OR REPLACE INTO stores ({', '.join(keys)}) VALUES ({placeholders})"
    
    count = 0
    for item in items:
        values = []
        for key in keys:
            val = item.get(key)
            if isinstance(val, (list, dict)):
                val = json.dumps(val, ensure_ascii=False)
            values.append(val)
        cursor.execute(insert_sql, values)
        count += 1
    
    conn.commit()
    return count

def main():
    page_index = 0
    total_total = 0
    conn = None
    keys = None
    
    print("Starting full data collection...")
    
    while True:
        print(f"Fetching Page {page_index}...", end=" ", flush=True)
        data = fetch_data(page_index)
        
        if not data or 'items' not in data or not data['items']:
            print("\nFinal page reached or no more items.")
            break
            
        items = data['items']
        
        # 첫 페이지에서 테이블 초기화
        if page_index == 0:
            conn, keys = initialize_db(items[0])
            if not conn:
                print("Failed to initialize database.")
                break
        
        saved_count = save_items(conn, keys, items)
        total_total += saved_count
        print(f"Saved {saved_count} items. (Cumulative: {total_total})")
        
        page_index += 1
        time.sleep(0.5) # 서버 부하 조절
    
    if conn:
        conn.close()
    
    print(f"\nCollection complete. Total items saved: {total_total}")

if __name__ == "__main__":
    if not os.path.exists("data"):
        os.makedirs("data")
    main()
