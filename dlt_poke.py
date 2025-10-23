import os, time, requests, dlt
from typing import Iterator
from dlt.destinations import postgres

POKEAPI_BASE = "https://pokeapi.co/api/v2"

@dlt.resource(name="pokemon", write_disposition="replace")
def fetch_all_pokemon(limit_per_page: int = 100, pause_s: float = 0.05, max_pokemon=151):
    next_url = f"{POKEAPI_BASE}/pokemon?limit={limit_per_page}&offset=0"
    all_entries = []
    while next_url:
        r = requests.get(next_url, timeout=30); r.raise_for_status()
        j = r.json()
        all_entries.extend(j.get("results", []))
        next_url = j.get("next")
        time.sleep(pause_s)

    for entry in all_entries[:max_pokemon]:
        d = requests.get(entry["url"], timeout=30).json()
        types = [t["type"]["name"] for t in d.get("types", [])]
        abilities = [a["ability"]["name"] for a in d.get("abilities", [])]
        stats = {s["stat"]["name"]: s["base_stat"] for s in d.get("stats", [])}
        yield {
            "id": d.get("id"),
            "name": d.get("name"),
            "height": d.get("height"),
            "weight": d.get("weight"),
            "base_experience": d.get("base_experience"),
            "types_csv": ",".join(types),
            "abilities_csv": ",".join(abilities),
            "stats_json": stats,
            "raw_payload": d,
        }

@dlt.source
def poke_source():
    return fetch_all_pokemon()

def main():
    dsn = os.environ.get(
        "POKE_PG_DSN",
        "postgresql://{user}:{pwd}@{host}:{port}/{db}".format(
            user=os.environ["POKE_PG_USER"],
            pwd=os.environ["POKE_PG_PWD"],
            host=os.environ.get("POKE_PG_HOST","localhost"),
            port=os.environ.get("POKE_PG_PORT","5432"),
            db=os.environ["POKE_PG_DB"],
        ),
    )

    pipeline = dlt.pipeline(
        pipeline_name="poke_pipeline_pg",
        destination=postgres(credentials=dsn),
        dataset_name=os.environ.get("POKE_PG_SCHEMA","poke_bronze"),
    )

    info = pipeline.run(poke_source())
    print(info)

if __name__ == "__main__":
    main()
