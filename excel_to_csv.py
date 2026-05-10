import sys
from pathlib import Path
import pandas as pd


def excel_to_csv_folder(excel_path: str) -> None:
    path = Path(excel_path)
    if not path.exists():
        raise FileNotFoundError(f"File not found: {excel_path}")

    output_dir = path.parent / path.stem
    output_dir.mkdir(exist_ok=True)

    xl = pd.ExcelFile(path)
    for sheet_name in xl.sheet_names:
        df = xl.parse(sheet_name)
        csv_path = output_dir / f"{sheet_name}.csv"
        df.to_csv(csv_path, index=False)
        print(f"  {csv_path}")

    print(f"\nDone — {len(xl.sheet_names)} sheet(s) written to {output_dir}/")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python excel_to_csv.py <path/to/file.xlsx>")
        sys.exit(1)
    excel_to_csv_folder(sys.argv[1])
