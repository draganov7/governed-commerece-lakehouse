# pyrefly: ignore [missing-import]
from download_olist import main as download_main
# pyrefly: ignore [missing-import]
from load_to_postgres import main as load_main

def main():
    download_main()
    load_main()


if __name__ == "__main__":
    main()