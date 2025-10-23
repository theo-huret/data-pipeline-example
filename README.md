# Data Pipeline Example

> A learning project demonstrating modern data engineering practices with dlt and dbt

This repository is a hands-on example of building a complete data pipeline from ingestion to analytics-ready tables. It showcases how to use **dlt** (Data Load Tool) for data ingestion and **dbt** (Data Build Tool) for transformations, following the Medallion Architecture pattern.

## 📚 Learning Objectives

This project helps you understand:

- **Data ingestion** with dlt from REST APIs
- **Data transformation** patterns using dbt
- **Medallion Architecture** (Bronze, Silver, Gold layers)
- **PostgreSQL** as a data warehouse
- **Schema management** and custom macros in dbt
- **Data quality testing** with dbt tests

## Data Flow

1. **Bronze Layer** (`poke_bronze` schema): Raw data ingested from the Pokemon API using dlt
2. **Silver Layer** (`poke_silver` schema): Cleaned and normalized data transformed by dbt
3. **Gold Layer** (`poke_gold` schema): Business-ready aggregated tables for analytics

## 🛠️ Tech Stack

- **[dlt](https://dlthub.com/)**: Python library for data ingestion
- **[dbt](https://www.getdbt.com/)**: SQL-based transformation framework
- **PostgreSQL**: Data warehouse
- **Python 3.12**: Programming language

## 🚀 Getting Started

### Prerequisites

- Python 3.12
- PostgreSQL database
- Git

### Installation

1. **Clone the repository**
>git clone https://github.com/theo-huret/data-pipeline-example.git
>cd data-pipeline-example

2. **Set up Python environment**
>python3.12 -m venv .venv
>source .venv/bin/activate # On Windows: .venv\Scripts\activate

3. **Install dependencies**
>pip install dltdbt-core dbt-postgres requests
 
4. **Configure environment variables**
>export POKE_PG_HOST="localhost"
>export POKE_PG_PORT="5432"
>export POKE_PG_USER="your_username"
>export POKE_PG_PWD="your_password"
>export POKE_PG_DB="pokemon_db"
>export POKE_PG_SCHEMA="poke_bronze"

5. **Run dlt to ingest data**
>python dlt_poke.py

6. **Run dbt transformations**
>dbt run

## 🧪 Models Description

### Silver Layer

**`stg_raw_pokemon`**: Staging model that selects and cleans raw Pokemon data from the Bronze layer.

### Gold Layer

**`pokemon_gold`**: Complete Pokemon dataset with all attributes ready for analytics.

**`pokemon_by_type`**: Aggregated table showing Pokemon count, min/max IDs by type.

## 📝 License

This project is open source and available under the MIT License.

## 🙏 Acknowledgments

- [PokeAPI](https://pokeapi.co/) for providing free Pokemon data
- [dlt community](https://dlthub.com/) for the excellent ingestion tool
- [dbt community](https://www.getdbt.com/) for the powerful transformation framework
