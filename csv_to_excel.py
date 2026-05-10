import sys
from pathlib import Path
import pandas as pd


def csv_folder_to_excel(folder_path: str) -> None:
    folder = Path(folder_path)
    if not folder.is_dir():
        raise NotADirectoryError(f"Not a directory: {folder_path}")

    excel_path = folder.parent / f"{folder.name}.xlsx"

    with pd.ExcelWriter(excel_path, engine="openpyxl") as writer:
        for csv_file in sorted(folder.glob("*.csv")):
            df = pd.read_csv(csv_file)
            df.to_excel(writer, sheet_name=csv_file.stem, index=False)
            print(f"  {csv_file.stem}")

    print(f"\nDone — written to {excel_path}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python csv_to_excel.py <path/to/folder>")
        sys.exit(1)
    csv_folder_to_excel(sys.argv[1])
